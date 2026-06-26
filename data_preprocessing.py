import pandas as pd
import numpy as np

# -----------------------------
# 1. Load dataset
# -----------------------------
file_path = "Salary_data.xlsx"
df = pd.read_excel(file_path)

# -----------------------------
# 2. Basic cleaning
# -----------------------------
df["Education Level"] = df["Education Level"].replace({
    "Bachelor's": "Bachelor's Degree",
    "Master's": "Master's Degree",
    "phD": "PhD"
})

# Keep only needed columns
cols = ["Age", "Gender", "Education Level", "Job Title", "Years of Experience", "Salary"]
df = df[cols].copy()
print(df[cols])# Convert numeric columns
for col in ["Age", "Years of Experience", "Salary"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# 3. Basic dataset information
# -----------------------------
print("========== BASIC INFO ==========")
print("Shape of dataset:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

# Drop missing values for analysis
df_clean = df.dropna().copy()

print("\nShape after removing missing values:", df_clean.shape)

# Keep only Male and Female for gender-based analysis
df_gender = df_clean[df_clean["Gender"].isin(["Male", "Female"])].copy()

# -----------------------------
# 4. Gender count
# -----------------------------
print("\n========== GENDER COUNT ==========")
print(df_gender["Gender"].value_counts())

print("\nGender percentage:")
print((df_gender["Gender"].value_counts(normalize=True) * 100).round(2))

# -----------------------------
# 5. Salary summary by gender
# -----------------------------
print("\n========== SALARY SUMMARY BY GENDER ==========")
print(
    df_gender.groupby("Gender")["Salary"].agg(
        count="count",
        mean="mean",
        median="median",
        std="std",
        min="min",
        max="max"
    ).round(2)
)

# -----------------------------
# 6. Salary summary by education level
# -----------------------------
print("\n========== SALARY SUMMARY BY EDUCATION LEVEL ==========")
print(
    df_gender.groupby("Education Level")["Salary"].agg(
        count="count",
        mean="mean",
        median="median",
        std="std"
    ).round(2).sort_values(by="mean", ascending=False)
)

# -----------------------------
# 7. Salary summary by experience
# -----------------------------
print("\n========== SALARY SUMMARY BY YEARS OF EXPERIENCE ==========")
print(
    df_gender.groupby("Years of Experience")["Salary"].agg(
        count="count",
        mean="mean",
        median="median"
    ).round(2).head(15)
)

# -----------------------------
# 8. Correlation matrix
# -----------------------------
print("\n========== CORRELATION ==========")
print(df_gender[["Age", "Years of Experience", "Salary"]].corr().round(3))

# -----------------------------
# 9. Salary bands for chi-square
# -----------------------------
df_gender["Salary Band"] = pd.qcut(df_gender["Salary"],q=4,
    labels=["Q1_Low", "Q2", "Q3", "Q4_High"])

print("\n========== GENDER x SALARY BAND TABLE ==========")
print(pd.crosstab(df_gender["Gender"], df_gender["Salary Band"]))

# -----------------------------
# 10. Matched groups count for paired t-test
# -----------------------------
# Create experience bands
bins = [-1, 2, 5, 10, 15, 20, np.inf]
labels = ["0-2", "3-5", "6-10", "11-15", "16-20", "20+"]
df_gender["Experience Band"] = pd.cut(df_gender["Years of Experience"], bins=bins, labels=labels)

# Group by Job Title + Education Level + Experience Band + Gender
grouped = df_gender.groupby(["Job Title", "Education Level", "Experience Band", "Gender"])["Salary"].mean().reset_index()

# Pivot to create male-female matched groups
paired = grouped.pivot_table(index=["Job Title", "Education Level", "Experience Band"],
    columns="Gender",values="Salary").dropna(subset=["Male", "Female"])

print("\n========== MATCHED GROUPS FOR PAIRED t-TEST ==========")
print("Number of valid matched groups:", paired.shape[0])

# Paired difference preview
paired["Difference"] = paired["Male"] - paired["Female"]

print("\nSummary of paired differences:")
print(paired["Difference"].agg(["count", "mean", "median", "std", "min", "max"]).round(2))
# Two-sample t-test on Salary by Gender
# Dataset file: Salary_Data.csv
