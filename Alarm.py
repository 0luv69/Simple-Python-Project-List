import time
from win10toast import ToastNotifier
import pyttsx3
import winsound


def push_notify():
    timess = time.strftime("%H:%M:%S")
    notify = ToastNotifier()
    notify.show_toast(
        "Hey, its Alarm",
        f"The time is {timess} ",
        # icon_path = r'C:/Users/Rujal Baniya/Desktop/_Code_/Learn_language/Python/2-6-2023/projects/drink water/3.ico',
        duration = 10,
        threaded = True,)
    talk = pyttsx3.init()
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    talk.say(f"Hey Boss, its alarm for {timess} tig.. ting.. tinng... tinnng....tinnnng....tinng")
    talk.runAndWait()    
    talk.stop()
    
if __name__== "__main__":
    while True:
        example = time.strftime("%H:%M:%d")
        time_ask= input(f"\nEnter the time in format of [Hour:Minutes:Days] eg,\'{example}\':\t")
        alarm_array = time_ask.split(":")
        if len(alarm_array)==2:
            if int(alarm_array[0])>=24 or int(alarm_array[0])<0 or int(alarm_array[1])>=60 or int(alarm_array[1])<0: 
                print("Sorry wrong format input, plz try again:\t")
            else:
                break 
        elif len(alarm_array)==3:
            if int(alarm_array[0])>=24 or int(alarm_array[0])<=0 or int(alarm_array[1])>=60 or int(alarm_array[1])<=0 or int(alarm_array[2])<=0 or int(alarm_array[2])>=30 : 
                print("Sorry wrong format input, plz try again:\t")
            else:
                break 
           
    now_array = (time.strftime("%H:%M:%S")).split(":")
    if len(alarm_array)==3:
        day= int(alarm_array[2])-int(time.strftime("%d"))
        hour = day*60*60*24        
    else:
        hour = 0    

    alarm_second = int(alarm_array[0])*60*60 + int(alarm_array[1])*60 + hour
    now_second = int(now_array[0])*60*60 + int(now_array[1])*60 + int(now_array[2])
    difference = alarm_second-now_second
    if len(str(difference))==2:
        difference_e=f"{difference} Seconds" 
    elif len(str(difference))==3:
        lo =(difference/60)
        po=("{:.2f}".format(lo)).split(".")

        difference_e =f"{po[0]} Minutes {po[1]} Seconds"  
    elif len(str(difference))==4:
        toime = []
        for i,input in enumerate(alarm_array):
            go =int(input)-int(now_array[i])
            toime.append(go)
        difference_e =f"{toime[0]} Hours {toime[1]} Minutes"  

    elif len(str(difference))>=5 :
        toime = []
        now_arrays= (time.strftime("%H:%M:%d")).split(":")
        for i,input in enumerate(alarm_array):

            go =int(input)-int(now_arrays[i])         
            if go <0:
                go2 = int(input)+go
                toime.append(go2)
            else:
                toime.append(go)  
        difference_e =f"{toime[2]} Days {toime[0]} Hours and {toime[1]} Minutes" 

    print(f"\nAlarm will ring after {difference_e} ")
    try:
        time.sleep(difference) 
        push_notify()
    except:
        print("Sorry, your time has already passed")    
    


            


