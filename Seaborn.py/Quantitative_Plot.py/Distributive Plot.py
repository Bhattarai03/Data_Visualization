# Distributive plot is for visualizing the distribution of quantitative data i.e. age,salary etc.
# Distributive plot is not for qualitative dataset.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv("tips.csv")
print(data)
print(data["size"].unique())

plt.subplot(1,2,1)
sns.histplot(data["total_bill"],bins=20,kde=True)
plt.subplot(1,2,2)
sns.histplot(data["tip"],bins=20,kde=True)
plt.show()