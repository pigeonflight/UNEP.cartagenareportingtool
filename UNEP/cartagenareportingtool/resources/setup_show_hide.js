$(document).ready(function() { 
var show_checked_divs = function(){

	// get the id of all checked radio buttons
	$.each( $('.radio-widget.choice-field:checked'),function(index,radio){
	    // iterate over all available triggers
		$.each(triggers,function(idx,itm){
          // if the id of the radio is in the trigger array

          if ( ~$.inArray(radio.id,  itm.trigger) ) {
            // then iterate over all the corresponding divs
            // retrieve their names to the target variable 
            // and show them
            $.each(itm.divs,function(ix,target){
    
          	   $("#"+target).show();

            });

          }

		});
	});

}
var setup_show_hide = function(sources,target) {
	
	// if radio field clicked
	$('.radio-widget.choice-field').click(function () {
		

    	//if (this.id == source) {
    	if (~$.inArray(this.id,sources)) {	
        	$("#"+target).show('slow');
    	} else {
        	$("#"+target).hide('slow');
    	}
	


	});



	


	// if checkbox clicked

   
}


triggers = [
	{trigger:['form-widgets-pollution_emergencies_in_the_convention_area-0'],
		divs:[
		'formfield-form-widgets-if_yes_describe_pollution_emergencies'
		]
	},
	// section 1
	// section1#1
	{trigger:['form-widgets-does_your_country_have_a_designated_national_focal_point_for_the_cartagena_convention_-0'],
		divs:[
		'formfield-form-widgets-national_focal_point_name_of_organization',
		'formfield-form-widgets-national_focal_point_contact_person',
		'formfield-form-widgets-national_focal_point_job_title',
		'formfield-form-widgets-national_focal_point_department',
		'formfield-form-widgets-national_focal_point_address',
		'formfield-form-widgets-national_focal_point_telephone',
		'formfield-form-widgets-national_focal_point_email',
		'formfield-form-widgets-national_focal_point_website',
		'formfield-form-widgets-national_agency_website'
		]
	},
	// section1#2
	{trigger:['form-widgets-designated_national_agency_ministry_institution-0'],
		divs:[
		'formfield-form-widgets-national_agency_name_of_organization',
		'formfield-form-widgets-national_agency_contact_person',
		'formfield-form-widgets-national_agency_job_title',
		'formfield-form-widgets-national_agency_department',
		'formfield-form-widgets-national_agency_address',
		'formfield-form-widgets-national_agency_telephone',
		'formfield-form-widgets-national_agency_email',
		'formfield-form-widgets-national_agency_website'
		]
	},
	// section1#3
	{trigger:['form-widgets-implementation_plans-0','form-widgets-implementation_plans-2'],
     divs:[
     'formfield-form-widgets-if_yes_brief_details_of_main_implementation_plans_article4']
     },
	{trigger:['form-widgets-implementation_plans-1'],
     divs:['formfield-form-widgets-if_why_no_plans_article4']
     },
     {trigger:['form-widgets-implementation_plans-3'],
     divs:[
     'formfield-form-widgets-if_plans_exist_article4'
     ]
     },
     // section1#4
	{trigger:['form-widgets-has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans-0'],
     divs:['formfield-form-widgets-if_yes_please_identify_the_source_external_financial_assistance']
     },
	{trigger:['form-widgets-has_your_country_recieved_any_external_financial_assistance_to_develop_and_or_implement_existing_plans-1'],
     divs:['formfield-form-widgets-if_no_please_state_why_not_financial_assistance']
     },
     // section1#5
	{trigger:['form-widgets-difficulties_in_the_implementation_of_plan_s_-0'],
     divs:['formfield-form-widgets-if_why_implementation_difficulties_with_details']
     },
     // section 2
     // section2#1
	{trigger:['form-widgets-is_there_a_national_definition_for_pollution_sources-0'],
     divs:[
     'formfield-form-widgets-if_yes_to_pollution_definitions_discharges_from_ships',
     'formfield-form-widgets-if_yes_to_pollution_definitions_dumping_of_wastes_and_other_matter_at_sea',
     'formfield-form-widgets-if_yes_to_pollution_definitions_exploration_or_exploitation_of_sea_bed',
     'formfield-form-widgets-if_yes_to_pollution_definitions_discharges_air_emissions_into_atmosphere'
     ]
     },
     // section2#2
     {trigger:['form-widgets-management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area-0'],
     divs:['if_yes_details_of_pollution_source_management_action_since_last_reporting_period']
     },
     {trigger:['form-widgets-management_measures_since_the_last_reporting_period_sources_of_pollution_in_the_convention_area-1'],
     divs:['formfield-form-widgets-if_no_why_no_action_since_last_reporting_period']
     },
     //section2#3
     {trigger:['form-widgets-other_pollution_sources_or_types_that_may_affect_marine_resources-0'],
      divs:['formfield-form-widgets-if_yes_please_specify_answer_below']
      },
     //section2#4a
      {trigger:['form-widgets-policies_for_marine_pollution_management_for_special_consideration-0',
              'form-widgets-policies_for_marine_pollution_management_for_special_consideration-2'],
      divs:['formfield-form-widgets-if_yes_policies_please_provide_details','formfield-form-widgets-if_yes_policy_website_for_marine_pollution']
      },
      {trigger:['form-widgets-policies_for_marine_pollution_management_for_special_consideration-1'],
      divs:['formfield-form-widgets-if_no_policies_why_not_for_marine_pollution']
      },
      {trigger:['form-widgets-policies_for_marine_pollution_management_for_special_consideration-3'],
       divs:['formfield-form-widgets-if_other_specify']
      },
      //section2#4b
      {trigger:['form-widgets-laws_for_marine_pollution_management_for_special_consideration-0',
             'form-widgets-laws_for_marine_pollution_management_for_special_consideration-2'],
       divs:['formfield-form-widgets-if_yes_laws_please_provide_details',
          'formfield-form-widgets-if_yes_laws_website_for_marine_pollution']
      },
      {trigger:['form-widgets-laws_for_marine_pollution_management_for_special_consideration-1'],
        divs:['formfield-form-widgets-if_no_laws_why_not_for_marine_pollution']
      },
      {trigger:['form-widgets-laws_for_marine_pollution_management_for_special_consideration-3'],
        divs:['formfield-form-widgets-if_other_laws_specify']
      },
      //section2#4c
      {trigger:['form-widgets-plans_for_marine_pollution_management_for_special_consideration-0',
            'form-widgets-plans_for_marine_pollution_management_for_special_consideration-2'],
        divs:['formfield-form-widgets-if_yes_plans_please_provide_details',
             'formfield-form-widgets-if_yes_plans_website_for_marine_pollution']
       },
       {trigger:['form-widgets-plans_for_marine_pollution_management_for_special_consideration-1'],
        divs:['formfield-form-widgets-if_no_plans_why_not_for_marine_pollution']
       },
       {trigger:['form-widgets-plans_for_marine_pollution_management_for_special_consideration-3'],
        divs:['formfield-form-widgets-if_other_plans_specify']
       },
       // section 3
       //section3#1
       {trigger:['form-widgets-pollution_emergencies_in_the_convention_area-0'],
       divs:['formfield-form-widgets-if_yes_describe_pollution_emergencies',
       'formfield-form-widgets-if_yes_provide_a_website_url_pollution_emergencies']
       },
       {trigger:['form-widgets-response_to_emergencies-2.checkbox-widget'],
       divs:['formfield-form-widgets-if_cooperation_contracting_parties_and_experience',
             'formfield-form-widgets-if_yes_provide_a_website_url_response_to_situation']},
       {trigger:['form-widgets-jointly_developed_and_promoted_contingency_plans-0'],
        divs:['formfield-form-widgets-if_yes_list_contingency_plans_developed',
        'formfield-form-widgets-if_yes_provide_a_website_url_jointly_developed_and_promoted_contingency_plans']}
]

show_checked_divs();

// configure show hide
$.each( triggers, function(index, thetrigger){
	//console.log(thetrigger);
	$.each(thetrigger.divs, function(index, div){
		setup_show_hide(thetrigger.trigger,div)
	})
});

});
