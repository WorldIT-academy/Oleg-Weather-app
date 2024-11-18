import customtkinter as ctk
from .scroll_frame import vertical_scroll

class City_Frame(ctk.CTkFrame):
    def __init__(self, child_master):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = 236,
            height = 100,
            border_width = 2,
            border_color = "#FFFFFF"
        )
        self.pack(anchor = "center", pady = 7)

for i in range(10):
    cf = City_Frame(vertical_scroll)