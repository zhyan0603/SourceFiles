import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as consts
import pandas as pd
from brokenaxes import brokenaxes

temps = []
sigma_Ts = [] 
Nframes = []
cells = []
Eas = []
handles = []
fits_dict = {} 

def read_msd_file(msd_file):
    data = np.loadtxt(msd_file)
    dts = data[:, 0]  
    msds = np.sum(data[:, 1:4], axis=1)  
    return dts, msds

def get_conversion_factor(structure_volume, species_charge, num_ions, temperature):
    """
    Conversion factor to convert between cm^2/s diffusivity measurements and
    S/cm conductivity measurements based on number of atoms of diffusing
    species.
    """
    z = species_charge
    n = num_ions

    vol = structure_volume * 1e-24  # units cm^3
    return (
        1
        * n
        / (vol * consts.N_A)
        * z**2
        * (consts.N_A * consts.e) ** 2
        / (consts.R * temperature)
    )


tetra_legend_dict = {
    "pristine": "Li$_7$La$_3$Zr$_2$O$_{12}$",
    "O_vac": "Li$_{6.96875}$La$_3$Zr$_2$O$_{11.984375}$",
    "2O_vac": "Li$_{6.9375}$La$_3$Zr$_2$O$_{11.96875}$",
    "4O_vac": "Li$_{6.875}$La$_3$Zr$_2$O$_{11.9375}$",
    "8O_vac": "Li$_{6.75}$La$_3$Zr$_2$O$_{11.875}$",
}

volume_dict = {
    "pristine": {700: 17652.190,750: 17702.818,800: 17755.873,850: 17811.661,900: 17879.135,1000: 17992.418,1100: 18106.747,1200: 18239.891},
    "O_vac": {700: 17654.963,750: 17706.453,800: 17759.390,850: 17814.057,900: 17876.480,1000: 17989.490,1100: 18106.752,1200: 18237.978},
    "2O_vac": {700: 17655.543,750: 17708.004,800: 17760.687,850: 17816.258,900: 17881.649,1000: 17993.405,1100: 18109.130,1200: 18236.968},
    "4O_vac": {700: 17660.781,750: 17711.465,800: 17764.163,850: 17817.352,900: 17871.316,1000: 17982.183,1100: 18103.428,1200: 18226.845},
    "8O_vac": {700: 17660.893,750: 17710.404,800: 17761.654,850: 17813.622,900: 17867.781,1000: 17975.751,1100: 18094.979,1200: 18214.373},
}

ion_count_dict = {
    "pristine": 56*8,
    "O_vac": 56*8-2,
    "2O_vac": 56*8-4,
    "3O_vac": 56*8-6,
    "4O_vac": 56*8-8,
    "8O_vac": 54*8,
}

results_df = pd.DataFrame()

plt.rcParams.update({'font.size': 10})

save_results_to_file = False

