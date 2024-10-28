import random

from kivy.uix.screenmanager import Screen, NoTransition
from kivymd.uix.button import MDFloatingActionButton, MDFillRoundFlatButton
from kivymd.uix.label import MDLabel

from kivy.utils import get_color_from_hex

from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.textfield import MDTextField


class ListIncomeCategory(Screen):
    def __init__(self, **kwargs):
        super(ListIncomeCategory, self).__init__(**kwargs)

        self.categories = []

        layout = FloatLayout()

        layout.add_widget(MDLabel(
            text="FinTrack",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H2",
            halign="center",
        ))

        layout.add_widget(MDLabel(
            text="Доходы",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H6",
            halign="center",
        ))

        layout.add_widget(MDFloatingActionButton(
            icon="static/imgs/white-add-40.png",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            md_bg_color=get_color_from_hex("#3030A6"),
            on_release=self.add_income_category
        ))

        self.category_list = MDList()
        scroll_view = ScrollView(size_hint=(1, 0.4), pos_hint={"center_x": 0.5, "center_y": 0.4})
        scroll_view.add_widget(self.category_list)
        layout.add_widget(scroll_view)

        layout.add_widget(MDFloatingActionButton(
            icon="static/imgs/arrow-back-40.png",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            md_bg_color=get_color_from_hex("#3030A6"),
            on_release=self.back
        ))

        layout.add_widget(MDLabel(
            text="ByAlexandrow",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="Body1",
            halign="center",
        ))

        self.add_widget(layout)

    
    def add_income_category(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'create_income_category'
    

    def add_category(self, category_name, category_color):
        self.categories.append((category_name, category_color))
        self.category_list.clear_widgets()
        for name, color in self.categories:
            item = OneLineAvatarListItem(text=name)
            item.text_color = color
            self.category_list.add_widget(item)
    

    def back(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'main_menu'


class CreateIncomeCategory(Screen):
    def __init__(self, **kwargs):
        super(CreateIncomeCategory, self).__init__(**kwargs)

        layout = FloatLayout()

        layout.add_widget(MDLabel(
            text="FinTrack",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H2",
            halign="center",
        ))

        layout.add_widget(MDLabel(
            text="Доходы",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="H6",
            halign="center",
        ))

        self.category_name_input = MDTextField(
            hint_text="Название категории",
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            size_hint=(0.8, None),
            height=20,
        )
        layout.add_widget(self.category_name_input)

        layout.add_widget(MDFillRoundFlatButton(
            text="Создать",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            text_color=get_color_from_hex("#FFFFFF"),
            md_bg_color=get_color_from_hex("#3030A6"),
            font_name="Comfortaa",
            font_size="15sp",
            on_release=self.create_category
        ))

        layout.add_widget(MDFloatingActionButton(
            icon="static/imgs/arrow-back-40.png",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            md_bg_color=get_color_from_hex("#3030A6"),
            on_release=self.back
        ))

        layout.add_widget(MDLabel(
            text="ByAlexandrow",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            text_color=get_color_from_hex("#3030A6"),
            theme_text_color="Custom",
            font_style="Body1",
            halign="center",
        ))

        self.add_widget(layout)
    

    def create_category(self, instance):
        category_name = self.category_name_input.text.capitalize()
        random_color = self.generate_random_color()
        list_income_category_screen = self.manager.get_screen('list_income_category')
        list_income_category_screen.add_category(category_name, random_color)
        self.manager.transition = NoTransition()
        self.manager.current = 'list_income_category'
        self.category_name_input.text = ""


    def generate_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return get_color_from_hex(f"#{r:02X}{g:02X}{b:02X}")


    def back(self, instance):
        self.manager.transition = NoTransition()
        self.manager.current = 'list_income_category'


class EditIncomeCategory(Screen):
    def __init__(self, **kwargs):
        super(EditIncomeCategory, self).__init__(**kwargs)


class DeleteIncomeCategory(Screen):
    def __init__(self, **kwargs):
        super(DeleteIncomeCategory, self).__init__(**kwargs)
