import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
fig, ax = plt.subplots()
print(fig, ax)
x_index = 3
colors = ['blue', 'red', 'green','yellow']
for label, color in zip(range(len(iris.target_names)), colors):
    ax.hist(iris.data[iris.target==label, x_index],
        label=iris.target_names[label],
        color=color)
    
ax.set_xlabel(iris.feature_names[x_index])
ax.legend(loc='upper right')
plt.show()