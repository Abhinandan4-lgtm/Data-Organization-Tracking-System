import pandas as pd

df = pd.read_csv("data/raw_data.csv")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Standardize names
df["Name"] = df["Name"].str.title()

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("\nCleaned Data")
print(df)

# Create department summary
summary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department")
print(summary)