var carritoItems = [
{id:1, productName:'zapato casual', precio:10990, cantidad: 1},
{id:2, productName:'zapato escolar', precio:19990, cantidad: 2}
];
 
window.addEventListener('load', fillCarrito); //colocar el addeventlistener ANTES de la funcion si no se rellena 2 veces
window.addEventListener('load', sumaItems);

function fillCarrito(){
   var total = 0;
   const ul = document.getElementById('carritoLista'); //targetea el UL a rellenar
   carritoItems.forEach(item => { //inicia iteracion del arreglo carritoItems
      total = total + item.precio*item.cantidad;
      const li = document.createElement('li'); //prepara un elemento LI
      li.textContent = `${item.productName} - $${item.precio} - ${item.cantidad}`; //lo rellena con contenido desde el arreglo
      ul.appendChild(li); //lo inserta en el UL
    });
    //agregar el total
    const li = document.createElement('li');
    li.textContent = `Total: $${total}`; //lo rellena con contenido desde el arreglo
    ul.appendChild(li);
}

function sumaItems(){
   //actualiza la cantidad de items en el carrito, para incluirlo en cada click de cantidad + -
       document.getElementById("suma-items").innerHTML = carritoItems.length;
}


//logica para el modal demo

function modalPOP(){
   let newState = -1;
   setTimeout(function(){
      if(newState == -1){
         //funciona, lanzar a pagina de inicio con carrito vacio
         carritoItems.length = 0;
         window.location.replace("index.html");
      }
  }, 5000);
}


var count = 0;
var count = document.getElementById("count");
function plus(){
    count++;
    count.value = count;
}
function minus(){
  if (count > 1) {
    count--;
    count.value = count;
  }  
}

/*
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
}*/