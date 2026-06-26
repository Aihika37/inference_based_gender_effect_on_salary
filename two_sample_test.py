import pandas as pd
import numpy as np
from scipy import stats

# 1. Load the dataset
file_path = "Salary_data.xlsx"
df = pd.read_excel(file_path)

# Make sure Salary is numeric
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df = df.dropna(subset=["Salary"])

#Split into two groups
male_salary = df[df["Gender"] == "Male"]["Salary"]
female_salary = df[df["Gender"] == "Female"]["Salary"]

# -----------------------------
# 4. Descriptive statistics
# -----------------------------
print("----- Sample Sizes -----")
print(f"Male count   : {len(male_salary)}")
print(f"Female count : {len(female_salary)}")

print("\n----- Descriptive Statistics -----")
print(f"Male mean salary   : {male_salary.mean():.2f}")
print(f"Female mean salary : {female_salary.mean():.2f}")
print(f"Male std dev       : {male_salary.std(ddof=1):.2f}")
print(f"Female std dev     : {female_salary.std(ddof=1):.2f}")

#Two-sample t-test
# Welch's t-test (does not assume equal variances)
t_stat, p_two_tailed = stats.ttest_ind(male_salary, female_salary, equal_var=False)

print("\n----- Welch Two-Sample t-Test -----")
print(f"t-statistic  : {t_stat:.6f}")
print(f"Two-tailed p : {p_two_tailed:.6f}")

#One-tailed p-values
# H1: mean(Male) > mean(Female)
if t_stat > 0:
    p_right = p_two_tailed / 2
else:
    p_right = 1 - (p_two_tailed / 2)

# H1: mean(Male) < mean(Female)
if t_stat < 0:
    p_left = p_two_tailed / 2
else:
    p_left = 1 - (p_two_tailed / 2)

print("\n----- One-Tailed p-values -----")
print(f"Right-tailed p-value [H1: mu_male > mu_female] : {p_right:.6f}")
print(f"Left-tailed p-value  [H1: mu_male < mu_female] : {p_left:.6f}")


#95% confidence interval for (mu_male - mu_female)
mean_m = male_salary.mean()
mean_f = female_salary.mean()
var_m = male_salary.var(ddof=1)
var_f = female_salary.var(ddof=1)
n_m = len(male_salary)
n_f = len(female_salary)

# Mean difference
mean_diff = mean_m - mean_f

# Standard error
se = np.sqrt(var_m / n_m + var_f / n_f)

# Welch-Satterthwaite degrees of freedom
df_welch = ((var_m / n_m + var_f / n_f) ** 2) / (((var_m / n_m) ** 2) / (n_m - 1)
    + ((var_f / n_f) ** 2) / (n_f - 1))
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha / 2, df_welch)

#finding confidence intervals
ci_low = mean_diff - t_critical * se
ci_high = mean_diff + t_critical * se

print("\n----- 95% Confidence Interval -----")
print(f"Mean difference : {mean_diff:.2f}")
print(f"95% CI          : ({ci_low:.2f}, {ci_high:.2f})")


#Decision at 5% significance level
print("\n----- Decision at alpha = 0.05 -----")

# Two-tailed test
if p_two_tailed < 0.05:
    print("Two-tailed test: Reject H0")
else:
    print("Two-tailed test: Fail to reject H0")

# Right-tailed test: H1 mu_male > mu_female
if p_right < 0.05:
    print("Right-tailed test: Reject H0")
else:
    print("Right-tailed test: Fail to reject H0")

# Left-tailed test: H1 mu_male < mu_female
if p_left < 0.05:
    print("Left-tailed test: Reject H0")
else:
    print("Left-tailed test: Fail to reject H0")