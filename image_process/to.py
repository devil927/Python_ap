import cv2
import numpy as np

def nothing(x):
    pass
mode=True
draw=False
ix,iy=-1,-1
r,g,b=0,0,0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global r,b,g
    global ix, iy, draw, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        draw=True
        ix,iy=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        draw=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
        else:
            cv2.circle(img,(x,y),5,(b,g,r),-1)
    elif event==cv2.EVENT_MOUSEMOVE:
        if draw==True:
            if mode==True:
                cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            else:
                cv2.circle(img, (x, y), 5, (b, g, r), -1)



# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)


while(1):
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

    cv2.imshow('Draw', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    if k == ord('q'):
        break
cv2.destroyAllWindows()
