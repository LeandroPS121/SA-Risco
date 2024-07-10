function getCSRFToken() {
    var name = 'csrftoken=';
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookies = decodedCookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return '';
}

function desactiveButton(btnId){
    let botao = document.getElementById('btnId')
    botao.disable = true;
    setInterval(function(){
        botao.disable = false;
    }, 5000);
}

var formulario = document.getElementById('myForm');
formulario.planta.textContent;
document.getElementsByTagName("<code>")