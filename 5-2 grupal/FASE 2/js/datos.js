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
        {
          codigo: "9",
          imagen: "",
          nombre: "Chalas zico",
          descripcion: "Pporque lo vales",
          precio: 25990,
          preciomayor: 23391
        },
        {
          codigo: "10",
          imagen: "",
          nombre: "Zancos",
          descripcion: "Para gente de 1.5m",
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


  });



