$(document).ready(function () {

    var dataSet = [
        {
          codigo: "1",
          nombre: "Zapato casual",
          descripcion: "Para toda ocasión",
          precio: 10990,
          preciomayor: 9891
        },
        {
          codigo: "2",
          nombre: "Zapato escolar",
          descripcion: "Sencillo y funcional",
          precio: 19990,
          preciomayor: 17991
        },
        {
          codigo: "3",
          nombre: "Zapato negro",
          descripcion: "Elegante y cómodo",
          precio: 15000,
          preciomayor: 13500
        },
        {
          codigo: "4",
          nombre: "Chalabota",
          descripcion: "Lo último en mal diseño",
          precio: 12990,
          preciomayor: 11691
        },
        {
          codigo: "5",
          nombre: "Bototos",
          descripcion: "De toda la vida",
          precio: 45000,
          preciomayor: 40500
        },
        {
          codigo: "6",
          nombre: "Tacos",
          descripcion: "Estilo, pero a qué costo?",
          precio: 69000,
          preciomayor: 62100
        },
        {
          codigo: "7",
          nombre: "Zapato con plataforma",
          descripcion: "14 cm de gracia",
          precio: 12990,
          preciomayor: 11691
        },
        {
          codigo: "8",
          nombre: "Zapatilla",
          descripcion: "Para hacer deporte",
          precio: 25990,
          preciomayor: 23391
        },
        {
          codigo: "9",
          nombre: "Chalas zico",
          descripcion: "Porque lo vales",
          precio: 25990,
          preciomayor: 23391
        },
        {
          codigo: "10",
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
        { title: "Descripcion", data: "descripcion" },
        { title: "Precio", data: "precio" },
        { title: "PrecioxMayor", data: "preciomayor" },
      ],
    });

  });



