from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    def button_on_release(self):
        self.label.text = self.text_input.text


class MyApp(App):
    def build(self):
        return Container()


def main():
    MyApp().run()


if __name__ == "__main__":
    main()
