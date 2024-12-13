import customtkinter as ctk
from .scroll_frame import vertical_scroll
import requests
import json
import os
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

# cities = ["Dnipro", "Kyiv", "Budapest", "Warsaw", "Vienna", "Prague", "Berlin", "Milan", "Paris", "London", "NewYork"] 

# my_city_info = requests.get("https://ipinfo.io/json")
# my_city_name = my_city_info.json()["city"]

# if my_city_name not in cities: #не в (списке, словаре)
#     cities.append(my_city_name) 

my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "r") as file:
    weather_data = json.load(file) #dump - для вгрузки, load - для выгрузки

for city_weather in weather_data: #range(), "stewtwert", [1,2,3,4,5]

    # url = f"http://wttr.in/{city_name}?format=j1"
    # result = requests.get(url)
    
    temp = city_weather["current_condition"][0]["temp_C"] + "°"
    condition = city_weather["current_condition"][0]["weatherDesc"][0]["value"]
    min_max = city_weather["weather"][0]["mintempC"] + " " + city_weather["weather"][0]["maxtempC"]
    
    my_lat = city_weather["nearest_area"][0]["latitude"]
    my_long = city_weather["nearest_area"][0]["longitude"]
    
    timezona_name = TimezoneFinder().timezone_at(lat = float(my_lat), lng = float(my_long))
    zona = zoneinfo.ZoneInfo(timezona_name)
    my_time = datetime.datetime.now(zona)
    time = my_time.strftime("%H:%M")

    cf = City_Frame(vertical_scroll, "Город", time, temp, condition, min_max) 