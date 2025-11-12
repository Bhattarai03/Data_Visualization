# Heat Map is used for showing the corelation between data in the  graphs.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)
dat=data[["total_bill","tip","size"]]
print(dat)
print(dat.corr())
sns.heatmap(dat.corr(),annot=True)   # Annot is for displaying the corr value in the graph.
plt.show()