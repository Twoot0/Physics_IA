import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import csv

# Define HSV range for pink color
lower_pink = np.array([150, 80, 80])  # Adjust based on lighting conditions
upper_pink = np.array([170, 255, 255])

init_cx = 0
init_cy = 0

# Initialize variables
time_values = []
y_positions = []
start_time = time.time()

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create mask for pink color
    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(largest_contour) > 500:  # Threshold to avoid noise
            M = cv2.moments(largest_contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                
                # Store initial values
                if not time_values:
                    init_cx, init_cy = cx, cy
                
                # Draw the largest contour and center point
                cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
                
                # Record time and position
                current_time = time.time() - start_time
                time_values.append(current_time)
                y_positions.append(cy)
    
    # Display frames
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Write data to CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "Vertical Position (pixels)"])
    for t, y in zip(time_values, [-temp_y + init_cy for temp_y in y_positions]):
        writer.writerow([t, y])

# Plot results
plt.plot(time_values, [-temp_y + init_cy for temp_y in y_positions], marker='o', linestyle='-')
plt.xlabel('Time (s)')
plt.ylabel('Vertical Position (pixels)')
plt.title('Vertical Position of Largest Pink Object Over Time')
plt.grid()
plt.show()
