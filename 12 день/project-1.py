import requests, json
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate" 
KEY = "trnsl.1.1.20190820T213023Z.7cb391ea0f4f1f98.025d65795179de3f0f0aaf55179e0eef247fc2fb"
api_key = "6d52ee3afd200918244fad8611d15a2b"

def translate_me(mytext):

    params = {
        "key": KEY,     
        "text": mytext,
        "lang": 'en-ru' 
        }
    response = requests.get(URL ,params=params)
    return response.json()

base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    json = translate_me(weather_description)
    c = current_temperature - 273.15
    print(" Температура = " +
                    str(c) + 
          "\n атмосферное давление (в единице гПа) = " +
                    str(current_pressure) +
          "\n влажность (в процентах) = " +
                    str(current_humidiy) +
          "\n описание = " +
                    str(''.join(json['text'])))
else:
    print(" City Not Found ")