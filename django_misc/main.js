$DOM = $(document)
$DOM.ready(function(){

    function call_ajax(url, type, data) {
         // this function will perform ajax calls and returns request object

         data = data || '';
         var request = $.ajax({
                             type: type,
                             url: url,
                             data:data,
                       });
         return request;
    }

    function test_fun(){
        console.log('everyhting working fine')
    }

    function bindEvents() {
		$DOM.on('change', '#test_fun', test_fun)
    }

    bindEvents();
});

