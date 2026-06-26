import pandas as pd
import numpy as np
from scipy.stats import f

#Load dataset
df = pd.read_excel("Salary_data.xlsx")
# Clean
df["Gender"] = df["Gender"].str.strip()
# Extract data
male = df[df["Gender"] == "Male"]["Salary"].dropna().values
female = df[df["Gender"] == "Female"]["Salary"].dropna().values
#Variances
var_m = np.var(male, ddof=1)
var_f = np.var(female, ddof=1)
print("Male variance:", var_m)
print("Female variance:", var_f)

# Right-tailed test
F = var_m / var_f
df1 = len(male) - 1
df2 = len(female) - 1
alpha = 0.05
F_critical = f.ppf(1 - alpha, df1, df2)
p_value = 1 - f.cdf(F, df1, df2)
print("F:", F)
print("F-critical:", F_critical)
print("p-value:", p_value)
if F > F_critical:
    print("Reject H0: Male variance is greater")
else:
    print("Fail to reject H0")

# Left-tailed test
F = var_m / var_f
df1 = len(male) - 1
df2 = len(female) - 1
alpha = 0.05
F_critical = f.ppf(alpha, df1, df2)
p_value = f.cdf(F, df1, df2)
print("F:", F)
print("F-critical:", F_critical)
print("p-value:", p_value)
if F < F_critical:
    print("Reject H0: Male variance is smaller")
else:
    print("Fail to reject H0")

# Two-tailed test
# Always put larger variance on top
if var_m > var_f:
    F = var_m / var_f
    df1 = len(male) - 1
    df2 = len(female) - 1
else:
    F = var_f / var_m
    df1 = len(female) - 1
    df2 = len(male) - 1
alpha = 0.05
F_critical = f.ppf(1 - alpha/2, df1, df2)
p_value = 2 * (1 - f.cdf(F, df1, df2))
print("F:", F)
print("F-critical:", F_critical)
print("p-value:", p_value)
if F > F_critical:
    print("Reject H0")
else:
    print("Fail to reject H0")