for cell_idx, cell in enumerate(["pristine","O_vac","2O_vac","4O_vac"]):
    group_Ts_tetra = []
    group_sigmaTs_tetra = [] 
    group_Ts_cubic = []
    group_sigmaTs_cubic = []  
    folder = f'./{cell}/'
    tetra_temp_list = [700, 750, 800, 850]  # Tetra
    cubic_temp_list = [900, 1000, 1100, 1200]  # Cubic

    color = f'C{cell_idx}'  

    for temp in tetra_temp_list:
        temp_folder = f'{temp}K/'
        msd_file = os.path.join(folder, temp_folder, 'msd.out')

        dts, msds = read_msd_file(msd_file)

        start = int(len(dts) * 0.1)
        end = int(len(dts) * 0.4)

        k, b = np.polyfit(dts[start:end], msds[start:end], 1)[:2]
        D_xyz = k * 10**(-4) / 6  
        D = np.average(D_xyz)

        volume = volume_dict[cell][temp]
        num_ions = ion_count_dict[cell]

        conversion_factor = get_conversion_factor(volume, 1, num_ions, temp)
        conductivity = conversion_factor * D
        sigma_T = conductivity * temp 

        Nframes.append(len(dts))
        group_sigmaTs_tetra.append(sigma_T)
        group_Ts_tetra.append(temp)
        cells.append(cell)
        plt.scatter(1000 / temp, np.log(sigma_T), color=color, s=40)

    for temp in cubic_temp_list:
        temp_folder = f'{temp}K/'
        msd_file = os.path.join(folder, temp_folder, 'msd.out')

        dts, msds = read_msd_file(msd_file)

        start = int(len(dts) * 0.1)
        end = int(len(dts) * 0.4)

        k, b = np.polyfit(dts[start:end], msds[start:end], 1)[:2]
        D_xyz = k * 10**(-4) / 6 
        D = np.average(D_xyz)

        volume = volume_dict[cell][temp]
        num_ions = ion_count_dict[cell]
        conversion_factor = get_conversion_factor(volume, 1, num_ions, temp)
        conductivity = conversion_factor * D
        sigma_T = conductivity * temp  

        Nframes.append(len(dts))
        group_sigmaTs_cubic.append(sigma_T)
        group_Ts_cubic.append(temp)
        cells.append(cell)
        plt.scatter(1000 / temp, np.log(sigma_T), color=color, s=40)

    k_tetra, b_tetra = np.polyfit(1000 / np.array(group_Ts_tetra), np.log(np.array(group_sigmaTs_tetra)), 1)[:2]
    Ea_tetra = -k_tetra * 1000 * consts.k / consts.e
    fits_dict[cell] = {'k_tetra': k_tetra, 'b_tetra': b_tetra} 
    print(f"T-{cell}, Ea: {Ea_tetra:.3f} eV")

    sigma_Ts += group_sigmaTs_tetra
    temps += group_Ts_tetra
    Eas.append(Ea_tetra)

    line_handle_tetra, = plt.plot(1000 / np.array(group_Ts_tetra), k_tetra * 1000 / np.array(group_Ts_tetra) + b_tetra, linestyle='-', linewidth=2, marker='o', color=color, label=tetra_legend_dict[cell])
    handles.append(line_handle_tetra)

    k_cubic, b_cubic = np.polyfit(1000 / np.array(group_Ts_cubic), np.log(np.array(group_sigmaTs_cubic)), 1)[:2]
    Ea_cubic = -k_cubic * 1000 * consts.k / consts.e
    fits_dict[cell]['k_cubic'] = k_cubic
    fits_dict[cell]['b_cubic'] = b_cubic
    print(f"C-{cell}, Ea: {Ea_cubic:.3f} eV")

    sigma_Ts += group_sigmaTs_cubic
    temps += group_Ts_cubic
    Eas.append(Ea_cubic)

    line_handle_cubic, = plt.plot(1000 / np.array(group_Ts_cubic), k_cubic * 1000 / np.array(group_Ts_cubic) + b_cubic, linestyle='-', linewidth=2, marker='o', color=color) #, label=cubic_legend_dict[cell]
    #handles.append(line_handle_cubic)

    df_tetra = pd.DataFrame({
        'Temperature': group_Ts_tetra,
        'Sigma_T': group_sigmaTs_tetra,
        'Cell': cell,
        'Phase': 'Tetra'
    })

    df_cubic = pd.DataFrame({
        'Temperature': group_Ts_cubic,
        'Sigma_T': group_sigmaTs_cubic,
        'Cell': cell,
        'Phase': 'Cubic'
    })

    results_df = pd.concat([results_df, df_tetra, df_cubic], ignore_index=True)

if save_results_to_file:
    results_df.to_csv('conductivity_results.csv', index=False)


for cell_idx, cell in enumerate(["8O_vac"]):
    group_Ts_tetra = []
    group_sigmaTs_tetra = []  
    group_Ts_cubic = []
    group_sigmaTs_cubic = [] 
    folder = f'./{cell}/'
    tetra_temp_list = [700, 750, 800, 850, 900, 1000, 1100, 1200]  # Tetra
    #cubic_temp_list = [900, 1000, 1100, 1200]  # Cubic

    color = f'C{cell_idx}' 

    for temp in tetra_temp_list:
        temp_folder = f'{temp}K/'
        msd_file = os.path.join(folder, temp_folder, 'msd.out')

        dts, msds = read_msd_file(msd_file)

        start = int(len(dts) * 0.1)
        end = int(len(dts) * 0.4)

        k, b = np.polyfit(dts[start:end], msds[start:end], 1)[:2]
        D_xyz = k * 10**(-4) / 6  # A^2/ps to cm^2/s # 3D diffusion
        D = np.average(D_xyz)

        volume = volume_dict[cell][temp]
        num_ions = ion_count_dict[cell]
        conversion_factor = get_conversion_factor(volume, 1, num_ions, temp)
        conductivity = conversion_factor * D
        sigma_T = conductivity * temp 

        Nframes.append(len(dts))
        group_sigmaTs_tetra.append(sigma_T)
        group_Ts_tetra.append(temp)
        cells.append(cell)
        plt.scatter(1000 / temp, np.log(sigma_T), color=color, s=40)

    k_tetra, b_tetra = np.polyfit(1000 / np.array(group_Ts_tetra), np.log(np.array(group_sigmaTs_tetra)), 1)[:2]
    Ea_tetra = -k_tetra * 1000 * consts.k / consts.e
    fits_dict[cell] = {'k_tetra': k_tetra, 'b_tetra': b_tetra}  
    print(f"T-{cell}, Ea: {Ea_tetra:.3f} eV")

    sigma_Ts += group_sigmaTs_tetra
    temps += group_Ts_tetra
    Eas.append(Ea_tetra)

    line_handle_tetra, = plt.plot(1000 / np.array(group_Ts_tetra), k_tetra * 1000 / np.array(group_Ts_tetra) + b_tetra, linestyle='-', linewidth=2, marker='o', color='C4', label=tetra_legend_dict[cell])
    handles.append(line_handle_tetra)


