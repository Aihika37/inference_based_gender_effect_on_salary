import pandas as pd
import statsmodels.api as sm
data=pd.read_excel("Salary_data.xlsx")

#converting the categorical variables to numeric
data["Male"] = (data["Gender"] == "Male").astype(int)
data = pd.get_dummies(data, columns=["Education Level", "Job Title"], drop_first=True)
data = data.drop(columns=["Gender"])
data = data.dropna() # dropping null values

X = data.drop(columns=["Salary"])   # independent variables
X = X.astype(float)
y = data["Salary"]  # dependent variable
X = sm.add_constant(X)  # adds intercept
model = sm.OLS(y, X).fit()
print(model.summary())


