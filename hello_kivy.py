#! /usr/bin/env python3
"""hello_kivy.py - Simple kivy program."""

from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    """Displays hello message."""
    def build(self) -> Label:
        label = Label(text='Hello from Kivy',
                      size_hint=(0.5, 0.5),
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})

        return label


if __name__ == "__main__":
    app = MainApp()
    app.run()
