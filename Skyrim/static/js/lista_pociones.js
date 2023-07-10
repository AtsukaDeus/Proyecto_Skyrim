fetch("lista_pociones")
    .then(response => response.json())
    .then(data => {
        const pocionesContainer = document.getElementById('pociones-container');

        data.forEach(pocion => {
            const pocionElement = document.createElement('li');
            const nombreElement = document.createElement('p');
            const ingredientesElement = document.createElement('p');
            const editar = document.createElement('a');
            const eliminar = document.createElement('a');

            ingredientesElement.classList.add('ingredientes-item');
            pocionElement.classList.add('li-item-pociones');

            nombreElement.textContent = `${pocion.nombre}`;
            ingredientesElement.textContent = `Ingredientes: ${pocion.ingredientes}`;
            editar.textContent = 'Editar';
            eliminar.textContent = 'Eliminar';

            editar.href = `editar_pocion/${pocion.id}`;
            eliminar.href = `eliminar_pocion/${pocion.id}`;

            pocionElement.appendChild(nombreElement);
            pocionElement.appendChild(editar);
            pocionElement.appendChild(eliminar);
            pocionElement.appendChild(ingredientesElement);

            pocionesContainer.appendChild(pocionElement);
        });
    })
    .catch(error => console.error('Error:', error));



