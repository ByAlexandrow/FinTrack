from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from scenes.main_menu import MainMenu
from scenes.income import ListIncomeCategory, CreateIncomeCategory, EditIncomeCategory, DeleteIncomeCategory
from scenes.waste import ListWasteCategory, CreateWasteCategory, EditWasteCategory, DeleteWasteCategory


class FinTrackApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"

        LabelBase.register(name="Comfortaa", fn_regular="static/fonts/Comfortaa.ttf")

        self.sm = ScreenManager()
        self.sm.add_widget(MainMenu(name='main_menu'))
        self.sm.add_widget(ListIncomeCategory(name='list_income_category'))
        self.sm.add_widget(CreateIncomeCategory(name='create_income_category'))
        self.sm.add_widget(EditIncomeCategory(name='edit_income_category'))
        self.sm.add_widget(DeleteIncomeCategory(name='delete_income_category'))
        self.sm.add_widget(ListWasteCategory(name='list_waste_category'))
        self.sm.add_widget(CreateWasteCategory(name='create_waste_category'))
        self.sm.add_widget(EditWasteCategory(name='edit_waste_category'))
        self.sm.add_widget(DeleteWasteCategory(name='delete_waste_category'))
        return self.sm


if __name__ == '__main__':
    FinTrackApp().run()