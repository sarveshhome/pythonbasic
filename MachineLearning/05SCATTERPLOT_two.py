import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
fig, ax = plt.subplots()
x_index = 3
y_index = 0
colors = ['blue', 'red', 'green']

for label, color in zip(range(len(iris.target_names)), colors):
    ax.scatter(iris.data[iris.target==label, x_index],
        iris.data[iris.target==label, y_index],
        label=iris.target_names[label],
        c=color)
ax.set_xlabel(iris.feature_names[x_index])
ax.set_ylabel(iris.feature_names[y_index])
ax.legend(loc='upper left')
plt.show()