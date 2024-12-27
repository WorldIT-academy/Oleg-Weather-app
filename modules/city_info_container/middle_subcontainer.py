import customtkinter as ctk
from .info_container import info_cont

class Middle_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master, city_name = "Dnipro", temp = "11°С", condition = "Clear", min_max = '↓4°С  ↑11°С'):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color = "#91bdc7",
            border_width=1,
            border_color = "green"
        )
        self.grid(row=0, column=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.city_name = city_name
        self.temp = temp
        self.condition = condition
        self.min_max = min_max
        
        self.current_position = ctk.CTkLabel(
            master = self,
            text = "Поточна позиція",
            font = ("Arial", 35, "bold"),
            text_color = "white"
        )        
        self.current_position.grid(row = 0, column = 0)
        
        self.city = ctk.CTkLabel(
            master = self,
            text = self.city_name,
            font = ("Arial", 22),
            text_color = "white"
        )        
        self.city.grid(row = 1, column = 0)
        
        self.temp_text = ctk.CTkLabel(
            master = self,
            text = self.temp,
            font = ("Arial", 80),
            text_color = "white"
        )        
        self.temp_text.grid(row = 2, column = 0)
        
        self.condition_text = ctk.CTkLabel(
            master = self,
            text = self.condition,
            font = ("Arial", 30),
            text_color = "white"
        )        
        self.condition_text.grid(row = 3, column = 0)

        self.min_max_text = ctk.CTkLabel(
            master = self,
            text = self.min_max,
            font = ("Arial", 30),
            text_color = "white"
        )        
        self.min_max_text.grid(row = 4, column = 0)
                


middle_subcont = Middle_Subcontainer(info_cont)