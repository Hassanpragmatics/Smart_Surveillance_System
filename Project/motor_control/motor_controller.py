from fake_gpio import GPIO # For testing in PC
from time import sleep 
# import RPi.GPIO as GPIO # For testing in Raspberry Pi

class MotorController(object):

  def __init__(self):
    self.working = False

  def start_motor(self):

    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change

    Clockwise_rotation =0
    Anticlockwise_Rotation =1
    Rotation_Per_Step =0.225

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)

    step_count0 = int(90/Rotation_Per_Step)
    step_count1 = int(270/Rotation_Per_Step)
    step_count2 = int(90/Rotation_Per_Step)
    step_delay=0.01
    

    #.................................Motor will rotate 90 degree Clockwise 
    GPIO.output(self.PIN_DIR, Clockwise_rotation)
    self.working = True
    print("Motor Status",self.working)

    for x in range (step_count0):
      GPIO.output(25, GPIO.HIGH)
      sleep(step_delay)
      GPIO.output(25, GPIO.LOW)
      sleep(step_delay)

    self.working = False
    print("Motor Status",self.working)
    sleep(2)

    #.................................Motor will rotate 270 degree Clockwise 
    self.working = True
    print("Motor Status",self.working)

    for x in range (step_count1):
      GPIO.output(25, GPIO.HIGH)
      sleep(step_delay)           
      GPIO.output(25, GPIO.LOW)
      sleep(step_delay)
    
    self.working = False
    print("Motor Status",self.working)
    sleep(2)

    #.................................Motor will rotate 90 degree Anticlockwise 
    GPIO.output(self.PIN_DIR,Anticlockwise_Rotation)
    self.working = True
    print("Motor Status",self.working)

    for x in range(step_count2):    
      GPIO.output(25, GPIO.HIGH)
      sleep(step_delay)
      GPIO.output(25, GPIO.LOW)
      sleep(step_delay)

    self.working = False
    print("Motor Status",self.working)
    GPIO.cleanup()

  def is_working(self):
    return self.working
