import math
import matplotlib.pyplot as plt
import random

#поиск a
def coef_a(x, y, b):
    a = 0
    for i in range(len(x)):
        a += y[i] - b * x[i]
    return a / len(x)

#поиск b
def coef_b(x, y):
    avrgX = sum(x) / len(x)
    avrgY = sum(y) / len(y)
    num = 0
    denum = 0

    for i in range(len(x)):
        num += (y[i] - avrgY) * (x[i] - avrgX)
        denum += math.pow((x[i] - avrgX), 2)

    return num / denum


#регрессия
def reg(data):
    x = data[:-1]
    y = data[1:]
    b = coef_b(x, y)
    a = coef_a(x, y, b)
    res = []

    for i in data:
        rand = random.randint(0, 4)
        if rand % 2 == 0:
           res.append(a + b * i + random.uniform(0, 0.01 * i))
        else:
           res.append(a + b * i - random.uniform(0, 0.01 * i))

    fig, ax = plt.subplots()  
    ax.plot(data)
    ax.plot(res)
    plt.show()