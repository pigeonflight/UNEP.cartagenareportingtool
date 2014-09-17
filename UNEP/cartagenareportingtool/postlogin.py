# Python imports
import logging

# Zope imports
from zope.component.hooks import getSite

# CMFCore imports
from Products.PluggableAuthService.interfaces.events import IUserLoggedInEvent

# Caveman imports
from five import grok

# Plone imports
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
#from plone import api

# Logger output for this module
logger = logging.getLogger(__name__)


@grok.subscribe(IUserLoggedInEvent)
def logged_in_handler(event):
    """
    Listen to the event and perform the action accordingly.
    """

    portal = getSite()
    request = getattr(portal, "REQUEST", None)
    portal_url = portal.absolute_url()
    user = event.object
    pm = portal['portal_membership']
    members_folder = pm.membersfolder_id
   
    #redirect_to_user folder
    # this means that the information is always available at the default memberfolder
    sub_path = "%s/%s" % (members_folder,user.getId())

    # if the logged in user is an administrator then redirect to the controlpanel
    print "get roles",user.getRoles()
    if 'Manager' in user.getRoles():
        sub_path = "@@cartagenareportingtool-controlpanel"
    
    redirect_path = "%s/%s" % (portal_url,sub_path)
    #print redirect_path 
    # bruteforce came_from to always be empty
    if request.get('came_from', None):
            request['came_from'] = ''
            request.form['came_from'] = ''
    request.response.redirect(redirect_path)
