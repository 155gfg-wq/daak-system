from kivy.app import App
from kivy.uix.label import Label

class DaakApp(App):
    def build(self):
        return Label(text='DAAK System - Ready', font_size='24sp')

DaakApp().run()