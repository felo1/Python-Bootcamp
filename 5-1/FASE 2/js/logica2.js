let carritoItems = ['1','Chalas','Caipirinha'];

/* function generarLista(array) {
    // Create the list element:
    var list = document.createElement('ul');

    for (var i = 0; i < array.length; i++) {
        // Create the list item:
        var item = document.createElement('li');

        // Set its contents:
        item.append(document.createTextNode(array[i]));

        // Add it to the list:
        list.append(item);
    }

    // Finally, return the constructed list:
    return list;
} */

// Add the contents of options[0] to #foo:
//document.getElementById('carrito').appendChild(generarLista(carritoItems[0]));


/*
Try to reduce the actions on the DOM as much as possible. Every appendChild on 
unorderedList forces the browser to re-render the complete page. Use documentFragement 
for that sort of action.

var frag = document.createDocumentFragment();
for (var i = alphabet.length; i--; ) {
   var li = document.createElement("li");
   li.appendChild(document.createTextNode(alphabet[indexNum++]));
   frag.appendChild(li);
}
unorderedList.appendChild(frag);
So there will be only one DOM action which forces a complete redraw instead of alphabet.length redraws*/


/* var frag = document.createDocumentFragment();

for (var i = 0; i < array.length; i++) {
   var li = document.createElement("li");
   li.appendChild(document.createTextNode(carritoItems[i]));
   frag.appendChild(li);
}

unorderedList.appendChild(frag);

window.onload=function(){<!-- w  ww .  j ava2 s.c  o  m-->
    el = document.createElement('li');
    el.innerHTML = 'Jeff';
    document.getElementById('MyUl').appendChild(el);
} */

/* yo me comprometi a trabajar en el punto 5, de hacer el carrito y que se llene con un arreglo que sea manipulable
desde otros puntos de la página (para agregar items), y que cada list item además tb de la opción de borrarlos. */

/*burdo pero funciona
window.onload=function(){

    el = document.createElement('li');
    el.innerHTML = ['1','Chalas','Caipirinha'];
    document.getElementById('MyUl').appendChild(el);
}
*/


window.onload=function generarLista(array){
    var list = document.createElement('li');
    for (var i=0;i< array.length; i++){
        var item = document.createElement('li');
        item.append(document.createTextNode(array[i]));
        list.append(item);
    }
    return list;
}

var options = [
    set0 = ['Option 1','Option 2'],
    set1 = ['First Option','Second Option','Third Option']
];

window.onload=function makeUL(array) {
// Create the list element:
var list = document.createElement('ul');

for(var i = 0; i < array.length; i++) {
    // Create the list item:
    var item = document.createElement('li');

    // Set its contents:
    item.appendChild(document.createTextNode(array[i]));

    // Add it to the list:
    list.appendChild(item);
}

// Finally, return the constructed list:
return list;
}

// Add the contents of options[0] to #foo:
document.getElementById('carrito').appendChild(makeUL(carritoItems[0]));