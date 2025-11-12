# Voilin Plot = Box plot+kde
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)
fig=plt.figure()
sns.violinplot(y=data["tip"],x=data["day"],data=data,palette="rainbow")

plt.show()