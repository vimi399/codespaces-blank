# slovarji (dictionary) - JSON

prazen = {}
print(type(prazen))

#"ključ" : "vrednost"
raznoliki = {"starost" : 30, 
             "ime" : "Luka",
             "seznam" : [1,2,3,4],
             "slovar" : {"firma": "Dacia", "moč": 120}   }
# dostop do slovarja
print(raznoliki["starost"])
print(sum(raznoliki["seznam"]))

#dostop do napačnih ključev
#print(raznoliki["krneki"])

# slovar.get("ključ", "ne najdem ključa") 
print(raznoliki.get("krneki", "ne najdem ključa"))


import requests #enkrat bomo uporabljali paket Request ne requests
baseurl = "https://api.open-meteo.com/v1/forecast"
params = {"latitude" : 46.0511,
          "longitude": 14.5051,
          "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
          "timezone" : "Europe/Berlin",
          "forecast_days": 1}

call = requests.get(baseurl, params= params)
print(call.url)
#?latitude=46.0511&longitude=14.5051&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m&timezone=Europe%2FBerlin&forecast_days=1"
toJson = call.json()
print(toJson["current"]["temperature_2m"])
print(toJson["current"]["relative_humidity_2m"])
print(toJson["current"]["wind_speed_10m"])
print(toJson["current"]["wind_direction_10m"])

print("vaja1")
#Izpiši temperature za naslednjih 7 dni.
baseUrl = "https://api.open-meteo.com/v1/forecast"
params = {"latitude" : 46.0511,
          "longitude": 14.5051,
          "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
          "timezone" : "Europe/Berlin",
          "forecast_days": 7,
          "daily" : "temperature_2m_max"}

call = requests.get(baseUrl, params= params)
toJson = call.json()
print(toJson["daily"]["temperature_2m_max"])


#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
print("vaja2")
baseUrl = "https://api.open-meteo.com/v1/forecast"
params = {"latitude" : 46.0511,
          "longitude": 14.5051,
          "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
          "timezone" : "Europe/Berlin",
          "forecast_days": 7,
          "daily" : "temperature_2m_max,temperature_2m_min"}
call = requests.get(baseUrl, params= params)
toJson = call.json()
print(toJson["daily"]["temperature_2m_min"],toJson["daily"]["temperature_2m_max"])
minTemp= toJson["daily"]["temperature_2m_min"]
maxTemp = toJson["daily"]["temperature_2m_max"]
print(max(maxTemp), min(minTemp))
#Ugotovi, kateri dan ima največjo razliko med dnevno in nočno temperaturo.
print("vaja3")
največjaRazlika = 0
baseUrl = "https://api.open-meteo.com/v1/forecast"
params = {"latitude" : 46.0511,
          "longitude": 14.5051,
          "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
          "timezone" : "Europe/Berlin",
          "forecast_days": 7,
          "daily" : "temperature_2m_max,temperature_2m_min"}
call = requests.get(baseUrl, params=params)
toJson = call.json()
minTemp = toJson["daily"]["temperature_2m_min"]
maxTemp = toJson["daily"]["temperature_2m_max"]
for i in range(len(minTemp)):
    trenutnaRazlika = maxTemp[i]-minTemp[i]
    if trenutnaRazlika > največjaRazlika:
        največjaRazlika = trenutnaRazlika
        dan = i 
print(f"{i}. dan je največja temperaturna razlika med dnevno in nočno temperaturo ki je {round(največjaRazlika,1)})")

#Med 10 največjimi slovenskimi mesti poišči tisto;
mesta = [
    ("Ljubljana", 46.0511, 14.5051),
    ("Maribor",   46.5558, 15.6459),
    ("Kranj",     46.2389, 14.3556),
    ("Celje",     46.2309, 15.2604),
    ("Koper",     45.5482, 13.7296),
    ("Velenje",   46.3572, 15.1128),
    ("Novo mesto", 45.8040, 15.1689),
    ("Ptuj",      46.4201, 15.8702),
    ("Kamnik",    46.2259, 14.6121),
    ("Jesenice",  46.4324, 14.0623),
]
#ki bo danes najtoplejše oz. najhladnejše,
#NE DELA ŠE
mini = 4000
maxi = -273
baseUrl = "https://api.open-meteo.com/v1/forecast"
for a in mesta:
    params = {"latitude" : a[1],
            "longitude": a[2],
            "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m",
            "timezone" : "Europe/Berlin",
            "forecast_days":1,
            "daily":"temperature_2m_max,temperature_2m_min"}
    call = requests.get(baseUrl, params=params)
    toJson = call.json()
    maxTemp = toJson["daily"]["temperature_2m_max"]
    minTemp = toJson["daily"]["temperature_2m_min"]
    if minTemp < mini:
        mini = minTemp
        mestoMin = a[0]
    if maxTemp > maxi:
        maxi = maxTemp
        mestoMax = a[0]
print(mestoMin,mini)
print(mestoMax,maxi)
#ki bo imelo najmanj oz. največ dežja,
#ki bo imelo najmanj oz. največ vetra.