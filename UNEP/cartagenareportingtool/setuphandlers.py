# -*- coding: utf-8 -*-
#from CMFCore.utils import getToolByName
from plone import api
from Products.CMFPlone.interfaces import constrains
from plone.app.controlpanel.security import ISecuritySchema
import logging
from zExceptions import BadRequest


PROFILE_ID='profile-UNEP.cartagenareportingtool:default'
PRODUCT = 'UNEP.cartagenareportingtool'

def setupVarious(context):
    if context.readDataFile('unep.cartagenareportingtool.marker.txt') is None:
        return
    
    setup = api.portal.get_tool(name='portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo')
    
    if api.content.get('/news'):
        api.content.delete(api.content.get('/news'))
    if api.content.get('/Members'):
        api.content.delete(api.content.get('/Members'))
    if api.content.get('/events'):   
        api.content.delete(api.content.get('/events'))

    portal = api.portal.get()

    # configure default site view to be 'site_index'
    portal.manage_changeProperties(default_page='site_index')
    portal.setLayout("site_index")
    # we will be organizing folders by year
    # starting by hardcoding for 2014
    # no longer using the reports folder 
    
    memberfolder = '2014' #this can eventually be an environment variable or something
    if not api.content.get('/%s' % memberfolder):
        try:
            reportfolder = api.content.create(
            portal,
            'Folder',
            id=memberfolder,
            title='%s report' % memberfolder
            )
        except BadRequest:
            return
        api.content.transition(reportfolder, transition='publish')
        behavior = constrains.ISelectableConstrainTypes(reportfolder)
        behavior.setConstrainTypesMode(constrains.ENABLED)
        behavior.setLocallyAllowedTypes(['UNEP.cartagenareportingtool.countryreport'])
        behavior.setImmediatelyAddableTypes(['UNEP.cartagenareportingtool.countryreport'])
    mp = api.portal.get_tool(name='portal_membership')
    # set type to custom member type
    mp.setMemberAreaType('UNEP.cartagenareportingtool.memberfolder')
    # set member folder name
    print "setting members folder"
    mp.setMembersFolderById(memberfolder)
    
    # call update security 
    set_up_security(context)

def set_up_security(context):
    """ Enable/disable security controlpanel (a.k.a. @@security-controlpanel)
        settings.
    """

    site = context.getSite()
    
    #site security setup!
    security = ISecuritySchema(site)
    security.enable_user_folders = True
    #secSchema.set_enable_self_reg(True)
    #secSchema.set_enable_user_pwd_choice(True)
    
