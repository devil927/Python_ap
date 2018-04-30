import cv2
x=input("Enter the Video file name -> ")
cap=cv2.VideoCapture('{0}'.format(x))
i=0

while True:
    i=i+1
    _,f=cap.read()
    f=cv2.resize(f,(300,500))
    c = cv2.imwrite('imp/img{0}.jpg'.format(i), f)
    cv2.imshow('images',f)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()
