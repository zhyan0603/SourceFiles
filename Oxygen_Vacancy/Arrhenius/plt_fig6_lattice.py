import os
import pandas as pd
import matplotlib.pyplot as plt

folders = {
    "pristine": "./pristine/get_lattice",
    "O_vac": "./O_vac/get_lattice",
    "2O_vac": "./2O_vac/get_lattice",
    "4O_vac": "./4O_vac/get_lattice",
    "8O_vac": "./8O_vac/get_lattice",
    "removeLi_4Ovac": "./removeLi_4Ovac/get_lattice",
    "removeO_4Ovac": "./removeO_4Ovac/get_lattice"
}

data = {}

colors = {
    "pristine": "C0",
    "2O_vac": "C2",
    "O_vac": "C1",
    "4O_vac": "C3",
    "8O_vac": "C4",
    "removeLi_4Ovac": "C5",
    "removeO_4Ovac": "C6"
}

legend_dict = {
    "pristine": "Li$_7$La$_3$Zr$_2$O$_{12}$",
    "O_vac": "Li$_{6.96875}$La$_3$Zr$_2$O$_{11.984375}$",
    "2O_vac": "Li$_{6.9375}$La$_3$Zr$_2$O$_{11.96875}$",
    "4O_vac": "Li$_{6.875}$La$_3$Zr$_2$O$_{11.9375}$",
    "8O_vac": "Li$_{6.75}$La$_3$Zr$_2$O$_{11.875}$",
    "removeLi_4Ovac": "Li$_{6.875}$La$_3$Zr$_2$O$_{12}$",
    "removeO_4Ovac": "Li$_7$La$_3$Zr$_2$O$_{11.9375}$"
}

markers = ['o', 'o', 'o', 'o','o', 'o','o']

for key, folder in folders.items():
    file_path = os.path.join(folder, 'avg_thermo.txt')
    df = pd.read_csv(file_path, delim_whitespace=True, header=None)
    temperature = df[0][:-1]
    x_lattice = df[6][:-1]/4
    y_lattice = df[7][:-1]/4
    z_lattice = df[8][:-1]/4
    data[key] = {
        'temperature': temperature,
        'x_lattice': x_lattice,
        'y_lattice': y_lattice,
        'z_lattice': z_lattice
    }

plt.figure(figsize=(6, 3.5),dpi=100)

for i, key in enumerate(data):
    plt.plot(data[key]['temperature'], data[key]['x_lattice'], marker=markers[i], color=colors[key], label=legend_dict[key])
    plt.plot(data[key]['temperature'], data[key]['y_lattice'], marker=markers[i], color=colors[key])
    plt.plot(data[key]['temperature'], data[key]['z_lattice'], marker=markers[i], color=colors[key])

plt.legend(fontsize=10)
#plt.title('Lattice Parameters vs Temperature')
plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel(r'Lattice Parameter ($\AA$)', fontsize=12)
plt.tick_params(axis='y', labelcolor='black', labelsize=12)
plt.tick_params(axis='x', labelcolor='black', labelsize=12)

#plt.grid(True)

#plt.tight_layout()

plt.subplots_adjust(top=0.977,bottom=0.138,left=0.125,right=0.99,hspace=0.2,wspace=0.2)

#plt.show()
plt.savefig('Figure6_lattice_vacancy.pdf')

