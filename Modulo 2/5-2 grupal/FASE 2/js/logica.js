var carritoItems = [
//{codigo:"1", nombre:'zapato casual', precio:10990, cantidad: 1},
//{codigo:"2", nombre:'zapato escolar', precio:19990, cantidad: 2}
];
window.addEventListener('load', fillCarrito); //colocar el addeventlistener ANTES de la funcion si no se rellena 2 veces
window.addEventListener('load', sumaItems);

function fillCarrito(){
   var total = 0;
   const ul = document.getElementById('carritoLista'); //targetea el UL a rellenar
   ul.innerHTML = ''; // evita que se haga stacking de lista entera.
   carritoItems.forEach(item => { //inicia iteracion del arreglo carritoItems
    if (item.cantidad>0){ //con esto al refrescar el carrito IGNORA los con cantidad = 0. Sumado con que con cada refresco se vacía el UL (no los datos de origen).
      total = total + item.precio*item.cantidad;
      const li = document.createElement('li'); //prepara un elemento LI
      li.textContent = `${item.nombre} - $${item.precio} - ${item.cantidad}`; //lo rellena con contenido desde el arreglo
      ul.appendChild(li); //lo inserta en el UL
    }
    });
    //agregar el total
    const li = document.createElement('li');
    li.textContent = `Total: $${total}`; //lo rellena con contenido desde el arreglo
    ul.appendChild(li);
    sumaItems();
}

function sumaItems(){
   //actualiza la cantidad de items en el carrito, para incluirlo en cada click de cantidad + -
       //sumatoria real
       let sumatoria = 0;
        for(let carritoItem of carritoItems){ //no me resultó mi for each in
          sumatoria += carritoItem.cantidad;
        }
        document.getElementById("suma-items").innerHTML = sumatoria;
       
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

