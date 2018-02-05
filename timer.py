import time
import winsound
f=2500
d=5000
print("\t\t\t\t\tTimer")
t=time.time()
min=int(input("No of minutes "))
min=60*min
s=input("Start?> ")
if s=='Start':
    time.sleep(min)
    if time.time()>=t+min:
        winsound.Beep(f,d)
        r=input("Sleep/Stop?> ")
        while(r=='Sleep'):
            s=int(input("Enter no. of secs "))
            time.sleep(s)
            winsound.Beep(f,d)
            r=input("Sleep/Stop?> ")
            if r=='Stop':
                break
            
