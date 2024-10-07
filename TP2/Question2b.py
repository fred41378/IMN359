import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(-50.0, 50.0, 0.01)
y1 = 2*np.cos(t)
y2 = np.cos(t/3)
y3 = 3*np.cos(t/5)
ys = 2*np.cos(t)+np.cos(t/3)+3*np.cos(t/5)

fig, ax = plt.subplots()
ax.plot(t, y1, label='2cos(t)')
ax.plot(t, y2, label='cos(t/3)')
ax.plot(t, y3, label='3cos(t/5)')
ax.plot(t, ys, label='2cos(t)+cos(t/3)+3cos(t/5)')

ax.set(xlabel='Temps', ylabel='Amplitude',
       title='Question 2 b')
ax.legend()
ax.grid()
plt.show()