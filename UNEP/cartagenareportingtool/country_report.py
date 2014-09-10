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


from UNEP.cartagenareportingtool import MessageFactory as _
from UNEP.cartagenareportingtool import vocabulary
from interface import INumberSchema, ICountryReport


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
    def edit_report(self):
        """ determine if a report exists """
        url = "%s/edit" % self.context.absolute_url()
        return url

class EditForm(dexterity.EditForm):
    grok.context(ICountryReport)
    #grok.template('edit')
    
    def __call__(self):
        self.request.set('disable_border', 1)
        return super(EditForm, self).__call__()
    

class AddForm(dexterity.AddForm):
    """ custom add form """
    grok.name('UNEP.cartagenareportingtool.country_report')
#

"""
    "national_focal_point_contact_person",
    "national_focal_point_job_title",
    "national_focal_point_department",
    "national_focal_point_address",
    "national_focal_point_telephone",
    "national_focal_point_email",
    "national_focal_point_website",
    "national_agency_ministry_institution",
     "national_agency_name_of_organization",
    "national_agency_contact_person",
    "national_agency_job_title",
    "national_agency_department",
    "national_agency_address",
    "national_agency_telephone",
    "national_agency_email",
    "national_agency_website"]
"""
