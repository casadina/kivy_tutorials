#! /usr/bin/env python3
"""display_image.py - A program to display a simple image."""

from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self) -> Image:
        """Build the Kivy app."""
        img = Image(source='cookie.png',
                    size_hint=(1, 0.5),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return img


if __name__ == "__main__":
    app = MainApp()
    app.run()
