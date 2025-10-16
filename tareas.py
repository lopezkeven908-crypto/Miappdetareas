from kivy.app import App # clase App de Kivy 
from kivy.uix.boxlayout import BoxLayout # contenedor 
from kivy.uix.label import Label # parda mostrar texto
from kivy.uix.textinput import TextInput # entrada del texto 
from kivy.uix.button import Button # botones

class MiApp(App): # clase de la app
    def build(self): # metodo build
        # lista para almacenar las tareas 
       
        self.tareas = [] # lista

       
        self.caja = BoxLayout(orientation="vertical") # contenedor vertical de los label y botones

        
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

    def guardar(self):
        texto = self.entrada.text
        if texto != "":
            self.tareas.append(texto)
            self.mensaje.text = "Tarea guardada: " + texto
            self.entrada.text = ""
        else:
            self.mensaje.text = "Escribe algo primero."

    


# Ejecutar la app
MiApp().run()