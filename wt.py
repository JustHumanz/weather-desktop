import requests, json, os, schedule, random, time
from os.path import expanduser

api_key = "d2db1f13aac2f0e04f14847b236dfdc5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Indonesia,Malang" #change with your contry and city

#use minutes
intervals_1 = 30
intervals_2 = 10
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
            os.system('notify-send '+city_name+' ' +str(current_temperature)+'" celcius" -i ~/Pictures/Cuaca/Icon/thermometer.png')

        b()
        def c():
            time.sleep(intervals_2 * 60)
            print("Stage 2")
            print(weather_description)
            if (weather_description == "few clouds"):
                os.system('notify-send "few clouds" "Go to outside broh" -i ~/Pictures/Cuaca/Icon/cloudy.png')

            elif(weather_description == "clear sky"):
                os.system('notify-send "clear sky" "Go to outside broh,are you a NEET?" -i ~/Pictures/Cuaca/Icon/sun-3.png')

            elif(weather_description == "scattered clouds"):
                os.system('notify-send "scattered clouds" -i ~/Pictures/Cuaca/Icon/cloud-2.png')

            elif(weather_description == "broken clouds"):
                os.system('notify-send "broken clouds" "Better you stay in your room" -i ~/Pictures/Cuaca/Icon/cloud.png')

            elif(weather_description == "shower rain" or "light rain"):
                os.system('notify-send "shower rain" "Stay in your room" -i ~/Pictures/Cuaca/Icon/rain-1.png')

            elif(weather_description == "rain"):
                os.system('notify-send "rain" "Remember indomi ayam bawang" -i ~/Pictures/Cuaca/Icon/rain-8.png')

            elif(weather_description == "thunderstorm"):
                os.system('notify-send "thunderstorm" "Zeus will find you" -i ~/Pictures/Cuaca/Icon/thunder.png')

            elif(weather_description == "snow"):
                print("Salju") #gak mungkin banget lol
                os.system('notify-send "Snow" "Be careful with finland ski troops" -i ~/Pictures/Cuaca/Icon/snow.png')

            elif(weather_description == "mist"):
                print("Kabut")
        c()

        def d():
            time.sleep(intervals_3 * 60)
            print("Stage 3")
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
main()
def t():
    schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending()
t()
