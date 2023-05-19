$(document).ready(function(){

    $("#errores").hide()

    $("#formulario").submit(function(){
        var mensaje='';
        var nombre =$("#nombre").val();
        var correo =$("#correo").val();
        var pas=$("#pas").val();
        var fec=$("#fec").val();

        if (nombre=='' || correo==''||pas==''||fec==''){

            mensaje='<h5> Faltan datos por ingresar  </h5> ';
        }
    
        if (mensaje !=''){

            $("#errores").html(mensaje);
            $("#errores").fadeIn(2000);
            event.preventDefault();

        }

    })

});