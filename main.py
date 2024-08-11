from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationbar import MDNavigationItem

Window.size = (480, 853)


class MainScreen(MDScreen):
    def go_to_addition_screen(self):
        self.manager.current = "addition_screen"

    def go_to_report_screen(self):
        self.manager.current = "report_screen"


class AdditionScreen(MDScreen):
    def go_to_main_screen(self):
        self.manager.current = "main_screen"


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
