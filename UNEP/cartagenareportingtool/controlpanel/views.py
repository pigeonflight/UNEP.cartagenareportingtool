#from zope.interface import Interface
#from zope import schema
from five import grok
#from UNEP.cartagenareportingtool.interface import IReportStatus
from Products.CMFCore.interfaces import ISiteRoot
from plone import api


#from plone.z3cform import layout
#from plone.directives import form, dexterity
#from plone.app.registry.browser.controlpanel import RegistryEditForm
#from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

# had to explicitly define the location of the template directory
grok.templatedir('controlpanel_templates')

# note the use of grok.View (in contrast to dexterity.DisplayForm)
# grok.View does not try to "inspect" the context and return
# custom widgets, which would be a problem with a context of ISiteRoot
class ControlPanelView(grok.View):
    """
    View for controlpanel
    """

    grok.name("cartagenareportingtool-controlpanel")
    grok.context(ISiteRoot)

    def get_country_report(self,user):
        pm = api.portal.get_tool(name='portal_membership')
        members_folder = pm.membersfolder_id
        path = "/%s/%s/country-report" % (members_folder,user)
        
        try:
            country_report = api.content.get(path=path)
        except AttributeError:
            country_report = None
        
        return country_report

    def status_info(self):
        """
        returns data in the form
          [
                {'username':"JAM",
                'name':"Jamaica",
                 'status':"good",
                  'progress':10},
                 {'username':'TNT',
                 name':"Trinidad",
                 'status':"also good",
                 'progress':50}
                ]
        """
        user_status = []
        users = api.user.get_users()
        for user in users:
            username = user.id
            country_report = self.get_country_report(username)
            progress = 0
            doclink = ''
            status = 'not started'
            css_class = "%s %s" % (username,'not-started')
            if country_report:
                progress = 5
                doclink = country_report.absolute_url()
                status = 'started'
                css_class = "%s %s" % (username,'started')
            props = {}
            props['username'] = username
            props['name'] = user.getProperty('fullname')
            props['status'] = status
            props['class']  = css_class
            props['progress'] = progress
            props['doclink']  = doclink
            user_status.append(props)
        return user_status
        