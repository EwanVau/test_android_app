import kivy
import random

from kivy.app import App
from kivy.uix.button import Button

# Kivy offers different UI layout schemes:
# BoxLayout, FloatLayout and GridLayout and more

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# colour format: RGB + alpha/transparency
red = [1, 0, 0, 0.9]
green = [0, 1, 0, 0.2]
blue = [0, 0, 1, 0.8]
purple = [1, 0, 1, 0.3]


class HorizontalBoxScheme(App):
    def build(self):
        layout = BoxLayout(padding=[10, 200, 10, 200])
        colors = [red, green, blue, purple]
        # list comprehension adds 5 buttons to layout
        [layout.add_widget(Button(text=f'Button {(i+1)}',
                                  background_color=random.choice(colors)
                                  )) for i in range(5)]

        return layout


if __name__ == '__main__':
    app = HorizontalBoxScheme()
    app.run()
