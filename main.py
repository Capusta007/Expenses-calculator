from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.menu import MDDropdownMenu

Window.size = (480, 853)


class MainScreen(MDScreen):
    def go_to_addition_screen(self):
        self.manager.current = "addition_screen"

    def go_to_report_screen(self):
        self.manager.current = "report_screen"


class AdditionScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.menu_items = [
            {   
                "text": "Еда",
                "on_release": lambda x="Еда": self.menu_callback(x)},
            {
                "text": "Транспорт",
                "on_release": lambda x="Транспорт": self.menu_callback(x),
            },
            {   
                "text": "Работа", 
                "on_release": lambda x="Работа": self.menu_callback(x)},
            {
                "text": "Развлечения",
                "on_release": lambda x="Развлечения": self.menu_callback(x),
            },
        ]
        self.menu = MDDropdownMenu(caller=self.ids.dropdown_button, items=self.menu_items)

    def go_to_main_screen(self):
        self.manager.current = "main_screen"

    def menu_callback(self, text_item):
        self.ids.dropdown_button_text.text = text_item
        self.menu.dismiss()


class ReportScreen(MDScreen):
    def go_to_main_screen(self):
        self.manager.current = "main_screen"


class MyApp(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(AdditionScreen(name="addition_screen"))
        sm.add_widget(ReportScreen(name="report_screen"))
        return sm


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
