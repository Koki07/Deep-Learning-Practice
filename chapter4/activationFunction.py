import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y軸の範囲を指定


plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y軸の範囲を指定


plt.show()


def relu(x):
    return np.maximum(0, x)  # 0 か x のどちらか大きい方を出力する


y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y軸の範囲を指定
# plt.show()
