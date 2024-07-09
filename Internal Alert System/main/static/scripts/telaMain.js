document.addEventListener("DOMContentLoaded", function () {
    const table = document.getElementById('tabela-relatorios');
    const checkboxes = table.querySelectorAll('tbody input[type="checkbox"]');
    const checkTodos = document.getElementById('checkTodos');

    // Adicionar evento ao checkbox "Selecionar Todos"
    checkTodos.addEventListener('change', function () {
        checkboxes.forEach(function (checkbox) {
            checkbox.checked = checkTodos.checked;
            const row = checkbox.closest('tr');
            if (checkTodos.checked) {
                row.classList.add('selected');
            } else {
                row.classList.remove('selected');
            }
        });
    });

    // Adicionar eventos para os checkboxes individuais
    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener('click', function (event) {
            event.stopPropagation();
            const row = this.closest('tr');
            if (this.checked) {
                row.classList.add('selected');
            } else {
                row.classList.remove('selected');
            }
        });

        // Adiciona evento de clique na linha para ativar/desativar o checkbox
        checkboxes[i].closest('tr').addEventListener('click', function () {
            const checkbox = this.querySelector('input[type="checkbox"]');
            checkbox.checked = !checkbox.checked;
            if (checkbox.checked) {
                this.classList.add('selected');
            } else {
                this.classList.remove('selected');
            }
        });
    }
});

// Função para excluir linhas selecionadas
function excluirSelecionados() {
    const checkboxes = document.querySelectorAll('#tabela-relatorios tbody input[type="checkbox"]:checked');
    
    checkboxes.forEach(function (checkbox) {
        checkbox.closest('tr').remove();
    });

    verificaDadosPlanilha();
}
function verificaDadosPlanilha(){
    const table = document.getElementById('tabela-relatorios');
    const tbody = table.querySelector('tbody');
    
    // Verifica se ainda há linhas na tabela
    if (tbody.rows.length === 0) {
        const tableContainer = document.querySelector('.table-container');
        const mensagem = document.createElement('div');
        mensagem.textContent = 'Não há dados na planilha.';
        mensagem.classList.add('text-center', 'mt-3', 'text-muted');
        tableContainer.replaceWith(mensagem);
    }
}

// Função para filtrar a tabela
function filtrarTabela() {
    const input = document.getElementById('btn-pesquisar');
    const filter = input.value.toUpperCase();
    const table = document.getElementById('tabela-relatorios');
    const trs = table.getElementsByTagName('tr');

    // Loop pelas linhas da tabela
    for (let i = 1; i < trs.length; i++) {
        let matchFound = false;
        const tds = trs[i].getElementsByTagName('td');

        for (let j = 0; j < tds.length; j++) {
            const td = tds[j];
            if (td) {
                let textValue = td.textContent || td.innerText;
                if (textValue.toUpperCase().indexOf(filter) > -1) {
                    matchFound = true;
                    break;
                }
            }
        }

        if (matchFound) {
            trs[i].style.display = '';
        } else {
            trs[i].style.display = 'none';
        }
    }
}
verificaDadosPlanilha();