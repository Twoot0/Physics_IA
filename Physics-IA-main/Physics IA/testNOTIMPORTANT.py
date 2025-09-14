import cv2

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not access the webcam.")
else:
    # Get the default resolution
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"Webcam Resolution: {width}x{height}")

# Release the webcam
cap.release()
