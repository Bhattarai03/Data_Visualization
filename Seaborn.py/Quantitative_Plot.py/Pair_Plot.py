# Pair plot is for showing graphs of each and every numerical datasets

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




data=pd.read_csv("tips.csv")
print(data)
sns.pairplot(data,hue="size",palette="rainbow")
plt.show()