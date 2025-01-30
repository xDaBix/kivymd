from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

# class Myapp(App):
#     def build(self):
        
#         return Label(text="hello world",font_size="72sp",italic=True,color=(1,0,0,1))

# Myapp().run()

# class ButttonApp(App):
#     def build(self):
#         btn=Button(text="click me",size_hint=(.09,.1),pos_hint={"center_x":.5,"center_y":.5},on_press=self.btnclick)
#         return btn
    
#     def btnclick(self,btn):
#         print("button is clicked")
    
# ButttonApp().run() 

# class Imageapp(App):
#     def build(self):
#         img=Image(source="mha-dabi-identity-reveal-todoroki.webp")
#         return img
    
# Imageapp().run()


class BoxApp(App):
    def build(self):
        box=BoxLayout(orientation="vertical",spacing=10,padding=10)
        
        btn1=Button(text="button1")
        btn2=Button(text="button2")
        btn3=Button(text="button3")
        
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        return box 
    
BoxApp().run()


