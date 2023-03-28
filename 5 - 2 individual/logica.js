/* 
const inputText = document.getElementById('inputPalabra');
const outputText = document.getElementById('outputPalabra');

window.onload = function formatText(text) {
    //regex??? para limpiar simbolos
  const cleanedText = text.replace(/\d+/g, '');

    //capitalizar
  const firstLetter = cleanedText.charAt(0).toUpperCase();
  const lastLetter = cleanedText.charAt(cleanedText.length - 1).toUpperCase();
  const middleText = cleanedText.slice(1, -1);
  const formattedText = `${firstLetter}${middleText}${lastLetter}`;

  return formattedText;
} */

 /*inputText.addEventListener('', () => {
    const text = inputText.value;
    const formattedText = formatText(text);
    outputText.textContent = formattedText; 
  });

*/
  
const input = document.querySelector("input");
const log = document.getElementById("log");

input.addEventListener("keydown", logKey);

function logKey(e) {
  log.textContent += ` ${e.code}`;
}