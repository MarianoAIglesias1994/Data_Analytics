import numpy as np
import matplotlib.pyplot as plt

# A workaround is used to get the desired shape, adding two extra points not shown.
x = [-1, 1, 2, 3, 5]
y = [0, 0.5, 0.8, 1.0, 1.0]

fig, ax = plt.subplots(figsize=(8, 4))

ax.set_xlim([0, 4])
ax.set_ylim([0, 1.1])

ax.step(x, y, where='post', label='F_x')
ax.plot(x, y, 'C2o', alpha=0.5)

ax.grid(True)
ax.set_title('Cumulative distribution function for the example')
ax.legend(title='Cumulative distribution function')
ax.set_xlabel('Values')
ax.set_ylabel('Likelihood of occurrence')
plt.show()

fig.savefig('./exercise_1.png', transparent=False, dpi=80, bbox_inches='tight')