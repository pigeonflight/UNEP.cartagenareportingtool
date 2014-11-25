from plone.testing import z2
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import quickInstallProduct
from plone.app.testing import PLONE_FIXTURE
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from zope.configuration import xmlconfig

class UNEP_CARTAGENAREPORTINGTOOLLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        
        # load dependencies
        import collective.z3cform.datagridfield
        self.loadZCML(package=collective.z3cform.datagridfield)
        
        
        import UNEP.cartagenareportingtool
        self.loadZCML(package=UNEP.cartagenareportingtool)
        
        #xmlconfig.file('configure.zcml',
        #    Products.ECQuiz, context=configurationContext)
#

        #z2.installProduct(app,'Products.ECQuiz')
        #z2.installProduct(app,'Products.ECAssignmentBox')
        #z2.installProduct(app,'Products.DataGridField')
        

    def setUpPloneSite(self, portal):
        # Set default workflow chain, because PLONE_FIXTURE has not one
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')
        # Apply profile for ep.core
        quickInstallProduct(portal,'UNEP.cartagenareportingtool')

    def tearDownZope(self, app):
        pass
#        z2.uninstallProduct(app,'Products.ECQuiz')
#        z2.uninstallProduct(app,'Products.DataGridField')
        
UNEP_CARTAGENAREPORTINGTOOL_FIXTURE = UNEP_CARTAGENAREPORTINGTOOLLayer()

UNEP_CARTAGENAREPORTINGTOOL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UNEP_CARTAGENAREPORTINGTOOL_FIXTURE,),
    name='UNEP_CARTAGENAREPORTINGTOOL:Integration')

UNEP_CARTAGENAREPORTINGTOOL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UNEP_CARTAGENAREPORTINGTOOL_FIXTURE,),
    name='UNEP_CARTAGENAREPORTINGTOOL:Functional')


class UNEP_CARTAGENAREPORTINGTOOLAcceptanceLayer(PloneSandboxLayer):
    defaultBases = (UNEP_CARTAGENAREPORTINGTOOL_FIXTURE,)

UNEP_CARTAGENAREPORTINGTOOL_ROBOT_TESTING = FunctionalTesting(
   bases=(
          UNEP_CARTAGENAREPORTINGTOOL_FIXTURE, 
          AUTOLOGIN_LIBRARY_FIXTURE,
          z2.ZSERVER_FIXTURE),
          name="UNEP_CARTAGENAREPORTINGTOOL:Robot"
         )
