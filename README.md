# Smart Surveillance System

The Smart Surveillance System integrates camera, motor, and sensor controllers to create a versatile solution for monitoring and surveillance tasks. Developed using Python and Raspberry Pi, this system provides functionalities such as video streaming, motorized movement, and distance tracking.

## Components

1. **Camera Controller:** Utilizes OpenCV to capture video frames from a camera source.
2. **Motor Controller:** Controls the movement of a motor for physical repositioning.
3. **Sensor Controller:** Tracks distance using ultrasonic sensors for proximity detection.

## Project Structure

- **app.py:** Flask application to manage system functionalities and provide a web interface.
- **task1_opencv_control:** Manages video streaming and motion detection using OpenCV.
- **task2_motor_control:** Controls motor movement for repositioning the surveillance system.
- **task3_sensor_control:** Tracks distance using ultrasonic sensors for proximity detection.

## Usage

1. **Installation:**
   - Clone the repository to your Raspberry Pi.
   - Install required Python dependencies using `pip install -r requirements.txt`.

2. **Setup:**
   - Connect the camera, motor, and ultrasonic sensor to the Raspberry Pi as per the hardware specifications.
   - Ensure proper wiring and configuration of GPIO pins.

3. **Running the System:**
   - Run `python app.py` to start the Flask server.
   - Access the web interface on your browser to view the live video feed and monitor system status.

4. **Functionality:**
   - Start/stop the motor to adjust the camera's viewing angle.
   - Monitor the surroundings with real-time video streaming.
   - Track distance using ultrasonic sensors for object detection and proximity alerts.

## Notes

- This system is designed for educational and experimental purposes and may require customization for specific applications.
- Ensure proper wiring and configuration of hardware components to avoid malfunctions.
- Refer to the documentation and comments within the code for detailed explanations of each component and functionality.
