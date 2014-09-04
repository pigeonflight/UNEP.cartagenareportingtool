from Products.CMFCore.utils import getToolByName
try:
    from  os import SEEK_END
except ImportError:
    from posixfile import SEEK_END
import urllib

from zope.component import adapter, getMultiAdapter
from zope.interface import implementer, implements, implementsOnly
from zope.size import byteDisplay

from z3c.form.interfaces import IFieldWidget, IFormLayer, IDataManager, NOVALUE
from z3c.form.widget import FieldWidget
from z3c.form.browser import text

from .interfaces import ITwoLineField,ITwoLineWidget
from plone.namedfile.utils import safe_basename, set_headers, stream_data


from Products.Five.browser import BrowserView
from zope.publisher.interfaces import IPublishTraverse, NotFound

from Acquisition import Explicit, aq_inner

from ZPublisher.HTTPRequest import FileUpload

class TwoLineWidget(text.TextWidget):
    """A widget for a two line 
    """
    implementsOnly(ITwoLineWidget)

    klass = u'two-line-widget'
    value = None # don't default to a string

    @property
    def allow_nochange(self):
        return not self.ignoreContext and \
                   self.field is not None and \
                   self.value is not None and \
                   self.value != self.field.missing_value



    def action(self):
        action = self.request.get("%s.action" % self.name, "nochange")
        if hasattr(self.form, 'successMessage') and self.form.status == self.form.successMessage:
            # if form action completed successfully, we want nochange
            action = 'nochange'
        return action

    def extract(self, default=NOVALUE):
        action = self.request.get("%s.action" % self.name, None)
        if self.request.get('PATH_INFO', '').endswith('kss_z3cform_inline_validation'):
            action = 'nochange'

        if action == 'remove':
            return None
        elif action == 'nochange':
            if self.ignoreContext:
                return default
            dm = getMultiAdapter((self.context, self.field,), IDataManager)
            # For sub-widgets to function use a query() not get()
            return dm.query(default)



@implementer(IFieldWidget)
@adapter(ITwoLineField, IFormLayer)
def TwoLineWidget(field, request):
    return FieldWidget(field,TwoLineWidget(request))
