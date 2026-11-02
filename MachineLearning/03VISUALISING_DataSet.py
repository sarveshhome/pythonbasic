from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data[iris.target==1][:5])
print(iris.data[iris.target==1, 0][:5])