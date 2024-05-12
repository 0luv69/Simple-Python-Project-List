import requests
import os
import json
import time
import pyttsx3

def advance_mode():...

soucre_id=["the-kathmandu-post","abc-news-au","bbc-new","the-new-york-times","google-news"]


while True:
    print("Hey guys ur welcome over sano news\n")
    for index,each_id in enumerate(soucre_id):
        print(f"{index+1}) {each_id}")
    while True:    
        try:    
            selcect_soucre=int(input(f"select number from 1 to {len(soucre_id)}:\t") )
            if selcect_soucre != 0 and selcect_soucre < len(soucre_id)+1:
                break
        except:
            print("Plz choose only numer") 
    query_text = input("Type your Query here:\t\t")
    ranges=int(input("Enter how many lines you want to print:\t"))
    os.system('cls')
    api= "c6588ba603a4477bb1824853cd7c3af1"
    soucre_id=soucre_id[selcect_soucre-1]
    from_date="2024-02-11" 
    to_date= "2024-02-11"

    print(f"Sources from {soucre_id}, Query on {query_text}, from {from_date} to {to_date}\n")
    request= requests.get(f"https://newsapi.org/v2/everything?q={query_text}&id={soucre_id}&from={from_date}&to={to_date}&sortBy=popularitys&language=en&apiKey={api}")

    loades = json.loads(request.text)
    
    title = []
    for i in (loades["articles"]):
        title.append(i["title"])
    lengths = (len(title))
    
    if lengths < ranges:
        ranges = lengths
    
    speak = pyttsx3.init()

    for ij in range(ranges):
        print(f"{ij+1}) {title[ij]}")
        speak.say(title[ij])
        speak.runAndWait()
        print("-----------------------____________----------------------")
        time.sleep(1.2) 
    

    clear_view = int(input("Enter the number of News that you want to know in more clear way:  "))
    apo = ((loades["articles"])[clear_view])["description"]
    apo1 = ((loades["articles"])[clear_view])["content"]
    print(apo)
    print(apo1)
    
    speak.say(apo)
    speak.say(apo1)
    
    speak.runAndWait()
    speak.stop()
    break


input("Ht Enter key to exits")
