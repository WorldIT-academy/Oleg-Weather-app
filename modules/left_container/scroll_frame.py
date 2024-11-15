import customtkinter
from ..mainframe import screen

vertical_scroll = customtkinter.CTkScrollableFrame( #класс для скролл-рамки
    master=screen, #родительский элемент
    width=275, #ширина
    height=800, #высота
    border_color="#FFFFFF", #цвет рамки
    border_width=3, #ширина рамки
    corner_radius=20 #закругление углов
)   
vertical_scroll.pack(anchor="w") #разместили в родителе, прижав к ЗАПАДУ "w"