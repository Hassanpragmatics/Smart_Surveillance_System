# Please note that this is a fake camera, it will just 
# yield the images 1.jpg, 2.jpg, 3.jg and 4.jpg. It is
# just for testing purposes. You should actually use the
# picamera module and implement the get_frame properly  

# from picamera.array import PiRGBArray
# from picamera import PiCamera

from time import time
import os, sys
import cv2

class Camera(object):
    def __init__(self):
        directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        self.test_frames_name = ['1.jpg', '1.jpg']
        self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]

    def get_frame(self):
        # random_index = int(time()) % 4
        # print('Frame', self.test_frames_name[random_index])
        # return self.frames[random_index]

        capture = cv2.VideoCapture(0)
     
        ret, frame = capture.read()    
        return frame
        # capture.release()
        # cv2.destroyAllWindows()

        # camera = PiCamera()
        # camera.resolution = (640, 480)
        # camera.framerate = 32
        # rawCapture = PiRGBArray(camera, size=(640, 480))

        # for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        #     image = frame.array
        #     return image

        