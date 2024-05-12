import pyttsx3
lists = []
num = int(input("\nEnter the number of people:\t"))
for i in range(num):
    name = input("\n\nEnter the name of the person:\t")
    lists.append(name)

Engine = pyttsx3.init()
for j in lists: 
    Engine.say(f"soutout to our {j}")
    Engine.runAndWait()
Engine.stop()
