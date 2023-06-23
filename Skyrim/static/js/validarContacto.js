$(document).ready(function() {

    $("#btnContacto").click(function(event) {
      var nombre = $("#nombre").val();
      var email = $("#email").val();
      var asunto = $("#asunto").val();
      var mensaje = $("#mensaje").val();
      
      if (nombre === "" || email === "" || asunto === ""|| mensaje === "" ) {
        alert("Por favor complete todos los campos");
        event.preventDefault();
      } 
      
      else { 
        alert("Formulario enviado correctamente");
      
    
    }
    });
  });