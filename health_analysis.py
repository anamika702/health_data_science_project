import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('diabetes_01.csv')
print("Data Info:")
print(data.info())
print("\nData Head:")
print(data.head())
print("\nMissing Values in Data:")
print(data.isnull().sum())

data.drop_duplicates(inplace=True)
print("\nData Description:")
print(data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data['BMI'], kde=True)
plt.title("Distribution of BMI")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

selected_columns = ['BMI', 'PhysActivity','Diabetes_binary']
sns.pairplot(data[selected_columns], hue='Diabetes_binary')
plt.suptitle("Pairplot of Selected Health Indicators vs. Diabetes Status", y=1.02)
plt.show()
