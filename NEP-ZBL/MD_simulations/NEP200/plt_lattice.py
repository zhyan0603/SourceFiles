import numpy as np
import matplotlib.pyplot as plt
import sys
from cycler import cycler

# 设置自定义配色方案
custom_colors = ['#8FA2CD', '#F8BC7E', '#A9CA70', '#F09BA0', '#9D9EA3', '#B7B7EB']
plt.rcParams['axes.prop_cycle'] = cycler(color=custom_colors)

# 加载数据
data_h = np.loadtxt('./lattice/thermo_heating.out')
data_c = np.loadtxt('./lattice/thermo_cooling.out')

# 提取晶格常数
def process_data(data):
    return data[:, -3]/4, data[:, -2]/4, data[:, -1]/4

a_h, b_h, c_h = process_data(data_h)
a_c, b_c, c_c = process_data(data_c)

# 生成温度曲线
def generate_temperature(data, mode):
    n = len(data)
    if mode == 'heating':
        return np.linspace(600, 1200, n)  # 修正加热起始温度为600K
    elif mode == 'cooling':
        # 分段降温设置
        n1 = n // 4
        n2 = n // 2
        n3 = n - n1 - n2
        return np.concatenate([
            np.linspace(1200, 950, n1),
            np.linspace(950, 850, n2),
            np.linspace(850, 600, n3)
        ])

# 生成温度数组
temp_h = generate_temperature(data_h, 'heating')
temp_c = generate_temperature(data_c, 'cooling')

# 绘图设置
plt.figure(figsize=(4.5, 3), dpi=150)

# 绘制加热过程（600→1200K）
for y, alpha in zip([a_h, b_h, c_h], [1.0, 1.0, 1.0]):
    plt.plot(temp_h, y, color='#DD7C4F', alpha=alpha)

# 绘制冷却过程（1200→600K分段）
for y, alpha in zip([a_c, b_c, c_c], [1.0, 1.0, 1.0]):
    plt.plot(temp_c, y, color='#84BA42', alpha=alpha)

# 创建图例代理对象
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='#DD7C4F', lw=2, label='Heating'),
    Line2D([0], [0], color='#84BA42', lw=2, label='Cooling')
]

# 坐标轴标签和图例
plt.xlabel('Temperature (K)')
plt.ylabel('Lattice Constants (Å)')
plt.legend(handles=legend_elements, frameon=False)

plt.tight_layout()
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    plt.savefig('lattice.png', dpi=300, bbox_inches='tight')
else:
    plt.show()