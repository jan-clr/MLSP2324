import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np


def J(w):
    return 5 * w[0] ** 2 + w[1] ** 2


def grad_J(w):
    return np.array([10 * w[0], 2 * w[1]])


def GradientDescent(w, eta, grad):
    grd = grad(w)
    print(w, grd)
    w = w - eta * grd
    return w


def main():
    eta = 0.01
    min_delta = 0.0001
    w = [np.array([6, 6])]
    for i in range(500):
        w.append(GradientDescent(w[-1], eta, grad_J))

    plot = plt.figure()
    ax = plot.add_subplot(111)
    w_1 = np.linspace(-.1, 7.5, 1000)
    w_2 = np.linspace(-.1, 7.5, 1000)
    W_1, W_2 = np.meshgrid(w_1, w_2)
    Z = J([W_1, W_2])
    ax.contourf(W_1, W_2, Z, 20, cmap='RdYlGn')
    ax.contour(W_1, W_2, Z, 20, colors='black', alpha=0.5, linewidths=0.5)
    ax.set_xlabel('w1')
    ax.set_ylabel('w2')
    ax.set_title('Contour plot of J(w)')
    ax.plot([w[i][0] for i in range(len(w))], [w[i][1] for i in range(len(w))], '-', color='black', markersize=0.5)
    ax.plot([w[i][0] for i in range(len(w))], [w[i][1] for i in range(len(w))], '.', color='blue', markersize=2)
    plt.show()


if __name__ == '__main__':
    main()
