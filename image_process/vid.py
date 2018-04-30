# Import library
import cv2

# Capture the video
video=cv2.VideoCapture(0)
fcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter('output.avi', fcc, 20.0, (640, 480))
# Play the video
while(True):
    ch, f = video.read()
    img=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video',f)
    k=cv2.waitKey(1)
    if k==ord('s'):
        out.write(f)
    # if u press q it will quit
    if k==ord('q'):
        break
# Stop capturing
video.release()
# Delete window
cv2.destroyAllWindows()