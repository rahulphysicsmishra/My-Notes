from sklearn import datasets
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt



iris = datasets.load_iris()
# print(iris.target_names)
# print(iris.data, 'target->', iris.target)
x = iris.data[:, 0] # sepal length
y = iris.data[:, 1] # sepal width
x1 = iris.data[:,2] # petal length
y1 = iris.data[:, 3] # petal width

species = iris.target # species
x_min, x_max = x.min() - 0.5, x.max() + 0.5
y_min, y_max = y.min() - 0.5, y.max() + 0.5

x1_min, x1_max = x1.min() - 0.5, x1.max() + 0.5
y1_min, y1_max = y1.min() - 0.5, y1.max() + 0.5

plt.figure()
#plt.scatter(x, y,c= species)
plt.scatter(x1, y1, c=species)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('Iris Dataset - Classification By Pepal Size')
plt.xlim(x1_min, x1_max)
plt.ylim(y1_min, y1_max)
plt.legend(['Iris silky',' virginica Iris',"Iris versicolor"], loc=2)
# plt.xticks(())
# plt.yticks(())
plt.show()

