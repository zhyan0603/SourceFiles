import numpy as np
import matplotlib.pyplot as plt
import sys

# Function to read data from the given file
def read_data(file_name):
    data = np.loadtxt(file_name)
    return data[:, 0], (data[:, 1] + data[:, 2] + data[:, 3])

# Function to calculate the slope of the first 50% of the data
def calculate_slope(x, y):
    half_idx = len(x) // 2
    x_half, y_half = x[:half_idx], y[:half_idx]
    coeffs = np.polyfit(x_half, y_half, 1)  # Linear fit
    return coeffs[0]  # Slope of the linear fit

# Read the data from the files
time_800, msd_800 = read_data('./msd/msd_800K.out')
time_1200, msd_1200 = read_data('./msd/msd_1200K.out')

# Calculate slopes for the first 50% of the data
slope_800 = calculate_slope(time_800, msd_800)
slope_1200 = calculate_slope(time_1200, msd_1200)

fig, ax1 = plt.subplots(figsize=(4, 3), dpi=150)

# Plot for 800K with the left y-axis
ax1.plot(time_800, msd_800, label='800K', color='#D95319')
ax1.set_xlabel('dt (ps)')
ax1.set_ylabel(r'MSD (Å$^2$) - 800K', color='#D95319')
ax1.tick_params(axis='y', labelcolor='#D95319')
ax1.set_ylim(-0.1,1.9)

# Add slope annotation for 800K
ax1.text(0.35, 0.18, f'Slope (800K): {slope_800:.3f} Å$^2$/ps', transform=ax1.transAxes, 
         fontsize=8, color='#D95319', verticalalignment='top')

# Create a second y-axis for 1200K
ax2 = ax1.twinx()
ax2.plot(time_1200, msd_1200, label='1200K', color='#1F8E42')
ax2.set_ylabel(r'MSD (Å$^2$) - 1200K', color='#1F8E42')
ax2.tick_params(axis='y', labelcolor='#1F8E42')
ax2.set_ylim(-3,52)

# Add slope annotation for 1200K
ax2.text(0.35, 0.10, f'Slope (1200K): {slope_1200:.3f} Å$^2$/ps', transform=ax2.transAxes, 
         fontsize=8, color='#1F8E42', verticalalignment='top')

# Adjust layout and save or show the plot
fig.tight_layout()
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('msd.png', dpi=600)
else:
    plt.show()