$(document).ready(function() {
  
  $('#principalForm').on('submit', function(event) {
    event.preventDefault(); // Evita que se envíe el formulario de forma automática
    var valor = $('input[name="buscar"]').val(); // Obtiene el valor del campo de texto
    if (valor !== undefined) {
      valor = valor.toLowerCase(); 
    }

    if (valor === "") {
      alert("Por favor, ingrese un valor de búsqueda.");
      return;
    }

    var encontrado = false; // variable que indica si se ha encontrado alguna coincidencia

    $.get('../text/pocionesCuracion.txt', function(contenido) { // Lee el contenido de los archivos texto
        var coincidencia = contenido.match(new RegExp(valor)); // Busca las coincidencias
        if(coincidencia == valor){
            coincidencia = true;
        }
        
        if (coincidencia == true) {
          window.location.href = "../Paginas/RestaurarSalud.html";
          encontrado = true;
          return;
        } 

    });

    $.get('../text/pocionesRespiracionAcuatica.txt', function(contenido) { 
      var coincidencia = contenido.match(new RegExp(valor)); 
      
      if(coincidencia == valor){
        coincidencia = true;
      }

      if (coincidencia == true) {
        window.location.href = "../Paginas/RespiracionAcuatica.html";
        encontrado = true;
        return;
      } 

    });

    $.get('../text/pocionesResistenciaEscarcha.txt', function(contenido) { 
      var coincidencia = contenido.match(new RegExp(valor)); 

      if(coincidencia == valor){
        coincidencia = true;
      }

      if (coincidencia == true) {
        window.location.href = "../Paginas/ResistenciaEscarcha.html";
        encontrado = true;
        return;
      } 

    });

    $.get('../text/pocionesResistenciaFuego.txt', function(contenido) {
      var coincidencia = contenido.match(new RegExp(valor));
      
      if(coincidencia == valor){
        coincidencia = true;
      }  

      if (coincidencia == true){
        window.location.href = "../Paginas/ResistenciaFuego.html";
        encontrado = true;
        return;
      }

    });

    $.get('../text/pocionesResistenciaMagia.txt', function(contenido) {
      var coincidencia = contenido.match(new RegExp(valor));
      
      if(coincidencia == valor){
        coincidencia = true;
      } 

      if (coincidencia == true){
        window.location.href = "../Paginas/ResistenciaMagia.html";
        encontrado = true;
        return;
      }
      
    });

    $.get('../text/pocionesResistenciaVeneno.txt', function(contenido){
      var coincidencia = contenido.match(new RegExp(valor));
      

      if(coincidencia == valor){
        coincidencia = true;
      }
      

      if (coincidencia == true){
        window.location.href = "../Paginas/ResistenciaVeneno.html";
        encontrado = true;
        return;
      }

    });

    setTimeout(function() {
      if(!encontrado) {
        alert("No se han encontrado coincidencias, intente con otras palabras.");
      }
    }, 100); 

  });
});