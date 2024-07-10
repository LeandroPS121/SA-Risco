function loadRiscos() {
    selectedId = document.getElementById('situacao').value
    fetch('/IAS/form/lr/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({ 'situacao_id': selectedId })
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw alert('erro envio');
        })
        .then(data => {
            riscos = data.riscos;
            let options = "<option value='0'>--</option>\n";
            // alert("riscos: "+riscos)
            riscos.forEach(function (item) {
                console.log('nome: ' + item.nome_risco)
                options += "<option value=" + item.id + ">" + item.id + " - " + item.nome_risco + "</option>\n"
            })
            document.getElementById('risco').innerHTML = options;
        })
        .catch(error => {
            console.error('Erro:', error);
        });
}