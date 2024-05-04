from fake_gpio import GPIO # For testing in PC
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
from numpy.core.fromnumeric import mean
import numpy as np
import time 

class SensorController:

  def __init__(self):
  
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    # GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(self.PIN_ECHO, GPIO.IN)
    print('Sensor controller initiated')

  def track_rod(self):
  
    print('Monitoring')
    x=0
    count = 10
    start = True
    distance_array = []
    pulse_start = 0
    pulse_end = 0

    while start:
      # print(count)
      for i in range(x,count):                        
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_ECHO)==0:
          pulse_start = time.time()
        while GPIO.input(self.PIN_ECHO)==1:
          pulse_end = time.time()
        
        duration = (pulse_end - pulse_start)/2
        distance = duration * 34300
        distance_array.append(distance)                     # Distance is calculated and appended into the distance array
      
      listTofloat=np.array(distance_array).astype(np.float)
      # print(listTofloat)
      stDev1 = np.std(listTofloat[-10:])
      # print("Standard Deviation",stDev1)
      
      if(stDev1 <= 0.5 ):                                   # If Standard deviation <= 0.5 then mean of last 10 distance value is calculated 
        meanOfArray = round(np.mean(listTofloat[-10:]),2)          
        self.distance=str(meanOfArray)+" cm"
        start = False
      else:  
        x=count
        count = count + 1
        if(count > 40):                                     # Checks whether count is greater then 40. 
          start = False
          medianOfArray = round(np.median(listTofloat),2)
          self.distance=str(medianOfArray)+" cm"
  
  def get_distance(self):
    return self.distance
