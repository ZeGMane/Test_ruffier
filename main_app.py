# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import ruffier
import instructions
import seconds
import sits
import runner
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

bg_color = get_color_from_hex('FFB273')
Window.clearcolor = bg_color
button_color = get_color_from_hex('FF9640')


def chech_int(ch):
    try:
        return int(ch)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       lay = BoxLayout(orientation='vertical', padding=15, spacing=15)
       self.text = Label(text='[color=#A64B00]'+instructions.txt_instruction+ '[/color]', halign = 'center', markup = True)

       set_name = Label(text='[color=#A64B00]'+'Введите имя:'+'[/color]', size_hint=(0.6,1), halign = 'right', markup = True)
       self.name_name = TextInput(halign='left', focus=False, multiline=False, size_hint=(0.4, 1), background_color=bg_color)

       input_line = BoxLayout(orientation='horizontal', size_hint=(1, None), height='40sp', spacing=10)
       input_line.add_widget(set_name)
       input_line.add_widget(self.name_name)

       set_age = Label(text='[color=#A64B00]'+'Введите возраст'+'[/color]', size_hint=(0.6,1), halign = 'right', markup = True)
       self.age_t = TextInput(text="18", halign='left', focus=False, multiline=False, size_hint=(0.4, 1),background_color=bg_color)
       
       input_line2 = BoxLayout(orientation='horizontal', size_hint=(1, None), height='40sp', spacing=10)
       input_line2.add_widget(set_age)
       input_line2.add_widget(self.age_t)

       self.button = Button(text='Начать', size_hint=(0.4,None), height='50sp', pos_hint={'center_x': 0.5})
       self.button.background_color = button_color

       lay.add_widget(self.text)
       lay.add_widget(input_line)
       lay.add_widget(input_line2)
       lay.add_widget(self.button)

       self.add_widget(lay)

       self.button.on_press = self.press

    def press(self):
        self.age = chech_int(self.age_t.text)
        if self.age == False and self.age < 7:
            self.age_t.text = 'Введено не коректное число'
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'First'
            global name, age
            name = self.name_name.text
            age = int(self.age)


