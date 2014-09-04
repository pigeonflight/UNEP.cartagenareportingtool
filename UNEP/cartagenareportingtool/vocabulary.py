from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

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
