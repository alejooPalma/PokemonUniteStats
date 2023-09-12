from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from StatsPoke import *
from StatsObjetos import *
from Preguntas import *

Builder.load_file("clasesPokemon.kv")


class Pokemon(GridLayout):
    nivelObjetoValor = StringProperty("1")
    nivelObjetoStackValor = StringProperty("1")
    nivelPokemonValor= StringProperty("1")
    pokemon = 0
    objeto = 0
    nivelPokemonValorInt= 0
    nivelObjetoStackValorInt = 0
    nivelObjetoValorInt= 0
    results = StringProperty("")

    def aegislash(self, widget):
        if widget.state == "down":
            self.pokemon = 1
        return self.pokemon


    def azumarill(self, widget):
        if widget.state == "down":
            self.pokemon = 2

        return self.pokemon

    def nivelPokemon(self,widget):
        self.nivelPokemonValor = str(int(widget.value))
        self.nivelPokemonValorInt = int(self.nivelPokemonValor)
        print(self.nivelPokemonValorInt)
        return self.nivelPokemonValorInt


    def aeosCookie(self, widget):
        if widget.state == "down":
            self.objeto = 1
        return self.objeto

    def assaultVest(self, widget):
        if widget.state == "down":
            self.objeto = 2
        return self.objeto


    def attackWeight(self, widget):
        if widget.state == "down":
            self.objeto = 3
        return self.objeto

    def nivelObjeto(self, widget):
        self.nivelObjetoValor = str(int(widget.value))
        self.nivelObjetoValorInt = int(self.nivelObjetoValor)
        print(self.nivelObjetoValorInt)
        return self.nivelObjetoValorInt


    def nivelObjetoStack(self,widget):
        self.nivelObjetoStackValor = str(int(widget.value))
        self.nivelObjetoStackValorInt = int(self.nivelObjetoStackValor)
        print(self.nivelObjetoStackValorInt)
        return int(self.nivelObjetoStackValor)


    def on_button_click(self):
        results = preguntas.preguntaPoke(self.pokemon, (self.nivelPokemonValorInt-1), self.objeto,
                               self.nivelObjetoValorInt, self.nivelObjetoStackValorInt)















