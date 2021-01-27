import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

data = pd.read_csv('data2.txt')
X0 = data.iloc[:, 0]
X1 = data.iloc[:, 1]
Y = data.iloc[:, 2]

# número de features
theta_0 = 1
theta_1 = 1
theta_2 = 1

alpha = 0.0000001  # taxa de aprendizado
epochs = 100  # número de iterações
m = float(len(X0))  # números de elementos de X

loss_function_values = []

for i in range(epochs):
    Y_pred = theta_2 * X1 + theta_1 * X0 + theta_0  # Valor previsto para Y
    D_a1 = (-1 / m) * sum(X0 * (Y - Y_pred))  # derivada do theta_2
    D_a2 = (-1 / m) * sum(X1 * (Y - Y_pred))  # derivada do theta_1
    D_y = (-1 / m) * sum(Y - Y_pred)  # Derivada do theta_0
    theta_1 = theta_1 - (alpha * D_a1)  # Atualiza o theta_2
    theta_2 = theta_2 - (alpha * D_a2)  # Atualiza o theta_1
    theta_0 = theta_0 - (alpha * D_y)  # Atualiza o theta_0
    err = 0
    for index, e in enumerate(X0):
        err = err + (Y_pred[index] - Y[index]) ** 2
    loss_function_values.append(1 / (2 * m) * err)

print("Theta 2: " + str(theta_2) + "\nTheta 1: " + str(theta_1) + "\nTheta 0: " + str(theta_0))

# Criando a função Y
Y_pred = theta_2 * X1 + theta_1 * X0 + theta_0  # Valor previsto para Y

# Plotando os valores com a regressão
ax = plt.axes(projection='3d')
ax.scatter3D(X0, X1, Y, c=Y)
# start | lenght | end
ax.plot3D([min(X0), max(X0)], [min(X1), max(X1)], [min(Y_pred), max(Y_pred)], color='red')  # regression line

plt.show()