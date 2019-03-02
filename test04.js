// hello worldhello worldhello world

// hello world
// hello world

//  c= function(){
// console.log("a-b*2")
// }()
$(function () {
    // $("#background").click(function (e) { 
    //     $(this).css({width: "50px",height:"50px",backgroundColor:"red"});
    //     console.log(this)
    //     $(this).slideToggle(1000,function(){
    //         console.log("ok")

    //     });
    // });
    $("#insert").click(function (e) {
        $(this).addClass("active");
        console.log(e)
    }).focus(function (e) { 
        $(this).removeClass("active");
   });
    
    // (function(e){
    //     $(this).removeClass("active");
       
    // });
})