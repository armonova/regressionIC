import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

data_file = "data1.txt"
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

# put de data file in variables
for line in data:
    splitted = line.split(",")
    if splitted != ['']:
        _x = float(splitted[0]) if splitted[0] != "" else 0
        _y = float(splitted[1]) if splitted[1] != "" else 0
        x.append(_x)
        y.append(_y)

x_axis = np.array(x).reshape((-1, 1))
y_axis = np.array(y)


def calculate_cost(x_in, theta0, theta1):
    return theta0 + (theta1 * x_in)


def descent_gradient(x_in, y_in, theta0, theta1, learning_rate=0.01, iterations=1000):
    costs = []
    m = len(y)
    for i in range(iterations):
        new_theta0 = theta0 - learning_rate * (1 / m) * (calculate_cost(x_in, theta0, theta1) - y_in)
        new_theta1 = theta1 - learning_rate * (1 / m) * (calculate_cost(x, theta0, theta1) - y_in) * x_in

        theta0 = new_theta0
        theta1 = new_theta1
        costs[i] = (theta0, theta1)
    return theta0, theta1


model = LinearRegression().fit(x_axis, y_axis)
coefficient = model.score(x_axis, y)
print("𝑓(𝑥) = 𝑏₀ + 𝑏₁𝑥")
print("\nCoeficiente de determinação (R²): ", coefficient)
print("Intercessão no eixo Y (theta0): ", model.intercept_)
print("Inclinação da reta (theta1): ", model.coef_[0])
print(f"\n𝑓(𝑥) = {model.intercept_} + {model.coef_[0]}𝑥")


x_plot = np.linspace(0, 24, 100)
y_plot = (model.coef_[0] * x_plot) + model.intercept_
plt.plot(x_plot, y_plot)

# plot the data
plt.plot(x, y, "bo")

plt.xlabel("População")
plt.ylabel("Lucro")

plt.title("Regressão linear - Gradiente Descendente")

plt.show()
