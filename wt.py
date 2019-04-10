import requests, json, os, schedule, random, time
from os.path import expanduser

api_key = "d2db1f13aac2f0e04f14847b236dfdc5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Indonesia,Malang"

#def grap(list):
#    url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
#    print("Update")
#    print(url)
#    return url


def main():
    url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
    response = requests.get(url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print("Loop")

        def b():
            time.sleep(1800)
            os.system('notify-send '+city_name+' ' +str(current_temperature)+'" celcius" -i ~/Pictures/Cuaca/Icon/thermometer.png')

        b()
        def c():
            time.sleep(1200)
            if (weather_description == "few clouds"):
                os.system('notify-send "Sedikit Awan" "tuturu" -i ~/Pictures/Cuaca/Icon/cloudy.png')

            elif(weather_description == "clear sky"):
                os.system('notify-send "Cerah" -i ~/Pictures/Cuaca/Icon/sun-3.png')

            elif(weather_description == "scattered clouds"):
                os.system('notify-send "Banyak Awan" -i ~/Pictures/Cuaca/Icon/cloud-2.png')

            elif(weather_description == "broken clouds"):
                os.system('notify-send "Mendung" "Siapin Payung" -i ~/Pictures/Cuaca/Icon/cloud.png')

            elif(weather_description == "shower rain" or "light rain"):
                os.system('notify-send "Gerimis" "Angkat Jemuran" -i ~/Pictures/Cuaca/Icon/rain-1.png')

            elif(weather_description == "rain"):
                os.system('notify-send "Hujan" "Masak indomi skuy" -i ~/Pictures/Cuaca/Icon/rain-8.png')

            elif(weather_description == "thunderstorm"):
                os.system('notify-send "Badai" "Awas petir bray" -i ~/Pictures/Cuaca/Icon/thunder.png')

            elif(weather_description == "show"):
                print("Salju") #gak mungkin banget lol
                os.system('notify-send "Salju" -i ~/Pictures/Cuaca/Icon/snow.png')

            elif(weather_description == "mist"):
                print("Kabut")
        c()

        def d():
            time.sleep(600)
            if (weather_description == "few clouds" or weather_description == "broken clouds" or weather_description == "shower rain" or weather_description == "rain" or weather_description == "shower rain" or weather_description == "thunderstorm" ):
                path = expanduser("~/Pictures/Cuaca/Hujan")
                files = os.listdir(path)
                index = random.randrange(0, len(files))
                img = files[index]
                print(path+"/"+str(img))
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))

            elif (weather_description == "mist"):
                path = expanduser("~/Pictures/Cuaca/Kabut")
                files = os.listdir(path)
                index = random.randrange(0, len(files))
                img = files[index]
                print(path+"/"+str(img))
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))

            else:
                path = expanduser("~/Pictures/Cuaca/Cerah")
                files = os.listdir(path)
                index = random.randrange(0, len(files))
                img = files[index]
                print(path+"/"+str(img))
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
        d()
    else:
        print(" City Not Found ")
#main()
def t():
    schedule.every(10).minutes.do(main)
    #schedule.every(1).minutes.do(c)
    #schedule.every(1).minutes.do(d)

    while True:
        schedule.run_pending()
t()
