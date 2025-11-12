import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,11)
y=x**2

fig=plt.figure()
ax=fig.add_axes([0.1,0.1,1,1])
ax.plot(y,x)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
plt.savefig("Basic-Plot.png")
plt.show()
