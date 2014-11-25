# -*- coding: utf-8 -*-
#from CMFCore.utils import getToolByName
from plone import api
from Products.CMFPlone.interfaces import constrains
from plone.app.controlpanel.security import ISecuritySchema
import logging
from zExceptions import BadRequest
import Globals


logger = logging.getLogger(__name__)

PROFILE_ID='profile-UNEP.cartagenareportingtool:default'
PRODUCT = 'UNEP.cartagenareportingtool'

def setupVarious(context):
    if context.readDataFile('unep.cartagenareportingtool.marker.txt') is None:
        return
    setup = api.portal.get_tool(name='portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo')
    
    if api.content.get('/news'):
        api.content.delete(api.content.get('/news'))
        logger.info('removed the news folder')
    if api.content.get('/Members'):
        api.content.delete(api.content.get('/Members'))
        logger.info('removed the Members folder')
    if api.content.get('/events'):   
        api.content.delete(api.content.get('/events'))
        logger.info('removed the events folder')

    portal = api.portal.get()

    # configure default site view to be 'site_index'
    portal.manage_changeProperties(default_page='site_index')
    portal.setLayout("site_index")
    logger.info('replaced the default front page of the site')
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
            logger.info('created custom memberfolder called %s' % memberfolder)
        except BadRequest:
            logger.info('unable to create custom memberfolder called %s' % memberfolder)
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
    
    mp.setMembersFolderById(memberfolder)
    logger.info("set members folder to %s" % memberfolder)
    
    # call update security 
    set_up_security(context)
    set_up_users(context)
    logger.info("created memberstate user accounts")

def set_up_users(context):
    memberstates = context.readDataFile('memberstates.csv')
    
    # we assume that he file has a heading
    # the [1:] at the end slices off the heading of the file
    for member in memberstates.splitlines()[1:]:
        member = member.split(',')

        properties = dict(
            fullname=member[4],
            location=member[5],
            description=member[6]
            )
        username = member[0]
        email = member[3]
        if '@' not in email:
            email = "changeme@example.com"
        print "using: ",email
        if Globals.DevelopmentMode:
            user = api.user.create(
                      username=username,
                      email=email,
                      password='password',
                      properties=properties,
                    )
        else:
            user = api.user.create(
                      username=username,
                      email=email,
                      properties=properties,
                    )

def set_up_security(context):
    """ Enable/disable security controlpanel (a.k.a. @@security-controlpanel)
        settings.
    """

    site = context.getSite()
    
    #site security setup!
    security = ISecuritySchema(site)
    security.enable_user_folders = True
    security.set_enable_self_reg(True)
    security.set_enable_user_pwd_choice(True)
    
