from z3c.form.interfaces import ITextWidget
from zope import schema
from zope.schema.interfaces import IObject

class ITwoLineField(IObject):
    """A field for a two line
    """

class ITwoLineWidget(ITextWidget):
    """A widget for a two line
    """
    name = schema.TextLine(title=u"Name of reporting officer", required=False)
    title = schema.TextLine(title=u"Title of reporting officer", required=False)
