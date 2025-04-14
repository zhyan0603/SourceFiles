import sys
import numpy as np
import matplotlib.pyplot as plt

iterations = np.arange(0, 14)

training_size = np.array([100, 196, 226, 294, 294, 342, 573, 573, 602, 747, 778, 786, 802, 802])
Lidist_samp = np.array([2.138, 1.763, 1.833, 1.861, 1.888, 1.803, 1.640, 1.576, 1.750, 1.676, 1.803, 1.749, 1.871, 1.871])
force_barrier = np.array([1.819511, 1.759334, 1.756151, 1.683204, 1.683204, 2.041223, 2.107919, 2.107919, 2.615703, 2.309992, 2.564373, 2.564373, 2.564373, 2.782801])
distance_cor_force = np.array([1.81, 1.75, 1.67, 1.69, 1.69, 1.71, 1.69, 1.69, 1.59, 1.64, 1.65, 1.65, 1.65, 1.62])
energy_cor_force = np.array([0.936034, 0.951258, 0.928851, 0.897838, 0.897838, 1.018466, 1.070410, 1.070410, 1.404331, 1.200411, 1.414000, 1.414000, 1.414000, 1.491229])

force_cor_energy = np.array([0.035587, -0.044283, 0.029400, 0.012960, 0.012960, -0.039429, 0.002411, 0.002411, -0.059380, 0.063912, 0.042290, 0.042290, 0.042290, -0.053475])
distance_cor_energy = np.array([1.51, 1.45, 1.33, 1.38, 1.38, 1.33, 1.38, 1.38, 1.22, 1.36, 1.35, 1.35, 1.35, 1.32])
energy_barrier = np.array([1.309098, 1.303962, 1.326032, 1.256361, 1.256361, 1.521767, 1.512426, 1.512426, 2.052293, 1.648079, 1.933874, 1.933874, 1.933874, 2.049663])

highlight_iterations = [4, 7, 11, 12]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(5.5, 6), sharex=True)

ax1.plot(iterations, energy_barrier, 'C0-o', label='Energy Barrier')
ax1.plot(iterations[highlight_iterations], energy_barrier[highlight_iterations], 
         's', markersize=12, markeredgecolor='grey', markerfacecolor='none', 
         markeredgewidth=1)
#ax1.set_ylim(1.5, 3)
ax1.set_ylabel(r'Energy Barrier (eV)')
ax1.legend(loc='lower right')
ax1.margins(y=0.15)

ax2.plot(iterations, distance_cor_energy, 'C1-o', label='Breakdown Distance')
ax2.plot(iterations[highlight_iterations], distance_cor_energy[highlight_iterations], 
         's', markersize=12, markeredgecolor='grey', markerfacecolor='none', 
         markeredgewidth=1)
ax2.set_xlabel('Iteration')
ax2.set_ylabel(r'Breakdown Distance ($\AA$)')
ax2.legend(loc='upper right')
ax2.margins(y=0.15)

# ax3.plot(iterations, Lidist_samp, 'C2-o', label='Training Size')
# ax3.plot(iterations[highlight_iterations], Lidist_samp[highlight_iterations], 
#          's', markersize=12, markeredgecolor='grey', markerfacecolor='none', 
#          markeredgewidth=1)
# ax3.set_xlabel('Iteration')
# ax3.set_ylabel(r'min_dist$_{Li-Li}$')
# ax3.legend(loc='lower right')
# ax3.margins(y=0.15)

ax3.plot(iterations, training_size, 'C2-o', label='Training Size')
#ax3.plot(iterations[highlight_iterations], training_size[highlight_iterations], 
#         's', markersize=12, markeredgecolor='grey', markerfacecolor='none', 
#         markeredgewidth=1)
ax3.set_xlabel('Iteration')
ax3.set_ylabel('Training Size')
ax3.legend(loc='lower right')
ax3.margins(y=0.15)

#plt.tight_layout()
plt.subplots_adjust(top=0.975, bottom=0.095, left=0.132, right=0.975, hspace=0.0, wspace=0.2)

if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('./Figure3_iteration_energy.png', dpi=600)
else:
    plt.show()