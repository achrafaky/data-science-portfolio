from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path="museum_visitors.csv"
data=pd.DataFrame()
data=pd.read_csv(file_path , index_col="Date", parse_dates=True)
'''sns.set_theme(style="darkgrid")
plt.figure(figsize=(16,6))
sns.lineplot(data=data , linewidth=2.5)
plt.title("museum visitors over time")
plt.xlabel("Year")
plt.ylabel("number of visitors")
plt.show()'''
plt.figure(figsize=(16,6))
sns.lineplot(data=data[['Avila Adobe']] , linewidth=2.5)
sns.lineplot(data=data['Chinese American Museum'] , linewidth=2.5)
plt.title("Avila Adobe vs Chinese American Museum")
plt.xlabel("Year")
plt.ylabel("number of visitors")
plt.legend()
plt.show()