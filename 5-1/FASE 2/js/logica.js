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

/*
Atrapa cada btn click del selector de cantidad.
Chequea si ya está el item. Si está, agrega 1, si no:
Agrega 1 al total tomando codigo, precio y nombre, foto tb quizá?


mockup




carritoCheck(item){
   found = false
   for(let i of carritoItems){
      if(item=carritoItems(i)){
         found = true;
         return i (donde I es la posicion del arreglo donde encontró el item.)
         break;
      }
   }
   if(found){
      return (carritoItems(i));
   }  
   else{
      return null
   }

}

btnAdd(item){
   if(carritoCheck(item)!=null){ //chequear si está el item, la funcion me devuelve un null o ubicacion en arreglo 
      carritoUpdate(item);
   }
   else{
      carritoAdd(item);
   }
}

*/

