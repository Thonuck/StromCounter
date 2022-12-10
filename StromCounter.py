
from kivymd.app import MDApp
import logging
import datetime
import EingabeScreen

logger = logging.getLogger()

class StromCounterApp(MDApp):
    def callback(self):
        logger.info("The callback was called!!!")

    def get_date(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M")

    def enter_data(self):
        logger.info("Enter Data Called!")
        app = self.get_running_app()
        app.ids


StromCounterApp().run()
