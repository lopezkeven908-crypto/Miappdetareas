import kivy # indica la versión de Kivy
kivy.require("2.1.0") # versión mínima requerida
from kivy.app import App # Clase base para la aplicación
from kivy.uix.button import Label # Importa el widget Label (elementos de interfaz de usuario,como botones, etiquetas, etc)
from kivy.uix.boxlayout import BoxLayout # Importa el widget BoxLayout (diseño de caja para organizar widgets)
from kivy.uix.button import Button # Importa el widget Button (botón interactivo)

class MyApp(App): # Define la clase principal de la aplicación
    def build(self): # Método que construye la interfaz de usuario
        return Label(text="Hola, Mundo!" , font_size=40) # Retorna una etiqueta con el texto "Hola, Mundo!"
    def build(self): # Método que construye la interfaz de usuario
        layout_botones = BoxLayout(orientation='horizontal') # Crea un diseño de caja vertical
        btn_agregar = Button(text="Agregar tarea") # Crea un botón con el texto "Agregar tarea"
        btn_eliminar = Button(text="Eliminar tarea") # Crea un botón con el texto "Eliminar tarea"
        btn_mostrar = Button(text="Mostrar tareas") # Crea un botón con el texto "Mostrar tareas"
        btn_modificar = Button(text="Modificar tarea") # Crea un botón con el texto "Modificar tarea"




        layout_botones.add_widget(btn_agregar) # Agrega el botón "Agregar tarea" 
        layout_botones.add_widget(btn_eliminar) # Agrega el botón "Eliminar tarea"
        layout_botones.add_widget(btn_mostrar) # Agrega el botón "Mostrar tareas" 
        layout_botones.add_widget(btn_modificar) # Agrega el botón "Modificar tarea"

        return layout_botones #caja con los botones
       

           
   
  



        


if __name__ == "__main__":
    MyApp().run()