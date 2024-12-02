import customtkinter as ctk
from .scroll_frame import vertical_scroll
import requests

class City_Frame(ctk.CTkFrame):
    def __init__(self, child_master, city_name, time, temp, condition, min_max):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            width = 236,
            height = 100,
            border_width = 2,
            border_color = "#FFFFFF",
            fg_color = "#91bdc7"
        )
        self.pack(anchor = "center", pady = 7)
        
        self.grid_propagate(False) #родитель игнорирует подстраивание под ребенка
        self.grid_columnconfigure(0, weight=1) # колонка 0 имеет размер 1
        self.grid_columnconfigure(1, weight=1) # колонка 1 имеет размер 1

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.city_label = ctk.CTkLabel(
            master = self,
            text = city_name,
            font = ("Comic Sans MS", 25)
        )
        self.city_label.grid(row = 0, column = 0, sticky = "w", padx=(10,0), pady=(10,0))

        self.time_label = ctk.CTkLabel(
            master = self,
            text = time,
            font = ("Arial", 14)
        )
        self.time_label.grid(row = 1, column = 0, sticky = "w", padx=(10,0), pady=(0,10))

        self.temp_label = ctk.CTkLabel(
            master = self,
            text = temp,
            font = ("Arial", 35)
        )
        self.temp_label.grid(row = 0, column = 1, sticky = "e", padx=(0,10), pady=(10,0))

        self.condition_label = ctk.CTkLabel(
            master = self,
            text = condition,
            font = ("Arial", 16)
        )
        self.condition_label.grid(row = 2, column = 0, sticky = "w", padx=(10,0), pady=(10,10))

        self.min_max_label = ctk.CTkLabel(
            master = self,
            text = min_max,
            font = ("Arial", 14)
        )
        self.min_max_label.grid(row = 2, column = 1, sticky = "e", padx=(0,10), pady=(10,10))

cities = ["Dnipro", "Kyiv", "Budapest", "Warsaw", "Vienna", "Prague", "Berlin", "Milan", "Paris", "London", "Athens", "Jerusalem"] 

for city_name in cities:

    # url = f"https://wttr.in/{city_name}?format=j1"
    # result = requests.get(url)

    # time = result.json()["current_condition"][0]["localObsDateTime"].split(" ")[1]
    # temp = result.json()["current_condition"][0]["temp_C"] + "°"
    # condition = result.json()["current_condition"][0]["weatherDesc"][0]["value"]
    # min_max = result.json()["weather"][0]["mintempC"] + " " + result.json()["weather"][0]["maxtempC"]
    
    time = "10:55"
    temp = "20°"
    condition = "sunny"
    min_max = "мин. 15, макс. 26"

    cf = City_Frame(vertical_scroll, city_name, time, temp, condition, min_max) 