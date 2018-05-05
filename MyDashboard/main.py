from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty

class MyDashboardScreen(Screen):
    fullscreen = BooleanProperty(False)

    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(MyDashboardScreen, self).add_widget(*args)

class MyDashboardApp(App):

    def build(self):
        self.title = 'hello world'
        return MyDashboardScreen()

if __name__ == '__main__':
    MyDashboardApp().run()
