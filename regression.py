import matplotlib.pyplot as plt

data_file = '../data1.txt'
data_readed = open(data_file, 'r', encoding='utf8')

try:
    data = data_readed.read().split('\n')
    data_readed.close()
except Exception as ex:
    print('Error while parsing csv')
    data_readed.close()
    exit(-1)

x = []
y = []

for line in data:
    splitted = line.split(',')
    _x = float(splitted[0]) if splitted[0] is not '' else 0
    _y = float(splitted[1]) if splitted[1] is not '' else 0
    x.append(_x)
    y.append(_y)

plt.plot(x, y, 'bo')

plt.xlabel('Population')
plt.ylabel('Profit')

plt.title('Graph')

plt.show()
