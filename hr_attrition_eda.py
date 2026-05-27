# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Step 2: Load Dataset
df = pd.read_csv(r'C:\Users\sri2v\HR_Attrition_Project\WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Step 3: First Look at Data
print("Shape:", df.shape)
print("\nAttrition Count:")
print(df['Attrition'].value_counts())
print("\nAttrition Rate:", round(df['Attrition'].value_counts(normalize=True)['Yes']*100, 2), "%")

dept=df.groupby('Department')['Attrition'].value_counts()
print(dept)
ot = df.groupby('OverTime')['Attrition'].value_counts()
print(ot)
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,25,35,45,60], labels=['18-25','26-35','36-45','46-60'])
age = df.groupby('AgeGroup', observed=True)['Attrition'].value_counts()
print(age)


# Step 7: Chart - Attrition by Department
dept_yes = df[df['Attrition']=='Yes']['Department'].value_counts()
plt.figure(figsize=(8,5))
sns.barplot(x=dept_yes.index, y=dept_yes.values, palette='Reds_d')
plt.title('Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees Left')
plt.tight_layout()
plt.savefig('attrition_by_department.png')
plt.show()
print("Chart saved!")

# Step 8: Chart - Attrition by OverTime
ot_yes = df[df['Attrition']=='Yes']['OverTime'].value_counts()
plt.figure(figsize=(6,5))
sns.barplot(x=ot_yes.index, y=ot_yes.values, palette='Blues_d')
plt.title('Attrition by OverTime')
plt.xlabel('OverTime')
plt.ylabel('Number of Employees Left')
plt.tight_layout()
plt.savefig('attrition_by_overtime.png')
plt.show()
print("Chart saved!")

# Step 9: Chart - Attrition by Age Group
age_yes = df[df['Attrition']=='Yes']['AgeGroup'].value_counts()
plt.figure(figsize=(8,5))
sns.barplot(x=age_yes.index, y=age_yes.values, palette='Greens_d')
plt.title('Attrition by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees Left')
plt.tight_layout()
plt.savefig('attrition_by_agegroup.png')
plt.show()
print("Chart saved!")
