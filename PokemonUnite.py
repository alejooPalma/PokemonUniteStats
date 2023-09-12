from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window


class PokemonUniteApp(App):
    from kivy.core.window import Window
    Window.size = (800,600)


PokemonUniteApp().run()