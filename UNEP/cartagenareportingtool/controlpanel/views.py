import math
from zope.interface.interfaces import IMethod
#from zope import schema
from five import grok
from UNEP.cartagenareportingtool.interface import ICountryReport
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
                 {'username':'TTO',
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
            country_data = []
            if country_report:
                for name, desc in ICountryReport.namesAndDescriptions():
                    value = getattr(country_report,name)
                    if IMethod.providedBy(desc):
                        value = value()
                    country_data.append(value)

                progress = 5
                doclink = country_report.absolute_url()
                
                status = api.content.get_state(country_report)
                css_class = "%s %s" % (username,'started')
                for idx in range(len(country_data)):
                    #print country_data[idx]
                    if country_data[idx]:
                        progress = progress + 1
                progress = int(math.ceil(float(progress) / float(len(country_data)) * 100))
                print "prg",progress
            props = {}
            props['username'] = username
            props['report_data'] = country_data
            props['name'] = user.getProperty('fullname')
            props['status'] = status
            props['class']  = css_class
            props['progress'] = progress
            props['doclink']  = doclink
            user_status.append(props)
        return user_status
        