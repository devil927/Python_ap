import cv2
import numpy as np
mode=True
draw=False
ix,iy=-1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, draw, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        draw=True
        ix,iy=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        draw=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,255,255),-1)
    elif event==cv2.EVENT_MOUSEMOVE:
        if draw==True:
            if mode==True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 255, 255), -1)



# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break

cv2.destroyAllWindows()