import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import sys

custom_colors = ['#8FA2CD', '#F8BC7E', '#A9CA70', '#F09BA0', '#9D9EA3', '#B7B7EB']
plt.rcParams['axes.prop_cycle'] = cycler(color=custom_colors)

data_pp = np.loadtxt('./dimer_perturb_pseudo_200.data')
data_pp_200_zbl = np.loadtxt('./dimer_pp_200_zbl.data')
data_stand = np.loadtxt('./dimer_standard.data')

fig, axs = plt.subplots(2, 1, figsize=(4, 5.2), dpi=150)

# Plot the first subplot
axs[0].plot(data_stand[:, 0], data_stand[:, 1] + 0.508613, label=r'NEP$_{std}$')
axs[0].plot(data_pp[:, 0], data_pp[:, 1] + 9.843880, label=r'NEP$_{200}$')
axs[0].plot(data_pp_200_zbl[:, 0], data_pp_200_zbl[:, 1] + 11.942707, label=r'NEP$_{200}$-ZBL')
axs[0].set_xlabel('Dimer Distance (Å)')
axs[0].set_ylabel(r'$\Delta$E (eV)')
axs[0].legend(fontsize=8, loc='upper left')  # Ensure legend stays in the main plot

# Add inset to the first subplot
# Using `add_axes` to freely control position and size
inset1 = fig.add_axes([0.5, 0.67, 0.4, 0.25])  # [left, bottom, width, height]
inset1.plot(data_stand[:, 0], data_stand[:, 1] + 0.508613)
inset1.plot(data_pp[:, 0], data_pp[:, 1] + 9.843880)
inset1.plot(data_pp_200_zbl[:, 0], data_pp_200_zbl[:, 1] + 11.942707)
inset1.set_xlim(0.8, 2.2)
inset1.set_ylim(-1, 3)  # Adjust as necessary
inset1.axvline(0.9, color='grey', linestyle='--', linewidth=1)
inset1.axvline(1.8, color='grey', linestyle='--', linewidth=1)
inset1.set_xlabel('Dimer Distance (Å)', fontsize=8)
inset1.set_ylabel(r'$\Delta$E (eV)', fontsize=8)
inset1.tick_params(axis='both', labelsize=7.5)

# Plot the second subplot
axs[1].plot(data_stand[:, 0], data_stand[:, 2], label=r'NEP$_{std}$')
axs[1].plot(data_pp[:, 0], data_pp[:, 2], label=r'NEP$_{200}$')
axs[1].plot(data_pp_200_zbl[:, 0], data_pp_200_zbl[:, 2], label=r'NEP$_{200}$-ZBL')
axs[1].set_xlabel('Dimer Distance (Å)')
axs[1].set_ylabel('Fx (eV/Å)')
axs[1].legend(fontsize=8, loc='upper left')  # Ensure legend stays in the main plot

# Add inset to the second subplot
inset2 = fig.add_axes([0.5, 0.23, 0.4, 0.25])  # [left, bottom, width, height]
inset2.plot(data_stand[:, 0], data_stand[:, 2])
inset2.plot(data_pp[:, 0], data_pp[:, 2])
inset2.plot(data_pp_200_zbl[:, 0], data_pp_200_zbl[:, 2])
inset2.set_xlim(0.6, 3)
inset2.set_ylim(-3.2, 6)  # Adjust as necessary
inset2.axvline(0.9, color='grey', linestyle='--', linewidth=1)
inset2.axvline(1.8, color='grey', linestyle='--', linewidth=1)
inset2.set_xlabel('Dimer Distance (Å)', fontsize=8)
inset2.set_ylabel('Fx (eV/Å)', fontsize=8)
inset2.tick_params(axis='both', labelsize=7.5)

fig.subplots_adjust(top=0.987, bottom=0.085, left=0.154, right=0.97, hspace=0, wspace=0.25)
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('Figure3.png', dpi=600)
else:
    plt.show()
