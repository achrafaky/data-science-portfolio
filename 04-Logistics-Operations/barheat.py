import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
file_path="flight_delays.csv"
data=pd.DataFrame()
data=pd.read_csv(file_path , index_col="Month", parse_dates=True)
sns.set_theme(style="darkgrid")
plt.figure(figsize=(16,6))
sns.barplot(x=data.index , y=data['AS'] , color='red' , label='Alask airlines' )
plt.ylabel("retard de vols en minutes")
plt.show()
plt.figure(figsize=(16,6))
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.xlabel("Correlation between different airlines")
plt.show()
#df is your dataframe




