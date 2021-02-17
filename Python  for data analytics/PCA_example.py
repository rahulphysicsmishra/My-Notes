from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()
species = iris.target
x_reduced = PCA(n_components=3).fit_transform(iris.data)

# Scatterplot
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title("Iris Dataset By PCA", size=100)
ax.scatter(x_reduced[:, 0], x_reduced[:, 1], x_reduced[:, 2], c=species)
ax.set_xlabel('First eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Third eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
plt.show()
