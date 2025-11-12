import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data=pd.read_csv("tips.csv")
print(data)
sns.jointplot(x="total_bill",y="tip",data=data,kind="scatter")  
plt.show()  
sns.jointplot()