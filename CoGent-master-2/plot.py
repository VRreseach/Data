import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/LongCombined/means/MeansLong.csv')
sns.boxplot(x="category", y="score", hue="VR", data=df, palette="Set3")
plt.show()
