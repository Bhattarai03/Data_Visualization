import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,11)
y=x**2
print(x,y)
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
plt.plot(x,y)

plt.subplot(2,2,2)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
plt.plot(y,x)

plt.subplot(2,2,3)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
plt.plot(x**2,y*3)

plt.subplot(2,2,4)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")
plt.plot(x*1.5,y*0.5)
plt.show()