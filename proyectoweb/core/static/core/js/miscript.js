function Validacion(){ 
    if(document.getElementById("nombre").value.length==0) { 
        alert("Tienes que ingresar tu nombre")
        document.getElementById("nombre").focus()
        return 0;
    }

    edad = parseInt(document.getElementById("edad").value)
    if (isNaN(edad)){ 
        alert("Ingrese un numero en la casilla!")
        document.Formulario.edad.focus()
        return 0;
    }else{
        if (edad<18){
            alert("Debes ser mayor de edad")
            document.Formulario.edad.focus()
            return 0;
        }
    }
    if(document.getElementById("email").value.length==0){
        alert("Ingresar su coreo electronico")
        document.getElementById("email").focus()
        return 0;
    }
    alert("Datos validados");
    document.Formulario.submit();
}