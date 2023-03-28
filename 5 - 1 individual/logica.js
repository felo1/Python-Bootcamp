var liIndex = 0;

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


