import  pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 
insurance_file_path="insurance.csv"
data=pd.DataFrame()
insurance_data=pd.read_csv(insurance_file_path , index_col="age")
sns.set_theme(style="darkgrid")
plt.figure(figsize=(16,6))
plt.figure(figsize=(10, 6))

# X = BMI (Poids), Y = Charges (Prix)
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

plt.title("Relation brute : Poids vs Prix")
plt.show()
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
plt.title("Relation avec distinction Fumeur / Non-Fumeur : Poids vs Prix")
plt.show()
sns.regplot(x=insurance_data['bmi'] , y=insurance_data['charges'])
plt.title("Relation avec ligne de tendance : Poids vs Prix")
plt.show()
sns.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)
plt.title("Relation avec ligne de tendance et distinction Fumeur / Non-Fumeur : Poids vs Prix")
plt.show()
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
plt.title("Comparaison des prix : Fumeur vs Non-Fumeur")
plt.show()