# Exp_Wan
experimental_data = [
#    (293.15, -6.157248524),
    (303.15, -5.56430314),
    (313.15, -5.012630148),
    (323.15, -4.546084538),
    (333.15, -4.019897866),
    (343.15, -3.528485186),
    (353.15, -3.130266548),
    (363.15, -2.735455162),
#    (373.15, -2.25663616)
]

experimental_temps = [1000 / data[0] for data in experimental_data]
experimental_ln_sigmaT = [data[1] for data in experimental_data]

plt.scatter(experimental_temps, experimental_ln_sigmaT, c='none',marker='o',edgecolors='grey')
#plt.plot(experimental_temps, experimental_ln_sigmaT, color='red', marker='o',label='Exp.')
plt.text(3.0, -3.0, 'Exp. (Wan)', color='grey')


exp_weilai = [
    (0.978899083, 5.553835244),
    (1.028440367, 5.406469798),
    (1.078899083, 5.295945714),
    (1.110091743, 5.231473331),
]

exp_weilai_x = [point[0] for point in exp_weilai]
exp_weilai_y = [point[1] for point in exp_weilai]

plt.scatter(exp_weilai_x, exp_weilai_y, c='none',marker='o',edgecolors='grey') #zorder=10
plt.text(0.86, 3.0, 'Exp. (Lai)', color='grey')

specified_temperature = 300

for cell_idx, cell in enumerate(["pristine","O_vac","2O_vac","4O_vac","8O_vac"]):  
    k_tetra = fits_dict[cell]['k_tetra']
    b_tetra = fits_dict[cell]['b_tetra']

    short_dash_x = 1000 / np.array(range(293, 701, 10))
    short_dash_y = k_tetra * short_dash_x + b_tetra
    plt.plot(short_dash_x, short_dash_y, linestyle='--', color=f'C{cell_idx}', alpha=0.6)


    ln_sigmaT_specified = k_tetra * 1000/specified_temperature + b_tetra
    sigma_specified = np.exp(ln_sigmaT_specified) / specified_temperature

    #plt.text(3.333 + 0.03, ln_sigmaT_specified, f'{sigma_specified:.2e} S/cm', fontsize=9, color=f'C{cell_idx}')
    
    print(f"At {specified_temperature}K, {cell}, Sigma: {sigma_specified:.3e}, b: {b_tetra}, ln_sigmaT: {ln_sigmaT_specified:.6}")

plt.gcf().set_size_inches(8.5, 3.5)
plt.gcf().set_dpi(200)

plt.xlabel('1000/T (1/K)', fontsize=11)
plt.ylabel(r'$\ln(\sigma \cdot T)$ (K S/cm$^{-1}$)', fontsize=11) 
plt.xlim(0.75,3.3333)
plt.legend(handles=handles, loc='lower left', fontsize=9)

ax1 = plt.gca()  
ax2 = ax1.twiny() 

def tick_function(X):
    V = 1000 / X  
    return ["%.0f" % z for z in V]


ax2.set_xticks(ax1.get_xticks())
ax2.set_xbound(ax1.get_xbound())  
ax2.set_xticklabels(tick_function(ax1.get_xticks()))
ax2.set_xlabel("T (K)", fontsize=11)

plt.text(3.360, -26.8559, f'{7.236e-15:.2e} S/cm', fontsize=9, color=f'C0')
plt.text(3.360, -10.62602, f'{2.200e-07:.2e} S/cm', fontsize=9, color=f'C1')
plt.text(3.360, -8.67523, f'{5.692e-07:.2e} S/cm', fontsize=9, color=f'C2')
plt.text(3.360, -5.1916, f'{1.854e-05:.2e} S/cm', fontsize=9, color=f'C3')
plt.text(3.360, -1.03825, f'{1.180e-03:.2e} S/cm', fontsize=9, color=f'C4')


plt.text(2.360, -16.8559, f'E$_a$ = 1.227 eV', rotation=-20, fontsize=9, color=f'C0')
plt.text(2.360, -7.62602, f'E$_a$ = 0.564 eV', rotation=-10, fontsize=9, color=f'C1')
plt.text(2.360, -4.2, f'E$_a$ = 0.544 eV',  rotation=-8.5, fontsize=9, color=f'C2')
plt.text(2.360, -1.6, f'E$_a$ = 0.425 eV', rotation=-6.5, fontsize=9, color=f'C3')
plt.text(2.360, 1.83825, f'E$_a$ = 0.263 eV', rotation=-4, fontsize=9, color=f'C4')

plt.tight_layout()  
plt.show()
#plt.savefig('Figure4_Arrhenius.pdf')