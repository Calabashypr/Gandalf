import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath

# 定义函数
def complex_function(x, y):
    z = cmath.sin(abs(x) + y) / cmath.sqrt(cmath.cos(abs(x + y)))
    return z

# 创建数据点
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.array([complex_function(xi, yi) for xi, yi in zip(X.flatten(), Y.flatten())]).reshape(X.shape)

# 绘制曲面图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z.real, cmap='viridis')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加标题
plt.title('z = sin(|x| + y) / sqrt(cos(|x+y|))')

# 显示图形
plt.show()
