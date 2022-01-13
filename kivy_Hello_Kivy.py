from kivy.app import App
from kivy.uix.label import Label
from datetime import date
# Hello, Kivy! programm


class MainApplication(App):
    # Kivy needs subclass 'App' and override 'build()'
    def build(self):
        '''Place all UI code or make calls to other functions that define UI code'''
        date_now = str(date.today())
        label = Label(text=f'Hello! Welcome to my application.\n Today\'s date is:{date_now}',
                      size_hint=(0.5, 0.5),  # width and height of control
                      pos_hint={'center_x': 0.5, 'center_y': 0.5},  # position (X,Y) of UI
                      valign="middle", halign="left")

        return label


if __name__ == '__main__':
    app = MainApplication()
    app.run()
