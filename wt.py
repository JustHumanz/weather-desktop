import requests, json, os, schedule, random
from os.path import expanduser

api_key = "d2db1f13aac2f0e04f14847b236dfdc5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
#city_name = input("Enter city name : ")
city_name = "Indonesia,Malang"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]


    # print following values
    # print(" Temperature (in celcius unit) = " +
    #                str(current_temperature) +
    #      "\n atmospheric pressure (in hPa unit) = " +
    #                str(current_pressure) +
    #      "\n humidity (in percentage) = " +
    #                str(current_humidiy) +
    #      "\n description = " +
    #                str(weather_description))

    def q():
        os.system('notify-send '+city_name+' ' +str(current_temperature)+'" celcius" -i ~/Pictures/Cuaca/Icon/thermometer.png')

    def a():
        if (weather_description == "few clouds"):
            #print("Sedikit awan")
            os.system('notify-send "Sedikit Awan" "tuturu" -i ~/Pictures/Cuaca/Icon/cloudy.png')

        elif(weather_description == "clear sky"):
            #print("Cerah")
            os.system('notify-send "Cerah" -i ~/Pictures/Cuaca/Icon/sun-3.png')

        elif(weather_description == "scattered clouds"):
            #print("Banyak Awan")
            os.system('notify-send "Banyak Awan" -i ~/Pictures/Cuaca/Icon/cloud-2.png')

        elif(weather_description == "broken clouds"):
            #print("Mendung")
            os.system('notify-send "Mendung" "Siapin Payung" -i ~/Pictures/Cuaca/Icon/cloud.png')

        elif(weather_description == "shower rain"):
            #print("Gerimis")
            os.system('notify-send "Gerimis" "Siapin Payung" -i ~/Pictures/Cuaca/Icon/rain-1.png')

        elif(weather_description == "rain"):
            #print("Hujan")
            os.system('notify-send "Hujan" "Masak indomi skuy" -i ~/Pictures/Cuaca/Icon/rain-8.png')

        elif(weather_description == "thunderstorm"):
            #print("Badai")
            os.system('notify-send "Badai" -i ~/Pictures/Cuaca/Icon/thunder.png')

        elif(weather_description == "show"):
            print("Salju") #gak mungkin banget lol
            os.system('notify-send "Salju" -i ~/Pictures/Cuaca/Icon/snow.png')

        elif(weather_description == "mist"):
            print("Kabut")

    a()
    def b():
        if (weather_description == "few clouds" or weather_description == "broken clouds" or weather_description == "shower rain" or weather_description == "rain" or weather_description == "shower rain" or weather_description == "thunderstorm" ):
            path = expanduser("~/Pictures/Cuaca/Hujan")
            files = os.listdir(path)
            index = random.randrange(0, len(files))
            img = files[index]
            print(path+"/"+str(img))
            #os.system('zsh')
            os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
            os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))

        elif (weather_description == "mist"):
            path = expanduser("~/Pictures/Cuaca/Kabut")
            files = os.listdir(path)
            index = random.randrange(0, len(files))
            img = files[index]
            print(path+"/"+str(img))
            #os.system('zsh')
            os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
            os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))

        else:
            path = expanduser("~/Pictures/Cuaca/Cerah")
            files = os.listdir(path)
            index = random.randrange(0, len(files))
            img = files[index]
            print(path+"/"+str(img))
            #os.system('zsh')
            os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
            os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))


    #b()
    def t():
        schedule.every(30).minutes.do(q)
        schedule.every(40).minutes.do(a)
        schedule.every(60).minutes.do(b)

        while True:
            schedule.run_pending()
    #t()

else:
    print(" City Not Found ")
