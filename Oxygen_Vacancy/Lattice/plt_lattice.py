import matplotlib.pyplot as plt
import numpy as np

# 读取数据
data = np.loadtxt('./lattice_gpumd.txt')
data_exp = np.loadtxt('./lattice_chenyan.txt')

# 提取数据
temperature = data[:, 0]
a_values = data[:, 1]
b_values = data[:, 2]
ab = (a_values + b_values)/2
c_values = data[:, 3]

temperature_exp = data_exp[:, 1]
b_values_exp = data_exp[:, 2]
c_values_exp = data_exp[:, 3]


# 创建 1x2 的子图
fig, ax1 = plt.subplots(figsize=(6, 3.5), dpi=150)

# 左边的子图：abc晶格参数
ax1.plot(temperature, ab, label='Latt a', marker='o', color='C2')
ax1.plot(temperature, c_values, label='Latt c', marker='o', color='C3')


ax1.scatter(temperature_exp, b_values_exp, label='Exp.', marker='o', c='none', edgecolors='C4')
ax1.scatter(temperature_exp, c_values_exp, c='none', marker='o', edgecolors='C4')


ax1.set_xlabel('Temperature (K)', fontsize=12)
ax1.set_ylabel(r'Lattice Parameter ($\AA$)', color='black', fontsize=12)
ax1.tick_params(axis='y', labelcolor='black', labelsize=12)
ax1.tick_params(axis='x', labelcolor='black', labelsize=12)
ax1.legend(loc='best', fontsize=11)

plt.subplots_adjust(top=0.977,bottom=0.138,left=0.125,right=0.99,hspace=0.2,wspace=0.2)

# 显示图形
#plt.show()
plt.savefig('Figure3_lattice.pdf')
