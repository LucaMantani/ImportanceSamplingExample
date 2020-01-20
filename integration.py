import numpy as np
import matplotlib.pyplot as plt


def linear(x):
    return 2*x


def F(x):
    return x**2


N = 100

trials = 1000

bins = np.linspace(0, 1, 50)


# Monte Carlo integration with uniform distribution and with linear
integ_1 = []
integ_2 = []

for i in range(trials):

    uniform = np.random.rand(N)

    probabilities = linear(uniform)/sum(linear(uniform))

    lin = np.random.choice(uniform, size=N, p=probabilities)

    integ_1.append(sum(F(uniform))/uniform.shape[0])

    integ_2.append(sum(F(lin)/linear(lin))/lin.shape[0])


fig = plt.figure(figsize=(5, 5))

ax = fig.add_subplot(111)

ax.hist(integ_1, histtype='step', label='uniform')
ax.hist(integ_2, histtype='step', label='linear')

ax.set_xlabel("Integral")
ax.legend()

plt.show()

