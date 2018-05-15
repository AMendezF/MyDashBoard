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

import numpy as np
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivy import FigureCanvas


class MyDashboardScreen(Screen):
    fullscreen = BooleanProperty(False)
    statusColor = ListProperty([0, .9, 0, 1])

    def __init__(self,):
        super(MyDashboardScreen, self).__init__()
        self.add_plot()
        

    def add_plot(self):
        plt.style.use('seaborn-colorblind')
        fig, ax = plt.subplots(facecolor='dimgray', constrained_layout=False)

        ax.set_xlim(auto=True)
        ax.set_ylim(auto=True)

        ax.set_title('Status', size='xx-large')
        ax.set_xlabel('Time (min)', labelpad=0, size='x-large')
        ax.set_ylabel('Quantity (Litres)', labelpad=0, size='x-large')
        
        ax.grid(c='lightgrey', ls='dashed', lw=1)
        ax.tick_params(labelcolor='k', labelsize='medium')
        ax.plot(np.cumsum(np.random.randn(1, 1000)), 'C1')
        ax.plot(np.cumsum(np.random.randn(1, 1000)), 'r')
        data = [0, 100, 220, 340, 560, 870, 940, 1000]
        ax.fill_between(data, min(data), data, facecolor='b', alpha=0.5)

        #fig.tight_layout()
        #fig.autofmt_xdate()
        
        masterPlot = FigureCanvas(figure=fig, size_hint_y=0.55)
        
        self.ids.content.add_widget(masterPlot, index=1)


    '''def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(MyDashboardScreen, self).add_widget(*args)'''


class MyDashboardApp(App):

    def build(self):
        self.title = 'MyDashboard'
        return MyDashboardScreen()


if __name__ == '__main__':
    MyDashboardApp().run()
