from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_file("EingabeScreen.kv")

class EingabeScreen(MDScreen):
    datum = StringProperty("")
    uhrzeit = StringProperty("")
    stand = StringProperty("")
    
