import numpy as np
import scipy.stats as stats

lower_range = 4.0
upper_range = 4.4

time_index_needed = []

with open('data.csv', 'r') as file:
    # Read each line as a string
    data = file.readlines()

# Strip newlines from each line if you want clean strings
data = [line.strip() for line in data]

#convert strings to floats
data = [tuple(map(float, item.split(','))) for item in data]


# Split into two lists
time = [x[0] for x in data]  # First column
y_distance = [x[1] for x in data]  # Second column

for i in range(0, len(time)):
    if time[i] > upper_range:
        break
    if time[i] > lower_range:
        time_index_needed.append(i)
    

# Extract relevant data points from the given interval (3.2s to 3.5s)
time_values = np.array([
    time[x] for x in time_index_needed
])
position_values = np.array([
    y_distance[y] for y in time_index_needed
])

print(time_values)

# Calculate the average slope using the first and last points
avg_slope = (position_values[-1] - position_values[0]) / (time_values[-1] - time_values[0])

# Perform linear regression to find the best fit line (y = mx + b)
slope, intercept, r_value, _, _ = stats.linregress(time_values, position_values)

# Compute the average deviation from the best-fit line
predicted_positions = slope * time_values + intercept
average_deviation = np.mean(np.abs(position_values - predicted_positions))

# Return results
print(f"{avg_slope} pixels per second", f"y = {slope}", intercept, f"{average_deviation} average deviation")
