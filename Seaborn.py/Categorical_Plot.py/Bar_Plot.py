import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)

# In bar plot, x axis must contain categorical data and y axis must contain quantitative data

sns.barplot(x=data["sex"],y=data["total_bill"])  # Estimator = :mean (by default)
plt.show()

sns.barplot(x=data["sex"],y=data["total_bill"],estimator=np.sum)
plt.show()