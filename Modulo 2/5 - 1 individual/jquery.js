$(document).ready(function(){
  var inputReader = inputTextJQuery;
  $("#fillListJQ").click(function(){
    
        $("#listaItemsJQ").append("<li id='hideMe'>"+ inputReader.value + "</li>")
        //inputTextJQuery.value
  });
  $("#listaItemsJQ").on("click", "#hideMe", function(){ 
    $(this).hide();
  });
});



/* mis event listeners:
Yes, the jQuery code is using event listeners. Specifically, it's using the .click() 
function to listen for click events on the #fillListJQ button and the .on() function 
to delegate a click event to the #listaItemsJQ unordered list and hide the clicked item. */