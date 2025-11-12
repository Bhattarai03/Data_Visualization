# For adjusting the axes by yourselves.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,11)
y=x**2



fig=plt.figure(figsize=(10,5),dpi=200)
axis1=fig.add_axes([.1,.1,1,1])
axis1.plot(x,y)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
axis2=fig.add_axes([.1,.1,1,1])
axis2.plot(x,y)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
plt.show()

