import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("        DATASET OF STATE CERTIFIED PUBLIC ACCOUNTANTS OF WASHINGTON\n    *******************************************************************")
df = pd.read_csv("C:\\Users\\HP\\Downloads\\Washington_State_Certified_Public_Accountants_20250306.csv")

df_cleaned = df.drop(columns=["Last Updated", "Preferred Name"])

print("OBJECTIVE 3:EXPIRATION AND RENEWAL PATTERNS\n*********************************\n")
expiration_summary = df['Expiration Date'].describe()
print("Expiration Date Summary:")
print(expiration_summary)
# Converting the expiration date column
df['Expiration Date'] = pd.to_datetime(df['Expiration Date'], errors='coerce')
df['Expiration Year'] = df['Expiration Date'].dt.year
plt.style.use('dark_background')
plt.figure(figsize=(10, 6))
sns.histplot(df['Expiration Year'].dropna(), 
             bins=20, 
             kde=True, 
             color="#00FFC6",     
             edgecolor='#00FFAA',  
             linewidth=1.2)

plt.title('CPA License Expiration Years', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Expiration Year', fontsize=13, color='white')
plt.ylabel('Number of Expiring Licenses', fontsize=13, color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()




