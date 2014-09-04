from plone.supermodel import model

class INumberSchema(model.Schema):
    """Schema for dict rows used in DataGridFields
    """
#
    model.load("models/number.xml")
