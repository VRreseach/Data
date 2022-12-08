import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/WidePaper/means/MeansPaper.csv')
df1 = pd.melt(df, id_vars=['participant'], var_name='category', value_name='score')
print(df1.head)
df1.to_csv('data/LongPaper/MeansPaperLong.csv')