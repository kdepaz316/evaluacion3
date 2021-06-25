$(document).ready(function(){
    $('#DatosClima').hide();
})
    


function cargar_clima(){
    var clima = new XMLHttpRequest();
    var ciudad = document.getElementById("ciudad").Value;
    clima.open('GET','https://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=8fefcdc4f65e87fdd7c08f9e34215dc5&units=metric', false);
    clima.send(null);


    var datos = JSON.parse(clima.response);
    var ciudad = datos.name;
    var temp = datos.main.temp_min;
    var humedad = datos.main.humidity;
    var viento = datos.wind.speed;

    $('#ubicacion').html(ciudad);
    $('#temp').html(temp);
    $('#humedad').html(humedad);
    $('#viento').html(viento);
    $('#ciudad').val('');

    $('#DatosClima').show();
    
}