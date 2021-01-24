import matplotlib.pyplot as plt
import numpy as np

############################################################
# 1. Catch the data file
############################################################
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
# put de data file in the variables
for line in data:
    split_data = line.split(",")
    if split_data != ['']:
        _x = float(split_data[0]) if split_data[0] != "" else 0
        _y = float(split_data[1]) if split_data[1] != "" else 0
        x.append(_x)
        y.append(_y)

x_axis = np.array(x)
y_axis = np.array(y)


# in this point we have the x and y values into arrays

############################################################
# 2. function to estimate the coefficients
############################################################
def estimate_coefficients(x_in, y_in):
    # number of observations/points
    n = np.size(x_in)
    print(n)

    # mean of x and y vector
    m_x, m_y = np.mean(x_in), np.mean(y_in)
    print(m_x)
    print(m_y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x_in) - n * m_y * m_x
    SS_xx = np.sum(x * x_in) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1


coefficients = estimate_coefficients(x_axis, y_axis)
print("Coeficientes:\na: " + str(coefficients[1]) + " b: " + str(coefficients[0]))
x_plot = x_axis
y_plot = coefficients[1] * x_plot + coefficients[0]
plt.plot(x_plot, y_plot)
# plot the data
plt.plot(x, y, "bo")

plt.xlabel("População")
plt.ylabel("Lucro")

plt.title("Regressão linear - Gradiente Descendente")

plt.show()
