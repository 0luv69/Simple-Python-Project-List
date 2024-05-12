import time
import os

today= str(time.strftime("%m_%d_%Y--%H_%M"))
file_name=f"{today}.txt"
f = open(file_name,"w+")
os.startfile(file_name)
f.close()