from django.urls import path
from skyapp.views import index, servicios, contacto
from skyapp.views import respiracionAcuatica, restaurarSalud, resistenciaEscarcha, resistenciaFuego, resistenciaMagia, resistenciaVeneno
from skyapp.views import verPociones, crearPociones, editarPociones, eliminarPociones

urlpatterns = [
    path('', index, name='index'),
    path('servicios', servicios, name='servicios'),
    path('contacto', contacto, name='contacto'),
    
    # path de pociones
    path('respiracion_acuatica', respiracionAcuatica, name='respiracion_acuatica'),
    path('restaurar_salud', restaurarSalud, name='restaurar_salud'),
    path('resistencia_escarcha', resistenciaEscarcha, name='resistencia_escarcha'),
    path('resistencia_fuego', resistenciaFuego, name='resistencia_fuego'),
    path('resistencia_magia', resistenciaMagia, name='resistencia_magia'),
    path('resistencia_veneno', resistenciaVeneno, name='resistencia_veneno'),
    
    # path de crud
    path('ver_pociones', verPociones, name='ver_pociones'),
    path('crear_pocion', crearPociones, name='crear_pocion'),
    path('editar_pocion/<int:id>', editarPociones, name='editar_pocion'),
    path('eliminar_pocion/<int:id>', eliminarPociones, name='eliminar_pocion'),
]
