(function($) {
  'use strict';

  var metas = document.getElementsByTagName('meta');
  var i;

  if (navigator.userAgent.match(/iPhone/i)) {
    for (i=0; i<metas.length; i++) {
      if (metas[i].name == "viewport") {
        metas[i].content = "width=device-width, minimum-scale=1.0, maximum-scale=1.0";
      }
    }

    document.addEventListener("gesturestart", gestureStart, false);
  }

  function gestureStart() {
    for (i=0; i<metas.length; i++) {
      if (metas[i].name == "viewport") {
        metas[i].content = "width=device-width, minimum-scale=0.25, maximum-scale=1.6";
      }
    }
  }

  $(function(){
    $('.tweetme').click(function(e) {
      var width = 575;
      var height = 400;
      var left = ($(window).width()  - width)  / 2;
      var top = ($(window).height() - height) / 2;
      var url = this.href;
      var opts = [
        'status=1',
        ',width=', width,
        ',height=', height,
        ',top=', top,
        ',left=', left
      ].join('');

      window.open(url, 'tweet', opts);

      return false;
    });
    $('time.timeago').timeago();
  });

})(jQuery);
