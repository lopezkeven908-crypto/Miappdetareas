from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MiApp(App):
    def build(self):
       
        self.tareas = []

       
        self.caja = BoxLayout(orientation="vertical")

        
        self.caja.add_widget(Label(text="Mi lista de tareas"))

       
        self.entrada = TextInput()
        self.caja.add_widget(self.entrada)

        
        boton_guardar = Button(text="Guardar tarea")
        boton_guardar.on_press = self.guardar
        self.caja.add_widget(boton_guardar)

        
        boton_ver = Button(text="Ver tareas")
        boton_ver.on_press = self.ver


        self.caja.add_widget(boton_ver)

        
        boton_cambiar = Button(text="Cambiar primera tarea")
        boton_cambiar.on_press = self.cambiar
        self.caja.add_widget(boton_cambiar)

        
        boton_borrar = Button(text="Borrar primera tarea")
        boton_borrar.on_press = self.borrar
        self.caja.add_widget(boton_borrar)

       
        self.mensaje = Label(text="")
        self.caja.add_widget(self.mensaje)

        return self.caja


# Ejecutar la app
MiApp().run()