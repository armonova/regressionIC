import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

data_file = "data2.txt"
data_read = open(data_file, "r", encoding="utf8")

try:
    data = data_read.read().split("\n")
    data_read.close()
except Exception as ex:
    print("Error while parsing csv")
    data_read.close()
    exit(-1)

x = []
y = []
z = []

# put de data file in variables
for line in data:
    splitted = line.split(",")
    if splitted != ['']:
        _x = float(splitted[0]) if splitted[0] != "" else 0
        _y = float(splitted[1]) if splitted[1] != "" else 0
        _z = float(splitted[2]) if splitted[2] != "" else 0
        x.append(_x)
        y.append(_y)
        z.append(_z)

x_axis = np.array(x).reshape((-1, 1))
y_axis = np.array(y)
z_axis = np.array(z)

# plot the data

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(x_axis, y_axis, z_axis, c=z_axis, cmap='Greens')


# Axes3D.plot_wireframe(x_axis, y_axis, z_axis)
#
ax.set_xlabel('Tamanho da casa (mº)')
ax.set_ylabel('Nº quartos')
ax.set_zlabel('Preço')

# plt.xlabel("População")
# plt.ylabel("Lucro")

# plt.title("Regressão linear - Gradiente Descendente")

plt.show()
