import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create customer churn dataset
data = {
    "CustomerID": range(1, 16),
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],
    "Tenure": [
        2, 12, 5, 24, 1, 36, 8, 18, 3, 48,
        6, 30, 10, 42, 4
    ],
    "MonthlyCharges": [
        80, 60, 90, 50, 95, 45, 85, 55, 100, 40,
        88, 52, 78, 48, 92
    ],
    "Contract": [
        "Monthly", "Yearly", "Monthly", "Yearly",
        "Monthly", "Yearly", "Monthly", "Yearly",
        "Monthly", "Yearly", "Monthly", "Yearly",
        "Monthly", "Yearly", "Monthly"
    ],
    "Churn": [
        "Yes", "No", "Yes", "No", "Yes",
        "No", "Yes", "No", "Yes", "No",
        "Yes", "No", "Yes", "No", "Yes"
    ]
}

df = pd.DataFrame(data)

print("CUSTOMER CHURN DATASET")
print(df)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Introduce a missing value to demonstrate handling
df.loc[2, "MonthlyCharges"] = np.nan

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numerical values using median
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].median()
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 3. Remove duplicate records
df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df.shape)

# 4. Summary statistics using Pandas
print("\nSUMMARY STATISTICS")
print(df.describe())

# 5. Statistical analysis using NumPy
charges = df["MonthlyCharges"].to_numpy()

print("\nNUMPY ANALYSIS")
print("Mean Monthly Charges:", np.mean(charges))
print("Median Monthly Charges:", np.median(charges))
print("Standard Deviation:", np.std(charges))
print("Minimum Charges:", np.min(charges))
print("Maximum Charges:", np.max(charges))

# 6. Customer churn count and percentage
print("\nCUSTOMER CHURN COUNT")
print(df["Churn"].value_counts())

print("\nCUSTOMER CHURN PERCENTAGE")
print(df["Churn"].value_counts(normalize=True) * 100)

# 7. Visualize churn distribution
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 8. Churn by contract type
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 9. Tenure vs churn
sns.boxplot(data=df, x="Churn", y="Tenure")
plt.title("Customer Tenure vs Churn")
plt.xlabel("Churn Status")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.show()

# 10. Monthly charges vs churn
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges vs Churn")
plt.xlabel("Churn Status")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

# 11. Correlation heatmap
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8, 5))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 12. Churn rate by contract
print("\nCHURN RATE BY CONTRACT (%)")
churn_rate = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(churn_rate)

print("\nEDA COMPLETED SUCCESSFULLY!")