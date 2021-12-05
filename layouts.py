#! /usr/bin/env python3
"""layouts.py - A program to explore BoxLayout in Kivy"""

import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class HBoxLayoutExample(App):
    def build(self) -> BoxLayout:
        layout = BoxLayout(padding=10)
        colors = ['red', 'green', 'blue', 'purple']

        for i in range(5):
            btn = Button(text=f"Button #{i + 1}",
                         background_color=random.choice(colors)
                         )
            layout.add_widget(btn)
        return layout


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
