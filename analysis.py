import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sample_dataset.csv")

# Quick check
print("First rows:")
print(df.head())
print("\nColumns:")
print(df.columns)

# Total boxes by year
boxes_by_year = df.groupby("year")["boxes"].sum()
print("\nTotal boxes by year:")
print(boxes_by_year)

plt.figure(figsize=(8,5))
boxes_by_year.plot(marker="o")
plt.title("Antibiotic consumption by year")
plt.xlabel("Year")
plt.ylabel("Number of boxes")
plt.grid(True)
plt.tight_layout()
plt.savefig("antibiotics_by_year.png")
plt.show()

# Total boxes by region
boxes_by_region = df.groupby("region")["boxes"].sum().sort_values(ascending=False)
print("\nTotal boxes by region:")
print(boxes_by_region)

plt.figure(figsize=(10,5))
boxes_by_region.plot(kind="bar")
plt.title("Antibiotic consumption by region")
plt.xlabel("Region")
plt.ylabel("Number of boxes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("antibiotics_by_region.png")
plt.show()
