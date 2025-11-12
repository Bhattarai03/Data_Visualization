import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv("tips.csv")
print(data)
sns.rugplot(data["total_bill"])
plt.show()