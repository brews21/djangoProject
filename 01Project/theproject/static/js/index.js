(function($) {
  var refreshId = setInterval(function(){
    var flashit = document.getElementsByClassName('flashit')
    console.log(flashit);
    if (flashit.length > 0){
      console.log("Timer");
      //$( "#content" ).load("");
      $("#content").load(location.href+" #content>*","");
    }
  }, 1000);
})(jQuery);
