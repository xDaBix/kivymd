from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem,MDList,TwoLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivy.lang.builder import Builder

style = """
MDScrollView:
    MDList:
        id:mylist
"""


class KivysList(MDApp):
    def build(self):
        bldr=Builder.load_string(style)
        return bldr
    
    def on_start(self):
        for i in range(1,11):
            self.root.ids.mylist.add_widget(OneLineListItem(text=f"Item {i}"))

        return 
KivysList().run()