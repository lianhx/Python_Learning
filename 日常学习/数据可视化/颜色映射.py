"""
从起始颜色渐变到结束颜色，在可视化中，颜色映射用于突出数据的规律
例如，你可用较浅的颜色显示较小的值，并使用较深的颜色显示较大的值
"""
import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=10)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.show()

# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')
