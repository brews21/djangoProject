// (function($)
// {
//     $(document).ready(function()
//     {
//         $.ajaxSetup(
//         {
//             cache: false,
//             beforeSend: function() {
//                 $('#content').hide();
//                 //$('#loading').show();
//             },
//             complete: function() {
//                 //$('#loading').hide();
//                 $('#content').show();
//             },
//             success: function() {
//                 //$('#loading').hide();
//                 $('#content').show();
//             }
//         });
//         var $container = $("#content");
//         //$container.load("rss-feed-data.php");
//         var refreshId = setInterval(function()
//         {
//             //$container.load('rss-feed-data.php');
//             console.log("Timer");
//         }, 9000);
//     });
// })(jQuery);


// (function($) {
//   var refreshId = setInterval(function(){
//     $.ajax({
//       method: "POST",
//       url: "/theapp/index/",
//       data: {},
//       headers: {'Access-Control-Allow-Origin':'true'},
//       success: function(data) {
//         console.log(data) // check out how data is structured
//         // Update the coin amount
//         //$('.status').contents()[0].textContent = 'Balance&nbsp'+data.coins
//         }
//       })
//     }, 1000);
//   })(jQuery);

// (function ($) {
//   $.ajax({
//     url: '/theapp/index/',
//     data: {},
//     success: function(data) {
//       console.log("Timer");
//       console.log(data);
//       $('.result').html(data);
//     },
//     complete: function() {
//       // Schedule the next request when the current one's complete
//       setTimeout(5000);
//     }
//   });
// })(jQuery);

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
