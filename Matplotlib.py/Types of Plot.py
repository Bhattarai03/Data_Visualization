import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,11)
y=x**2
z=[22, 25, 30, 24, 29, 31,35, 35,36,26, 40, 38, 30, 33]
# For Scatter plotting
plt.scatter(x,y)
plt.title("X vs Y")
plt.xlabel("X-Axis")
plt.ylabel("y-Axis")

plt.show()

# For Histogram ; It is only univariant data set to find the statictics data of certain datasets.
plt.hist(z)

plt.show()


# For Box Plot
plt.boxplot(z)
plt.show()