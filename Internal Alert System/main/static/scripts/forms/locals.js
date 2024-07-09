function loadLocals(){

    selectedId=document.getElementById('planta').value

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
        console.log("AAAAAAAAAAAAAAAAAAA")
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