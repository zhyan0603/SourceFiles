import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

# 定义默认的颜色列表
# custom_colors = ['#9DBAD2', '#A9CA70', '#F18C54', '#d62728', '#9467bd']

custom_colors = ['#8FA2CD', '#F8BC7E', '#A9CA70', '#F09BA0', '#9D9EA3', '#B7B7EB', '#F27873', '#B384BA']

# 设置默认配色
plt.rcParams['axes.prop_cycle'] = cycler(color=custom_colors)

# Get the current directory (assumed to be the directory containing the temperature folders)
base_dir = os.getcwd()  # Get the current working directory

# Define the temperature range (500K to 1200K, step of 100K)
temperatures = list(range(600, 1300, 100))  # Temperature range: 500K to 1200K with a step of 100K

# Initialize a dictionary to store x and y data for each temperature
data_dict = {}

# Loop through each temperature folder
for temp in temperatures:
    folder_name = f"./rdf/{temp}K"  # Folder name corresponding to each temperature (e.g., "500K")
    folder_path = os.path.join(base_dir, folder_name)

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_name} does not exist, skipping.")
        continue
    
    # Path to the rdf.out file in the current temperature folder
    rdf_file_path = os.path.join(folder_path, "rdf.out")
    
    # Check if the rdf.out file exists
    if not os.path.isfile(rdf_file_path):
        print(f"File {rdf_file_path} does not exist, skipping.")
        continue

    # Read the rdf.out file, skipping the first row (header)
    try:
        data = np.loadtxt(rdf_file_path, skiprows=1)
    except Exception as e:
        print(f"Error reading {rdf_file_path}: {e}")
        continue

    # Extract the first column (x-axis) and third column (y-axis)
    x = data[:, 0]
    y = data[:, 2]

    # Store the x and y data in the dictionary for this temperature
    data_dict[temp] = (x, y)

# Create a plot
plt.figure(figsize=(4.5, 3),dpi=150)

# Loop through the stored data and plot each temperature as a separate line
for temp, (x, y) in data_dict.items():
    plt.plot(x, y, label=f"{temp}K")  # Plot each temperature with a label

plt.ylim(-0.1, 3.8)
# Add labels and a legend
plt.xlabel(r'r($\AA$)')
plt.ylabel('g(r)')
#plt.title(sys.argv[1])
plt.legend(loc='upper left', fontsize=8)

plt.tight_layout()
# Show the plot
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('rdf.png', dpi=500)
else:
    plt.show()
