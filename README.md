🚨 Helmet Detection and Alert System
📜 Project Description
The Helmet Detection and Alert System is a real-time AI-based application built using Python and a custom YOLOv8 model. It detects whether individuals captured on a webcam are wearing helmets. If a person without a helmet is detected, an automatic alarm sound is triggered, and the detection details (timestamp, class, confidence, and ID) are logged for record-keeping. This system promotes safety compliance in traffic monitoring, construction sites, and industrial workplaces.

🛠️ Technologies Used
Python 3

OpenCV (for video processing)

Ultralytics YOLOv8 (for object detection)

NumPy (for centroid tracking)

Winsound (for sound alerts on Windows)

🚀 Features
Real-time helmet and no-helmet detection via webcam.

Sound alert when a person without a helmet is detected.

Live count display of helmeted and non-helmeted individuals.

Logging of all detections into a text file with timestamps.

Person tracking to avoid double-counting based on centroid distance.

📂 Project Structure
bash
Copy
Edit
helmet-detection/
├── best.pt                   # Trained YOLO model
├── helmet_detection.py        # Main Python script
├── detections_log.txt         # Auto-generated log file
├── README.md                  # Project documentation
⚙️ Setup Instructions
Clone the Repository

bash
Copy
Edit
git clone <your-repo-link>
cd helmet-detection
Install Required Libraries

bash
Copy
Edit
pip install opencv-python
pip install ultralytics
pip install numpy
Run the Project

bash
Copy
Edit
python helmet_detection.py
📌 Notes
Make sure your custom YOLO model (best.pt) is trained to classify at least two classes: helmet and no helmet.

This system uses winsound — it works on Windows OS.
If you want to run on Linux or Mac, the sound part needs to be replaced (for example with playsound or pygame).

Adjust the confidence threshold or distance threshold in the code if needed for your environment.

📷 Demo
(Insert a GIF or screenshot here showing the system detecting a helmet and triggering sound without helmet.)

🏁 Future Improvements
Extend support for multi-camera systems.

Deploy it as a web or mobile application.

Add automatic reporting/notifications to supervisors.

🤝 Acknowledgements
YOLOv8 by Ultralytics

OpenCV Team
