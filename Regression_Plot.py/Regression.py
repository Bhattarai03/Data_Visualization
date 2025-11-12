import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv("tips.csv")
print(data)
print(data.columns)
sns.lmplot(x="total_bill",y="tip",data=data,hue="sex",palette="rainbow",markers=['o','v'])
plt.show()