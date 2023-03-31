$(document).ready(function () {

    var dataSet = [
        {
          codigo: "1",
          imagen: "",
          nombre: "Zapato casual",
          descripcion: "Para toda ocasión",
          precio: 10990,
          preciomayor: 9891
        },
        {
          codigo: "2",
          imagen: "",
          nombre: "Zapato escolar",
          descripcion: "Sencillo y funcional",
          precio: 19990,
          preciomayor: 17991
        },
        {
          codigo: "3",
          imagen: "",
          nombre: "Zapato negro",
          descripcion: "Elegante y cómodo",
          precio: 15000,
          preciomayor: 13500
        },
        {
          codigo: "4",
          imagen: "",
          nombre: "Chalabota",
          descripcion: "Lo último en mal diseño",
          precio: 12990,
          preciomayor: 11691
        },
        {
          codigo: "5",
          imagen: "",
          nombre: "Bototos",
          descripcion: "De toda la vida",
          precio: 45000,
          preciomayor: 40500
        },
        {
          codigo: "6",
          imagen: "",
          nombre: "Tacos",
          descripcion: "Estilo, pero a qué costo?",
          precio: 69000,
          preciomayor: 62100
        },
        {
          codigo: "7",
          imagen: "",
          nombre: "Zapato con plataforma",
          descripcion: "14 cm de gracia",
          precio: 12990,
          preciomayor: 11691
        },
        {
          codigo: "8",
          imagen: "",
          nombre: "Zapatilla",
          descripcion: "Para hacer deporte",
          precio: 25990,
          preciomayor: 23391
        },
      ];

    $("#example").DataTable({
      data: dataSet,
      columns: [
        
        { title: "Codigo", data: "codigo" },
        { title: "Nombre", data: "nombre" },
        { title: "Imagen", data: "imagen" },
        { title: "Descripcion", data: "descripcion" },
        { title: "Precio", data: "precio" },
        { title: "PrecioxMayor", data: "preciomayor" },
        {
          title: "En carrito",
          data: null,
          render: function (data, type, row) {
              return ('<button class="agregar">+</button>' +
              '<span class="contador'+ row.codigo+'"></span>' + //notese la manera de introducir js ahi dentro y referenciar el row
              '<button class="quitar">-</button>'
              );
          }}
      ],
    });

//esfuerzos por hacer el button a fuerza bruta con append.
    
    //$("#example tr").css("padding-bottom","555px");
    
    //$("#example tr").prepend("<div><tr><td><button class='agrega1'>+</button><p codigo='contador'>0</p><button class='quita1'>-</button></td></div>");

    //$("#example thead tr div").html("");


    
      $('#example tbody').on('click', '.agregar', function agregar() {
        let table = $('#example').DataTable();

        let data = table.row($(this).closest('tr')).data(); // lleno una variable con toda fila (no es un arreglo peruseable)
        let codigo = data.codigo; // pero si puedo hacer estos llamados a sus parametros así. Estimo que son funciones del js importado datatables
        //let contador = parseInt($('#contador').text()) + 1; //falta agregar logica para evitar que se vaya a -1 abajo
        //$('#contador').text(contador);
        
        var itemIndex = carritoItems.findIndex(function(item) { //item e item index son iteradores arbitrarios
          //con item peruseo los datos en toda esa columna en el carrito. con data me refiero a la columna del html
          return item.codigo === data.codigo; 
        });
        
        //si no está en el carrito, push al arreglo
        if (itemIndex === -1) { //honestamente, no sé porqué tiene que ser -1 y no 0 
          //para que funcione. buena pregunta para el docente. //si es 0 da undefined.
          carritoItems.push({codigo: data.codigo, nombre: data.nombre, precio: data.precio, cantidad: 1});
        }
        // de lo contrario (existe), en lugar de push al arreglo sube la cantidad internamente
        else {
          carritoItems[itemIndex].cantidad++;
        }
        //console.log(carritoItems);
        fillCarrito(); //sin esto, no hace un llamado a actualizar el carrito.
      });

      $('#example tbody').on('click', '.quitar', function quitar() {
        
        let table = $('#example').DataTable();
        let data = table.row($(this).closest('tr')).data(); // lleno una variable con toda fila (no es un arreglo peruseable)
        let codigo = data.codigo; // pero si puedo hacer estos llamados a sus parametros así. Estimo que son funciones del js importado datatables
        
        var itemIndex = carritoItems.findIndex(function(item) {
          if(item.codigo === codigo && item.cantidad >= 1){ //ignorar clicks si el contador está en 0, apuntar a solo ESE codigo (lol sin eso saca 1 de todos)
           item.cantidad--;
           fillCarrito();
          }
        }); //item = carrito, data = html
        //de lo contrario, no hacear nada
      });

      /* Funciona btw
      var table = $('#example').DataTable();
 
      $('#example tbody').on( 'click', 'button.agrega1', function () {

          console.log( table.row( $(this).closest('tr') ).data())
      } ); 
      */

      /* Ejemplo básico de pass
      $('#example tbody').on( 'click', 'tr', function () {
        console.log( table.row( this ).data() );
      } ); */ 

    /*   $("table").css({
        "background-color": "yellow",
        "width": "50%"
                }) */
  });



