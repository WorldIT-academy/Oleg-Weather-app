import customtkinter as ctk
from .info_container import info_cont

class Left_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color = "green"
        )
        self.grid(row=0, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

left_subcont = Left_Subcontainer(info_cont)