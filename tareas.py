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

    def guardar(self):
        texto = self.entrada.text
        if texto != "":
            self.tareas.append(texto)
            self.mensaje.text = "Tarea guardada: " + texto
            self.entrada.text = ""
        else:
            self.mensaje.text = "Escribe algo primero."

    def ver(self):
        if len(self.tareas) > 0:

            texto = ""
        for tarea in self.tareas:
            texto += tarea + "\n"
            self.mensaje.text = texto
        else:
            self.mensaje.text = "No hay tareas."

    def cambiar(self):
        nuevo = self.entrada.text
        if nuevo != "":
            if len(self.tareas) > 0:
                self.tareas[0] = nuevo
                self.mensaje.text = "Primera tarea cambiada."
                self.entrada.text = ""
            else:
                self.mensaje.text = "No hay tareas para cambiar."
        else:
            self.mensaje.text = "Escribe la nueva tarea."

    def borrar(self):
        if len(self.tareas) > 0:
            self.tareas.pop(0)
            self.mensaje.text = "Primera tarea borrada."
        else:
            self.mensaje.text = "No hay tareas para borrar."

# Ejecutar la app
MiApp().run()