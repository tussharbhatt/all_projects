from sklearn import datasets
import numpy


iris=datasets.load_iris()

x=iris.data
y=iris.target

print(x)