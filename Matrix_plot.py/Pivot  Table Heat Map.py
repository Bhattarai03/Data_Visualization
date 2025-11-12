import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("flights.csv")
print(data.columns)

pvt_flight=data.pivot_table(values="passengers",index="month",columns="year")
print(pvt_flight)
sns.heatmap(pvt_flight)
plt.show()