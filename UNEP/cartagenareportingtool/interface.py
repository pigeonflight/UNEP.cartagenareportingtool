from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import invariant, Interface, Invalid
from plone.directives import dexterity, form
from zope import schema
from UNEP.cartagenareportingtool import MessageFactory as _
from UNEP.cartagenareportingtool import vocabulary
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from plone.supermodel import model
from z3c.form import field, group

class INumberSchema(Interface):
    phone_type = schema.Choice(
                     title=_(u"Type"),
                     required=False,
                     source=vocabulary.phone_type,
                        )
    number = schema.TextLine(
                     title=_(u"Number"),
                     required=False,
                        )
class IStatusSchema(Interface):
    protocol = schema.Choice(
                     title=_(u"Protocol"),
                     required=False,
                     source=vocabulary.protocols,
                        )
    status = schema.TextLine(
                     title=_(u"Status"),
                     required=False,
                        )

schema1 = []
schema2 = []
schema3 = []
schema4 = []
schema5 = []
schema6 = []
schema7 = []
schema8 = []
schema9 = []       

class ICountryReport(form.Schema, IImageScaleTraversable):
    
    # default schema
    form.mode(title='hidden')
    title = schema.TextLine(
        title = _(u'Title'),
        required = False,
    )
    country=schema.Choice(
    title = _(u"Country",
               mapping={'number':''}),
    required=False,
    source=vocabulary.countries
    )
    reporting_period_start=schema.Date(
    title = _(u"Reporting Period Start",
               mapping={'number':''}),
    required=False,
    
    )
    reporting_period_end=schema.Date(
    title = _(u"Reporting Period End",
               mapping={'number':''}),
    required=False,
    
    )
    full_name_of_reporting_institution=schema.TextLine(
    title = _(u"Full name of reporting institution",
               mapping={'number':''}),
    required=False,
    
    )
    reporting_officer_name=schema.TextLine(
    title = _(u"Name and Title of reporting officer",
               mapping={'number':''}),
    required=False,
    
    )
    agency=schema.TextLine(
    title = _(u"Agency",
               mapping={'number':''}),
    required=False,
    
    )
    mailing_address=schema.Text(
    title = _(u"Mailing Address",
               mapping={'number':''}),
    required=False,
    
    )
    form.widget(telephone=DataGridFieldFactory)
    telephone = schema.List(
    title=_(u"Telephone"),
    readonly=False,
    min_length=1,
    value_type=DictRow(
            title=_(u"Number"),
            schema=INumberSchema
            )
    )
    email=schema.TextLine(
    title = _(u"E-mail",
               mapping={'number':''}),
    required=False,
    
    )
    web_page=schema.TextLine(
    title = _(u"Webpage",
               mapping={'number':''}),
    required=False,
    
    )
    date_the_report_was_submitted=schema.Date(
    title = _(u"Date the report was submitted",
               mapping={'number':''}),
    required=False,
    
    )
    signature=schema.TextLine(
    title = _(u"Signature",
               mapping={'number':''}),
    required=False,
    
    )

    # schema1
    schema1.append('does_your_country_have_a_designated_national_focal_point_for_the_cartagena_convention_')
    form.widget(does_your_country_have_a_designated_national_focal_point_for_the_cartagena_convention_=RadioFieldWidget)
    does_your_country_have_a_designated_national_focal_point_for_the_cartagena_convention_=schema.Choice(
    title = _(u"Does your country have a designated National Focal Point for the Cartagena Convention?",
               mapping={'number':'1.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema1.append('national_focal_point_name_of_organization')
    national_focal_point_name_of_organization=schema.TextLine(
    title = _(u"National Focal Point:Name of Organization",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_contact_person')
    national_focal_point_contact_person=schema.TextLine(
    title = _(u"National Focal Point:Contact Person",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_job_title')
    national_focal_point_job_title=schema.TextLine(
    title = _(u"National Focal Point:Job Title",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_department')
    national_focal_point_department=schema.TextLine(
    title = _(u"National Focal Point:Department",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_address')
    national_focal_point_address=schema.Text(
    title = _(u"National Focal Point:Address",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_telephone')
    national_focal_point_telephone=schema.TextLine(
    title = _(u"National Focal Point:Telephone",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_email')
    national_focal_point_email=schema.TextLine(
    title = _(u"National Focal Point:Email",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_focal_point_website')
    national_focal_point_website=schema.TextLine(
    title = _(u"National Focal Point:Website",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('designated_national_agency_ministry_institution')
    form.widget(designated_national_agency_ministry_institution=RadioFieldWidget)
    designated_national_agency_ministry_institution=schema.Choice(
    title = _(u"Does your country have a designated National Agency/Ministry/Institution or other appropriate authority for coordinating the implementation of the Cartagena Convention (Article 15, paragraph 2)?",
               mapping={'number':'2.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema1.append('national_agency_name_of_organization')
    national_agency_name_of_organization=schema.TextLine(
    title = _(u"National Agency/Ministry:Name of Organization",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_contact_person')
    national_agency_contact_person=schema.TextLine(
    title = _(u"National Agency/Ministry:Contact Person",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_job_title')
    national_agency_job_title=schema.TextLine(
    title = _(u"National Agency/Ministry:Job Title",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_department')
    national_agency_department=schema.TextLine(
    title = _(u"National Agency/Ministry:Department",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_address')
    national_agency_address=schema.Text(
    title = _(u"National Agency/Ministry:Address",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_telephone')
    national_agency_telephone=schema.TextLine(
    title = _(u"National Agency/Ministry:Telephone",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_email')
    national_agency_email=schema.TextLine(
    title = _(u"National Agency/Ministry:Email",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('national_agency_website')
    national_agency_website=schema.TextLine(
    title = _(u"National Agency/Ministry:Website",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('implementation_plans')
    form.widget(implementation_plans=RadioFieldWidget)
    implementation_plans=schema.Choice(
    title = _(u"Has your country developed an implementation plans(s) to carry out the general obligations of the Cartagena Convention? (Article 4)",
               mapping={'number':'3.'}),
    required=False,
    source=vocabulary.yes_no_inprep_existingplans
    )
    schema1.append('if_yes_brief_details_of_main_implementation_plans_article4')
    if_yes_brief_details_of_main_implementation_plans_article4=schema.Text(
    title = _(u"If yes or in preparation, please provide brief details of all of the main implementation plan(s) that are developed and/or being used in your country, or that are in preparation.",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('if_why_no_plans_article4')
    if_why_no_plans_article4=schema.Text(
    title = _(u"If no, please describe why not.",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('if_plans_exist_article4')
    if_plans_exist_article4=schema.Text(
        title = _(u"If plans exist, please specify what existing frameworks are being used for implementation of the Convention.",
                    mapping={'number':''}),
        required=False,
        )
    schema1.append('has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans')
    form.widget(has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans=RadioFieldWidget)
    has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans=schema.Choice(
    title = _(u"Has your country received any external financial assistance to develop and/or implement existing plan(s)?",
               mapping={'number':'4.'}),
    required=False,
    source=vocabulary.yes_no
    )

    schema1.append('if_yes_please_identify_the_source_external_financial_assistance')
    if_yes_please_identify_the_source_external_financial_assistance=schema.TextLine(
    title = _(u"If yes, please identify the source of the assistance.",
               mapping={'number':''}),
    required=False,
    
    )
    schema1.append('if_no_please_state_why_not_financial_assistance')
    if_no_please_state_why_not_financial_assistance=schema.TextLine(
    title = _(u"If no, please state why not.",
               mapping={'number':''}),
    required=False,
    
    )

    schema1.append('difficulties_in_the_implementation_of_plan_s_')
    form.widget(difficulties_in_the_implementation_of_plan_s_=RadioFieldWidget)
    difficulties_in_the_implementation_of_plan_s_=schema.Choice(
    title = _(u"Has your country experienced any difficulties in the implementation of the above-mentioned plan(s)?",
               mapping={'number':'5.'}),
    required=False,
    source=vocabulary.yes_no
    )
    schema1.append('if_why_implementation_difficulties_with_details')
    if_why_implementation_difficulties_with_details=schema.TextLine(
    title = _(u"If yes, please describe why with details.",
               mapping={'number':''}),
    required=False,
    
    )
    
    # ====================== schema2 ==========================
    schema2.append('is_there_a_national_definition_for_pollution_sources')
    form.widget(is_there_a_national_definition_for_pollution_sources=RadioFieldWidget)
    is_there_a_national_definition_for_pollution_sources=schema.Choice(
    title = _(u"Is there a national definition within existing pollution related legislation or regulations for 'Pollution from Ships', 'Discharging or Dumping of wastes at sea', 'Exploration or Exploitation of the  Sea-Bed Activities', and 'Discharges (emissions) to the Atmosphere' (Articles 5, 6, 8, 9)?",
               mapping={'number':'1.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema2.append('if_yes_to_pollution_definitions_discharges_from_ships')
    if_yes_to_pollution_definitions_discharges_from_ships=schema.Text(
    title = _(u"Discharges from ships:"),
    required=False,
    )
    schema2.append('if_yes_to_pollution_definitions_dumping_of_wastes_and_other_matter_at_sea')
    if_yes_to_pollution_definitions_dumping_of_wastes_and_other_matter_at_sea=schema.Text(
    title = _(u"Dumping of wastes and other matter at sea:"),
    required=False,
    )
    schema2.append('if_yes_to_pollution_definitions_exploration_or_exploitation_of_sea_bed')
    if_yes_to_pollution_definitions_exploration_or_exploitation_of_sea_bed=schema.Text(
    title = _(u"Exploration or exploitation of the sea-bed:"),
    required=False,
    )
    schema2.append('if_yes_to_pollution_definitions_discharges_air_emissions_into_atmosphere')
    if_yes_to_pollution_definitions_discharges_air_emissions_into_atmosphere=schema.Text(
    title = _(u"Discharges (air emissions) into the atmosphere:"),
    required=False,
    )
    schema2.append('management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area')
    form.widget(management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area=RadioFieldWidget)
    management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area=schema.Choice(
    title = _(u"${number} Has your country taken any measures since the last reporting period necessary to prevent, reduce and control the abovementioned sources of pollution in the Convention area? ",
               mapping={'number':'2.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema2.append('if_yes_details_of_pollution_source_management_action_since_last_reporting_period')
    if_yes_details_of_pollution_source_management_action_since_last_reporting_period=schema.Text(
    title = _(u"If yes or in preparation, please provide the details of the major actions taken since the last reporting period",
               mapping={'number':''}),
    required=False,
    )
    schema2.append('if_no_why_no_action_since_last_reporting_period')
    if_no_why_no_action_since_last_reporting_period=schema.Text(
    title = _(u"If no, briefly state why not.",
               mapping={'number':''}),
    required=False, 
    )
    schema2.append('other_pollution_sources_or_types_that_may_affect_marine_resources')
    form.widget(other_pollution_sources_or_types_that_may_affect_marine_resources=RadioFieldWidget)
    other_pollution_sources_or_types_that_may_affect_marine_resources=schema.Choice(
    title = _(u"${number} Are there any other sources and/or types of pollution that may affect marine resources in the Convention area which require special consideration in your country?",
               mapping={'number':'3.'}),
    required=False,
    source=vocabulary.yes_no
    )
    schema2.append('if_yes_please_specify_answer_below')
    if_yes_please_specify_answer_below=schema.Text(
    title = _(u"If yes please specify and answer #${number} below",
               mapping={'number':'4'}),
    required=False,
    )
    schema2.append('policies_for_marine_pollution_management_for_special_consideration')
    form.widget(policies_for_marine_pollution_management_for_special_consideration=RadioFieldWidget)
    policies_for_marine_pollution_management_for_special_consideration=schema.Choice(
    title = _(u"Does your country have any national policies for marine pollution prevention, reduction and control for these activities requiring special consideration?",
               mapping={'number':'4.'}),
    required=False,
    source=vocabulary.yes_no_inprep_other
    )
    schema2.append('if_yes_policies_please_provide_details')
    if_yes_policies_please_provide_details=schema.Text(
    title=_(u"If yes or in preparation, please provide brief details."),
    required=False,
    )
    schema2.append('if_yes_policy_website_for_marine_pollution')
    if_yes_policy_website_for_marine_pollution=schema.TextLine(
    title = _(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country.",
               mapping={'number':''}),
    required=False,
    )
    schema2.append('if_no_policies_why_not_for_marine_pollution')
    if_no_policies_why_not_for_marine_pollution=schema.Text(
    title = _(u"If no, describe why not.",
               mapping={'number':''}),
    required=False,    
    )
    schema2.append('if_other_specify')
    if_other_specify=schema.Text(
    title = _(u"If other, specify.",
               mapping={'number':''}),
    required=False,
    )
    schema2.append('laws_for_marine_pollution_management_for_special_consideration')
    form.widget(laws_for_marine_pollution_management_for_special_consideration=RadioFieldWidget)
    laws_for_marine_pollution_management_for_special_consideration=schema.Choice(
    title = _(u"Does your country have any national laws for marine pollution prevention, reduction and control for these activities requiring special consideration?",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep_other
    )
    schema2.append('if_yes_laws_please_provide_details')
    if_yes_laws_please_provide_details=schema.Text(
    title=_(u"If yes or in preparation, please provide brief details."),
    required=False,
    )
    schema2.append('if_yes_laws_website_for_marine_pollution')
    if_yes_laws_website_for_marine_pollution=schema.TextLine(
    title = _(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country.",
               mapping={'number':''}),
    required=False,
    )
    schema2.append('if_no_laws_why_not_for_marine_pollution')
    if_no_laws_why_not_for_marine_pollution=schema.Text(
    title = _(u"If no, describe why not.",
               mapping={'number':''}),
    required=False,    
    )
    schema2.append('if_other_laws_specify')
    if_other_laws_specify=schema.Text(
    title = _(u"If other, specify.",
               mapping={'number':''}),
    required=False,
    )
    schema2.append('plans_for_marine_pollution_management_for_special_consideration')
    form.widget(plans_for_marine_pollution_management_for_special_consideration=RadioFieldWidget)
    plans_for_marine_pollution_management_for_special_consideration=schema.Choice(
    title = _(u"Does your country have any national plans for marine pollution prevention, reduction and control for these activities requiring special consideration?",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema2.append('if_yes_plans_please_provide_details')
    if_yes_plans_please_provide_details=schema.Text(
    title=_(u"If yes or in preparation, please provide brief details."),
    required=False,
    )
    schema2.append('if_yes_plans_website_for_marine_pollution')
    if_yes_plans_website_for_marine_pollution=schema.TextLine(
    title = _(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country.",
               mapping={'number':''}),
    required=False,
    )
    schema2.append('if_no_plans_why_not_for_marine_pollution')
    if_no_plans_why_not_for_marine_pollution=schema.Text(
    title = _(u"If no, describe why not.",
               mapping={'number':''}),
    required=False,    
    )
    schema2.append('if_other_plans_specify')
    if_other_plans_specify=schema.Text(
    title = _(u"If other, specify.",
               mapping={'number':''}),
    required=False,
    )

    # ========================= schema3
    schema3.append('pollution_emergencies_in_the_convention_area')
    form.widget(pollution_emergencies_in_the_convention_area=RadioFieldWidget)
    pollution_emergencies_in_the_convention_area=schema.Choice(
    title = _(u"Has your country experienced any pollution emergencies in the Convention area (including emergencies in which the Convention area is in imminent danger of being polluted or already polluted)?",
               mapping={'number':'1.'}),
    required=False,
    source=vocabulary.yes_no
    )
    
    schema3.append('if_yes_describe_pollution_emergencies')
    if_yes_describe_pollution_emergencies=schema.Text(
    title = _(u"If yes, please describe the details and answer the question below. ",
               mapping={'number':''}),
    required=False,
    )
    schema3.append('if_yes_provide_a_website_url_pollution_emergencies')
    if_yes_provide_a_website_url_pollution_emergencies=schema.TextLine(
    title = _(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country.",
               mapping={'number':''}),
    required=False,
    )
    schema3.append('response_to_emergencies')
    form.widget(response_to_emergencies=CheckBoxFieldWidget)
    response_to_emergencies=schema.List(
    title = _(u"In regards to the question above, did your country respond to the situation through any of the following:",
               mapping={'number':'2.'}),
    required=False,
    value_type=schema.Choice(source=vocabulary.plans)
    
    )
    
    schema3.append('if_cooperation_contracting_parties_and_experience')
    if_cooperation_contracting_parties_and_experience=schema.Text(
    title = _(u"If cooperation took place with other Contracting Parties, please specify the name of Contracting Parties you have worked with and briefly describe the experience.",
               mapping={'number':''}),
    required=False,
    )
    schema3.append('if_yes_provide_a_website_url_response_to_situation')
    if_yes_provide_a_website_url_response_to_situation=schema.TextLine(
    title = _(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country."),
    required=False,
    )
    schema3.append('if_no_response_to_emergencies')
    if_no_response_to_emergencies=schema.Text(
     title = _(u"If no, describe why not"),
     required=False,
     )
    schema3.append('jointly_developed_and_promoted_contingency_plans')
    form.widget(jointly_developed_and_promoted_contingency_plans=RadioFieldWidget)
    jointly_developed_and_promoted_contingency_plans=schema.Choice(
    title = _(u"Has your country, jointly with another country or with other countries, developed and promoted any contingency plans for responding to incidents involving pollution or the threat thereof in the Convention area?",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no
    )
    schema3.append('if_yes_list_contingency_plans_developed')
    if_yes_list_contingency_plans_developed=schema.Text(
        title=_(u"If yes, please list the contingency plans developed and the countries involved."),
        required=False,
    )
    schema3.append('if_yes_provide_a_website_url_jointly_developed_and_promoted_contingency_plans')
    if_yes_provide_a_website_url_jointly_developed_and_promoted_contingency_plans=schema.TextLine(
        title=_(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country."),
        required=False,
    )

    # ========================= schema4
    schema4.append('technical_guidelines_to_assist_planning_of_major_development_projects')
    form.widget(technical_guidelines_to_assist_planning_of_major_development_projects=RadioFieldWidget)
    technical_guidelines_to_assist_planning_of_major_development_projects=schema.Choice(
        title = _(u"Does your country currently have any technical and other guidelines (e.g., EIAs) to assist the planning of major development projects in such a way as to prevent or minimize harmful impacts on the Convention Area?",
               mapping={'number':'1. '}),
        required=False,
        source=vocabulary.yes_no_inprep_other
    )
    schema4.append('if_yes_or_in_preparation_please_provide_brief_details_technical_guidelines_to_assist_planning_of_major_development_projects')
    if_yes_or_in_preparation_please_provide_brief_details_technical_guidelines_to_assist_planning_of_major_development_projects=schema.Text(
        title=_(u"If yes or in preparation, please provide brief details."),
        required=False,
    )
    schema4.append('if_yes_provide_a_website_url_technical_guidelines_to_assist_planning_of_major_development_projects')
    if_yes_provide_a_website_url_technical_guidelines_to_assist_planning_of_major_development_projects=schema.TextLine(
        title=_(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country."),
        required=False,
    )
    schema4.append('if_no_describe_why_not_technical_guidelines_to_assist_planning')
    if_no_describe_why_not_technical_guidelines_to_assist_planning=schema.Text(
        title=_(u"If no, describe why not."),
        required=False)

    # ======================== schema5 
    schema5.append('technical_cooperation_agreements')
    form.widget(technical_cooperation_agreements=RadioFieldWidget)
    technical_cooperation_agreements=schema.Choice(
    title = _(u"Does your country have technical cooperation agreements with any other Contracting Parties relating to the purposes of the Convention?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no
    )

    ###########
    schema5.append('status_of_ratification_of_the_existing_protocols')
    form.widget(status_of_ratification_of_the_existing_protocols=RadioFieldWidget)
    status_of_ratification_of_the_existing_protocols=schema.Choice(
    title = _(u"Please indicate the status of ratification/accession of the existing Protocols to the Cartagena Convention.",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )

    schema5.append('if_yes_please_provide_the_names_of_cooperative_agreements')
    if_yes_please_provide_the_names_of_cooperative_agreements=schema.Text(
        title=_(u"If yes, please provide the names of cooperating parties with areas of cooperation covered by the agreements."),
        required=False)
    
    schema5.append('if_yes_provide_a_website_url_cooperative_agreements')
    if_yes_provide_a_website_url_cooperative_agreements=schema.Text(
        title=_(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country."),
        required=False
        )
    schema5.append('if_no_describe_areas_in_which_such_agreements_desired')
    if_no_describe_areas_in_which_such_agreements_desired=schema.Text(
        title=_(u"If no, describe areas in which such agreements are desired."),
        required=False
        )
    schema5.append('if_other_specify_cooperative_agreements')
    if_other_specify_cooperative_agreements=schema.Text(
    title = _(u"If other, specify.",
               mapping={'number':''}),
    required=False,
    )
   
    # ==================== schema6
    schema6.append('please_indicate_the_status_of_ratification_of_existing_protocols')
    form.widget(please_indicate_the_status_of_ratification_of_existing_protocols=DataGridFieldFactory)
    please_indicate_the_status_of_ratification_of_existing_protocols = schema.List(
    title=_(u"Please indicate the status of ratification/accession of the existing Protocols to the Cartagena Convention."),
    readonly=False,
    min_length=1,
    value_type=DictRow(
            title=_(u"Status"),
            schema=IStatusSchema
            )
    )
    schema6.append('if_country_not_yet_ratified_to_cartagena_convention_summary_of_efforts')
    if_country_not_yet_ratified_to_cartagena_convention_summary_of_efforts = schema.Text(
        title=_(u"If your country has not yet ratified/acceded to the Cartagena Convention or any of the Protocols listed above, please provide a summary of efforts towards ratification/accession"),
        required=False,
    )
    schema6.append('if_yes_provide_a_website_url_summary_of_efforts_to_ratify')
    if_yes_provide_a_website_url_summary_of_efforts_to_ratify=schema.Text(
        title=_(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country."),
        required=False
        )

    schema6.append('plans_to_propose_amendments_to_the_convention')
    form.widget(plans_to_propose_amendments_to_the_convention=RadioFieldWidget)
    plans_to_propose_amendments_to_the_convention=schema.Choice(
    title = _(u"Does your country currently have any plan to propose any amendments to the Cartagena Convention?",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no
    )
    schema6.append('if_yes_provide_a_website_url_a_brief_summary_of_your_proposal')
    if_yes_provide_a_website_url_a_brief_summary_of_your_proposal=schema.Text(
        title=_(u"Provide a website or URL reference to link the response to the appropriate information that is maintained by your country."),
        required=False
        )
    # ========================== schema7
    schema7.append('designated_focal_point_for_the_oil_spills_protocol_')
    form.widget(designated_focal_point_for_the_oil_spills_protocol_=RadioFieldWidget)
    designated_focal_point_for_the_oil_spills_protocol_=schema.Choice(
    title = _(u"Does your country have a designated Focal Point for the Oil Spills Protocol?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema7.append('designated_focal_point_full_name_of_reporting_institution')
    designated_focal_point_full_name_of_reporting_institution=schema.TextLine(
    title = _(u"Full name of reporting institution",
               mapping={'number':''}),
    required=False,
    
    )
    schema7.append('designated_focal_point_contact_person')
    designated_focal_point_contact_person=schema.TextLine(
    title = _(u"Contact Person",
               mapping={'number':''}),
    required=False,
    
    )
    schema7.append('designated_focal_point_contact_person_job_title')
    designated_focal_point_contact_person_job_title=schema.TextLine(
    title = _(u"Job Title",
               mapping={'number':''}),
    required=False,
    
    )
    schema7.append('designated_focal_point_department')
    designated_focal_point_department=schema.Text(
    title = _(u"Department",
               mapping={'number':''}),
    required=False,
    
    )
    schema7.append('designated_focal_point_for_oilspills_address')
    designated_focal_point_for_oilspills_address=schema.Text(
        title = _(u"Address",
               mapping={'number':''}),
        required=False,
    )
    schema7.append('designated_focal_point_for_oilspills_telephone')
    form.widget(designated_focal_point_for_oilspills_telephone=DataGridFieldFactory)
    designated_focal_point_for_oilspills_telephone = schema.List(
    title=_(u"Telephone"),
    readonly=False,
    min_length=1,
    value_type=DictRow(
            title=_(u"Number"),
            schema=INumberSchema
            )
    )
    schema7.append('designated_focal_point_for_oilspills_email')
    designated_focal_point_for_oilspills_email=schema.TextLine(
    title = _(u"E-mail",
               mapping={'number':''}),
    required=False,
    
    )
    schema7.append('designated_focalpoint_for_oilspills_web_page')
    designated_focalpoint_for_oilspills_web_page=schema.TextLine(
    title = _(u"Website",
               mapping={'number':''}),
    required=False,
    
    )









    schema7.append('does_country_have_national_policies_for_management_of_oil_spill_pollution')
    form.widget(does_country_have_national_policies_for_management_of_oil_spill_pollution=RadioFieldWidget)
    does_country_have_national_policies_for_management_of_oil_spill_pollution=schema.Choice(
    title = _(u"Does your country currently have any national policies for prevention, reduction and control of oil spill pollution? ",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )

    schema7.append('does_country_have_national_laws_for_management_of_oil_spill_pollution')
    form.widget(does_country_have_national_laws_for_management_of_oil_spill_pollution=RadioFieldWidget)
    does_country_have_national_laws_for_management_of_oil_spill_pollution=schema.Choice(
    title = _(u"national laws for management of oil spill pollution",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema7.append('does_country_have_national_plans_for_management_of_oil_spill_pollution')
    form.widget(does_country_have_national_plans_for_management_of_oil_spill_pollution=RadioFieldWidget)
    does_country_have_national_plans_for_management_of_oil_spill_pollution=schema.Choice(
    title = _(u"national plans for management of oil spill pollution",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema7.append('national_operational_measures_for_responding_to_oil_spill_incidents')
    form.widget(national_operational_measures_for_responding_to_oil_spill_incidents=RadioFieldWidget)
    national_operational_measures_for_responding_to_oil_spill_incidents=schema.Choice(
    title = _(u"Has your country established any national operational measures such as establishing national oil spill contingency plans for responding to oil spill incidents (Article 7 of the Oil Spills Protocol)?",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    schema7.append('oil_spill_incidents_since_1986')
    form.widget(oil_spill_incidents_since_1986=RadioFieldWidget)
    oil_spill_incidents_since_1986=schema.Choice(
    title = _(u"Has your country experienced any oil-spill incidents since 1986 (Article 1, paragraph 4)?",
               mapping={'number':'4. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )

    # =============== schema8
    form.widget(designated_focal_point_for_the_spaw_protocol=RadioFieldWidget)
    designated_focal_point_for_the_spaw_protocol=schema.Choice(
    title = _(u"Does your country have a designated Focal Point for the SPAW Protocol?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(national_policies_for_the_protection_of_wild_flora_and_fauna=RadioFieldWidget)
    national_policies_for_the_protection_of_wild_flora_and_fauna=schema.Choice(
    title = _(u"Does your country currently have any national policies, laws, mechanisms or measures for the protection of Wild Flora and Fauna? (Article 10 of the SPAW Protocol)",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(national_laws_for_the_protection_of_wild_flora_and_fauna=RadioFieldWidget)
    national_laws_for_the_protection_of_wild_flora_and_fauna=schema.Choice(
    title = _(u"national laws for the protection of Wild Flora and Fauna",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(national_plans_for_the_protection_of_wild_flora_and_fauna=RadioFieldWidget)
    national_plans_for_the_protection_of_wild_flora_and_fauna=schema.Choice(
    title = _(u"national plans for the protection of Wild Flora and Fauna",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(established_protected_areas_pursuant_to_the_spaw_protocol=RadioFieldWidget)
    established_protected_areas_pursuant_to_the_spaw_protocol=schema.Choice(
    title = _(u"Has your country established any protected areas pursuant to the SPAW Protocol? (Article 4 of the SPAW Protocol) ",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(identified_all_endangered_threatened_species_within_your_country=RadioFieldWidget)
    identified_all_endangered_threatened_species_within_your_country=schema.Choice(
    title = _(u"Has your country identified all of the endangered / threatened species listed in Annexes I, II, and III of the SPAW Protocol that are within your country (i.e. within areas over which your country exercises sovereignty, sovereign rights, or jurisdiction)?",
               mapping={'number':'4. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(measures_to_ensure_strict_protection_of_the_endangered_threatened_species=RadioFieldWidget)
    measures_to_ensure_strict_protection_of_the_endangered_threatened_species=schema.Choice(
    title = _(u"Has your country taken measures to ensure strict protection of the endangered/threatened species listed in Annexes I and II (Article 11.1(a) and 11.1(b) of the SPAW Protocol)?",
               mapping={'number':'5. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(plans_for_the_management_of_endangered_threatened_species=RadioFieldWidget)
    plans_for_the_management_of_endangered_threatened_species=schema.Choice(
    title = _(u"Has your country formulated, adopted, and implemented any plans for the management and use of species listed in Annex III (Article 11.1 (c) of the SPAW Protocol)?",
               mapping={'number':'6. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(exemptions_to_species_protection=RadioFieldWidget)
    exemptions_to_species_protection=schema.Choice(
    title = _(u"Has your country adopted exemptions to species protection (Articles 11.2 and 14 of the SPAW Protocol)?",
               mapping={'number':'7. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(changes_in_the_delimitation_of_protected_areas_or_to_changes_in_their_status=RadioFieldWidget)
    changes_in_the_delimitation_of_protected_areas_or_to_changes_in_their_status=schema.Choice(
    title = _(u"Did your country proceed to any changes in the delimitation of protected areas and/or to changes in their status (Article 15 of the SPAW Protocol)?",
               mapping={'number':'8. '}),
    required=False,
    source=vocabulary.yes_no
    )
    form.widget(changes_in_the_legal_status_of_species_listed=RadioFieldWidget)
    changes_in_the_legal_status_of_species_listed=schema.Choice(
    title = _(u"Did your country proceed to any changes in the legal status of species listed in Annexes I, III, or III (Article 15 of the SPAW Protocol)?",
               mapping={'number':'9. '}),
    required=False,
    source=vocabulary.yes_no
    )
    form.widget(common_guidelines_or_criteria_adopted=RadioFieldWidget)
    common_guidelines_or_criteria_adopted=schema.Choice(
    title = _(u"Has your country incorporated into its law or policy the common guidelines or criteria adopted under Article 21 of the SPAW Protocol?",
               mapping={'number':'10. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(designated_focal_point_for_the_lbs_protocol=RadioFieldWidget)
    designated_focal_point_for_the_lbs_protocol=schema.Choice(
    title = _(u"Does your country have a designated Focal Point for the LBS Protocol?",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(is_there_a_national_definitionof_pollution_from_land_based_sources_and_activites=RadioFieldWidget)
    is_there_a_national_definitionof_pollution_from_land_based_sources_and_activites=schema.Choice(
    title = _(u"Is there a national definition of pollution from 'Land-based sources and activities' (Article I (d))?",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(legislation_for_prevention_reduction_and_control_of_pollution_from_land_based_sources=RadioFieldWidget)
    legislation_for_prevention_reduction_and_control_of_pollution_from_land_based_sources=schema.Choice(
    title = _(u"Does your country currently have any legislation for the prevention, reduction and control pollution from land-based sources in the Convention area (Article III)?",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(plans_programs_and_measures_that_meet_objectives_of_the_lbs_protocol=RadioFieldWidget)
    plans_programs_and_measures_that_meet_objectives_of_the_lbs_protocol=schema.Choice(
    title = _(u"Has your country developed any implementation plans, programs, and measures to carry out the general terms of [or:  meet the objectives of] the LBS Protocol, including National Programmes of Action (NPAs)? (Article III)",
               mapping={'number':'4. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(new_and_or_amended_existing_national_policies__laws__regulations__plans__for_reducing_lbs_pollution=RadioFieldWidget)
    new_and_or_amended_existing_national_policies__laws__regulations__plans__for_reducing_lbs_pollution=schema.Choice(
    title = _(u"Has your country developed new and/or amended existing national policies, laws, regulations, plans, for reducing LBS pollution over the reporting period? ",
               mapping={'number':'5. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(other_types_and_or_sources_of_lbs_pollution=RadioFieldWidget)
    other_types_and_or_sources_of_lbs_pollution=schema.Choice(
    title = _(u"Are there any other types and/or sources of LBS pollution other than those listed in Annex I of the LBS Protocol that require special consideration in your country?",
               mapping={'number':'6. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(environmental_pollution_monitoring_and_assessment_programmes=RadioFieldWidget)
    environmental_pollution_monitoring_and_assessment_programmes=schema.Choice(
    title = _(u"Does your country have any existing environmental pollution monitoring and assessment programmes as outlined in LBS Protocol Article VI?",
               mapping={'number':'7. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(guidelines_concerning_environmental_impact_assessments=RadioFieldWidget)
    guidelines_concerning_environmental_impact_assessments=schema.Choice(
    title = _(u"Has your country developed and adopted guidelines concerning environmental impact assessments (EIAs) or has your country generated EIAs consistent with the LBS Protocol, Article VII (2)?",
               mapping={'number':'8. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(total_annual_estimate_of_pollutant_loads_from_lbs_activities=RadioFieldWidget)
    total_annual_estimate_of_pollutant_loads_from_lbs_activities=schema.Choice(
    title = _(u"Does your country have a total annual estimate of the pollutant loads to the marine environment for LBS activities?",
               mapping={'number':'9. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    form.widget(difficulties_in_the_implementation_of_the_lbs_protocol=RadioFieldWidget)
    difficulties_in_the_implementation_of_the_lbs_protocol=schema.Choice(
    title = _(u"Has your country experienced any difficulties in the implementation of the LBS protocol?",
               mapping={'number':'10. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    major_areas_of_assistance_required_to_implement_protocols=schema.Text(
    title = _(u"What are three major areas of assistance required to assist your country in implementing the obligations of the Cartagena Convention and its Protocols.",
               mapping={'number':'11. '}),
    required=False,
    
    )

    model.fieldset(
        'section1',
        label = _(u"Section 1"),
        description = _(u"Section 1: Designated National Focal Point, Institution and Implementation Plans - Articles 4, 15"),
        fields = schema1
       )
    model.fieldset(
        'section2',
        label = _(u"Section 2"),
        description = _(u"Section 2: Measures to Reduce Marine Pollution from Ships, Caused by Discharges or Dumping, from Exploration or Exploitation of the Sea-Bed , or from Discharges to the Atmosphere - Articles 5, 6, 8, 9"),
        fields = schema2
       )
    model.fieldset(
        'section3',
        label = _(u"Section 3"),
        description = _(u"Section 3: Cooperation in Cases of Emergency - Article 11"),
        fields = schema3
               )
    model.fieldset(
        'section4',
        label = _(u"Section 4"),
        description = _(u"Section 4: Environmental Impact Assessment - Article 12"),
        fields = schema4
       )
    model.fieldset(
        'section5',
        label = _(u"Section 5"),
        description = _(u"Section 5: Scientific and Technical Cooperation - Article 13"),
        fields = schema5
       )
    model.fieldset(
        'section6',
        label = _(u"Section 6"),
        description = _(u"Section 6: Adoption/Amendment of the Convention and its Protocols - Articles 17,18"),
        fields = schema6
       )
    model.fieldset(
        'section7',
        label = _(u"Section 7"),
        description = _(u"Section 7: The Protocol Concerning Cooperation in Combating Oil Spills in the Wider Caribbean Region"),
        fields = schema7
        )
    model.fieldset(
        'section8',
        label = _(u"Section 8"),
        description = _(u"Section 8: The Protocol Concerning Specially Protected Areas and Wildlife (SPAW) - Article 4, 10, 11, 20, 21"),
        fields = ['designated_focal_point_for_the_spaw_protocol','national_policies_for_the_protection_of_wild_flora_and_fauna','national_laws_for_the_protection_of_wild_flora_and_fauna','national_plans_for_the_protection_of_wild_flora_and_fauna','established_protected_areas_pursuant_to_the_spaw_protocol','identified_all_endangered_threatened_species_within_your_country','measures_to_ensure_strict_protection_of_the_endangered_threatened_species','plans_for_the_management_of_endangered_threatened_species','exemptions_to_species_protection','changes_in_the_delimitation_of_protected_areas_or_to_changes_in_their_status','changes_in_the_legal_status_of_species_listed','common_guidelines_or_criteria_adopted',]
       )
    model.fieldset(
        'section9',
        label = _(u"Section 9"),
        description = _(u"Section 9: The Protocol Concerning Pollution from Land-Based Sources  (LBS) and Activities - Articles I, III, VI, VII"),
        fields = ['designated_focal_point_for_the_lbs_protocol','is_there_a_national_definitionof_pollution_from_land_based_sources_and_activites','legislation_for_prevention_reduction_and_control_of_pollution_from_land_based_sources','plans_programs_and_measures_that_meet_objectives_of_the_lbs_protocol','new_and_or_amended_existing_national_policies__laws__regulations__plans__for_reducing_lbs_pollution','other_types_and_or_sources_of_lbs_pollution','environmental_pollution_monitoring_and_assessment_programmes','guidelines_concerning_environmental_impact_assessments','total_annual_estimate_of_pollutant_loads_from_lbs_activities','difficulties_in_the_implementation_of_the_lbs_protocol','major_areas_of_assistance_required_to_implement_protocols',]
       )

class TestGroup(group.Group):
    label = u'Test Group'
    fields = field.Fields(ICountryReport).select(
        'country', 'full_name_of_reporting_institution')      

