from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDRaisedButton


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