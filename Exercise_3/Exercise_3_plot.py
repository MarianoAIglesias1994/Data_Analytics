import numpy as np
import matplotlib.pyplot as plt

t = 645 # Total number of coins
m_array = np.zeros(t) # Possible number of coins Morgan receives

for p in range(1,t):
	m_array[p] = t % p

# Morgan best case. 
optimum_m = np.amax(m_array)
optimum_p = float(np.where(m_array == np.amax(m_array))[0])
optimum_c = (t - optimum_m)/optimum_p

# This happens when Morgan chooses **p** = 323 pirates,
# each one with only **c** = 1 coin, and he gets **m** = 322 coins.
print(optimum_m)
print(optimum_p)
print(optimum_c)

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(m_array, 'bo', alpha=0.1)
# The optimum solution is highlighted 
ax.plot(optimum_p, optimum_m, 'r*', alpha=0.5, markersize=12)

ax.grid(True)
ax.set_title('Possible solutions to Morgan\'s problem')
ax.set_xlabel('$p$: the number of pirates selected by Morgan')
ax.set_ylabel('$m$: the number of coins Morgan receives')
plt.show()

fig.savefig('./exercise_3.png', transparent=False, dpi=80, bbox_inches='tight')