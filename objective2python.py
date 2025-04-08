import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("        DATASET OF STATE CERTIFIED PUBLIC ACCOUNTANTS OF WASHINGTON\n    *******************************************************************")
df = pd.read_csv("C:\\Users\\HP\\Downloads\\Washington_State_Certified_Public_Accountants_20250306.csv")

#CLEANING THE DATSET
df_cleaned = df.drop(columns=["Last Updated", "Preferred Name"])
#BASIC INFORMATION OF DATA
print(df)

print("OBJECTIVE 2:DEMOGRAPHIC INSIGHTS\n************************************\n\n")

sns.set(style="whitegrid")

city_counts = df_cleaned['City'].value_counts().head(10)
print("Top 10 Cities with Most Certified Public Accountants:\n",city_counts)
plt.figure(figsize=(6, 6))
plt.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%',
        startangle=140, colors=sns.color_palette("Set2"))

# Add center circle
centre_circle = plt.Circle((0, 0), 0.5, color='white')
plt.gca().add_artist(centre_circle)

plt.title("Top 10 Cities with Most Certified Public Accountants")
plt.axis('equal')
plt.tight_layout()
plt.show()


