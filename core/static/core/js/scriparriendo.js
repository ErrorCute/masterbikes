$(document).ready(function(){

    $("#errores").hide()
    $("#formulario-arriendo").submit(function(){
        var mensaje='';
        var nombre_arrendador =$("#nombre_arrendador").val();
        var tipo_bicicleta =$("#tipo_bicicleta").val();
        var modelo =$("#modelo").val();
        var correo =$("#correo").val();
        var fecha_arriendo =$("#fecha_arriendo").val();

        if (nombre_arrendador=='' || tipo_bicicleta==''||modelo==''||correo==''||fecha_arriendo==''){

            mensaje='<h5> Faltan datos por ingresar  </h5> ';
        }
    
        if (mensaje !=''){

            $("#errores").html(mensaje);
            $("#errores").fadeIn(2000);
            event.preventDefault();

        }

    })

});