from kivy.app import App
from kivy.uix.button import Button

# Kivy languages allows separation of interface and application logic


class ButtonApp(App):
    def build(self):
        # Create button without any attributes or binding to events
        return Button()

    def on_press_button(self, instance):
        print('You pressed the button!')

# Kivy will automatically look for file with same name in lowercase, without the
# 'App' part of the class name


# In this case, class name = ButtonApp
# ====> Kivy looks for file named 'button.kv'
if __name__ == '__main__':
    APP = ButtonApp()
    APP.run()
