function definirArea(){
alert('ok')

    let selectedElement = document.getElementById('situacao');
    let selectedOption = selectedElement.options[selectedElement.selectedIndex];
    let selectedClass = selectedOption.getAttribute('class');

    situacaoVA=selectedClass;

    selectedElement = document.getElementById('risco');
    selectedOption = selectedElement.options[selectedElement.selectedIndex];
    selectedClass = selectedOption.getAttribute('class');

    riscoScore=parseInt(situacaoVA+selectedClass);

    alert(riscoScore)

    let area;
    if(riscoScore==0){
        area='HSE'
        
    }else if(riscoScore==1){
        area='AVALIAR'
    }else{
        area='C/AUP'
    }
    alert( document.getElementById('validarArea').value)
    document.getElementById('validarArea').value = area;
}


