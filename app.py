from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout as Gr
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout as A
from kivy.uix.floatlayout import FloatLayout as F
from kivy.uix.screenmanager import ScreenManager,Screen
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


# class BoxApp(App):
#     def build(self):
#         layout=Gr(cols=1,spacing=40,padding=150,row_force_default=True,row_default_height=40)
#         self.email=TextInput(hint_text="Enter your name",multiline=False)
#         self.password=TextInput(hint_text="Enter your password",multiline=False,password=True)
#         self.btn=Button(text="Login",on_press=self.submitbtn,size_hint=(.09,.1),pos_hint={"center_x":.5,"center_y":.5}, )
#         layout.add_widget(self.email)
#         layout.add_widget(self.password)
#         layout.add_widget(self.btn)
#         return layout 

#     def submitbtn(self,obj):
#         print(f"email={self.email.text}")
#         print(f"password={self.password.text}")
# BoxApp().run()



# class anchorlayoutApp(App):
#     def build(self):
#         layout=A(anchor_x="center",anchor_y="center")
#         btn=Button(text="click me ",size_hint=(None,None),width=200)
#         layout.add_widget(btn)
#         return layout
    
# anchorlayoutApp().run()


# class floatlayoutApp(App):
#     def build(self):
#         layout=F()
#         btn=Button(text="click me ",size_hint=(None,None),width=200,pos_hint={"center_x":.9,"center_y":.5})
#         layout.add_widget(btn)
#         return layout
    
# floatlayoutApp().run()


# class Mykvapp(App):
#     pass

# Mykvapp().run()

from kivy.lang import Builder

# Load KV file content
kv = """
ScreenManager:
    Home:
    First:

<Home>:
    name: "home"
    Label:
        text: "Home"
    Button:
        text: "home"
        size_hint: .2, .1
        on_release:
            app.root.current="first" 
            root.manager.transition.direction="left"

<First>:
    name: "first"
    Label:
        text: "First"
    Button:
        text:"first"
        size_hint: .2, .1
        on_release:
            app.root.current="home"
            root.manager.transition.direction="right"ṇ
"""

class Home(Screen):
    pass

class First(Screen):
    pass

class Manager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_string(kv)

MyApp().run()
