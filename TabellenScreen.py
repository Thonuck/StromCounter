from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import logging

logger = logging.getLogger()


class TabellenScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logger.info("IDS: {}".format(self.ids))
         
        table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.9),
            check = False,  # draw checkbox for each row
            column_data = [("Datum", dp(20)),
                           ("Uhrzeit", dp(18)),
                           ("Stand", dp(20))],
            row_data = [("15.12.2022", "21:56", "123456.7"),
                        ("13.12.2022", "20:16", "123400.7"),
                        ("10.12.2022", "05:16", "123304.7")]

        )
        table.bind(on_check_press=self.on_press_checkbox)
        table.bind(on_row_press=self.on_select_row)

        self.add_widget(table)
    def on_press_checkbox(self, instanace_table, current_row):
        logger.info("SELECT ROW: {} - {}".format(instance_table, current_row))

    def on_select_row(self, instance_table, instance_row):
        logger.info("SELECT ROW: {} - {}".format(instance_table, instance_row))


