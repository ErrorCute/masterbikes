$(document).ready(function(){
    
    // asignar click al boton
    
    fetch('https://mindicador.cl/api').then(function(response) {
    return response.json();
}).then(function(dailyIndicators) {
    document.getElementById("UF").innerHTML = 'El valor actual de la UF es $' + dailyIndicators.uf.valor;
    document.getElementById("DolarO").innerHTML = 'El valor actual del Dólar observado es $' + dailyIndicators.dolar.valor;
    document.getElementById("DolarA").innerHTML = 'El valor actual del Dólar acuerdo es $' + dailyIndicators.dolar_intercambio.valor;
    document.getElementById("UTM").innerHTML = 'El valor actual de la UTM es $' + dailyIndicators.utm.valor;
 
}).catch(function(error) {
    console.log('Requestfailed', error);
});


});