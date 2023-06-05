$(document).ready(function(){

    $("#errores").hide()
    
    $("#login").submit(function(){

        var mensaje='';
        var correo=$('#correo').val();
        var password=$('#password').val();

        if (correo==''){

            mensaje='<h5> Debe ingresar correo </h5> ';
        }
        if (password==''){

            mensaje +='<h5> Debe ingresar Clave</h5> ';
        }


        if (mensaje !=''){

            $("#errores").html(mensaje);
            $("#errores").fadeIn(2000);
            event.preventDefault();
        }

        

    })

    



});