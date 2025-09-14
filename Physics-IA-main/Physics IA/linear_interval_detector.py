import numpy as np

# The x-values from your dataset 
with open('data.csv', 'r') as file:
    # Read each line as a string
    x_values = file.readlines()

# Strip newlines from each line forclean strings
x_values = [line.strip() for line in x_values]

# Convert strings to floats
x_values = [tuple(map(float, item.split(','))) for item in x_values]

# Separate the x-values and y-values for easier processing
x = [item[0] for item in x_values]
y = [item[1] for item in x_values]

# Calculate the differences between consecutive x-values and y-values
diff_x = np.diff(x)
diff_y = np.diff(y)

# Calculate the slopes (rate of change) for the x-values
slopes = diff_y / diff_x  # slope = Δy / Δx

# Find the longest interval where the slopes are nearly constant (with small variance)
max_len = 0
start_idx = 0
end_idx = 0
threshold = 0.01  # Slope difference threshold for considering intervals as mostly linear

for i in range(1, len(slopes)):
    # Compare current slope with the previous slope
    if abs(slopes[i] - slopes[i-1]) < threshold:
        # If this is the longest interval found so far, update the max length and interval
        if i - start_idx > max_len:
            max_len = i - start_idx
            end_idx = i
    else:
        start_idx = i  # Reset the start of the interval

# Get the Largest Mostly Linear Interval
largest_interval_x_values = x[start_idx:end_idx+1]  # Include the end point
print(f"Largest Mostly Linear Interval (x-values): {largest_interval_x_values}")

