import customtkinter as ctk
from .scroll_frame import vertical_scroll
import requests

import datetime #библиотека для работы со временем (Timezone("Europe/Budapest") => "06.12.2024Z19:49:15")
import zoneinfo #конвертация текста в таймзону ("Europe/Budapest" => Timezone("Europe/Budapest"))
from timezonefinder import TimezoneFinder #конвертация координат в название зоны (51.254;26.678 => "Europe/Budapest")

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

cities = ["Dnipro", "Kyiv", "Budapest", "Warsaw", "Vienna", "Prague", "Berlin", "Milan", "Paris", "London", "NewYork"] 

for city_name in cities:

    url = f"https://wttr.in/{city_name}?format=j1"
    result = requests.get(url)

    # time = result.json()["current_condition"][0]["localObsDateTime"].split(" ")[1]
    # temp = result.json()["current_condition"][0]["temp_C"] + "°"
    # condition = result.json()["current_condition"][0]["weatherDesc"][0]["value"]
    # min_max = result.json()["weather"][0]["mintempC"] + " " + result.json()["weather"][0]["maxtempC"]
    
    my_lat = result.json()["nearest_area"][0]["latitude"]
    my_long = result.json()["nearest_area"][0]["longitude"]
    
    timezona_name = TimezoneFinder().timezone_at(lat = float(my_lat), lng = float(my_long))
    zona = zoneinfo.ZoneInfo(timezona_name)
    my_time = datetime.datetime.now(zona)

    time = my_time.strftime("%H:%M")
    temp = "20°"
    condition = "sunny"
    min_max = "мин. 15, макс. 26"

    cf = City_Frame(vertical_scroll, city_name, time, temp, condition, min_max) 