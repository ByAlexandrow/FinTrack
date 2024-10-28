from kivy.uix.screenmanager import Screen, NoTransition
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.label import MDLabel

from kivy.utils import get_color_from_hex


class ListWasteCategory(Screen):
    def __init__(self, **kwargs):
        super(ListWasteCategory, self).__init__(**kwargs)

        self.add_widget(MDLabel(
            text="FinTrack",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H2",
            halign="center",
        ))

        self.add_widget(MDLabel(
            text="Расходы",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H6",
            halign="center",
        ))

        self.add_widget(MDFloatingActionButton(
            icon="static/imgs/white-add-40.png",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            md_bg_color=get_color_from_hex("#3030A6"),
            on_release=self.add_waste_category
        ))

        self.add_widget(MDFloatingActionButton(
            icon="static/imgs/arrow-back-40.png",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            md_bg_color=get_color_from_hex("#3030A6"),
            on_release=self.back
        ))

        self.add_widget(MDLabel(
            text="ByAlexandrow",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="Body1",
            halign="center",
        ))

    
    def add_waste_category(self, instance):
        print("Добавить категорию расходов")
    

    def back(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'main_menu'


class CreateWasteCategory(Screen):
    def __init__(self, **kwargs):
        super(CreateWasteCategory, self).__init__(**kwargs)


class EditWasteCategory(Screen):
    def __init__(self, **kwargs):
        super(EditWasteCategory, self).__init__(**kwargs)


class DeleteWasteCategory(Screen):
    def __init__(self, **kwargs):
        super(DeleteWasteCategory, self).__init__(**kwargs)
