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
        console.log('ID da planta selecionada enviado com sucesso para a view Django:', data);
        // Aqui você pode tratar a resposta da view, se necessário
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}
