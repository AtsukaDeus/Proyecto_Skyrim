$(document).ready(function() {
    $('#principalForm').submit(function(event) {
      // Prevenir que el formulario se envíe sin validar
      event.preventDefault();
  
      // Obtener los valores de los campos del formulario
      var x = $('#search').val().toLowerCase();
        
      // Validar el campo nombre de pociones
      if (x.length < 1) {
        alert('Por favor, ingrese una busqueda.');
        return;
      }
      
      // opciones de pociones de curacion
      else if (x === 'pocion de curacion' || x === 'curacion' || x === 'pocion de salud' || x === 'salud' || x === 'curarse'){

        window.location.href = "../Paginas/RestaurarSalud.html";
        return;
      }

      else if (x === 'pocion de escarcha' || x === 'resistencia a la escarcha' || x === 'escarcha' || x === 'frio' || x === 'resistencia al frio'){

        window.location.href = "../Paginas/ResistenciaEscarcha.html";
        return;
      }

      else if (x === 'pocion de respiracion acuatica' || x === 'respiracion acuatica' || x === 'respirar bajo el agua' || x === 'no ahogarse' || x === 'respirar'){

        window.location.href = "../Paginas/RespiracionAcuatica.html";
        return;
      }

      

      else {
        // El valor no cumple ninguna opción, muestra un mensaje de error
        alert('El valor ingresado no cumple ninguna opción válida.');
      }

    });
  });