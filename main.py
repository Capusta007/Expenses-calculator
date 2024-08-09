from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Ellipse, Line

Window.size = (480, 853)


class MainScreen(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return MainScreen()


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
