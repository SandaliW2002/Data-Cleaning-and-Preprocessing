
import pandas as pd

df = pd.read_csv("data.csv")

print("Before cleaning:")
print(df.head())

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())
df = df.drop_duplicates()

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.lower().str.strip()

print("\nAfter cleaning:")
print(df.head())

df.to_csv("cleaned_dataset.csv", index=False)
print("\nSaved as 'cleaned_dataset.csv'")

