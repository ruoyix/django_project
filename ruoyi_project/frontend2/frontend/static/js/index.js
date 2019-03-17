$(document).ready(function(){
    $(".carousel-item").carousel({interval: 1000});
    $(".carousel").on("touchstart", function(data){
        data.preventDefault();
        start = data.originalEvent.changedTouches[0].pageX
    });
    $(".carousel").on("touchend", function(data){
        end = data.originalEvent.changedTouches[0].pageX
        differ = end-start
        if(differ>0){
          $(".carousel").carousel("prev");
        }
        else{
          $(".carousel").carousel("next");
        }
    });
});
