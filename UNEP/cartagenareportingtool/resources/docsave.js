$(document).ready(function(){
   
   if (~document.URL.indexOf("++add++")) {
       
     $('#form').ajaxForm(function() { 
           console.log("report saved!");
           editurl = window.location.href.split('++')[0] + 'unep-cartagenareportingtool-countryreport/edit'
           window.location.replace(editurl);
            
       }); 
       
     $('#form').submit();  
   } 
    
});