#! /usr/bin/env python3
"""calculator.py - A Kivy version of calculator."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MainApp(App):
    """Set up calculator app."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x_size = Window.width
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=self.x_size // 10)
        self.last_button = None
        self.last_was_operator = None
        self.operators = ["/", "*", "+", "-"]

    def build(self) -> BoxLayout:
        """Build calculator app."""
        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        """Create actions for button press."""
        # TODO: Figure out how to make font_size change on window resize.
        self.solution.font_size = Window.width // 20
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be operator
                return
            elif current == "" and button_text == "0":
                # Python doesn't want leading 0's
                return
            elif self.last_was_operator and button_text == "0":
                # Python doesn't want leading 0's
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        """Display solution."""
        _ = instance.text
        text = self.solution.text
        if text:
            # Simple calculator, so just display through hundredths.
            # Solve for float problem.
            solution = f'{float(eval(self.solution.text)):.2f}'
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
