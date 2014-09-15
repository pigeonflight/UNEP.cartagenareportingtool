$(document).ready(function() { 
	//only do this if on the edit page
 if(document.URL.indexOf("edit") >= 0){ 

            base_url = document.URL.split('edit')[0]
            $('#form').before($('<a id="view" href="'+ base_url + 'view"><button class="btn btn-primary">View</button></a>')
                                )


     // add doc saved message
     $('body').append("<div class='alert alert-success doc-saved' id='status-message-doc-save'>document saved</div>")
	// configure plone to support multiple submissions
	// basically disable form resubmission blocking
    $("#form-buttons-save").addClass("allowMultiSubmit");

	// prepare the form for ajax saving
    var options = { 
    
        success:       showResponse  // post-submit callback 
 
        // other available options: 
        //url:       url         // override for form's 'action' attribute 
        //type:      type        // 'get' or 'post', override for form's 'method' attribute 
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type) 
        //clearForm: true        // clear all form fields after successful submit 
        //resetForm: true        // reset the form after successful submit 
 
        // $.ajax options can be used here too, for example: 
        //timeout:   3000 
    }; 
 
    // bind form using 'ajaxForm' 
    $('#form').ajaxForm(options);

    // bind 'myForm' and provide a simple callback function 
    $('#form').ajaxForm(function() { 
        //console.log("form saved!"); 
        $('.doc-saved').fadeIn('slow', function(){
             $('.doc-saved').fadeOut(1500);
          });
    }); 

    // save every 30 seconds         
    setInterval(function () {
            $('#form-buttons-save').click();
            },30000);

    // submit form after an input field has been changed
    $("#form input[type=text],#form textarea").change(function() {
          console.log("form changed!");
          $('#form-buttons-save').click();

    });

    function showResponse(responseText, statusText, xhr, $form)  { 
  
        //console.log('status: ' + statusText ); 
     } 
  
}
}); 