import requests
#url = "https://api.agify.io?name=michael"
#klic = requests.get(url).json()
#print(klic["result"])
#iz seznama vaših družinskih imen
#imena = ["luka","ana","jaka"]
#izpišete najstarejše ime

imena = ["Franci","Mojca","Anže"]

#foreach
for i in imena:
    print(i)

#foreach z indeksi
#enumerate
#print(list(enumerate(imena)))
#for i,imena in enumerate(imena):
#    print(i,imena)
maxAge = 0
for i in imena:
    url = f"https://api.agify.io?name={i}"
    klic = requests.get(url).json()
    print(klic)
    starost = klic["age"]
    if maxAge < starost:
        maxAge = starost
        ime = i
print(maxAge,ime)

#
