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



function desactiveButton(){
    let botao = document.getElementById('btn-enviar')
    botao.disable = true;
    setTimeout(function(){
        botao.disable = false;
    }, 5000);
}