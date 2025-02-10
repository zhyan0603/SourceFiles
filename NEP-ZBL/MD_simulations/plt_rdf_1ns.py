import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

custom_colors = ['#8FA2CD', '#F8BC7E', '#A9CA70', '#F09BA0', '#9D9EA3', '#B7B7EB', '#F27873', '#B384BA']

# 设置默认配色
plt.rcParams['axes.prop_cycle'] = cycler(color=custom_colors)

data_200 = np.loadtxt('./NEP200/rdf/800K/rdf_1ns.out', skiprows=1)
data_std = np.loadtxt('./NEPstd/rdf/800K/rdf_1ns.out', skiprows=1)

plt.figure(figsize=(4.5, 3), dpi=150)

# 主图
plt.plot(data_200[:, 0], data_200[:, 2], label=r"NEP$_{200}$")  
plt.xlim(-0.5, 6.1)
plt.ylim(-0.1, 3.8)
plt.xlabel(r'r($\AA$)')
plt.ylabel('g(r)')
plt.legend(loc='upper left', fontsize=8)
plt.tight_layout()

# 添加插图
ax_inset = plt.axes([0.23, 0.32, 0.20, 0.35])  # 位置和大小 (左, 下, 宽, 高)
ax_inset.plot(data_200[:, 0], data_200[:, 2])
ax_inset.set_xlim(0.2, 0.8)
ax_inset.set_ylim(-0.01, 0.05)
#ax_inset.set_xticks(np.linspace(0.2, 0.8, 4))
#ax_inset.set_yticks(np.linspace(0, 0.1, 4))
ax_inset.tick_params(labelsize=7.4)
#ax_inset.set_title("Zoom In", fontsize=7)

# 显示或保存图片
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('Figure_S4_rdf_1ns.png', dpi=500)
else:
    plt.show()