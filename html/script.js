let loggedin = [];

function getindexOfElementByName(lijst, naam){

    return -1;
}

function handlelogin(){
    console.log(loggedin);
    console.log(Date());
}
    let naam = document.getElementById('inputnaam').value;
    if (naam.length <= 0){
        alert('Voer een naam in')
        return
   
    }
    console.log('U hebt op de button geklikt');

    let positie = getindexOfElementByName(loggedin,naam);
    if  (positie > -1){ 
        (loggedin.includes(naam))
        loggedin.splice(loggedin.indexOf(naam),1)
        console.log('U bent uitgelogd');
        document.getElementById('melding').innerText = 'U bent uitgelogt:' + naam;
    
    } else {
        loggedin.push({'naam': naam, 'moment': new Date()});
        console.log('U bent ingelogd');
        document.getElementById('melding').innerText = 'U bent uitgelogt:' + naam;
}   {
    
    loggedin.push(naam);
    console.log('U bent ingelogt');
    document.getElementById('melding').innerText = 'U bent ingelogd: ' + naam;
}
document.getElementById('inputnaam').value = ''
console.log(loggedin);
// document.getElementById('inlogButton').onclick = handlelogin;