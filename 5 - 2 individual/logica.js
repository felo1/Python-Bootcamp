document.addEventListener('DOMContentLoaded', function() { //importante que las cosas carguen luego del dom, 
  //eso rompia la logica. No sabía esto.

const inputPalabra = document.getElementById('inputPalabra');
const outputPalabra = document.getElementById('outputPalabra');

inputPalabra.addEventListener('input', function() {
const palabra = inputPalabra.value.replace(/[^a-zA-Z]/g, '');

outputPalabra.value = palabra;

if(palabra.length>1){
const ini = palabra.charAt(0).toUpperCase();
const fin = palabra.charAt(palabra.length - 1).toUpperCase();
outputPalabra.value = ini + palabra.slice(1, -1) + fin;
}
else if(palabra.length==1){
  outputPalabra.value = palabra.charAt(0).toUpperCase();;
}

});
});


function fillList() {
  const txt = document.getElementById('inputText').value;
  const ul = document.getElementById('listaItems'); //targetea el UL a rellenar
  const li = document.createElement('li');
  li.textContent = txt; //lo rellena con contenido desde el arreglo
  li.id = liIndex;
  liIndex++;
  ul.appendChild(li);
  li.onclick = function() { 
  this.parentNode.removeChild(this); //gracias stack overflow.
  };

  ul.appendChild(li);
}
