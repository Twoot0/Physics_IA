import cv2
import numpy as np

# Function to get color at clicked position
def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left click
        pixel_color = frame[y, x]  # Get BGR color
        b, g, r = int(pixel_color[0]), int(pixel_color[1]), int(pixel_color[2])
        print(f"RGB: ({r}, {g}, {b}) | HEX: #{r:02x}{g:02x}{b:02x}")

# Start video capture
cap = cv2.VideoCapture(0)

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", get_color)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
