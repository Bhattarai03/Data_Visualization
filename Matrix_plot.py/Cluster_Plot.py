import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)
dat=data[["total_bill","tip","size"]]
print(dat)
dat.corr()
print(dat.corr())
sns.clustermap(dat.corr())
plt.show()