import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("        DATASET OF STATE CERTIFIED PUBLIC ACCOUNTANTS OF WASHINGTON\n    *******************************************************************")
df = pd.read_csv("C:\\Users\\HP\\Downloads\\Washington_State_Certified_Public_Accountants_20250306.csv")

df_cleaned = df.drop(columns=["Last Updated", "Preferred Name"])




print("\n\nObjective 4: Professional Development Tracking\n********************************************\n")
df['Original Issue Date'] = pd.to_datetime(df['Original Issue Date'], errors='coerce')
df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], errors='coerce')

df['License Duration (Years)'] = (df['Expiration Date'] - df['Original Issue Date']).dt.days / 365.25

df = df[df['License Duration (Years)'] > 0]

print("\n\n📈 License Duration Summary (in years):\n*****************************************\n")
print(df['License Duration (Years)'].describe())
avg_duration_by_city = df.groupby('City')['License Duration (Years)'].mean().sort_values(ascending=False).head(10)
print("\n\nTop 10 Cities by Average License Duration:\n********************************************\n")
print(avg_duration_by_city)

df['Expiration Year'] = df['Expiration Date'].dt.year
plt.figure(figsize=(10, 6))
sns.histplot(df['License Duration (Years)'], bins=30, kde=True, color="#009688")
plt.title("Distribution of CPA License Durations")
plt.xlabel("Years Licensed")
plt.ylabel("Number of CPAs")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(x=df['License Duration (Years)'], color="#00BCD4")
plt.title("Boxplot of CPA License Durations")
plt.xlabel("Years Licensed")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df,x='Expiration Year',y='License Duration (Years)',hue='Status',alpha=0.6,palette='husl')
plt.title("License Duration vs. Expiration Year")
plt.xlabel("Expiration Year")
plt.ylabel("License Duration (Years)")
plt.legend(title="Status", fontsize=9, title_fontsize=10, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
