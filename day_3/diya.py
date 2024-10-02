import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv("Time-Wasters on Social Media.csv")
df

df.isnull().sum()

df.info()

df.duplicated().sum()

df.describe() 

df.nunique()

# 1. Average Total Time Spent by Age Group¶

# Define age bins and labels
bins = [19,25, 35, 45, 55, 65]  # Adjust the upper limit based on your dataset
labels = ['19-25', '26-35', '36-45', '46-55', '56-65']

# Create a new column for Age Group
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Group by Age Group and calculate the mean Total Time Spent
grouped_time_spent = df.groupby('Age Group')['Total Time Spent'].mean().reset_index()
grouped_time_spent

# Create a bar plot for Average Total Time Spent by Age Group
plt.figure(figsize=(8, 6))
sns.barplot(data=grouped_time_spent, x='Age Group', y='Total Time Spent', palette='Accent')
plt.title('Average Total Time Spent on Social Media by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Total Time Spent (minutes)')
plt.show()

# 2 Location vs.Total Time Spent:¶¶

# Bar plot: Location vs. Total Time Spent
plt.figure(figsize=(10,6))
location_avg_time = df.groupby('Location')['Total Time Spent'].mean().sort_values(ascending=False)
sns.barplot(x=location_avg_time.index, y=location_avg_time.values,palette='cubehelix')
plt.title('Average Time Spent on Social Media by Location')
plt.xticks(rotation=45)
plt.xlabel('Location')
plt.ylabel('Average Time Spent (minutes)')
plt.show()

# 3. Average Time Spent by Gender and Age Group

# Group by Age Group and Gender, calculate the mean Total Time Spent
avg_time_spent_gender_age = df.groupby(['Age Group', 'Gender'])['Total Time Spent'].mean().reset_index()
avg_time_spent_gender_age

# Create a bar plot for Average Time Spent by Age Group and Gender
plt.figure(figsize=(8, 6))
sns.barplot(data=avg_time_spent_gender_age, x='Age Group', y='Total Time Spent', hue='Gender',palette='PuBuGn')
plt.title('Average Time Spent on Social Media by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Average Time Spent (minutes)')
plt.legend(title='Gender')
plt.show()


# 4 Engagement Levels by Gender and Age Group

# Group by Age Group and Gender, calculate the mean Engagement
engagement_by_gender_age = df.groupby(['Age Group', 'Gender'])['Engagement'].mean().reset_index()
engagement_by_gender_age

# Create a bar plot for Average Engagement by Age Group and Gender
plt.figure(figsize=(10, 6))
sns.barplot(data=engagement_by_gender_age, x='Age Group', y='Engagement', hue='Gender', palette='pastel')
plt.title('Average Engagement Levels on Social Media by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Average Engagement Level')
plt.legend(title='Gender')
plt.show()

# 5. Average Addiction Level by Age Group and Gender¶

# Group by Age Group and Gender, calculate the mean Addiction Level
addiction_level_gender_age = df.groupby(['Age Group', 'Gender'])['Addiction Level'].mean().reset_index()
addiction_level_gender_age

# Create a bar plot for Average Addiction Level by Age Group and Gender
plt.figure(figsize=(10, 6))
sns.barplot(data=addiction_level_gender_age, x='Age Group', y='Addiction Level', hue='Gender', palette='cubehelix')
plt.title('Average Addiction Level by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Average Addiction Level')
plt.legend(title='Gender')
plt.show()

# 6.Comparison of Platforms Used by Age Group and Gender

# Group by Platform, Age Group, and Gender, then count the occurrences
platform_usage = df.groupby(['Platform', 'Age Group', 'Gender']).size().reset_index(name='Counts')
platform_usage

# Create a bar plot for Platform Usage by Age Group and Gender
plt.figure(figsize=(10, 6))
sns.barplot(data=platform_usage, x='Platform', y='Counts', hue='Age Group', palette='Blues')
plt.title('Platform Usage by Age Group and Gender')
plt.xlabel('Social Media Platform')
plt.ylabel('Number of Users')
plt.xticks(rotation=45)
plt.legend(title='Age Group')
plt.show()

# 7 Group by Age Group and Gender

# Group by Age Group and Gender, calculate the mean Scroll Rate
scroll_rate_gender_age = df.groupby(['Age Group', 'Gender'])['Scroll Rate'].mean().reset_index()
scroll_rate_gender_age 

# Create a bar plot for Average Scroll Rate by Age Group and Gender
plt.figure(figsize=(10 ,6))
sns.barplot(data=scroll_rate_gender_age, x='Age Group', y='Scroll Rate', hue='Gender', palette='GnBu')
plt.title('Average Scroll Rate on Social Media by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Average Scroll Rate')
plt.legend(title='Gender')
plt.show()

# 8. Location vs. Total Time Spent

# Box plot: Location vs. Total Time Spent
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Location', y='Total Time Spent',hue='Gender',palette='GnBu')
plt.title('Location vs. Total Time Spent on Social Media')
plt.xticks(rotation=45)
plt.xlabel('Location')
plt.ylabel('Total Time Spent (minutes)')
plt.show()