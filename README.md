🚨 Helmet Detection and Alert System
Project Overview:
The Helmet Detection and Alert System is a real-time computer vision application designed to ensure safety compliance by detecting whether individuals are wearing helmets. It uses a custom-trained YOLOv8 deep learning model to distinguish between people with and without helmets through a live webcam feed.

If a person without a helmet is detected, the system automatically triggers an audible alarm to alert authorities or nearby personnel, and logs the event for record-keeping.

Key Features:
Real-time Detection: Continuously monitors video feed from a webcam to detect helmets.

Sound Alert: Emits a warning beep when a person without a helmet is identified.

Detection Logging: Records the time, detected class (helmet/no helmet), confidence score, and person ID in a text log file.

Person Tracking: Prevents double-counting by tracking the movement of individuals based on centroid tracking.

Live Count Display: Shows the count of helmet-wearers and non-wearers directly on the screen.

Tools & Technologies Used:
Python (Core Programming)

OpenCV (for image/video processing)

Ultralytics YOLOv8 (for object detection)

NumPy (for centroid calculations)

Winsound (for generating alerts on Windows OS)

How It Works:
The system captures video frames from the webcam.

Each frame is passed through the YOLOv8 model to detect objects (helmet/no helmet).

Detections are analyzed:

If a helmet is detected, the helmet count is incremented.

If no helmet is detected, the no-helmet count is incremented and an alert sound is triggered.

The detection details are logged with a timestamp for future analysis.

The annotated frame with detection boxes and real-time counts is displayed on screen.

The program runs continuously until the user presses the 'q' key.

Applications:
Traffic monitoring at intersections.

Factory or construction site safety compliance.

Workplace monitoring where helmet usage is mandatory.

Public awareness campaigns promoting helmet usage.

