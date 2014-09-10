from zope.interface import implements,Interface
from zope.component import adapts
import uuid

from plone.app.content.interfaces import INameFromTitle

class INameForCountryReport(Interface):
    """Return a custom title"""


class NameForCountryReport(object):
    implements(INameFromTitle)
    adapts(INameForCountryReport)

    def __init__(self, context):
        pass

    # based on this http://stackoverflow.com/questions/7974285/is-there-a-way-to-extend-plone-dexteritys-inamefromtitle-behavior
    def __new__(cls, context):
        title = str(uuid.uuid4())[:8]
        inst = super(NameForCountryReport, cls).__new__(cls)

        inst.title = title
        context.setTitle(title)

        return inst
