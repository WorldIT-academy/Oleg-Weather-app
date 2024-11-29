import customtkinter as ctk
from .h_scroll_frame import h_s

class Time_Frame(ctk.CTkFrame):
    def __init__(self, child_master, n_column):
        ctk.CTkFrame.__init__(
            self,
            master=child_master,
            width=100,
            height=200,
            border_width=2,
            border_color="white",
            fg_color="#91bdc7"
        )
        self.grid(row=0, column=n_column, padx = 10)

for i in range(10):
    tf = Time_Frame(h_s, i)