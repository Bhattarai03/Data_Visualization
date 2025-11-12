# Box PLot is very important for showing the statical data.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)
fig=plt.figure()
sns.boxplot(y=data["tip"],x=data["day"],data=data,palette="rainbow")
plt.savefig("Box_plot")
plt.show()
