
from kivymd.app import MDApp
import logging
import datetime
import EingabeScreen
import TabellenScreen
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import MDNavigationLayout

logger = logging.getLogger()

class ApplicationLayout(MDNavigationLayout):
    pass

class StromCounterApp(MDApp):
    
    def build(self):
        self.app_layout = ApplicationLayout()
        return self.app_layout

    def callback(self):
        logger.info("The callback was called!!!")

    def get_date(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M")

    def enter_data(self):
        logger.info("Enter Data Called!")
        print(dir(self.app_layout.nested_sm))
        print("Screen Names: {}".format(self.app_layout.nested_sm.screen_names))
        self.app_layout.nested_sm.current = "Anschauen"


StromCounterApp().run()
