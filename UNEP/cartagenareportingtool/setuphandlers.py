# -*- coding: utf-8 -*-

from plone import api
from Products.CMFPlone.interfaces import constrains


def setupVarious(context):

    if context.readDataFile('unep.marker.txt') is None:
        return

    api.content.delete(api.content.get('/news'))
    api.content.delete(api.content.get('/Members'))
    api.content.delete(api.content.get('/front-page'))
    api.content.delete(api.content.get('/events'))

    portal = api.portal.get()
    
    #check for the existence of meetings and documents
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
        behavior.setLocallyAllowedTypes(['UNEP.cartagenareportingtool.memberfolder'])
        behavior.setImmediatelyAddableTypes(['UNEP.cartagenareportingtool.memberfolder'])