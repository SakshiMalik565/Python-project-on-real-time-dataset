
print("        DATASET OF STATE CERTIFIED PUBLIC ACCOUNTANTS OF WASHINGTON\n    *******************************************************************")
df = pd.read_csv("C:\\Users\\HP\\Downloads\\Washington_State_Certified_Public_Accountants_20250306.csv")

#CLEANING THE DATSET
df_cleaned = df.drop(columns=["Last Updated", "Preferred Name"])
#BASIC INFORMATION OF DATA
print(df)
print("\n➡️HEAD OF DATASET\n\n",df.head(),"\n\n\n")

print("\n➡️TAIL OF DATASET\n\n",df.tail(),"\n\n\n")

print("\n➡️SUMMARY STATISTICS OF DATASET\n\n",df.describe(),"\n\n\n")

print("\n➡️INFORMATION OF DATASET\n\n",df.info(),"\n\n\n")

print("\n➡️COLUMN NAMES\n\n",df.columns,"\n\n\n")

print("\n➡️SHAPE OF DATASET\n\n",df.shape,"\n\n\n")

print("\n ➡ COUNT  OF MISSING VALUES OF EACH COLUMN\n\n",df.isnull().sum(),"\n\n\n")

print("\n ➡ DROP ALL ROWS CONTAINING MISSING VALUES\n\n",df.dropna(),"\n\n\n")

df_cleaned["Original Issue Date"] = pd.to_datetime(df_cleaned["Original Issue Date"], errors="coerce")
df_cleaned["Expiration Date"] = pd.to_datetime(df_cleaned["Expiration Date"], errors="coerce")

print("\n➡ DUPLICATE ROWS=", df_cleaned.duplicated().sum(),'\n\n\n')

print("\n➡ COUNT OD UNIQUE COUNTRIES =",df_cleaned["Country"].nunique(),'\n\n\n')

print("\n➡ UNIQUE COUNTRIES NAMES\n",df_cleaned["Country"].unique(),'\n\n\n')

#CORRELATION AND COVARIANCE
CORRELATION=df_cleaned.corr(numeric_only=True)
print("\n➡ CORREALTION MATRIX\n",CORRELATION,'\n\n\n')
print("\n➡ COVARIANCE MATRIX\n",df_cleaned.cov(numeric_only=True),'\n\n\n')

#1.License Status Analysis
print("OBJECTIVE 1:License Status Analysis\n************************************\n\n")
status_counts = df_cleaned['Status'].value_counts()
print("LICENSE STATUS COUNTS:\n")
print(status_counts)

status_percent = (status_counts / len(df_cleaned)) * 100
print("\n\nLICENSE STATUS PERCENTAGES:\n")
print(status_percent.round(2))

#BARPLOT REPRESENTATION
status_df = status_counts.reset_index()
status_df.columns = ['Status', 'Count']
plt.figure(figsize=(10, 6))
sns.barplot(data=status_df, x='Count', y='Status', hue='Status', dodge=False, palette="coolwarm", legend=False)
plt.title("Distribution of CPA License Statuses")
plt.xlabel("Number of CPAs")
plt.ylabel("License Status")
plt.tight_layout()
plt.show()
#PIE CHART REPRESENTATION FOR VISUAL OF PROPORTIONS
colors = sns.color_palette("Set2", len(status_counts))
fig, ax = plt.subplots(figsize=(10, 10))  # Increased size
wedges, texts, autotexts = ax.pie(
    status_percent,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 12}
)
ax.legend(
    wedges,
    status_counts.index,
    title="License Status",
    loc='lower center',
    bbox_to_anchor=(0.5, -0.1),
    ncol=2,
    fontsize=11,
    title_fontsize=12
)
ax.set_title("CPA License Status", fontsize=16, pad=20)
ax.axis('equal')  # Circle shape
plt.tight_layout()
plt.show()
