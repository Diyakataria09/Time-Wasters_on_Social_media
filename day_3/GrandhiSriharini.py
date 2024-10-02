import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("Time-Wasters on Social Media.csv")
df

df.columns

df.info()

# Addiction level in social media
addiction_level_count=df['Addiction Level'].value_counts().to_frame().reset_index()
addiction_level_count                                                                                                     

age=pd.cut(df['Age'],bins=[df['Age'].min(),30,50,df['Age'].max()],labels=['young','middle age','old'])
age

age_addiction=df.groupby(age)['Addiction Level'].mean().to_frame().reset_index()
age_addiction  

plt.bar(age_addiction['Age'],age_addiction['Addiction Level'])
plt.title('AVERAGE ADDICTION LEVEL BY AGE GROUP',color='g')
plt.xlabel('AGE GROUP')
plt.ylabel('AVERAGE ADDICTION LEVEL')
plt.show()

# Usage of social media by profession
usage_profession=df['Profession'].value_counts().reset_index()
usage_profession      

plt.figure(figsize=(10,5))
plt.bar(usage_profession['Profession'],usage_profession['count'],color="red")
plt.title('USAGE OF SOCIAL MEDIA BY PROFESSION',color='red')
plt.xlabel('PROFESSION')
plt.ylabel('COUNT')
plt.xticks(rotation=90)
plt.show()



# Watching time of social media¶
watch_time=df['Watch Time'].value_counts().plot(kind='bar',figsize=(10,5),title='WATCHING TIME OF SOCIAL MEDIA')

# productivity Loss Distribution¶
plt.figure(figsize=(8, 6))
sns.histplot(df['ProductivityLoss'], bins=30, kde=True)
plt.title('Productivity Loss Distribution')
plt.xlabel('Productivity Loss')
plt.ylabel('Frequency')
plt.show()

#Regression plot of Addiction level Vs Productivity Loss
plt.figure(figsize=(8, 6))
sns.regplot(x='Addiction Level', y='ProductivityLoss', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Regression Plot of Addiction Level vs Productivity Loss')
plt.xlabel('Addiction Level')
plt.ylabel('Productivity Loss')
plt.show()

# Boxplot for Addiction Level
plt.figure(figsize=(8, 6))
sns.boxplot(df['Addiction Level'])
plt.title('Addiction Level Boxplot')
plt.show()

# Boxplot for Productivity Loss
plt.figure(figsize=(8, 6))
sns.boxplot(df['ProductivityLoss'])
plt.title('Productivity Loss Boxplot')
plt.show()