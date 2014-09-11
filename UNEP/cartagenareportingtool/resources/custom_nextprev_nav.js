$(document).ready(function() {


   //only do this if on the edit page
  if(document.URL.indexOf("edit") >= 0){ 



    var prevnext = {
    formTabs: null,

    next: function() { prevnext.formTabs.data('tabs').next(); prevnext._scrollToTop(); prevnext.save(); },
    prev: function() { prevnext.formTabs.data('tabs').prev(); prevnext._scrollToTop(); prevnext.save(); },

    _scrollToTop: function() {
        $(window).scrollTop(prevnext.formTabs.closest('form').offset().top);  
    },
    save: function() {
      $('#form-buttons-save').click();
      
    },

    showButtons: function(event, index) {
        var tabs = prevnext.formTabs.data('tabs'),
            index = typeof(index) === 'undefined' ? tabs.getIndex() : index,
            current = tabs.getTabs()[index],
            count = tabs.getTabs().length;

        $('#prevnext_previous').toggle(index !== 0);
        $('#prevnext_next').toggle(index !== (count - 1));

        $('.formControls:last :submit[name=form_submit]').toggle(index === (count - 1));
    },

    init: function() {
        var tabs;
        prevnext.formTabs = $('.formTabs');
        tabs = prevnext.formTabs.data('tabs');
        if (tabs.getTabs().length > 0) {
            if ($('fieldset#fieldset-default').length === 0)
                 return;
            $('formTabs').before(document.createTextNode('<div class="prev-next-nav"><i></i>hello</div>'));
            $('.formTabs').before($('<input id="prevnext_previous1" class="btn btn-primary" ' +
                                    '       type="button" value="" />')
                                .val('< Previous')
                                .click(prevnext.prev))
                          .before(document.createTextNode(' '));
            $('.formTabs').before($('<input id="prevnext_next1" class="btn btn-primary" ' +
                                 '       type="button" value="" />')
                             .val('Next >')
                             .click(prevnext.next))
       

            $('.formControls:last :submit:first')
                .before($('<input id="prevnext_previous" class="btn btn-primary" ' +
                          '       type="button" value="" />')
                      .val('< Previous')
                      .click(prevnext.prev))
                .before(document.createTextNode(' '));
            $('.formControls:last :submit:first')
                .before($('<input id="prevnext_next" class="btn btn-primary" ' +
                          '       type="button" value="" />')
                      .val('Next >')
                      .click(prevnext.next))
                .before(document.createTextNode(' '));
            prevnext.showButtons();
            tabs.onClick(prevnext.showButtons);
        }
    }
};

$(prevnext.init());

}

});