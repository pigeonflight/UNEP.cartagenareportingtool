# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from UNEP.cartagenareportingtool import MessageFactory as _

yes_no = SimpleVocabulary.fromValues(
    [
     _(u'Yes'),_(u'No')
     ]
    )
yes_no_inprep = SimpleVocabulary.fromValues(
    [
     _(u'Yes'),_(u'No'),_(u'In Preparation')
     ]
    )

yes_no_inprep_other = SimpleVocabulary.fromValues(
    [
     _(u'Yes'),_(u'No'),_(u'In Preparation'),_(u'Other')
     ]
    )
yes_no_inprep_existingplans = SimpleVocabulary.fromValues(
    [
     _(u'Yes'),_(u'No'),_(u'In Preparation'),_(u'Existing Plans')
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
legal_status = SimpleVocabulary.fromValues(
  (
  _(u'designated'),
  _(u'proposed'),
  _(u'other'),
    )
  )
status_of_management_plan = SimpleVocabulary.fromValues(
  (
    _(u'does not exist'),
    _(u'exists'),
    _(u'in preparation'),
    )
  )
protocols = SimpleVocabulary.fromValues(
  (
    _(u'Cartagena Convention and the Oil Spill Protocol'),
    _(u'SPAW Protocol'),
    _(u'LBS Protocol'),
  )
)

countries = SimpleVocabulary.fromItems((
      (_(u'Anguilla'),'AIA'),
      (_(u'Antigua and Barbuda'),'ATG'),
      (_(u'Aruba'),'ABW' ),
      (_(u'Bahamas'),'BHS'),
      (_(u'Barbados'),'BRB'),
      (_(u'Belize'),'BLZ'),
      (_(u'Bermuda'),'BMU'),
      (_(u'Bonaire, Saint Eustatius and Saba'),'BES'),
      (_(u'British Virgin Islands'),'VGB'),
      (_(u'Cayman Islands'),'CYM'),
      (_(u'Colombia'),'COL'),
      (_(u'Costa Rica'),'CRI'),
      (_(u'Cuba'),'CUB'),
      (_(u'Curacao'),'CUW'),
      (_(u'Dominica'),'DMA'),
      (_(u'Dominican Republic'),'DOM'),
      (_(u'France'),'FRA'),
      (_(u'French Guiana'),'GUF'),
      (_(u'Grenada'),'GRD'),
      (_(u'Guadeloupe'),'GLP'),
      (_(u'Guatemala'),'GTM'),
      (_(u'Guyana'),'GUY'),
      (_(u'Haiti'),'HTI'),
      (_(u'Honduras'),'HND'),
      (_(u'Jamaica'),'JAM'),
      (_(u'Martinique'),'MTQ'),
      (_(u'Mexico'),'MEX'),
      (_(u'Montserrat'),'MSR'),
      (_(u'Nicaragua'),'NIC'),
      (_(u'Netherlands'),'NLD'),
      (_(u'Panama'),'PAN'),
      (_(u'Puerto Rico'),'PRI'),
      (_(u'Saint-Barthelemy'),'BLM'),
      (_(u'Saint Kitts and Nevis'),'KNA'),
      (_(u'Saint Lucia'),'LCA'),
      (_(u'Saint-Martin (French part)'),'MAF'),
      (_(u'Saint Vincent and the Grenadines'),'VCT'),
      (_(u'Sint Maarten (Dutch part)'),'SXM'),
      (_(u'Suriname'),'SUR'),
      (_(u'Trinidad and Tobago'),'TTO'),
      (_(u'Turks and Caicos Islands'),'TCA'),
      (_(u'United Kingdom of Great Britain and Northern Ireland'),'GBR'),
      (_(u'United States of America'),'USA'),
      (_(u'United States Virgin Islands'),'VIR'),
      (_(u'Venezuela (Bolivarian Republic of)'),'VEN')  
     ))