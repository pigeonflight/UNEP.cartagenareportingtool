from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from UNEP.cartagenareportingtool import MessageFactory as _


# Interface class; used to define content-type schema.

class ICountryReport(form.Schema, IImageScaleTraversable):
    """
    Country Report for Cartagena Convention
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/country_report.xml to define the content type.

    form.model("models/country_report.xml")

yes_no_inprep = SimpleVocabulary(
    [
     SimpleTerm(value=u'Yes', title=_(u'Yes')),
     SimpleTerm(value=u'No', title=_(u'No')),
     SimpleTerm(value=u'In Preparation', title=_(u'In Preparation'))
     ]
    )
yes_no_inprep_other = SimpleVocabulary(
    [
     SimpleTerm(value=u'Yes', title=_(u'Yes')),
     SimpleTerm(value=u'No', title=_(u'No')),
     SimpleTerm(value=u'In Preparation', title=_(u'In Preparation')),
     SimpleTerm(value=u'Other', title=_(u'Other'))
     ]
    )

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

class SampleView(grok.View):
    """ sample view class """

    grok.context(ICountryReport)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here


translatable_strings = [
_(u'Full Name of Reporting Institution'),
_(u'World'),
  ]