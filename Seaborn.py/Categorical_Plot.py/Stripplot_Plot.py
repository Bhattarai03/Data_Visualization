import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)
sns.stripplot(x=data["day"],y=data["total_bill"],data=data)
plt.show()