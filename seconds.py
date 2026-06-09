# напиши модуль для реализации секундомера
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Seconds(Label):
    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        my_text = 'Прошло секунд '  + str(self.current)
        super().__init__(text='[color=#A64B00]'+my_text+ '[/color]', markup=True)

    def restart(self, total, **kwargs):
        self.total  =total
        self.done =False
        self.current = 0
        Clock.schedule_interval(self.change, 1)

    def start(self):
        self.done = False
        Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current += 1
        self.text = '[color=#A64B00]'+'Прошло секунд ' + str(self.current)+ '[/color]'
        if self.current >= self.total:
            self.done = True
            return False