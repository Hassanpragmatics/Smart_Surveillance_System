from opencv_controller import OpenCVController
from camera import Camera
import time
import cv2
import numpy as np
import base64

opencv_controller = OpenCVController()

for i in range(5):
  frame = opencv_controller.get_frame(Camera())
  
  # Display in window

  cv2.namedWindow('image', cv2.WINDOW_NORMAL)
  cv2.resizeWindow('image', 1000, 600)
  cv2.imshow('image', frame)

  print("Is in zone: ", opencv_controller.is_in_zone())
  print("---------------------------------")
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
