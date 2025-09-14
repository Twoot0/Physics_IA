import cv2
import numpy as np

def get_dominant_hsv(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Compute the histogram of the hue channel
    hue_channel = hsv[:, :, 0]
    hist = cv2.calcHist([hue_channel], [0], None, [180], [0, 180])
    
    # Find the most frequent hue value
    dominant_hue = np.argmax(hist)
    
    # Compute the average saturation and value
    saturation_channel = hsv[:, :, 1]
    value_channel = hsv[:, :, 2]
    avg_saturation = int(np.mean(saturation_channel))
    avg_value = int(np.mean(value_channel))
    
    return dominant_hue, avg_saturation, avg_value

def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        dominant_hue, avg_saturation, avg_value = get_dominant_hsv(frame)
        
        # Display dominant HSV on the frame
        text = f"Dominant HSV: ({dominant_hue}, {avg_saturation}, {avg_value})"
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("HSV Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
