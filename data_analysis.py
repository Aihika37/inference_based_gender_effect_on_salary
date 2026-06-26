import pandas as pd
import openpyxl

df = pd.read_excel("Salary_data.xlsx")

print(df.info())
print(df.describe())
print(df.isnull().sum())
import matplotlib.pyplot as plt

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
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Salary_data.xlsx")

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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Salary_data.xlsx")   # change path if needed

# Convert categorical variables to numeric (important for correlation)
df_encoded = df.copy()

# Example: encoding Gender (adjust if needed)
df_encoded['Gender'] = df_encoded['Gender'].map({'Male': 0, 'Female': 1})

# Convert other categorical columns if present
df_encoded = pd.get_dummies(df_encoded, drop_first=True)

# Compute correlation matrix
corr_matrix = df_encoded.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")

plt.title("Correlation Heatmap of Dataset")
plt.show()