class FirstTest(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       lay = BoxLayout(orientation='vertical', padding=15, spacing=15)
       self.timer = seconds.Seconds(5, markup = True)

       self.text = Label(text='[color=#A64B00]'+instructions.txt_test1+ '[/color]', halign = 'center', markup = True)

       input_line = BoxLayout(orientation='horizontal', size_hint=(1, None), height='40sp', spacing=10)
    
       self.result_text = Label(text='[color=#A64B00]'+'Введите результат'+ '[/color]', size_hint=(0.6,1), halign = 'right',markup = True)
       self.result1 = TextInput(text="0", halign='left', focus=False, multiline=False, size_hint=(0.4, 1), background_color=bg_color)
       self.result1.disabled = True
       input_line.add_widget(self.result_text)
       input_line.add_widget(self.result1) 
       self.button = Button(text='Старт', size_hint=(0.4,None), height='50sp', pos_hint={'center_x': 0.5})

      
       self.button.bind(on_press=self.start_timer)
       self.button.background_color = button_color

       lay.add_widget(self.text)
       lay.add_widget(self.timer)
       lay.add_widget(input_line)
       lay.add_widget(self.button)
       
       self.add_widget(lay)

    def start_timer(self, *args):
        self.button.disabled = True
        self.timer.bind(done = self.timer_finished)
        self.timer.start()
    
    def timer_finished(self, *args):
        self.button.disabled = False
        self.result1.disabled = False
        self.button.text = 'Продолжить'
        self.button.unbind(on_press=self.start_timer)
        self.button.bind(on_press=self.press)


    def press(self, *args):
        global resulta1
        resulta1 = chech_int(self.result1.text)
        if resulta1 == False:
            self.result1.text = 'Введено не коректное число'
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'Second'
        
             
class SecondTest(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.next_screen = False
       lay = BoxLayout(orientation='vertical', padding=15, spacing=15)
       self.text = Label(text='[color=#A64B00]'+instructions.txt_sits+ '[/color]', halign = 'center', markup = True)
       
       self.button = Button(text='Начать', size_hint=(0.4,None), height='50sp', pos_hint={'center_x': 0.5})
       self.sits = sits.Sits(30, color=(0.15, 0.21, 0.09, 1), font_size=24)
       self.run = runner.Runner(total=30, steptime=1.5)
       self.run.bind(finished = self.run_finished)

       lay.add_widget(self.text)
       lay.add_widget(self.button)
       lay.add_widget(self.sits)
       lay.add_widget(self.run)

       self.add_widget(lay)
       self.button.background_color = button_color
       self.button.on_press = self.press

    def press(self):
        if not self.next_screen:
            self.button.disabled = True
            self.run.start()
            self.run.bind(value = self.sits.next)
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'Third'
        

    def run_finished(self, instance, value):
        self.button.disabled = False
        self.button.text = 'Продолжить'
        self.next_screen = True

class ThirdTest(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)

       lay = BoxLayout(orientation='vertical', padding=15, spacing=15)
       self.text = Label(text='[color=#A64B00]'+instructions.txt_test3+ '[/color]', halign = 'center',markup = True)

       self.timer = seconds.Seconds(15)
       

       set_result2 = Label(text='[color=#A64B00]'+'Результат:'+ '[/color]', size_hint=(0.6,1), halign = 'right',markup = True)
       self.result2 = TextInput(text="0", halign='left', focus=False, multiline=False, size_hint=(0.4, 1), background_color=bg_color)
       self.result2.disabled = True

       input_line = BoxLayout(orientation='horizontal', size_hint=(1, None), height='40sp', spacing=10)
       input_line.add_widget(set_result2)
       input_line.add_widget(self.result2)

       set_result3 = Label(text='[color=#A64B00]'+'Результат после отдыха:'+ '[/color]',  size_hint=(0.6,1), halign = 'right',markup = True)
       self.result3 = TextInput(text="0", halign='left', focus=False, multiline=False, size_hint=(0.4, 1), background_color=bg_color)
       self.result3.disabled = True

       input_line2 = BoxLayout(orientation='horizontal', size_hint=(1, None), height='40sp', spacing=10)
       input_line2.add_widget(set_result3)
       input_line2.add_widget(self.result3)

       self.button = Button(text='Старт', size_hint=(0.4,None), height='50sp', pos_hint={'center_x': 0.5})
       self.button.background_color = button_color
       lay.add_widget(self.text)
       lay.add_widget(self.timer)
       lay.add_widget(input_line)
       lay.add_widget(input_line2)
       lay.add_widget(self.button)

       self.add_widget(lay)
       self.button.on_press = self.press_start
       

    def press(self):   
        global resulta2, resulta3
        resulta2 = chech_int(self.result2.text)
        resulta3 = chech_int(self.result3.text)
        if resulta2 == False:
            self.result2.text = 'Введено не коректное число'
        elif resulta3 == False:
            self.result3.text = 'Введено не коректное число'
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'Result'

    def press_start(self):
        self.button.disabled = True
        
        self.timer.bind(done = self.timer_finished1)
        self.timer.start()

    def timer_finished1(self, *args):
        if self.timer.done == True:
            self.timer.unbind(done = self.timer_finished1) 
            self.result2.disabled = False
            self.timer.bind(done = self.timer_finished2)
            self.timer.restart(30)

    
    def timer_finished2(self, *args):
        if self.timer.done == True:
            self.timer.unbind(done = self.timer_finished2) 
            self.timer.bind(done = self.timer_finished3)
            self.timer.restart(15)

    def timer_finished3(self, *args):
        if self.timer.done == True:
            self.timer.unbind(done = self.timer_finished3) 
            self.result3.disabled = False
            self.button.disabled = False
            self.button.text = 'Завершить'
            self.button.on_press = self.press


class ResultScr(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       lay = BoxLayout(orientation='vertical', padding=15, spacing=15)

       self.txt_index = Label(halign = 'center',markup = True)
       self.txt_workheart = Label(halign = 'center', markup = True)

       lay.add_widget(self.txt_index)
       lay.add_widget(self.txt_workheart)
       self.add_widget(lay)
       
       self.on_enter = self.before

    def before(self):
        global resulta1, resulta2, resulta3
        resultat = ruffier.ruffier_index(resulta1, resulta2, resulta3)
        self.txt_index.text = '[color=#A64B00]'+"Ваш индекс Руфье: " + str(resultat)+ '[/color]'
        self.txt_workheart.text = '[color=#A64B00]'+"Работоспособность сердца: " + ruffier.txt_res[ruffier.ruffier_result(ruffier.ruffier_index(resulta1, resulta2, resulta3), ruffier.neud_level(age))]+ '[/color]'

class Test (App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name ='Instruction'))
        sm.add_widget(FirstTest(name ='First'))
        sm.add_widget(SecondTest(name='Second'))
        sm.add_widget(ThirdTest(name='Third'))
        sm.add_widget(ResultScr(name='Result'))
        
        return sm

app = Test()
app.run()