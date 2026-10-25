import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
#print(iris.keys())          # सारे उपलब्ध keys दिखाएगा
#print(iris.data)            # फीचर्स का डेटा
#print(iris.target)          # टारगेट लेबल्स (0,1,2)
#print(iris["target_names"])
#print(iris.target_names)    # ['setosa' 'versicolor' 'virginica']
#print(iris.feature_names)   # फीचर्स के नाम
# print(iris.DESCR)           # डेटासेट का पूरा डिस्क्रिप्शन


# n_samples, n_features = iris.data.shape
# print('Number of samples:', n_samples)
# print('Number of features:', n_features)
# the sepal length, sepal width, petal length and petal width of t
#he first sample (first flower)
# print(iris.data)

#iris.data[[12, 26, 89, 114]]
#print(iris.data[[12, 26, 89, 114]])


print(np.bincount(iris.target))
