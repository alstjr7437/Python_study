from tkinter import *
import requests

api_key = '4344b0c5d63fb946ca403d0675a37478'

def search():
    city_name = cityE.get()
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?&q='+city_name+'&lang=kr&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()

    temp = str(round(int(weather_info["main"]["temp"]) - 273.15, 1)) + "도"
    humidity = str(weather_info["main"]["humidity"]) + "%"
    speed = str(weather_info["wind"]["speed"]) + "m/s"
    tempv.configure(text=str(temp))
    humV.configure(text=str(humidity))
    windV.configure(text=str(speed))

window = Tk()

img1 = PhotoImage(file="rain.png")
img2 = PhotoImage(file="z.png")
img3 = PhotoImage(file="snow.png")

tempL = Label(window, text="Tempearture")
tempv = Label(window, text="0")
humL = Label(window, text="Humidity")
humV = Label(window, text="0")
windL = Label(window, text="Wind Speed")
windV = Label(window, text="0.0")
cityL = Label(window, text="City")
cityE = Entry(window)
btnResult = Button(window, text="result", command=search)
btnexit = Button(window, text="exit")
img1L = Label(window, image=img1)
img2L = Label(window, image=img2)
img3L = Label(window, image=img3)

tempL.grid(row=0,column=0)
tempv.grid(row=0,column=1)
humL.grid(row=1,column=0)
humV.grid(row=1,column=1)
windL.grid(row=2,column=0)
windV.grid(row=2,column=1)
cityL.grid(row=3,column=0)
cityE.grid(row=3,column=1,columnspan=2)
btnResult.grid(row=4, column=0)
btnexit.grid(row=4, column=1)
img1L.grid(row=5,column=0)
img2L.grid(row=5,column=1)
img3L.grid(row=5,column=2)


window.mainloop()