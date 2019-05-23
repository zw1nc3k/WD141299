import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

# Data for plotting
t = np.arange(-5, 10)

fig, ax = plt.subplots()
ax.plot(np.exp(t))

ax.set(xlabel='x', ylabel='y',
       title='funkcja e^x')
ax.grid()
plt.xlim(-10, 10)
plt.ylim(0, 200)
print(np.exp(t))
plt.show()