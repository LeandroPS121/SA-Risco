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
    }, 1000);
}

function verificaVitima(){
    let nivelDanos = document.getElementById('nivelDanos');
    let houveVitima = document.getElementById("houveVitimas").value;
    // let statusBtn = false;
    let formDanos = document.getElementById('form-nivel-dano');
    formDanos.classList.remove('d-none');
    if (houveVitima == "nao") {
        formDanos.classList.add('d-none');
        // nivelDanos.value = "Sem vitimas"
        alert(nivelDanos.index)
        // statusBtn = true; <- opção para caso nao queira sumir com o input
    }
    // nivelDanos.disabled = statusBtn;
}