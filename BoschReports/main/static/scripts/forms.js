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

function refreshLocals(){


    selectedId=document.getElementById('planta').value

    alert(selectedId);

    fetch('/br/form/lp/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Inclua o token CSRF se necessário
        },
        body: JSON.stringify({ 'planta_id': selectedId })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw alert('erro envio');
    })
    .then(data => {
        locals=data.locals;
        options="";
        locals.forEach(function (item){
            console.log('nome: '+item.nome_local)
           options+="<option id="+item.id+">"+item.id+" - "+item.nome_local+"</option>\n"
        })
        document.getElementById('local').innerHTML=options
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function desactiveButton(){
    let botao = document.getElementById('btn-enviar')
    botao.disable = true;
    setTimeout(function(){
        botao.disable = false;
    }, 5000);
}