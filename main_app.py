# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import ruffier
import instructions

class InstrScr(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       lay = BoxLayout(orientation='vertical')
       self.text = Label(text=instructions.txt_instruction, pos_hint={'center_x' : 0.5, 'center_y' : 0.5})
       set_name = Label(text='Введите имя:', pos_hint={'center_x' : 0.2, 'center_y' : 0.2}, size_hint=(0.2,0.1))
       self.name_name = TextInput(halign='left', focus=False, multiline=False, pos_hint={'center_x' : 0.5, 'center_y' : 0.3}, size_hint=(0.4,0.07))
       set_age = Label(text='Введите возраст', pos_hint={'center_x' : 0.2, 'center_y' : 0.1}, size_hint=(0.2,0.1))
       self.age = TextInput(text="18", halign='left', focus=False, multiline=False, pos_hint={'center_x' : 0.5, 'center_y' : 0.2}, size_hint=(0.4,0.07))

       self.button = Button(text='Начать', pos_hint={'center_x' : 0.5, 'center_y' : 0.08}, size_hint=(0.25,0.15))

       lay.add_widget(self.text)
       lay.add_widget(set_name)
       lay.add_widget(self.name_name)
       lay.add_widget(set_age)
       lay.add_widget(self.age)
       lay.add_widget(self.button)

       self.add_widget(lay)

       self.button.on_press = self.press

    def press(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'First'
        global name, age
        name = self.name_name.text
        age = int(self.age.text)


class FirstTest(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       lay = BoxLayout(orientation='vertical')
       self.text = Label(text=instructions.txt_test1, pos_hint={'center_x' : 0.5, 'center_y' : 0.5})
       self.result_text = Label(text='Введите результат', pos_hint={'center_x' : 0.2, 'center_y' : 0.3}, size_hint=(0.2,0.1))
       self.result1 = TextInput(text="0", halign='left', focus=False, multiline=False, pos_hint={'center_x' : 0.5, 'center_y' : 0.3}, size_hint=(0.4,0.07))

       self.button = Button(text='Продолжить', pos_hint={'center_x' : 0.5, 'center_y' : 0.08}, size_hint=(0.25,0.15))

       lay.add_widget(self.text)
       lay.add_widget(self.result_text)
       lay.add_widget(self.result1)
       lay.add_widget(self.button)
       
       self.add_widget(lay)

       self.button.on_press = self.press

    def press(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Second'
        global resulta1
        resulta1 = int(self.result1.text)
       
class SecondTest(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       lay = BoxLayout(orientation='vertical')
       self.text = Label(text=instructions.txt_sits, pos_hint={'center_x' : 0.5, 'center_y' : 0.5})
       
       self.button = Button(text='Продолжить', pos_hint={'center_x' : 0.5, 'center_y' : 0.08}, size_hint=(0.25,0.15))

       lay.add_widget(self.text)
       lay.add_widget(self.button)

       self.add_widget(lay)
       self.button.on_press = self.press

    def press(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Third'


class ThirdTest(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)

       lay = BoxLayout(orientation='vertical')
       self.text = Label(text=instructions.txt_test3, pos_hint={'center_x' : 0.5, 'center_y' : 0.5})
       set_result2 = Label(text='Результат:', pos_hint={'center_x' : 0.2, 'center_y' : 0.2}, size_hint=(0.2,0.1))
       self.result2 = TextInput(text="0", halign='left', focus=False, multiline=False, pos_hint={'center_x' : 0.5, 'center_y' : 0.3}, size_hint=(0.4,0.07))
       set_result3 = Label(text='Результат после отдыха:', pos_hint={'center_x' : 0.2, 'center_y' : 0.1}, size_hint=(0.2,0.1))
       self.result3 = TextInput(text="0", halign='left', focus=False, multiline=False, pos_hint={'center_x' : 0.5, 'center_y' : 0.2}, size_hint=(0.4,0.07))

       self.button = Button(text='Завершить', pos_hint={'center_x' : 0.5, 'center_y' : 0.08}, size_hint=(0.25,0.15))

       lay.add_widget(self.text)
       lay.add_widget(set_result2)
       lay.add_widget(self.result2)
       lay.add_widget(set_result3)
       lay.add_widget(self.result3)
       lay.add_widget(self.button)

       self.add_widget(lay)

       self.button.on_press = self.press

    def press(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Result'
        global resulta2, resulta3
        resulta2 = int(self.result2.text)
        resulta3 = int(self.result3.text)

class ResultScr(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.txt_index = Label(pos_hint={'center_x' : 0.5, 'center_y' : 0.5})
       self.txt_workheart = Label(pos_hint={'center_x' : 0.5, 'center_y' : 0.4})

       self.add_widget(self.txt_index)
       self.add_widget(self.txt_workheart)
       self.on_enter = self.before

    def before(self):
        global resulta1, resulta2, resulta3
        resultat = ruffier.ruffier_index(resulta1, resulta2, resulta3)
        self.txt_index.text = "Ваш индекс Руфье: " + str(resultat)
        self.txt_workheart.text = "Работоспособность сердца: " + ruffier.txt_res[ruffier.ruffier_result(ruffier.ruffier_index(resulta1, resulta2, resulta3), ruffier.neud_level(age))]

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