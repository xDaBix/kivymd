from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout as Gr
from kivy.core.window import Window

# Window.clearcolor = (1,1,1,1)

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
        layout=Gr(cols=1,spacing=40,padding=150,row_force_default=True,row_default_height=40)
        email=TextInput(hint_text="Enter your name",multiline=False)
        password=TextInput(hint_text="Enter your password",multiline=False,password=True)
        btn=Button(text="Login",size_hint=(.09,.1),pos_hint={"center_x":.5,"center_y":.5})
        layout.add_widget(email)
        layout.add_widget(password)
        layout.add_widget(btn)
        return layout 
    
BoxApp().run()


