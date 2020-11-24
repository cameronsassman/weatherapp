import requests
from tkinter import *

root = Tk()
root.title("My temp app")
root.geometry("500x500")

def get_weather():
    api_address = "https://api.openweathermap.org/data/2.5/weather?appid=891de8808ec8bf8026096418890402b6&q="
    city = myentry.get()

    url = api_address + city

    data = requests.get(url).json()
    city = data['name']
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    my_city_lab.config(text=str(city))
    my_country_lab.config(text=str(country))
    my_temp_lab.config(text=str(temp))
    my_description_lab.config(text=str(description))
    my_humidity.config(text=str(humidity))
    my_wind_lab.config(text=str(wind))

myentry = Entry(root)
myentry.pack()
mybutton = Button(root, text="Check Weather", command=get_weather)
mybutton.pack()
my_city = Label(root, text="city")
my_city.pack()
my_city_lab = Label(root)
my_city_lab.pack()
my_country = Label(root, text="country")
my_country.pack()
my_country_lab = Label(root)
my_country_lab.pack()
mytemp_label = Label(root, text="Temperature")
mytemp_label.pack()
my_temp_lab = Label(root)
my_temp_lab.pack()
my_description = Label(root, text="description")
my_description.pack()
my_description_lab = Label(root)
my_description_lab.pack()
my_humidity = Label(root, text="Humidity")
my_humidity.pack()
my_Humidity_lab = Label(root)
my_Humidity_lab.pack()
my_wind = Label(root, text="wind")
my_wind.pack()
my_wind_lab = Label(root)
my_wind_lab.pack()





root.mainloop()
