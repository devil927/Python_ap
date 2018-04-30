# Import library
import cv2,pandas
from datetime import  datetime

# Capture the video
video=cv2.VideoCapture(0)
frst_f=None
time_list=[]
stat_list=[None,None]
df=pandas.DataFrame(columns=['start','end'])

# Play the video
while(True):
    
    # initialize
    status=0
    ch, f = video.read()
    img=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    
    # Blurness for removing noise and accuracy
    gray=cv2.GaussianBlur(img,(21,21),0)
    
    # Declaring first frame for comparision
    
    if frst_f is None:
        frst_f=gray
        continue
    
    # The compared frame
    
    delta_frame=cv2.absdiff(frst_f,gray)
    
    # Threshold frame for which each pixel value greater than 30 will convert into white

    th_del=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    # Dilate for more accurate frame

    th_del=cv2.dilate(th_del,None,iterations=5)

    # Find the contour in the frame for moving objects

    (_,cnts,_)=cv2.findContours(th_del.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            status=1
            continue

        # Finding the coordinates for binding contours

        (x,y,w,h)=cv2.boundingRect(contour)

        # Making Rectangle around moving obj
         cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),3)
         
    stat_list.append(status)
    cv2.imshow('Threshold',th_del)
    cv2.imshow('delta',delta_frame)
    cv2.imshow('delta', f)
    cv2.imshow('Video', gray)
    k = cv2.waitKey(1)
    if stat_list[-1]==1 and stat_list[-2]==0:
        time_list.append(datetime.now())
    if stat_list[-1]==0 and stat_list[-2]==1:
        time_list.append(datetime.now())

    # if u press q it will quit
    if k==ord('q'):
        if status==1:
            time_list.append(datetime.now())
        break
for i in range(0,len(time_list),2):
    df=df.append({'start':time_list[i],'end':time_list[1+1]},ignore_index=True)
df.to_csv('Time_details.csv')
# Stop capturing
video.release()
# Delete window
cv2.destroyAllWindows()
