from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from UNEP.cartagenareportingtool import MessageFactory as _

yes_no = SimpleVocabulary.fromValues(
    [
     'Yes','No'
     ]
    )
yes_no_inprep = SimpleVocabulary.fromValues(
    [
     'Yes','No','In Preparation'
     ]
    )

yes_no_inprep_other = SimpleVocabulary.fromValues(
    [
     'Yes','No','In Preparation','Other'
     ]
    )
yes_no_inprep_existingplans = SimpleVocabulary.fromValues(
    [
     'Yes','No','In Preparation','Existing Plans'
     ]
    )
plans = SimpleVocabulary.fromValues(
   [
  _(u'National Contingency Plans'),
  _(u'Regional Contingency Plans'),
  _(u'Cooperation with Contracting Parties')
]
)
phone_type = SimpleVocabulary.fromValues(
    (
    _(u'phone'),
    _(u'fax'),
    _(u'other'),
    )
 )
protocols = SimpleVocabulary.fromValues(
  (
    _(u'Cartagena Convention and the Oil Spill Protocol'),
    _(u'SPAW Protocol'),
    _(u'LBS Protocol'),
  )
)

countries = SimpleVocabulary.fromValues(
      (
  _(u'Antigua & Barbuda'),
  _(u'Aruba'),
  _(u'Bahamas'),
  _(u'Barbados'),
  _(u'Belize'),
  _(u'Bermuda'),
  _(u'Bonaire'),
  _(u'British Virgin Islands'),
  _(u'Cayman Islands'),
  _(u'Colombia'),
  _(u'Costa Rica'),
  _(u'Cuba'),
  _(u'Curacao'),
  _(u'Dominica'),
  _(u'Dominican Republic'),
  _(u'Grenada'),
  _(u'Guatemala'),
  _(u'Guyana'),
  _(u'Haiti'),
  _(u'Honduras'),
  _(u'Jamaica'),
  _(u'Mexico'),
  _(u'Netherlands Antilles'),
  _(u'Nicaragua'),
  _(u'Panama'),
  _(u'St. Kitts & Nevis'),
  _(u'Saint Lucia'),
  _(u'St. Vincent & the Grenadines'),
  _(u'Suriname'),
  _(u'Trinidad & Tobago'),
  _(u'Turks & Caicos Islands'),
  _(u'United States of America'),
  _(u'US Virgin Islands'),
  _(u'Venezuela'),
))
