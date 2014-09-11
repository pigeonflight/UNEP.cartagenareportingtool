Cartagena Reporting Tool
===========================
Allows the submission of a country report based on the Cartagena template

WARNING: this product deletes your news, Members, events folders, DON'T USE if you care about these folders!!!!!

Special template.py.z tool
------------------------------
There is a special tool called 'template.py.z'
Which reads the 'models/country_report.xml' and generates
a python schema. We hope to build on this to make it easier
for us to deal with large forms.

Usage:

      python template.py.z > output.schema

The resulting output looks similar to this:

    country=schema.Choice(
    title = _(u"Country)",
               mapping={'placeholder':''}),
    required=False,
    source=vocabulary.countries
    )

    reporting_period_start=schema.Date(
    title = _(u"Reporting Period Start)",
               mapping={'placeholder':''}),
    required=False,

    )

The resulting schema is used in the 'country_report.py' file.

