#from zope.interface import Interface
#from zope import schema
from five import grok
#from UNEP.cartagenareportingtool.interface import IReportStatus
from Products.CMFCore.interfaces import ISiteRoot

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

    def status_info(self):
        return [
              {'name':"Jamaica",
               'status':"good"},
               {'name':"Trinidad",
               'status':"also good"}
              ]
