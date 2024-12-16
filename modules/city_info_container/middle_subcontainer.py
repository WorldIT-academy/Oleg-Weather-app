import customtkinter as ctk
from .info_container import info_cont

class Middle_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color = "green"
        )
        self.grid(row=0, column=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #! больше строк (6)

middle_subcont = Middle_Subcontainer(info_cont)