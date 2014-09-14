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

        if self.user_is_logged_in():
            user = api.user.get_current()
            user_id = user.getId()
            #print "redirect to user folder"
            redirect_url = "%s/%s/%s" % (portal_url,members_folder,user_id)
        else:
            #print "redirect to top folder"
            redirect_url = "%s/%s" % (portal_url,members_folder)
        request.response.redirect(redirect_url)

    
    def __call__(self):
        self.redirect()
        #return "Hello %s" % self.name
     