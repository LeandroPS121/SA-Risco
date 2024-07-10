function loadLocals() {

    var selectedElement = document.getElementById('planta');
    var selectedOption = selectedElement.options[selectedElement.selectedIndex];
    var selectedId = selectedOption.getAttribute('name');
   

    if (selectedId != 0) {
        fetch('/IAS/form/ll/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ 'planta_id': selectedId })
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Erro no envio');
            })
            .then(data => {
                var locals = data.locals;
                let options = "<option name='0'>--</option>\n";
                locals.forEach(item => {
                    options += "<option id='" + item.id + "' name='" + item.id + "'>" + item.id + " - " + item.nome_local + "</option>\n";
                });

                // Atualiza o HTML do select 'local' após todas as opções serem geradas
                document.getElementById('local').innerHTML = options;
            })
            .catch(error => {
                console.error('Erro:', error);
            })
    } else {
        document.getElementById('local').innerHTML = "<option name='0'>--</option>\n";
    }
}
