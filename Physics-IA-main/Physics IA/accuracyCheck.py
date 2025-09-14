import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

a=0.75
b=0
# Experimental data: Temperature in Celsius and Terminal velocity in pixels per second
temperature_celsius = np.array([90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30])
#terminal_velocity_pixels = np.array([a * 129.14 - b, 77.87, a * 94.32 -b, 64.67, a * 91 -b, 51.267, a * 70.587 -b, 46.87, 41.943, 26.5, a * 32.921 -b, 10.625, 12.756])
#day 2
terminal_velocity_pixels = np.array([95, 77.87, 67.45, 64.67, 51.0, 51.267, 45.9, 46.87, 27.7, 26.5, 18.11, 10.625, 12.756])
# Convert temperatures to Kelvin
temperature_kelvin = temperature_celsius + 273.15

# Linear fit model: v(T) = m*T + b
def linear_temp_relation(T, m, b):
    return m * T + b

# Fit the experimental data to a linear model
popt, _ = curve_fit(linear_temp_relation, temperature_kelvin, terminal_velocity_pixels)

# Extract the fitted parameters
m_fitted, b_fitted = popt

# Calculate the fitted terminal velocities at each temperature
fitted_terminal_velocities = linear_temp_relation(temperature_kelvin, m_fitted, b_fitted)

# Plot the experimental data and the fitted line
plt.plot(temperature_celsius, terminal_velocity_pixels, 'o', label='Experimental Data', color='blue')
plt.plot(temperature_celsius, fitted_terminal_velocities, label='Linear Fit Model', color='red')
plt.xlabel('Temperature (°C)')
plt.ylabel('Terminal Velocity (pixels/sec)')
plt.title('Experimental vs Fitted Terminal Velocity vs Temperature')
plt.legend()
plt.show()

# Display the fitted parameters
m_fitted, b_fitted
