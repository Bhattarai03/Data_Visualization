# Count plot is for counting the specific categprical data through graphs.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data=pd.read_csv("tips.csv")
print(data)

sns.countplot(x=data["sex"],hue=data["smoker"])
plt.show()