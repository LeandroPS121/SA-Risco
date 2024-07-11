function rapidao(){
    var selectedElement = document.getElementById('situacao');
    var selectedOption = selectedElement.options[selectedElement.selectedIndex];
    var selectedClass = selectedOption.getAttribute('class');

    situacaoVA=selectedClass;

    selectedElement = document.getElementById('risco');
    selectedOption = selectedElement.options[selectedElement.selectedIndex];
    selectedClass = selectedOption.getAttribute('class');

    riscoScore=parseInt(situacaoVA+selectedClass);

    alert(riscoScore)

    if(riscoScore==0){
        document.getElementById('validarArea').textContent='HSE'
    }else if(riscoScore==1){
        document.getElementById('validarArea').textContent='AVALIAR'
    }else{
        document.getElementById('validarArea').textContent='C/AUP'
    }

}
