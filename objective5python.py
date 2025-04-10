import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("        DATASET OF STATE CERTIFIED PUBLIC ACCOUNTANTS OF WASHINGTON\n    *******************************************************************")
df = pd.read_csv("C:\\Users\\HP\\Downloads\\Washington_State_Certified_Public_Accountants_20250306.csv")

df_cleaned = df.drop(columns=["Last Updated", "Preferred Name"])


#5.Regulatory Compliance and Impact Assessment
print("\n\nObjective 5: Regulatory Compliance and Impact Assessment\n********************************************************\n")
df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], errors='coerce')
df['Expiration Year'] = df['Expiration Date'].dt.year
status_trend = df.groupby(['Expiration Year', 'Status']).size().unstack().fillna(0)
print("\nEarliest and latest expiration dates:")
print(df['Expiration Date'].min(), "to", df['Expiration Date'].max())
plt.style.use('dark_background')
print("\nDistribution of Expiration Years:")
print(df['Expiration Year'].value_counts().sort_index())
status_trend.plot(kind='line', marker='o', figsize=(12, 6), colormap='Set1')
plt.title("Trends of License Status Over Time")
plt.xlabel("Expiration Year")
plt.ylabel("Number of Licenses")
plt.legend(title="License Status")
plt.tight_layout()
plt.show()




