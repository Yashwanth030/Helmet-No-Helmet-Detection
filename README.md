# Helmet Detection System 
This project is a real-time Helmet Detection System built using YOLOv8 and OpenCV.
It opens your webcam live, detects whether a person is wearing a helmet or not, and sounds an alert beep when a person without a helmet is detected.

## How It Works
Webcam opens automatically on running the program.
YOLO model (best.pt) processes each frame.
If helmet is detected, it counts and displays.

If no helmet is detected, it:
Plays a beep alert (winsound used for Windows systems).
Logs detection details like timestamp, class, confidence, and person ID.
Live counts of helmet and no-helmet detections are shown on the video.
Press 'q' to exit safely.

## Features
- Real-time helmet detection from webcam feed.
- Alert sound when a person is detected without a helmet.
- Logging of each detection with timestamp into a text file (detections_log.txt).
- Live counter for number of helmets and no-helmets.
- Smooth and fast detection using YOLOv8 and OpenCV.

## Project Structure
bash

Helmet-Detection-Project/
│
├── best.pt                  # Trained YOLO model for helmet detection
├── detections_log.txt        # Detection logs (generated automatically)
├── helmet_detection.py       # Main Python script
├── README.md                 # Project documentation

 Requirements
- Python 3.8+
- OpenCV (cv2)
- NumPy
- Ultralytics (for YOLOv8)
- winsound (built-in for Windows)

## Install requirements:

bash
pip install opencv-python numpy ultralytics

## Model Details
The YOLOv8 model (best.pt) is trained to classify:
Class 0 → Helmet
Class 1 → No Helmet
(If your model's classes are different, adjust the class IDs in the script.)

## How To Run
Make sure best.pt is placed in the same folder as the script.

Run the Python script:
bash
python helmet_detection.py
Your webcam will open live, and detections will start!

## Notes
The beep alert only plays for detections without helmets.
Detection logs will be saved automatically into detections_log.txt.

If the webcam does not open:
Check if the webcam is free (no other apps using it).
Allow access if permission is required.
Try using cv2.VideoCapture(1) if you have multiple cameras.

## Demo
(You can later replace this with a real screenshot or video GIF of your working project!)

## Contribution
If you wish to improve the model accuracy or add features (like face recognition, better tracking, etc.)

