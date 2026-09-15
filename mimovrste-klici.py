
import requests #pip install requests
"""
# klic HTML strežnik
base_url = "https://www.mimovrste.com/"
call = requests.get(base_url)

print(call)
"""
# API klic
def getCurrTemp(lat, lon):
    url =f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"
    call = requests.get(url).json()

    print(call["current"]["temperature_2m"])
    return call["current"]["temperature_2m"]

getCurrTemp(46.21827172610609, 14.373366916081991)
#najdi natoplejše mesto
cities = [
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
maxTemp = -273.15
for a in cities:
    lat = a[1]
    lon = a[2]
    d = getCurrTemp(lat,lon)
    if d > maxTemp:
        maxTemp = d
        mesto = a[0]
print(mesto,maxTemp)