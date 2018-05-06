import kivy
kivy.require('1.10.0')

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'minimum_width', '1280')
Config.set('graphics', 'minimum_height', '720')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty, ListProperty

class MyDashboardScreen(Screen):
    fullscreen = BooleanProperty(False)
    statusColor = ListProperty([0, .9, 0, 1])

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(MyDashboardScreen, self).add_widget(*args)

class MyDashboardApp(App):

    def build(self):
        self.title = 'MyDashboard'
        return MyDashboardScreen()

if __name__ == '__main__':
    MyDashboardApp().run()
