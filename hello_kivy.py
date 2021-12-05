#! /usr/bin/env python3
"""hello_kivy.py - Simple kivy program."""

from kivy.app import App
from kivy.uix.button import Button


class NewButton(Button):
    def __repr__(self):
        return 'This button greets you.'


class MainApp(App):
    """Displays hello message."""
    def build(self) -> NewButton:
        button = NewButton(text='Hello from Kivy',
                           size_hint=(0.5, 0.5),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_press=self.on_press_button)
        return button

    @staticmethod
    def on_press_button(instance):
        print(instance)
        print('You pressed the button!')


if __name__ == "__main__":
    app = MainApp()
    app.run()
