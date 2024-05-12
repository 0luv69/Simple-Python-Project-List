import pyttsx3
import time
if __name__ == "__main__":
    Engine = pyttsx3.init()
    current_hour1 =time.strftime ('%H')
    current_hour = int(current_hour1)
    if current_hour >= 5 and current_hour < 12 :
        Engine.say(f"Good morning Rujal Boss, i welcome you ")
    elif current_hour >= 12 and current_hour< 18:
        Engine.say(f"Good afternoon Rujal Boss, i welcome you ")       
    elif current_hour >= 18 and current_hour < 19:
        Engine.say(f"Good Evening Rujal Boss, i welcome you ")    
    else:
        Engine.say(f"i welcome you to Have sweet night time Rujal Boss") 
    Engine.runAndWait()
    Engine.stop()







    