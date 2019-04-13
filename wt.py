import requests, json, os, schedule, random, time
from os.path import expanduser

api_key = "d2db1f13aac2f0e04f14847b236dfdc5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Indonesia,Malang" #change with your contry and city

#use minutes
intervals_1 = 30
intervals_2 = 1
intervals_3 = 1


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
        print("Main")

        def b():
            time.sleep(intervals_1 * 60)
            print("Stage 1")
            os.system('notify-send '+city_name+' ' +str(current_temperature)+'" celcius" -i ~/Pictures/Weather/Icon/thermometer.png')

        b()
        def c():
            time.sleep(intervals_2 * 60)
            print("Stage 2")
            print(weather_description)
            if (weather_description == "few clouds"):
                os.system('notify-send "Few clouds" "Go to outside broh" -i ~/Pictures/Weather/Icon/cloudy.png')

            elif(weather_description == "clear sky"):
                os.system('notify-send "Clear sky" "Go to outside broh,are you a NEET?" -i ~/Pictures/Weather/Icon/sun-3.png')

            elif(weather_description == "scattered clouds"):
                os.system('notify-send "Scattered clouds" -i ~/Pictures/Weather/Icon/cloud-2.png')

            elif(weather_description == "broken clouds"):
                os.system('notify-send "Broken clouds" "Better you stay in your room" -i ~/Pictures/Weather/Icon/cloud.png')

            elif(weather_description == "shower rain" or "light rain"):
                os.system('notify-send "Shower rain" "Stay in your room" -i ~/Pictures/Weather/Icon/rain-1.png')

            elif(weather_description == "rain"):
                os.system('notify-send "Rain" "Remember indomi ayam bawang" -i ~/Pictures/Weather/Icon/rain-8.png')

            elif(weather_description == "thunderstorm"):
                os.system('notify-send "Thunderstorm" "Zeus will find you" -i ~/Pictures/Weather/Icon/thunder.png')

            elif(weather_description == "snow"):
                print("Salju") #gak mungkin banget lol
                os.system('notify-send "Snow" "Be careful with finland ski troops" -i ~/Pictures/Weather/Icon/snow.png')

            elif(weather_description == "mist"):
                print("Kabut")
        c()

        def d():
            time.sleep(intervals_3 * 60)
            print("Stage 3")
            if (weather_description == "overcast clouds" or weather_description == "few clouds" or weather_description == "broken clouds" or weather_description == "shower rain" or weather_description == "rain" or weather_description == "shower rain" or weather_description == "thunderstorm" ):
                path = expanduser("~/Pictures/Weather/Rain")
                files = os.listdir(path)
                index = random.randrange(0, len(files))
                img = files[index]
                print(path+"/"+str(img))
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))

            elif (weather_description == "snow"):
                path = expanduser("~/Pictures/Weather/snow")
                files = os.listdir(path)
                index = random.randrange(0, len(files))
                img = files[index]
                print(path+"/"+str(img))
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))

            else:
                path = expanduser("~/Pictures/Weather/Sunny")
                files = os.listdir(path)
                index = random.randrange(0, len(files))
                img = files[index]
                print(path+"/"+str(img))
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-options zoom')
                os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'+(path+"/"+str(img)))
        d()
    else:
        print(" City Not Found ")
main()
def t():
    schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending() #make interval 1 min
t()
