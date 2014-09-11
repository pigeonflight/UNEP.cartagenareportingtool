# -*- coding: utf-8 -*-
#from CMFCore.utils import getToolByName
from plone import api
from Products.CMFPlone.interfaces import constrains
from plone.app.controlpanel.security import ISecuritySchema
import logging


PROFILE_ID='profile-UNEP.cartagenareportingtool:default'
PRODUCT = 'UNEP.cartagenareportingtool'

def setupVarious(context):
    if context.readDataFile('unep.cartagenareportingtool.marker.txt') is None:
        return
    
    setup = api.portal.get_tool(name='portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo')
    
    if not api.content.get('/news'):
        api.content.delete(api.content.get('/news'))
        api.content.delete(api.content.get('/Members'))
        api.content.delete(api.content.get('/events'))

    portal = api.portal.get()
    
    #check for the existence of reports folder
    #
    if not api.content.get('/r'):
        reports = api.content.create(
            portal,
            'Folder',
            id='r',
            title='Reports'
        )
        api.content.transition(reports, transition='publish')
        behavior = constrains.ISelectableConstrainTypes(reports)
        behavior.setConstrainTypesMode(constrains.ENABLED)
        behavior.setLocallyAllowedTypes(['UNEP.cartagenareportingtool.countryreport'])
        behavior.setImmediatelyAddableTypes(['UNEP.cartagenareportingtool.countryreport'])
    mp = api.portal.get_tool(name='portal_membership')
    # set type to custom member type
    mp.setMemberAreaType('UNEP.cartagenareportingtool.memberfolder')
    # set member folder name
    mp.setMembersFolderById('r')
    
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
    
