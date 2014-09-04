from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

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

