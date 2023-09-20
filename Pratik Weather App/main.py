from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Pratik Weather Analysis App")
root.geometry("1000x700+500+500")
root.resizable(False, False)
print("Hello there I am Pratik Khose and ")
print("I made this weather GUI interface")

def getWeather():
    city=textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj = TimezoneFinder()
    reasult = obj.timezone_at(lng=location.longitude,lat=location.latitude)


    home=pytz.timezone(reasult)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M%p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #weather
    api= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=78fdf6aa12b15758664e116293a07417"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE", temp,"°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)



# search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("Comic Sans MS", 25, "bold"), bg="#404848", border=0.5, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", command=getWeather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

#time
name=Label(root,font=("Comic Sans MS",26,"bold"))
name.place(x=600, y=80)
clock=Label(root,font=("Comic Sans MS",20,"bold"), fg="#388E3C")
clock.place(x=600, y=150)


# label
label1 = Label(root, text="WIND", font=("Comic Sans MS", 15, "bold"))
label1.place(x=120, y=600)

label2 = Label(root, text="HUMIDITY", font=("Comic Sans MS", 15, "bold"))
label2.place(x=250, y=600)

label3 = Label(root, text="DESCRIPTION", font=("Comic Sans MS", 15, "bold"))
label3.place(x=430, y=600)

label4 = Label(root, text="PRESSURE", font=("Comic Sans MS", 15, "bold"))
label4.place(x=650, y=600)

t = Label(font=("arial", 70, "bold"), fg="#2EB4F3")
t.place(x=600, y=200)
c = Label(font=("arial", 20, 'bold'), fg="#BF360C")
c.place(x=600, y=300)

w = Label(text="...", font=("Comic Sans MS", 20, "bold"))
w.place(x=120, y=640)

h = Label(text="...", font=("Comic Sans MS", 20, "bold"))
h.place(x=280, y=640)

d = Label(text="...", font=("Comic Sans MS", 20, "bold"))
d.place(x=400, y=640)

p = Label(text="...", font=("Comic Sans MS", 20, "bold"))
p.place(x=670, y=640)

root.mainloop()