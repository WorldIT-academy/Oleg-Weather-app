import customtkinter as ctk
from .scroll_frame import vertical_scroll

class City_Frame(ctk.CTkFrame):
    def __init__(self, child_master, city_name):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = 236,
            height = 100,
            border_width = 2,
            border_color = "#FFFFFF"
        )
        self.pack(anchor = "center", pady = 7)
        
        self.grid_propagate(False) #родитель игнорирует подстраивание под ребенка
        self.grid_columnconfigure(0, weight=1) # колонка 0 имеет размер 1
        self.grid_columnconfigure(1, weight=1) # колонка 1 имеет размер 1

        self.city_label = ctk.CTkLabel(
            master = self,
            text = city_name,
            font = ("Arial", 25)
        )
        self.city_label.grid(row = 0, column = 0, sticky = "w", padx=5, pady=5)


        self.temp_label = ctk.CTkLabel(
            master = self,
            text = "12°",
            font = ("Arial", 35)
        )
        self.temp_label.grid(row = 0, column = 1, sticky = "e", padx=10, pady=5)

        self.condition_label = ctk.CTkLabel(
            master = self,
            text = "Хмарно",
            font = ("Arial", 16)
        )
        self.condition_label.grid(row = 1, column = 0, sticky = "w", padx=10, pady=(10,0))

        self.min_max_label = ctk.CTkLabel(
            master = self,
            text = "мін. 11°, макс. 14°",
            font = ("Arial", 14)
        )
        self.min_max_label.grid(row = 1, column = 1, sticky = "e", padx=5, pady=(10,0))

cities = ["Kyiv", "Paris", "Warsaw", "Berlin", "Budapest"] 

for i in cities:
    #GET REQUEST
    cf = City_Frame(vertical_scroll, i)