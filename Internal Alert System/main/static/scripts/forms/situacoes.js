function loadSituacoes() {
    var selectedElement = document.getElementById('local');
    var selectedOption = selectedElement.options[selectedElement.selectedIndex];
    var selectedId = selectedOption.getAttribute('name');

        fetch('/IAS/form/ls/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ 'local_id': selectedId })
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw alert('erro envio');
            })
            .then(data => {
                situacoes = data.situacoes;
                let options = "<option value='0'>--</option>\n";
                // alert("situacoes: "+situacoes)
                situacoes.forEach(function (item) {
                    console.log('nome: ' + item.nome_situacao)
                    options += "<option id='" + item.id + "' name='" + item.id + "'>" + item.id + " - " + item.nome_situacao + "</option>\n";
                })
                document.getElementById('situacao').innerHTML = options;
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    }