from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.anchorlayout import MDAnchorLayout

class Datatable(MDApp):
    def build(self):
        return MDAnchorLayout(
            MDDataTable(
                size_hint=(0.7,0.6),
                check=True,
                use_pagination=True,
                column_data=[
                    ("no",dp(30)),
                     ("Price",dp(30)),
                     ("Name",dp(60))
                ],
                row_data=[
                    (str(i), f"${i*10}", f"Item {i}") for i in range(1, 100)
                ]
            )
        )
    
Datatable().run()