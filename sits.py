# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label

class Sits(Label):
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = str(self.total) 
        super().__init__(text='[color=#A64B00]'+'Осталось приседаний: ' +my_text+'[/color]',markup = True, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        self.text = '[color=#A64B00]'+'Осталось приседаний: ' + str(remain) +  '[/color]'