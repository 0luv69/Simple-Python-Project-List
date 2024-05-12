import ctypes
import time

def get_available_drives():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()

    for letter in range(65, 91):
        if bitmask & 1:
            drives.append(chr(letter))
        bitmask >>= 1

    return drives

def check_uniqe_drive(previous, newone):
    p_d= set(previous)
    n_d= set(newone)
    uniqe = n_d- p_d
    print("New Dirives Dected are:", list(uniqe))

if __name__=="__main__":
    previous_drives= []
    while True:
        available_drives = get_available_drives()
        print("Available drives at a time:", available_drives)
        check_uniqe_drive(previous_drives, available_drives)
        previous_drives= available_drives
        print("\n\nNote: To Kill program press \"crtl+c\"\nListening new drive entry after every 10 second......")
        time.sleep(10)



