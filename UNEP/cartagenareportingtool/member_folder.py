from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable
from plone import api


from UNEP.cartagenareportingtool import MessageFactory as _


# Interface class; used to define content-type schema.

class IMemberFolder(form.Schema, IImageScaleTraversable):
    """
    Folder to hold reports
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/member_folder.xml to define the content type.

    form.model("models/member_folder.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class MemberFolder(Container):
    grok.implements(IMemberFolder)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# member_folder_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class MemberFolderView(grok.View):
    """ sample view class """

    grok.context(IMemberFolder)
    grok.require('zope2.View')

    grok.name('view')
     
    # Add view methods here
    def edit_country_report(self):
        """ determine if a report exists """
        all_reports = self.get_all_reports
        if len(all_reports) == 0:
            url = "++add++UNEP.cartagenareportingtool.countryreport"
        else:
            url = "%s/edit" % all_reports[0].id
        return url
        
    @property
    def member_path(self):
        current_user = api.user.get_current()
        return '/'.join(self.context.getPhysicalPath())
        
    @property
    def get_all_reports(self):
        catalog = api.portal.get_tool(name='portal_catalog')

        documents = catalog(
                  portal_type='UNEP.cartagenareportingtool.countryreport',
                  path={'query': self.member_path, 'depth': 1}
                  )
        return documents