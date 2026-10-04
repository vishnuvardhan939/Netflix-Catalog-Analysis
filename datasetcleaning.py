import pandas as pd

# Step 1: Load the raw dataset
df = pd.read_csv("D:/internship/BESANT TECHNOLOGIES/Netfilx_Dashboard/netflix_titles.csv")

# Step 2: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 3: Remove duplicates
df = df.drop_duplicates()

# Step 4: Handle missing values
# Fill categorical/text columns with 'Unknown'
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna('Unknown')

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include=['float64','int64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Step 5: Trim whitespace from string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Step 6: Final check - ensure no missing values remain
print("Missing values after cleaning:\n", df.isnull().sum())
assert df.isnull().sum().sum() == 0, "There are still missing values!"

# Step 7: Save the fully cleaned dataset
df.to_csv("D:/internship/BESANT TECHNOLOGIES/Netfilx_Dashboard/final_cleaned_netflix_dataset.csv", index=False)

print("✅ Dataset fully cleaned and saved as final_cleaned_netflix_dataset.csv")
