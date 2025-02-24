from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivy.lang import Builder

style = """

MDBoxLayout:
    orientation:"vertical"
    padding:90
    spacing:10
    MDTextField:
        hint_text:"Enter your email"
        pos_hint:{"center_x":.5,"center_y":.5}
        helper_text:"Required"
        helper_text_mode:"on_focus"
        icon_left:"email"
        size_hint_x:None
        width:300

    MDTextField:
        hint_text:"Enter your password"
        pos_hint:{"center_x":.5,"center_y":.5}
        helper_text:"Required"
        helper_text_mode:"on_focus"
        icon_left:"lock-off"
        size_hint_x:None
        width:300

    MDRaisedButton:
        text:"Login"
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint_x:None
        width:300
        on_press:app.submitbtn()

"""


# class HelloApp(MDApp):
#     def build(self):
#         return MDLabel(text="Hello world",halign="center",theme_text_color="Primary",font_style="Caption",text_color=(1,1,1,1))
    
# HelloApp().run()


# class HelloApp(MDApp):
#     def build(self):
#         return MDIcon(icon="clock")
    
# HelloApp().run()



# class HelloApp(MDApp):
#     def build(self):
#         return MDRaisedButton(text="click me",pos_hint={"center_x":.5,"center_y":.5})
    
# HelloApp().run()


class HelloApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        return MDRaisedButton(text="click me",pos_hint={"center_x":.5,"center_y":.5})
    
HelloApp().run()


# class HelloApp(MDApp):
#     def build(self):
#         scrn=Screen()
#         bldr=Builder.load_string(style)
#         scrn.add_widget(bldr)
#         return scrn
# HelloApp().run()

        
        