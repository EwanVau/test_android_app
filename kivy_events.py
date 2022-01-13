from datetime import date
from kivy.app import App
from kivy.uix.button import Button


class MainApplication(App):
    def build(self):
        button = Button(text='Weclome to my app!',
                        size_hint=(0.5, 0.5),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # calling button bind and link to on_press_button event
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        date_now = str(date.today())
        print(f'You pressed the button!\non the date {date_now}')

        # Prints message to standard streams/ stdout (command line)
if __name__ == '__main__':
    app = MainApplication()
    app.run()
