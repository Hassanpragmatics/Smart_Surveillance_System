
from flask import Flask, render_template, Response, request, jsonify

from task1_opencv_control.opencv_controller import OpenCVController
from task1_opencv_control.camera import Camera
from task2_motor_control.motor_controller import MotorController
from task3_sensor_control.sensor_controller import SensorController

app = Flask(__name__)

motor_controller = MotorController()
opencv_controller = OpenCVController()
sensor_controller = SensorController()
should_stop_in_zone = False
startMotor = True


@app.route('/')
def index():
    return render_template('index.html') 

def get_frame(camera):
    while True:
        frame = opencv_controller.getVideo(camera)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')            

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_motor',methods=['POST'])
def start_motor():
    global startMotor
    for x in range(3):
        if(startMotor == False):
            startMotor = True
            break
        else:
            motor_controller.start_motor()
    return { 'success': True }

@app.route('/monitor')
def monitor():
    # ...
    sensor_controller.track_rod()
    return jsonify({
        "inZone": opencv_controller.is_in_zone(),
        "distance": sensor_controller.get_distance()
        })

@app.route('/stop_system',methods=['POST'])
def stop_system():
    global startMotor
    startMotor = False
    return { 'success': True }

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
