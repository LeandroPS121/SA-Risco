    // Função para selecionar/desselecionar uma linha ao clicar nela ou no checkbox
        document.addEventListener("DOMContentLoaded", function() {
            var table = document.getElementById('tabela-relatorios');
            var checkboxes = table.querySelectorAll('tbody input[type="checkbox"]');
            var checkTodos = document.getElementById('checkTodos');
            
            // Adicionar evento ao checkbox "Selecionar Todos"
            checkTodos.addEventListener('change', function() {
                checkboxes.forEach(function(checkbox) {
                    checkbox.checked = checkTodos.checked;
                    var row = checkbox.closest('tr');
                    if (checkTodos.checked) {
                        row.classList.add('selected');
                    } else {
                        row.classList.remove('selected');
                    }
                });
            });
            
            // Adicionar eventos para os checkboxes individuais
            for (var i = 0; i < checkboxes.length; i++) {
                checkboxes[i].addEventListener('click', function(event) {
                    event.stopPropagation();
                    var row = this.closest('tr');
                    if (this.checked) {
                        row.classList.add('selected');
                    } else {
                        row.classList.remove('selected');
                    }
                });
                
                // Adiciona evento de clique na linha para ativar/desativar o checkbox
                checkboxes[i].closest('tr').addEventListener('click', function() {
                    var checkbox = this.querySelector('input[type="checkbox"]');
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
            var checkboxes = document.querySelectorAll('#tabela-relatorios tbody input[type="checkbox"]:checked');
            var idsParaExcluir = [];
            
            checkboxes.forEach(function(checkbox) {
                idsParaExcluir.push(checkbox.value);
            });
            // Remover as linhas da tabela (apenas para visualização, a exclusão real deve ser feita no servidor)
            checkboxes.forEach(function(checkbox) {
                checkbox.closest('tr').remove();
            });
        }

        function filtrarTabela() {
        var input = document.getElementById('btn-pesquisar');
        var filter = input.value.toUpperCase();
        var table = document.getElementById('tabela-relatorios');
        var trs = table.getElementsByTagName('tr');

        for (var i = 0; i < trs.length; i++) {
            var matchFound = false;
            var tds = trs[i].getElementsByTagName('td');
            
            for (var j = 0; j < tds.length; j++) {
                var td = tds[j];
                if (td) {
                    var textValue = td.textContent || td.innerText;
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