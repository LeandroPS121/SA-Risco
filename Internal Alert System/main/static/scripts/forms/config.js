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
    let botao = document.getElementById(btnId)
    botao.disabled = true;
    setInterval(function(){
        botao.disabled = false;
    }, 5000);
}

function verificaVitima(){
    let nivelDanos = document.getElementById('nivelDanos');
    let houveVitima = document.getElementById("houveVitimas").value;
    let statusBtn = false;
    if (houveVitima == "nao") {
        statusBtn = true;
    }
    nivelDanos.disabled = statusBtn;
}