import time
import pyautogui

if __name__=="__main__":
    print("Note: plz make ready the area to type, you will have only 20 sec later")
    word = input("Enter a word to auto type: ")
    try:
        times= int(input("Enter how many times to auto type,[only num]"))
    except:
        print("sorry, you have to type Number only")

    print("You have 20 sec to go in the type box now::")        
    time.sleep(10)
    for i in range(50):
        pyautogui.typewrite(word)
        pyautogui.press('enter')

