from zope.component.hooks import getSite
from plone import api

class Index(object):
    def __init__(self, context, request):
        self.name = "world"
        self.context = context
        self.request = request

    def user_is_logged_in(self):
        if not api.user.is_anonymous():
            return True
        return False
    
    def redirect(self):
        portal = getSite()
        request = getattr(portal, "REQUEST", None)
        portal_url = portal.absolute_url()
        pm = portal['portal_membership']
        members_folder = pm.membersfolder_id
        # check if user is logged in
        

        # if the logged in user is an administrator then redirect to the controlpanel
        
        if self.user_is_logged_in():
            user = api.user.get_current()
            user_id = user.getId()
            sub_path = "%s/%s" % (members_folder,user_id)
            if 'Manager' in user.getRoles():
                sub_path = "@@cartagenareportingtool-controlpanel"
           
            redirect_url = "%s/%s" % (portal_url,sub_path)
        else:
            #print "redirect to top folder"
            redirect_url = "%s/%s" % (portal_url,members_folder)
        request.response.redirect(redirect_url)

    
    def __call__(self):
        self.redirect()
        #return "Hello %s" % self.name
     