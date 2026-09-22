#naredi kviz z open trivia database
import requests
import pprint
import random

amount = int(input("How many questions should this quiz have: "))
urlTrivia = f"https://opentdb.com/api.php?amount={amount}&category=15&type=multiple"
kt = requests.get(urlTrivia).json()



def izpis(kt,i,correct):
    if correct == 1:
        print("A ",kt["results"][i]["correct_answer"])
        print("B ",kt["results"][i]["incorrect_answers"][0])
        print("C ",kt["results"][i]["incorrect_answers"][1])
        print("D ",kt["results"][i]["incorrect_answers"][2])
    elif correct == 2:
        print("A ",kt["results"][i]["incorrect_answers"][0])
        print("B ",kt["results"][i]["correct_answer"])
        print("C ",kt["results"][i]["incorrect_answers"][1])
        print("D ",kt["results"][i]["incorrect_answers"][2])
    elif correct == 3:
        print("A ",kt["results"][i]["incorrect_answers"][0])
        print("B ",kt["results"][i]["incorrect_answers"][1])
        print("C ",kt["results"][i]["correct_answer"])
        print("D ",kt["results"][i]["incorrect_answers"][2])
    else:
        print("A ",kt["results"][i]["incorrect_answers"][0])
        print("B ",kt["results"][i]["incorrect_answers"][1])
        print("C ",kt["results"][i]["incorrect_answers"][2])
        print("D ",kt["results"][i]["correct_answer"])
        


for i in range(amount):
    ran = random.randint(1,4)
    print(kt["results"][i]["question"])
    izpis(kt,i,ran)
    if ran == 1: cor = "A"
    if ran == 2: cor = "B"
    if ran == 3: cor = "C"
    if ran == 4: cor = "D"
    odgovor = input()
    if odgovor.upper() == cor:
        print("Correct :D")
    else:
        print("Wrong :(")

    
    