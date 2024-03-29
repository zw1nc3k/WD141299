import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 6, endpoint=False)
print(x)
plt.subplot(3, 1, 1)
plt.plot(x, np.power(x, 2), 'r')
plt.grid(True)
plt.xlim(-5, 5)
plt.subplot(3, 1, 2)
plt.plot(x, np.power(x,3), 'g')
plt.grid(True)
plt.xlim(-5, 5)
plt.subplot(3, 1, 3)
plt.plot(x, np.power(x, 2), 'r', x, np.power(x, 3), 'g')
plt.grid(True)
plt.xlim(-5, 5)
plt.savefig("fig3.png", dpi=72)
plt.show()
