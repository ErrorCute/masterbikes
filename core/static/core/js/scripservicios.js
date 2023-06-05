$(document).ready(function(){

    $("#errores").hide()
    $("#formulario-arriendo").submit(function(){
        var mensaje='';
        var nombre_encargo =$("#nombre_encargo").val();
        var tipo_bicicleta =$("#tipo_bicicleta").val();
        var modelo =$("#modelo").val();
        var correo =$("#correo").val();
        var descripcion =$("#descripcion").val();

        if (nombre_encargo=='' || tipo_bicicleta==''||modelo==''||correo==''||descripcion== ''){

            mensaje='<h5> Faltan datos por ingresar  </h5> ';
        }
    
        if (mensaje !=''){

            $("#errores").html(mensaje);
            $("#errores").fadeIn(2000);
            event.preventDefault();

        }

    })

});