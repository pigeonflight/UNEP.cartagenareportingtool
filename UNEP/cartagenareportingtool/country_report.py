from five import grok

from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from z3c.form.browser.radio import RadioFieldWidget

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Interface
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model
from plone import api


from UNEP.cartagenareportingtool.member_folder import IMemberFolder
from UNEP.cartagenareportingtool import MessageFactory as _
from UNEP.cartagenareportingtool import vocabulary
from interface import INumberSchema, ICountryReport
from zope.lifecycleevent.interfaces import IObjectAddedEvent, IObjectCreatedEvent

#from z3c.form import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.api.exc import UserNotFoundError
from AccessControl import getSecurityManager


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

    
    
class CountryReport(Item):
    grok.implements(ICountryReport)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# country_report_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(dexterity.DisplayForm):
    """  view class """

    grok.context(ICountryReport)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
    def can_edit_report(self):
        user = api.user.get_current()
        try:
            permissions = api.user.get_permissions(username=user.id, 
                              obj=self.context) 
            can_edit = permissions['Modify portal content']           
        except UserNotFoundError:
            # check if they are an admin
            user = getSecurityManager().getUser()
            can_edit = 'Manager' in user.getRoles() 
        return can_edit
        
        
    def edit_report(self):
        """ determine if a report exists """
        url = "%s/edit" % self.context.absolute_url()
        return url

    def state(self):
        return api.content.get_state(self.context)

    def is_submitted(self):
        return self.state() == "submitted"
    
    @property    
    def submit_report_form(self):
        return "%s/%s" % (self.context.absolute_url(),'submit-report')
    
    @property    
    def submit_report(self):
        return "%s/%s" % (self.context.absolute_url(),'submit')
        
    @property    
    def reopen_report(self):
        return "%s/%s" % (self.context.absolute_url(),'reopen')
    
class Submit(grok.View):
    grok.context(ICountryReport)
    grok.name('submit')
    def render(self):
        # transition
        form_items = self.request.form.items()
        form_items = dict(form_items)
        self.context.public_consent = form_items['make-report-public']
        state_info = {}
        state_info['initial_state'] = api.content.get_state(self.context)
        api.content.transition(obj=self.context,transition='submit')
        state_info['new_state'] = api.content.get_state(self.context)
        self.request.response.setHeader("Content-type","application/json")
        return {"message":"""
                 the initial state was '%(initial_state)s' and the new state is
                '%(new_state)s'
                """ % state_info}

class SubmitReport(grok.View):
    grok.context(ICountryReport)
    grok.name('submit-report')
    
    @property    
    def submit_report(self):
        return "%s/%s" % (self.context.absolute_url(),'submit')
        
    def submit_action(self):
    # transition
        state_info = {}
        state_info['initial_state'] = api.content.get_state(self.context)
        api.content.transition(obj=self.context,transition='submit')
        state_info['new_state'] = api.content.get_state(self.context)
        self.request.response.setHeader("Content-type","application/json")
        return {"message":"""
                 the initial state was '%(initial_state)s' and the new state is
                '%(new_state)s'
                """ % state_info}

class Reopen(grok.View):
    grok.context(ICountryReport)
    grok.name('reopen')
    def render(self):
        # transition
        state_info = {}
        state_info['initial_state'] = api.content.get_state(self.context)
        api.content.transition(obj=self.context,transition='reopen')
        state_info['new_state'] = api.content.get_state(self.context)
        return {"message":"""
                 the initial state was '%(initial_state)s' and the new state is
                '%(new_state)s'
                """ % state_info}
            
class EditForm(dexterity.EditForm):
    grok.context(ICountryReport)
    #grok.template('edit')
    
    #groups = (TestGroup,)
    
    def __call__(self):
        self.request.set('disable_border', 1)
        return super(EditForm, self).__call__()
    

class AddForm(dexterity.AddForm):
    """ custom add form """
    grok.name('UNEP.cartagenareportingtool.country_report')
#
@grok.subscribe(IMemberFolder, IObjectAddedEvent)
def add_report_to_member_folder(folder, event):
    obj = api.content.create(
    type='UNEP.cartagenareportingtool.countryreport',
    title='Country Report',
    container=folder)

@grok.subscribe(ICountryReport, IObjectAddedEvent)
def add_default_country(item, event):
    value = item.absolute_url_path().split('/')[-2]
    try:
        term = vocabulary.countries.getTerm(value)
        item.default_country = term.value
    except LookupError:
        pass
        
    

#@form.default_value(field=ICountryReport['default_country'])
#def countryDefaultValue(data):
#    
#    return u'JAM'
