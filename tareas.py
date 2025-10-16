import kivy # indica la versión de Kivy
kivy.require("2.1.0") # versión mínima requerida
from kivy.app import App # Clase base para la aplicación
from kivy.uix.button import Label # Importa el widget Label (elementos de interfaz de usuario,como botones, etiquetas, etc)

class MyApp(App): # Define la clase principal de la aplicación
    def build(self): # Método que construye la interfaz de usuario
        return Label(text="Hola, Mundo!") # Retorna una etiqueta con el texto "Hola, Mundo!"

        


        


if __name__ == "__main__":
    MyApp().run()