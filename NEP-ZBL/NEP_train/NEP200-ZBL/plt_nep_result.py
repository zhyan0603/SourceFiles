import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

# 定义默认的颜色列表
# custom_colors = ['#9DBAD2', '#A9CA70', '#F18C54', '#d62728', '#9467bd']

custom_colors = ['#9BBBE1', '#EAB883', '#A9CA70', '#DD7C4F', '#F09BA0', '#B58C9A']

# 设置默认配色
plt.rcParams['axes.prop_cycle'] = cycler(color=custom_colors)

# Load data
train_data = np.loadtxt('energy_train.out')
force_test = np.loadtxt('force_train.out')
#virial_test = np.loadtxt('virial_train.out')
stress_test = np.loadtxt('stress_train.out')
loss = np.loadtxt('loss.out')

# Function to calculate RMSE
def calculate_rmse(pred, actual):
    return np.sqrt(np.mean((pred - actual) ** 2))

# Create a subplot with 1 row and 3 columns
fig, axs = plt.subplots(2, 2, figsize=(9, 7), dpi=100)

# Plotting the loss figure
axs[0, 0].loglog(loss[:, 1:7], '-', linewidth=2)
#axs[1, 1].loglog(loss[:,0], loss[:, 1:7], '-', linewidth=2)
axs[0, 0].set_xlabel('Generation/100', fontsize=10)
axs[0, 0].set_ylabel('Loss functions', fontsize=10)
axs[0, 0].tick_params(axis='both', labelsize=10)
axs[0, 0].legend(['Total', 'L1-Reg', 'L2-Reg', 'Energy-train', 'Force-train', 'Virial-train'], prop = {'size':8})
axs[0, 0].axis('tight')
axs[0, 0].text(-0.07, 1.03, "(a)", transform=axs[0, 0].transAxes, fontsize=12, va='top', ha='right')


# Plotting the train_data figure
axs[0, 1].plot(train_data[:, 1], train_data[:, 0], '.', markersize=10)
axs[0, 1].plot(np.arange(-7.48, -7.12, 0.01), np.arange(-7.48, -7.12, 0.01), linewidth=2, color='grey', linestyle='--')
axs[0, 1].set_xlabel(r'NEP$_{std}$ energy (eV/atom)', fontsize=10)
axs[0, 1].set_ylabel(r'NEP$_{200}$-ZBL energy (eV/atom)', fontsize=10)
axs[0, 1].tick_params(axis='both', labelsize=10)
axs[0, 1].legend(['energy'])
axs[0, 1].axis('tight')

# Calculate and display RMSE for energy
energy_rmse = calculate_rmse(train_data[:, 0], train_data[:, 1]) * 1000
axs[0, 1].text(0.5, 0.08, f'RMSE: {energy_rmse:.2f} meV/atom', transform=axs[0, 1].transAxes, fontsize=10, verticalalignment='center')
axs[0, 1].text(-0.07, 1.03, "(b)", transform=axs[0, 1].transAxes, fontsize=12, va='top', ha='right')

# Plotting the force_test figure
axs[1, 0].plot(force_test[:, 3:6], force_test[:, 0:3], '.', markersize=10)
axs[1, 0].plot(np.arange(-11.5, 11.5, 0.01), np.arange(-11.5, 11.5, 0.01), linewidth=2, color='grey', linestyle='--')
axs[1, 0].set_xlabel(r'NEP$_{std}$ force (eV/$\AA$)', fontsize=10)
axs[1, 0].set_ylabel(r'NEP$_{200}$-ZBL force (eV/$\AA$)', fontsize=10)
axs[1, 0].tick_params(axis='both', labelsize=10)
axs[1, 0].legend(['fx', 'fy', 'fz'])
axs[1, 0].axis('tight')

# Calculate and display RMSE for forces
force_rmse = [calculate_rmse(force_test[:, i], force_test[:, i + 3]) for i in range(3)]
mean_force_rmse = np.mean(force_rmse) * 1000
axs[1, 0].text(0.5, 0.08, f'RMSE: {mean_force_rmse:.2f} meV/$\AA$', transform=axs[1, 0].transAxes, fontsize=10, verticalalignment='center')
axs[1, 0].text(-0.07, 1.03, "(c)", transform=axs[1, 0].transAxes, fontsize=12, va='top', ha='right')

# Plotting the virial figure
axs[1, 1].plot(stress_test[:, 6:12], stress_test[:, 0:6], '.', markersize=10)
axs[1, 1].plot(np.arange(-17, 37, 0.01), np.arange(-17, 37, 0.01), linewidth=2, color='grey', linestyle='--')
axs[1, 1].set_xlabel(r'NEP$_{std}$ stress (GPa)', fontsize=10)
axs[1, 1].set_ylabel(r'NEP$_{200}$-ZBL stress (GPa)', fontsize=10)
axs[1, 1].tick_params(axis='both', labelsize=10)
axs[1, 1].legend(['xx', 'yy', 'zz', 'xy', 'yz', 'zx'])
axs[1, 1].axis('tight')

# Calculate and display RMSE for stresses
stress_rmse = [calculate_rmse(stress_test[:, i], stress_test[:, i + 6]) for i in range(6)]
mean_stress_rmse = np.mean(stress_rmse) 
axs[1, 1].text(0.5, 0.08, f'RMSE: {mean_stress_rmse:.4f} GPa', transform=axs[1, 1].transAxes, fontsize=10, verticalalignment='center')
axs[1, 1].text(-0.07, 1.03, "(d)", transform=axs[1, 1].transAxes, fontsize=12, va='top', ha='right')

# Adjust layout for better spacing
#plt.tight_layout()
fig.subplots_adjust(top=0.968,bottom=0.088,left=0.086,right=0.983,hspace=0.22,wspace=0.24)

# Show the combined subplot
#plt.show()
plt.savefig('Figure_S2.png',dpi=300)
