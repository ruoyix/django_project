//所有javascrapt都要写进$(function(){})里,$(document).ready(function){}的缩写
$(function(){
    //nav分类跳转的呈现
    $("#scroll-nav").hide();
    $(window).scroll(function(){
        if($(window).scrollTop()<=350){
            $(function(){$("#scroll-nav").hide();});
        }
        else{
            $(function(){$("#scroll-nav").show();});
        }
    });
    //鼠标经过事件
    $(".shower-card").mouseover(function(){
        $(this).css({"border-color":"red","opacity":"0.8"});
        $(this).mouseout(function(){
            $(this).css({"border-color":"","opacity":""});
        });
    });
    //form被触发事件
    $(".shower-card-form").submit(function(){
    });
    //form触发事件
    $(".shower-card").click(function(){
        var img = $(this).children("img").attr("src");
        var goods_info = $(this).children("div").children(".shower-card-h1").text();
        var price = $(this).children("div").children(".shower-card-h2").text();
        $(".shower-card-form").children(".form-input1").attr({"value":img});
        $(".shower-card-form").children(".form-input2").attr({"value":goods_info});
        $(".shower-card-form").children(".form-input3").attr({"value":price});
        $(".shower-card-form").submit();
    });
});


