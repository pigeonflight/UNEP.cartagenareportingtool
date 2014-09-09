from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import invariant, Interface, Invalid
from plone.directives import dexterity, form
from zope import schema
from UNEP.cartagenareportingtool import MessageFactory as _
from UNEP.cartagenareportingtool import vocabulary
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from plone.supermodel import model

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

class ICountryReport(form.Schema, IImageScaleTraversable):
    id = schema.Id(
        title=_(u"Identifier"),
        description=_(u"The unique identifier of object."),
        required=False
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
    max_length=5,
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
    does_your_country_have_a_designated_national_focal_point_for_the_cartagena_convention_=schema.Choice(
    title = _(u"Does your country have a designated National Focal Point for the Cartagena Convention?",
),
 #              mapping={'number':'1.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_focal_point_name_of_organization=schema.TextLine(
    title = _(u"National Focal Point:Name of Organization",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_contact_person=schema.TextLine(
    title = _(u"National Focal Point:Contact Person",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_job_title=schema.TextLine(
    title = _(u"National Focal Point:Job Title",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_department=schema.TextLine(
    title = _(u"National Focal Point:Department",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_address=schema.Text(
    title = _(u"National Focal Point:Address",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_telephone=schema.TextLine(
    title = _(u"National Focal Point:Telephone",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_email=schema.TextLine(
    title = _(u"National Focal Point:Email",
               mapping={'number':''}),
    required=False,
    
    )
    national_focal_point_website=schema.TextLine(
    title = _(u"National Focal Point:Website",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_ministry_institution=schema.Choice(
    title = _(u"Does your country have a designated National Agency/Ministry/Institution or other appropriate authority for coordinating the implementation of the Cartagena Convention (Article 15, paragraph 2)?",
               mapping={'number':'2.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_agency_name_of_organization=schema.TextLine(
    title = _(u"National Agency/Ministry:Name of Organization",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_contact_person=schema.TextLine(
    title = _(u"National Agency/Ministry:Contact Person",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_job_title=schema.TextLine(
    title = _(u"National Agency/Ministry:Job Title",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_department=schema.TextLine(
    title = _(u"National Agency/Ministry:Department",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_address=schema.Text(
    title = _(u"National Agency/Ministry:Address",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_telephone=schema.TextLine(
    title = _(u"National Agency/Ministry:Telephone",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_email=schema.TextLine(
    title = _(u"National Agency/Ministry:Email",
               mapping={'number':''}),
    required=False,
    
    )
    national_agency_website=schema.TextLine(
    title = _(u"National Agency/Ministry:Website",
               mapping={'number':''}),
    required=False,
    
    )
    implementation_plans=schema.Choice(
    title = _(u"Has your country developed an implementation plans(s) to carry out the general obligations of the Cartagena Convention? (Article 4)",
               mapping={'number':'3.'}),
    required=False,
    source=vocabulary.yes_no_inprep_existingplans
    )
    brief_details_of_main_implementation_plans=schema.Text(
    title = _(u"Brief details of main implementation plans",
               mapping={'number':''}),
    required=False,
    
    )
    why_no_plans=schema.TextLine(
    title = _(u"Why no plans",
               mapping={'number':''}),
    required=False,
    
    )
    difficulties_in_the_implementation_of_plan_s_=schema.Choice(
    title = _(u"Has your country experienced any difficulties in the implementation of the above-mentioned plan(s)?",
               mapping={'number':'4.'}),
    required=False,
    source=vocabulary.yes_no
    )
    why_implementation_difficulties_with_details=schema.TextLine(
    title = _(u"Why implementation difficulties with details",
               mapping={'number':''}),
    required=False,
    
    )
    has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans=schema.Choice(
    title = _(u"Has your country received any external financial assistance to develop and/or implement existing plan(s)?",
               mapping={'number':'5.'}),
    required=False,
    source=vocabulary.yes_no
    )
    national_definitions_for_pollution_sources=schema.Choice(
    title = _(u"${number} Is there a national definition within existing pollution related legislation or regulations for 'Pollution from Ships', 'Discharging or Dumping of wastes at sea', 'Exploration or Exploitation of the  Sea-Bed Activities', and 'Discharges (emissions) to the Atmosphere' (Articles 5, 6, 8, 9)?",
               mapping={'number':'1.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area=schema.Choice(
    title = _(u"${number} Has your country taken any measures since the last reporting period necessary to prevent, reduce and control the abovementioned sources of pollution in the Convention area? ",
               mapping={'number':'2.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    details_of_pollution_source_management_action_since_last_reporting_period=schema.Text(
    title = _(u"details of pollution source  management action since last reporting period",
               mapping={'number':''}),
    required=False,
    
    )
    why_no_action_since_last_reporting_period=schema.Text(
    title = _(u"Why no action since last reporting period",
               mapping={'number':''}),
    required=False,
    
    )
    other_pollution_sources_or_types_that_may_affect_marine_resources=schema.Choice(
    title = _(u"${number} Are there any other sources and/or types of pollution that may affect marine resources in the Convention area which require special consideration in your country?",
               mapping={'number':'3.'}),
    required=False,
    source=vocabulary.yes_no
    )
    text_for_discharges_from_ship=schema.Text(
    title = _(u"Text for Discharges from ship",
               mapping={'number':''}),
    required=False,
    
    )
    policies_for_marine_pollution_management_for_special_consideration=schema.Choice(
    title = _(u"${number} Does your country have any national policies for marine pollution prevention, reduction and control for these activities requiring special consideration? ",
               mapping={'number':'4.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    policy_website_for_marine_pollution=schema.Text(
    title = _(u"Policy website",
               mapping={'number':''}),
    required=False,
    
    )
    laws_for_marine_pollution_management_for_special_consideration=schema.Choice(
    title = _(u"National laws for marine pollution management",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    law_website_for_marine_pollution=schema.Text(
    title = _(u"Law Website",
               mapping={'number':''}),
    required=False,
    
    )
    plans_for_marine_pollution_management_for_special_consideration=schema.Choice(
    title = _(u"National plans for marine pollution management",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    plan_website_for_marine_pollution=schema.Text(
    title = _(u"Plan website",
               mapping={'number':''}),
    required=False,
    
    )
    pollution_emergencies_in_the_convention_area=schema.Choice(
    title = _(u"${number} Has your country experienced any pollution emergencies in the Convention area (including emergencies in which the Convention area is in imminent danger of being polluted or already polluted)?",
               mapping={'number':'1.'}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    describe_pollution_emergencies=schema.TextLine(
    title = _(u"Describe pollution emergencies",
               mapping={'number':''}),
    required=False,
    
    )
    related_marine_emergency_website=schema.TextLine(
    title = _(u"Related marine emergency website",
               mapping={'number':''}),
    required=False,
    
    )
    response_to_emergencies=schema.Text(
    title = _(u"${number} In regards to the question above, did your country respond to the situation through any of the following:",
               mapping={'number':'2.'}),
    required=False,
    
    )
    contracting_parties_and_experience=schema.Text(
    title = _(u"Contracting parties and experience",
               mapping={'number':''}),
    required=False,
    
    )
    jointly_developed_and_promoted_contingency_plans=schema.TextLine(
    title = _(u"Has your country, jointly with another country or with other countries, developed and promoted any contingency plans for responding to incidents involving pollution or the threat thereof in the Convention area?",
               mapping={'number':'3. '}),
    required=False,
    
    )
    technical_guidelines_to_assist_planning_of_major_development_projects=schema.Choice(
    title = _(u"Does your country currently have any technical and other guidelines (e.g., EIAs) to assist the planning of major development projects in such a way as to prevent or minimize harmful impacts on the Convention Area?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    technical_cooperation_agreements=schema.Choice(
    title = _(u"Does your country have technical cooperation agreements with any other Contracting Parties relating to the purposes of the Convention?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    status_of_ratification_of_the_existing_protocols=schema.Choice(
    title = _(u"Please indicate the status of ratification/accession of the existing Protocols to the Cartagena Convention.",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    plans_to_propose_amendments_to_the_convention=schema.Choice(
    title = _(u"Does your country currently have any plan to propose any amendments to the Cartagena Convention?",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    designated_focal_point_for_the_oil_spills_protocol_=schema.Choice(
    title = _(u"Does your country have a designated Focal Point for the Oil Spills Protocol?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_policies_for_management_of_oil_spill_pollution__=schema.Choice(
    title = _(u"Does your country currently have any national policies for prevention, reduction and control of oil spill pollution? ",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_laws_for_management_of_oil_spill_pollution=schema.Choice(
    title = _(u"national laws for management of oil spill pollution",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_plans_for_management_of_oil_spill_pollution=schema.Choice(
    title = _(u"national plans for management of oil spill pollution",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_operational_measures_for_responding_to_oil_spill_incidents=schema.Choice(
    title = _(u"Has your country established any national operational measures such as establishing national oil spill contingency plans for responding to oil spill incidents (Article 7 of the Oil Spills Protocol)?",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    oil_spill_incidents_since_1986=schema.Choice(
    title = _(u"Has your country experienced any oil-spill incidents since 1986 (Article 1, paragraph 4)?",
               mapping={'number':'4. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    designated_focal_point_for_the_spaw_protocol=schema.Choice(
    title = _(u"Does your country have a designated Focal Point for the SPAW Protocol?",
               mapping={'number':'1. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_policies_for_the_protection_of_wild_flora_and_fauna=schema.Choice(
    title = _(u"Does your country currently have any national policies, laws, mechanisms or measures for the protection of Wild Flora and Fauna? (Article 10 of the SPAW Protocol)",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_laws_for_the_protection_of_wild_flora_and_fauna=schema.Choice(
    title = _(u"national laws for the protection of Wild Flora and Fauna",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_plans_for_the_protection_of_wild_flora_and_fauna=schema.Choice(
    title = _(u"national plans for the protection of Wild Flora and Fauna",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    established_protected_areas_pursuant_to_the_spaw_protocol=schema.Choice(
    title = _(u"Has your country established any protected areas pursuant to the SPAW Protocol? (Article 4 of the SPAW Protocol) ",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    identified_all_endangered_threatened_species_within_your_country=schema.Choice(
    title = _(u"Has your country identified all of the endangered / threatened species listed in Annexes I, II, and III of the SPAW Protocol that are within your country (i.e. within areas over which your country exercises sovereignty, sovereign rights, or jurisdiction)?",
               mapping={'number':'4. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    measures_to_ensure_strict_protection_of_the_endangered_threatened_species=schema.Choice(
    title = _(u"Has your country taken measures to ensure strict protection of the endangered/threatened species listed in Annexes I and II (Article 11.1(a) and 11.1(b) of the SPAW Protocol)?",
               mapping={'number':'5. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    plans_for_the_management_of_endangered_threatened_species=schema.Choice(
    title = _(u"Has your country formulated, adopted, and implemented any plans for the management and use of species listed in Annex III (Article 11.1 (c) of the SPAW Protocol)?",
               mapping={'number':'6. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    exemptions_to_species_protection=schema.Choice(
    title = _(u"Has your country adopted exemptions to species protection (Articles 11.2 and 14 of the SPAW Protocol)?",
               mapping={'number':'7. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    changes_in_the_delimitation_of_protected_areas_or_to_changes_in_their_status=schema.Choice(
    title = _(u"Did your country proceed to any changes in the delimitation of protected areas and/or to changes in their status (Article 15 of the SPAW Protocol)?",
               mapping={'number':'8. '}),
    required=False,
    source=vocabulary.yes_no
    )
    changes_in_the_legal_status_of_species_listed=schema.Choice(
    title = _(u"Did your country proceed to any changes in the legal status of species listed in Annexes I, III, or III (Article 15 of the SPAW Protocol)?",
               mapping={'number':'9. '}),
    required=False,
    source=vocabulary.yes_no
    )
    common_guidelines_or_criteria_adopted=schema.Choice(
    title = _(u"Has your country incorporated into its law or policy the common guidelines or criteria adopted under Article 21 of the SPAW Protocol?",
               mapping={'number':'10. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    designated_focal_point_for_the_lbs_protocol=schema.Choice(
    title = _(u"Does your country have a designated Focal Point for the LBS Protocol?",
               mapping={'number':''}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    national_definition_of_pollution_from_land_based_sources_and_activiites=schema.Choice(
    title = _(u"Is there a national definition of pollution from 'Land-based sources and activities' (Article I (d))?",
               mapping={'number':'2. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    legislation_for_prevention_reduction_and_control_of_pollution_from_land_based_sources=schema.Choice(
    title = _(u"Does your country currently have any legislation for the prevention, reduction and control pollution from land-based sources in the Convention area (Article III)?",
               mapping={'number':'3. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    plans_programs_and_measures_that_meet_objectives_of_the_lbs_protocol=schema.Choice(
    title = _(u"Has your country developed any implementation plans, programs, and measures to carry out the general terms of [or:  meet the objectives of] the LBS Protocol, including National Programmes of Action (NPAs)? (Article III)",
               mapping={'number':'4. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    new_and_or_amended_existing_national_policies__laws__regulations__plans__for_reducing_lbs_pollution=schema.Choice(
    title = _(u"Has your country developed new and/or amended existing national policies, laws, regulations, plans, for reducing LBS pollution over the reporting period? ",
               mapping={'number':'5. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    other_types_and_or_sources_of_lbs_pollution=schema.Choice(
    title = _(u"Are there any other types and/or sources of LBS pollution other than those listed in Annex I of the LBS Protocol that require special consideration in your country?",
               mapping={'number':'6. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    environmental_pollution_monitoring_and_assessment_programmes=schema.Choice(
    title = _(u"Does your country have any existing environmental pollution monitoring and assessment programmes as outlined in LBS Protocol Article VI?",
               mapping={'number':'7. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    guidelines_concerning_environmental_impact_assessments=schema.Choice(
    title = _(u"Has your country developed and adopted guidelines concerning environmental impact assessments (EIAs) or has your country generated EIAs consistent with the LBS Protocol, Article VII (2)?",
               mapping={'number':'8. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
    total_annual_estimate_of_pollutant_loads_from_lbs_activities=schema.Choice(
    title = _(u"Does your country have a total annual estimate of the pollutant loads to the marine environment for LBS activities?",
               mapping={'number':'9. '}),
    required=False,
    source=vocabulary.yes_no_inprep
    )
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
        fields = ['does_your_country_have_a_designated_national_focal_point_for_the_cartagena_convention_','national_focal_point_name_of_organization','national_focal_point_contact_person','national_focal_point_job_title','national_focal_point_department','national_focal_point_address','national_focal_point_telephone','national_focal_point_email','national_focal_point_website','national_agency_ministry_institution','national_agency_name_of_organization','national_agency_contact_person','national_agency_job_title','national_agency_department','national_agency_address','national_agency_telephone','national_agency_email','national_agency_website','implementation_plans','brief_details_of_main_implementation_plans','why_no_plans','difficulties_in_the_implementation_of_plan_s_','why_implementation_difficulties_with_details','has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans',]
       )
    model.fieldset(
        'section2',
        label = _(u"Section 2"),
        description = _(u"Section 2: Measures to Reduce Marine Pollution from Ships, Caused by Discharges or Dumping, from Exploration or Exploitation of the Sea-Bed , or from Discharges to the Atmosphere - Articles 5, 6, 8, 9"),
        fields = ['national_definitions_for_pollution_sources','management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area','details_of_pollution_source_management_action_since_last_reporting_period','why_no_action_since_last_reporting_period','other_pollution_sources_or_types_that_may_affect_marine_resources','text_for_discharges_from_ship','policies_for_marine_pollution_management_for_special_consideration','policy_website_for_marine_pollution','laws_for_marine_pollution_management_for_special_consideration','law_website_for_marine_pollution','plans_for_marine_pollution_management_for_special_consideration','plan_website_for_marine_pollution',]
       )
    model.fieldset(
        'section3',
        label = _(u"Section 3"),
        description = _(u"Section 3: Cooperation in Cases of Emergency - Article 11"),
        fields = ['pollution_emergencies_in_the_convention_area','describe_pollution_emergencies','related_marine_emergency_website','response_to_emergencies','contracting_parties_and_experience','jointly_developed_and_promoted_contingency_plans',]
       )
    model.fieldset(
        'section4',
        label = _(u"Section 4"),
        description = _(u"Section 4: Environmental Impact Assessment - Article 12"),
        fields = ['technical_guidelines_to_assist_planning_of_major_development_projects',]
       )
    model.fieldset(
        'section5',
        label = _(u"Section 5"),
        description = _(u"Section 5: Scientific and Technical Cooperation - Article 13"),
        fields = ['technical_cooperation_agreements',]
       )
    model.fieldset(
        'section6',
        label = _(u"Section 6"),
        description = _(u"Section 6: Adoption/Amendment of the Convention and its Protocols - Articles 17,18"),
        fields = ['status_of_ratification_of_the_existing_protocols','plans_to_propose_amendments_to_the_convention',]
       )
    model.fieldset(
        'section7',
        label = _(u"Section 7"),
        description = _(u"Section 7: The Protocol Concerning Cooperation in Combating Oil Spills in the Wider Caribbean Region"),
        fields = ['designated_focal_point_for_the_oil_spills_protocol_','national_policies_for_management_of_oil_spill_pollution__','national_laws_for_management_of_oil_spill_pollution','national_plans_for_management_of_oil_spill_pollution','national_operational_measures_for_responding_to_oil_spill_incidents','oil_spill_incidents_since_1986',]
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
        fields = ['designated_focal_point_for_the_lbs_protocol','national_definition_of_pollution_from_land_based_sources_and_activiites','legislation_for_prevention_reduction_and_control_of_pollution_from_land_based_sources','plans_programs_and_measures_that_meet_objectives_of_the_lbs_protocol','new_and_or_amended_existing_national_policies__laws__regulations__plans__for_reducing_lbs_pollution','other_types_and_or_sources_of_lbs_pollution','environmental_pollution_monitoring_and_assessment_programmes','guidelines_concerning_environmental_impact_assessments','total_annual_estimate_of_pollutant_loads_from_lbs_activities','difficulties_in_the_implementation_of_the_lbs_protocol','major_areas_of_assistance_required_to_implement_protocols',]
       )
