let naamIngelogd = ''

function handlelogin(){
    let naam = document.getElementById('inputnaam').value;
    console.log('U hebt op de button geklikt');
    if (naamIngelogd === ''){
        naamIngelogd = naam;
        console.log('U bent ingelogd: ' + naam);
        document.getElementById('inputnaam').value= '';
    }
}