import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Salary_data.xlsx")

plt.hist(df['Salary'], bins=20)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

df.boxplot(column='Salary', by='Gender')
plt.title("Salary Distribution by Gender")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Salary")
plt.show()

df.boxplot(column='Years of Experience', by='Gender')
plt.title("Experience Distribution by Gender")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Years of Experience")
plt.show()

job_counts = df['Job Title'].value_counts()
plt.pie(job_counts)
plt.title("Overall Job Title Distribution")
plt.show()

df_encoded = df.copy()
df_encoded['Gender'] = df_encoded['Gender'].map({'Male': 0, 'Female': 1})
df_encoded = pd.get_dummies(df_encoded, drop_first=True)
corr_matrix = df_encoded.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Dataset")
plt.show()
