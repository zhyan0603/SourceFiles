import numpy as np
import sys
import matplotlib.pyplot as plt
import os
from cycler import cycler

#custom_colors = ['#8FA2CD', '#F8BC7E', '#A9CA70', '#F09BA0', '#9D9EA3', '#B7B7EB']
custom_colors = ['#8FA2CD', '#F8BC7E', '#A9CA70', '#F09BA0', '#9D9EA3', '#B7B7EB', '#F27873', '#B384BA']
plt.rcParams['axes.prop_cycle'] = cycler(color=custom_colors)

def process_data(data):
    return data[:, -3]/4, data[:, -2]/4, data[:, -1]/4

def generate_temperature(data, mode):
    n = len(data)
    if mode == 'heating':
        return np.linspace(600, 1200, n)
    elif mode == 'cooling':
        n1 = n // 4
        n2 = n // 2
        n3 = n - n1 - n2
        return np.concatenate([
            np.linspace(1200, 950, n1),
            np.linspace(950, 850, n2),
            np.linspace(850, 600, n3)
        ])

def read_msd_data(file_name):
    data = np.loadtxt(file_name)
    return data[:, 0], (data[:, 1] + data[:, 2] + data[:, 3])

def calculate_slope(x, y):
    half_idx = len(x) // 2
    x_half, y_half = x[:half_idx], y[:half_idx]
    coeffs = np.polyfit(x_half, y_half, 1)
    return coeffs[0]

data_h = np.loadtxt('./phasetransition/heating/thermo.out')
data_c = np.loadtxt('./phasetransition/cooling/thermo.out')
a_h, b_h, c_h = process_data(data_h)
a_c, b_c, c_c = process_data(data_c)
temp_h = generate_temperature(data_h, 'heating')
temp_c = generate_temperature(data_c, 'cooling')

temperatures = list(range(600, 1300, 100))
data_dict = {}
base_dir = os.getcwd()
for temp in temperatures:
    folder_name = f"./rdf/{temp}K"
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.exists(folder_path):
        rdf_file_path = os.path.join(folder_path, "rdf.out")
        if os.path.isfile(rdf_file_path):
            try:
                data = np.loadtxt(rdf_file_path, skiprows=1)
                data_dict[temp] = (data[:, 0], data[:, 2])
            except:
                continue

time_800, msd_800 = read_msd_data('./msd/800K/msd.out')
time_1000, msd_1000 = read_msd_data('./msd/1000K/msd.out')
slope_800 = calculate_slope(time_800, msd_800)
slope_1000 = calculate_slope(time_1000, msd_1000)

fig = plt.figure(figsize=(12, 2.8), dpi=150)

gs = fig.add_gridspec(1, 3, width_ratios=[1.55, 1.55, 1])

ax1 = fig.add_subplot(gs[0])
for y in [a_h, b_h, c_h]:
    ax1.plot(temp_h, y, color='#DD7C4F', alpha=1.0)
for y in [a_c, b_c, c_c]:
    ax1.plot(temp_c, y, color='#84BA42', alpha=1.0)
ax1.set_xlabel('Temperature (K)')
ax1.set_ylabel('Lattice Constants (Å)')
legend_elements = [
    plt.Line2D([0], [0], color='#DD7C4F', lw=2, label='Heating'),
    plt.Line2D([0], [0], color='#84BA42', lw=2, label='Cooling')
]
ax1.legend(handles=legend_elements, frameon=False)

ax2 = fig.add_subplot(gs[1])
ax2.set_prop_cycle(cycler(color=custom_colors))  
for temp, (x, y) in data_dict.items():
    ax2.plot(x, y, label=f"{temp}K")  
ax2.set_ylim(-0.1, 3.8)
ax2.set_xlabel(r'r($\AA$)')
ax2.set_ylabel('g(r)')
ax2.legend(loc='upper right', fontsize=8)

ax3 = fig.add_subplot(gs[2])
ax3.plot(time_800, msd_800, label='800K', color='#D95319')
ax3.set_xlabel('dt (ps)')
ax3.set_ylabel(r'MSD (Å$^2$) - 800K', color='#D95319')
ax3.tick_params(axis='y', labelcolor='#D95319')
ax3.set_ylim(-0.1, 1.7)
ax3.text(0.32, 0.18, f'Slope (800K): {slope_800:.3f} Å$^2$/ps', 
         transform=ax3.transAxes, fontsize=8, color='#D95319')

ax4 = ax3.twinx()
ax4.plot(time_1000, msd_1000, label='1000K', color='#1F8E42')
ax4.set_ylabel(r'MSD (Å$^2$) - 1000K', color='#1F8E42')
ax4.tick_params(axis='y', labelcolor='#1F8E42')
ax4.set_ylim(-2, 32)
ax4.text(0.32, 0.10, f'Slope (1000K): {slope_1000:.3f} Å$^2$/ps', 
         transform=ax4.transAxes, fontsize=8, color='#1F8E42')

#plt.tight_layout()
plt.subplots_adjust(top=0.966,bottom=0.185,left=0.064,right=0.95,hspace=0.2,wspace=0.21)

if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('performance.png', dpi=300, bbox_inches='tight')
else:
    plt.show()