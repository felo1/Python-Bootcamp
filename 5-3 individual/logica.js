document.addEventListener('DOMContentLoaded', (event) => {

document.onload = normal();

function normal(){ 
document.getElementById("luzazul").style.backgroundColor = "green";  

setTimeout(() => {
  document.getElementById("luzroja").style.backgroundColor = "black";
  document.getElementById("luzamarilla").style.backgroundColor = "yellow";  
  document.getElementById("luzazul").style.backgroundColor = "black";
  setTimeout(() => { 
    document.getElementById("luzroja").style.backgroundColor = "red";
    document.getElementById("luzamarilla").style.backgroundColor = "black";  
    document.getElementById("luzazul").style.backgroundColor = "black";
    setTimeout(() => { 
      document.getElementById("luzroja").style.backgroundColor = "black";
  }, 3000);
  }, 1000);
  }, 3000);
}

//* FIN DOCUMENTO ONLOAD */
})
/*
document.addEventListener("mousemove", function(event) {

  // Calculate the distance between the mouse position and the target div
  const luz = document.getElementById("luzamarilla");
  const luzFigurita = document.getElementById("figurita");

  const distancia = Math.sqrt(
    Math.pow(event.pageX - luz.offsetLeft, 2) +
    Math.pow(event.pageY - luz.offsetTop, 2)
  );

  if (distancia < 200) {
    console.log("ya close");
  }
});
*/