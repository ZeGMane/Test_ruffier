from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation

from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)
    def __init__(self, total=10, steptime=1, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.anim1 = Animation(pos_hint= {'top': 0.1}, duration = steptime/2)
        self.anim2 = Animation(pos_hint= {'top': 1.0}, duration = steptime/2)
        self.animation = self.anim1 + self.anim2
        self.anim2.bind(on_complete = self.next)
        self.btn = Button(text='Приседание', size_hint=(1, 0.1), pos_hint={'top':1.0})
        self.btn.background_color = get_color_from_hex('FF9640')
        self.add_widget(self.btn)

    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step, *args):
        self.value += 1
        if self.value >= self.total:
            self.animation.repeat = False
            self.finished = True