$(document).ready(function () {
    
$(".clases").html("chao");
$("h1").html("h1 feo");

$("#customlist li").html("notFirst");
$("#customlist li:first").html("cambio de texto");



$("button").addClass("btn btn-dark");

$("#contenido").append("<h1>Elemento agregado al final</h1>");
$("#redtext").css("color","red"); //horrible el formato pero funciona.
//creo que es relevante sobre la version dejquery usada.
$("#redtext").css("color","red","font-size","50px"); //horrible el formato pero funciona.

//se puede hacer desmenuzado:
$("#redtext").css({
        "background-color": "yellow",
        "font-weight": "bolder"
                })

$(".vainilla").click(function(){
$("#redtext").toggle();


});

//fin docu ready             
});   
