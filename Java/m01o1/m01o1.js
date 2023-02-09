let uitleg = "In een parkeergarage passen 80 auto's op de begane grond en 120 op een verdieping.\n"+
"Vraag het gewenste aantal auto's in de garage en bereken het aantal verdiepingen wat je nodig hebt.";

alert(uitleg);
let gewenste_aantal_autos = parseInt(prompt("Hoeveel autos wilt u kwijt in de parkeergarage?"));
console.log(gewenste_aantal_autos);
// Berekenen hier het aantal verdiepingen
let aantal_verdiepingen = 1;
gewenste_aantal_autos -= 80;
if (gewenste_aantal_autos > 120){;
    aantal_verdiepingen += gewenste_aantal_autos / verdieping
}; 

console.log(aantal_verdiepingen);

let tekst = 'hallo' + aantal_verdiepingen + 'gaat';
let antwoord = 'voor zoveel autos' + gewenste_aantal_autos + 'heb je zoveel verdiepingen nodig' + aantal_verdiepingen;
document.getElementById("antwoord").innerText = antwoord;

console.log("Om het gewenste aantal autos kwijt te kunnen heb ik x verdiepingen nodig.")
