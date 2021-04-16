# computer vision program designed to help identify people in video frame.
# press q to quit

import cv2 
import imutils 

print("press q to quit")

# Initializing the HOG person detector 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
   
capture = cv2.VideoCapture(0) 

while capture.isOpened(): 
    # Capture the frame
    ret, frame = capture.read() 
    if ret:
        # remove # to increase speeds
        #frame = imutils.resize(frame,  
        #                       width=min(400, frame.shape[1])) 
   
        # Detecting persons 
        (regions, _) = hog.detectMultiScale(frame, 
                                            winStride=(4, 4), 
                                            padding=(4, 4), 
                                            scale=1.05) 
        a=0
        b=0
        c=0
        d=0
        temp=0
        # Outlining the largest person
        for (x, y, w, h) in regions:
            if w*h > temp:
                a=x
                b=y
                c=w
                d=h

        cv2.rectangle(frame,(a, b),(a + c, b + d),(0, 0, 255), 2) 
   
        # Display the frame 
        cv2.imshow("Image", frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else: 
        break

# Release 
capture.release() 
cv2.destroyAllWindows()


