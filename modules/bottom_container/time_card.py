import customtkinter as ctk
from .h_scroll_frame import h_s
from PIL import Image
import random
import os

class Time_Frame(ctk.CTkFrame):
    def __init__(self, child_master, n_column, icon):
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
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.time_text = ctk.CTkLabel(
            master = self,
            text = "11:11",
            font = ("Arial", 22)
        )        
        self.time_text.grid(row = 0, column = 0)
        
        self.my_path = os.path.abspath(__file__)
        self.my_dir = os.path.dirname(self.my_path)
        self.my_icon = self.my_dir + "\\..\\..\\icons\\" + icon

        self.image = ctk.CTkImage(
            Image.open(self.my_icon),
            size = (75, 75)
        )

        self.image_text = ctk.CTkLabel(
            master = self,
            text = "",
            font = ("Arial", 15),
            image = self.image
        )        
        self.image_text.grid(row = 1, column = 0)
        
        self.temp_text = ctk.CTkLabel(
            master = self,
            text = "25*",
            font = ("Arial", 26)
        )        
        self.temp_text.grid(row = 2, column = 0)

icons_list = ["rain.png", "sun.png"]

for n_column in range(10):
    n_random = random.randint(0, 1)
    tf = Time_Frame(h_s, n_column, icons_list[n_random])