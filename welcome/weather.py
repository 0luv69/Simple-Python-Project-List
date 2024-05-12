import requests
import json
import pyttsx3


locations = input("Enter your location:\t")
results= requests.get(f"https://api.weatherapi.com/v1/current.json?key=ceab39a6c6054ab6a9b104838230104&q={locations}")
talk = pyttsx3.init()

if results.status_code == 200:
    alls =json.loads (results.text)
    situtation = (((alls["current"])["condition"])["text"])
    print(f"The situtation is {situtation}")
    Celsius  = (alls["current"])["feelslike_c"]
    print(f"The Celsius is {Celsius}") 
    talk.say(f"So, the weather situation in {locations} is, {situtation},, which has, {Celsius}  Celsius")
    talk.runAndWait()    
else:
    print("wrong place input")
    talk.say(f"Sorry I am getting Confused in The loaction name with {locations} ")
    talk.runAndWait()   
     
    
talk.stop()
