from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from datetime import datetime


class MainApplication(App):
    def build(self):
        # Use AsyncImage to load image from the web
        img = AsyncImage(source=r'https://static.wixstatic.com/media/122326_b1ab16ddd85f4a2a958a58f7745dc0ce~mv2.png/v1/fill/w_448,h_974,al_c,lg_1,q_90/Discover%20-%20Discover%20(Student).webp',
                         size_hint=(0.5, 0.5),
                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return img


if __name__ == '__main__':
    app = MainApplication()
    app.run()
