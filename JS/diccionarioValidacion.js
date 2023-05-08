  $(document).ready(function() {
    
    $('#principalForm').on('submit', function(event) {
      event.preventDefault(); // Evita que se envíe el formulario de forma automática
      var valor = $('input[name="buscar"]').val(); // Obtiene el valor del campo de texto
      if (valor !== undefined) {
        valor = valor.toLowerCase(); 
      }
      var coincidencia;

      $.get('../pocionesCuracion.txt', function(contenido) { // Lee el contenido del archivo de texto plano
          coincidencia = contenido.match(new RegExp(valor)); // Busca las coincidencias
          
          if (coincidencia !== null) {
            window.location.href = "../Paginas/RestaurarSalud.html";
            return;
          } 

      });

      $.get('../pocionesRespiracionAcuatica.txt', function(contenido) { 
        coincidencia = contenido.match(new RegExp(valor)); 
        
        if (coincidencia !== null) {
          window.location.href = "../Paginas/RespiracionAcuatica.html";
          return;
        } 

      });

      $.get('../pocionesResistenciaEscarcha.txt', function(contenido) { 
        coincidencia = contenido.match(new RegExp(valor)); 
        
        if (coincidencia !== null) {
          window.location.href = "../Paginas/ResistenciaEscarcha.html";
          return;
        } 

      });

      $.get('../pocionesResistenciaFuego.txt', function(contenido) {
        coincidencia = contenido.match(new RegExp(valor));

        if (coincidencia !== null){
          window.location.href = "../Paginas/ResistenciaFuego.html";
          return;
        }

      })

      $.get('../pocionesResistenciaMagia.txt', function(contenido) {
        coincidencia = contenido.match(new RegExp(valor));

        if (coincidencia !== null){
          window.location.href = "../Paginas/ResistenciaMagia.html";
          return
        }
        
      })

      $.get('../pocionesResistenciaVeneno.txt', function(contenido){
        coincidencia = contenido.match(new RegExp(valor));
        
        if (coincidencia !== null){
          window.location.href = "../Paginas/ResistenciaVeneno.html";
          return
        }
        
      })

      if(coincidencia === null){
        alert("No se han encontrado coincidencias, intente con otras palabras.");
      }


    });
  });
  