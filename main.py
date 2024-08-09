from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (480, 853)


class MainScreen(Screen):
    def go_to_addition_screen(self):
        self.manager.current = "addition_screen"


class AdditionScreen(Screen):
    def go_to_main_screen(self):
        self.manager.current = "main_screen"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(AdditionScreen(name="addition_screen"))
        return sm


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
