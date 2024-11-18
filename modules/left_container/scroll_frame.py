import customtkinter as ctk
from ..mainframe import screen

class Vertical_Scroll(ctk.CTkScrollableFrame):
    def __init__(self, child_master, width, height, border_color, border_width, corner_radius, side):
        ctk.CTkScrollableFrame.__init__(
            self,
            master=child_master,
            width=width,
            height=height, 
            border_color=border_color,
            border_width=border_width,
            corner_radius=corner_radius
        )
        self.pack(anchor=side)

vertical_scroll = Vertical_Scroll( screen, 275, 800, "#FFFFFF", 3, 20, "w" )