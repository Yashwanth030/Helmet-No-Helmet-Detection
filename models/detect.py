import cv2
import winsound  # For sound alert (Windows)
import time
import numpy as np
from ultralytics import YOLO

# Initialize the YOLO model
model = YOLO('best.pt')  # Load your .pt model

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Open a file to log detections (with timestamp)
with open('detections_log.txt', 'w') as log_file:
    log_file.write("Timestamp, Class, Confidence, Person_ID\n")

    # Store previously detected centroids (to avoid double-counting)
    prev_centroids = []
    person_id = 0  # Initial ID for new person

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Results after detection
        results = model(frame, conf=0.2)  # Adjust confidence threshold to 0.5 for better accuracy

        # Inspect the class names to verify which class corresponds to helmet
        print("Class Names:", results[0].names)  # This prints the class names, check the index for helmet

        # Annotate the frame with detection results
        annotated_frame = results[0].plot()

        # Initialize counters for each frame
        helmet_count = 0
        no_helmet_count = 0

        # List to store current frame centroids
        current_centroids = []

        # Count helmet vs no-helmet people and log them
        for result in results[0].boxes:
            class_id = int(result.cls)  # Convert class_id to integer
            confidence = result.conf
            timestamp = time.time()  # Current timestamp

            # Get bounding box coordinates
            x1, y1, x2, y2 = result.xyxy[0].tolist()
            centroid = (int((x1 + x2) / 2), int((y1 + y2) / 2))  # Calculate centroid

            # Log detection with timestamp
            log_file.write(f"{timestamp}, {class_id}, {confidence}, {person_id}\n")

            # Track the centroid and only count if it's a new person
            is_new_person = True
            for prev_centroid in prev_centroids:
                # Check if this centroid is within a threshold distance of a previous one
                if np.linalg.norm(np.array(prev_centroid) - np.array(centroid)) < 50:  # Threshold distance
                    is_new_person = False
                    break

            # If new person detected, increment the person ID and count
            if is_new_person:
                person_id += 1
                current_centroids.append(centroid)

                # Count helmet vs no-helmet
                if class_id == 0:  # Assuming class 0 is helmet (adjust according to your model output)
                    helmet_count += 1
                else:
                    no_helmet_count += 1

                    # Trigger sound alert if no helmet is detected
                    if class_id != 0:  # If detected class is not helmet
                        print(f"No helmet detected, class_id: {class_id}")
                        winsound.Beep(1000, 500)  # Sound alert (frequency, duration)

        # Update the list of previous centroids
        prev_centroids = current_centroids

        # Display the counts on the frame in real-time
        cv2.putText(annotated_frame, f"Helmet: {helmet_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f"No Helmet: {no_helmet_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the annotated frame with detections
        cv2.imshow("Helmet Detection", annotated_frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()
