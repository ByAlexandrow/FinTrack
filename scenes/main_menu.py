from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen, NoTransition
from kivymd.uix.button import MDFillRoundFlatButton, MDFloatingActionButton
from kivymd.uix.label import MDLabel

from kivy.utils import get_color_from_hex


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.add_widget(MDLabel(
            text="FinTrack",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H2",
            halign="center",
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Статистика",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            text_color=get_color_from_hex("#FFFFFF"),
            md_bg_color=get_color_from_hex("#3030A6"),
            font_name="Comfortaa",
            font_size="18sp",
            on_release=self.statistic
        ))

        self.add_widget(MDFillRoundFlatButton(
            text="Доход",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            text_color=get_color_from_hex("#FFFFFF"),
            md_bg_color=get_color_from_hex("#3030A6"),
            font_name="Comfortaa",
            font_size="15sp",
            on_release=self.add_income
        ))
        
        self.add_widget(MDFillRoundFlatButton(
            text="Расходы",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            text_color=get_color_from_hex("#FFFFFF"),
            md_bg_color=get_color_from_hex("#3030A6"),
            font_name="Comfortaa",
            font_size="15sp",
            on_release=self.add_expense
        ))
        
        self.add_widget(MDFloatingActionButton(
            icon="static/imgs/white-exit-40.png",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            md_bg_color=get_color_from_hex("#3030A6"),
            on_release=self.quit
        ))

        self.add_widget(MDLabel(
            text="ByAlexandrow",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="Body1",
            halign="center",
        ))

    
    def statistic(self, instance):
        print("Статистика")


    def add_income(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'list_income_category'


    def add_expense(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'list_waste_category'


    def quit(self, instance):
        MDApp.get_running_app().stop()
