#import ...
import cv2
import numpy as np

class OpenCVController(object):

    def __init__(self):
        self.in_zone = False
        print('OpenCV controller initiated')
    
    def getVideo(self,camera):
        frame = camera.get_frame()
        print("frmae",frame[0])
        return frame

    def get_frame(self, camera):
        frame = camera.get_frame()
        print("frame", frame)
        print(type(frame))
        # Code
        jpg_as_np = np.fromstring(frame, np.uint8)
        img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
        
        hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        lowerRed = np.array([0,100,20])  
        upperRed = np.array([20,255,255])
        
        maskRed = cv2.inRange(hsv,lowerRed, upperRed)
        contourR,h = cv2.findContours(maskRed,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for c in contourR:
            if cv2.contourArea(c)> 2000:
                xRed,yRed,w,h = cv2.boundingRect(c)
                xwRed=xRed+w
                cv2.rectangle(img,(xRed,yRed),(xRed+w, yRed+h),(0,0,255),thickness=3)
                
                cv2.rectangle(img, (xRed+2, yRed+h+40), (xRed + 100, yRed+h+2 ), (40,20,255), -1)
                cv2.putText(img,"Mark",(xRed+5, yRed+h+30),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)
        
        lowerBlue = np.array([80,195,25])
        upperBlue = np.array([135,255,255])

        maskBlue = cv2.inRange(hsv,lowerBlue, upperBlue)
        contourB,h = cv2.findContours(maskBlue,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for coun in contourB:
            if cv2.contourArea(coun)> 550:
                xBlue,yBlue,w,h = cv2.boundingRect(coun)
                xwBlue=(xBlue+w)
                cv2.rectangle(img,(xBlue,yBlue),(xBlue+w, yBlue+h),(255,0,0),thickness=3)
                
                cv2.rectangle(img, (xBlue, yBlue-40), (xBlue + 90, yBlue-2 ), (255,120,20), -1)
                cv2.putText(img,"Zone",(xBlue+5, yBlue-5),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)

        if xwRed >= xBlue and xRed <= xwBlue :
            self.in_zone = True
        else:
            self.in_zone = False
            
        print('Monitoring')
        return img


    def is_in_zone(self):
        return self.in_zone
