# Day 1 : Handle engagement and session analysis (Total Time Spent, Number of Sessions).

#importing libraries required for this project and drawing Insights
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Loading the Dataset
df=pd.read_csv("Time-Wasters on Social Media.csv")

# Displaying the top 15 rows of the dataframe
df.head(15)

# Checking for null values
df.isnull().sum()

# Checking for duplicates
df.duplicated().sum()

# Summarizing the differential statistics of dataframe of numerical datatypes
df.describe()

#Task 1 : Tried finding correlation between columns of numerical datatype.¶
corr=df.corr(numeric_only=True)
plt.figure(figsize=(15,10))
sns.heatmap(corr,annot=True)

# Focussed on two columns "Time Spent On Video","Number of Videos Watched" and compared the mean of those on the basis of Genders, Age Groups, and Profession.
df_genders=df.groupby('Gender')[["Time Spent On Video","Number of Videos Watched"]].mean().reset_index()
df_genders


df_Profession=df.groupby("Profession")[["Time Spent On Video","Number of Videos Watched"]].mean().reset_index()
df_Profession

# Finding lower and upper limit of Ages and adding an age group column
print(df['Age'].min(), df['Age'].max())
lower_bins=[18,24,34,44,54,64]
labels=['18-24','25-34','35-44','45-54','55-64']
df['Age Group'] = pd.cut(df['Age'], bins=lower_bins, labels=labels, right=False)
df[df['Age']==18] #Checking rows with age value = 18


# Gender Trends Plot
fig, axes=plt.subplots(1,2,figsize=(10,5)) #1 row, 2 columns for 2 graphs in one figure canvas
fig.suptitle("Gender Trends plot",x=0.5,y=1,fontsize=24)
# First line graph for on Average Time Spent on Video :
sns.lineplot(df_genders,x=df_genders['Gender'],y=df_genders['Time Spent On Video'],ax=axes[0])
# Second Line Graph for an Average Number of Video watched :
sns.lineplot(df_genders,x=df_genders['Gender'],y=df_genders['Number of Videos Watched'],ax=axes[1])
axes[0].set_title("Average Time Spent on Video v/s Gender")
axes[1].set_title("Average Number of Videos Watched v/s Gender")
plt.tight_layout(rect=[0, 0, 1, 1])
plt.show()


# Profession Trends Plot
fig, axes=plt.subplots(1,2,figsize=(10,5)) #1 row, 2 columns for 2 graphs in one figure canvas
fig.suptitle("Profession Trends plot",x=0.5,y=1,fontsize=24)
# First line graph for on Average Time Spent on Video :
sns.lineplot(df_genders,x=df_Profession['Profession'],y=df_Profession['Time Spent On Video'],ax=axes[0])
# Second Line Graph for an Average Number of Video watched :
sns.lineplot(df_genders,x=df_Profession['Profession'],y=df_Profession['Number of Videos Watched'],ax=axes[1])
axes[0].set_title("Average Time Spent on Video v/s Profession")
axes[1].set_title("Average Number of Videos Watched v/s Profession")
plt.tight_layout(rect=[0, 0, 1, 1])
axes[0].tick_params(axis='x',rotation=45)
axes[1].tick_params(axis='x',rotation=45)
plt.show()

# Age Group Trends Plot
fig, axes=plt.subplots(1,2,figsize=(10,5)) #1 row, 2 columns for 2 graphs in one figure canvas
fig.suptitle("Age Group Trends plot",x=0.5,y=1,fontsize=24)
# First line graph for on Average Time Spent on Video :
sns.lineplot(df_genders,x=df_age_group['Age Group'],y=df_age_group['Time Spent On Video'],ax=axes[0])
# Second Line Graph for an Average Number of Video watched :
sns.lineplot(df_genders,x=df_age_group['Age Group'],y=df_age_group['Number of Videos Watched'],ax=axes[1])
axes[0].set_title("Average Time Spent on Video v/s Age Group")
axes[1].set_title("Average Number of Videos Watched v/s Age Group")
plt.tight_layout(rect=[0, 0, 1, 1])
axes[0].tick_params(axis='x',rotation=45)
axes[1].tick_params(axis='x',rotation=45)
plt.show()

# Average duration spent (total time spent / total videos watched) classified by all three categories

df_genders_total=df.groupby("Gender")[["Time Spent On Video","Number of Videos Watched"]].sum().reset_index()
df_Profession_total=df.groupby("Profession")[["Time Spent On Video","Number of Videos Watched"]].sum().reset_index()
df_age_group_total=df.groupby("Age Group")[["Time Spent On Video","Number of Videos Watched"]].sum().reset_index()
df_genders_total['Average Duration Spent']=df_genders_total["Time Spent On Video"]/df_genders_total["Number of Videos Watched"]
df_Profession_total['Average Duration Spent']=df_Profession_total["Time Spent On Video"]/df_Profession_total["Number of Videos Watched"]
df_age_group_total['Average Duration Spent']=df_age_group_total["Time Spent On Video"]/df_age_group_total["Number of Videos Watched"]

fig, axes=plt.subplots(3,1,figsize=(15,15)) #3 rows, 1 column for 3 graphs in one figure canvas
fig.suptitle("Average Duration Trends plot",x=0.5,y=1,fontsize=24)
# First line graph for on Average Duration Spent on Video grouped by Gender:
sns.lineplot(df_genders_total,x=df_genders_total['Gender'],y=df_genders_total['Average Duration Spent'],ax=axes[0])
# Second Line Graph for an Average Duration Spent on Video grouped by Profession:
sns.lineplot(df_Profession_total,x=df_Profession_total['Profession'],y=df_Profession_total['Average Duration Spent'],ax=axes[1])
# Third Line Graph for an Average Duration Spent on Video grouped by Age Groups :
sns.lineplot(df_age_group_total,x=df_age_group_total['Age Group'],y=df_age_group_total['Average Duration Spent'],ax=axes[2])
axes[0].set_title("Average Duration Spent on Video v/s Gender")
axes[1].set_title("Average Duration Spent on Video v/s Profession")
axes[2].set_title("Average Duration Spent on Video v/s Age Group")
plt.tight_layout(rect=[0, 0, 1, 1])
plt.show()

average_duration_spent=df.groupby(["Age Group","Gender"])[["Time Spent On Video","Number of Videos Watched"]].sum().reset_index()
average_duration_spent['Average Duration Spent']=average_duration_spent["Time Spent On Video"]/average_duration_spent["Number of Videos Watched"]
# average_duration_spent
plt.figure(figsize=(10, 6))
sns.barplot(data=average_duration_spent, x='Age Group', y='Average Duration Spent', hue='Gender')
plt.title('Average Duration Spent on Video by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Average Duration Spent')
plt.legend(title='Gender')
plt.show()

#Analyze Time spent and session frequency over different demographics, age group, Gender.¶

# First DataFrame will consist of Time Spent and Session Frequncy and their average over Age Group and Gender
analyze_df_1=df.groupby(['Age Group','Gender'])[['Total Time Spent','Number of Sessions']].sum().reset_index()
analyze_df_1['Time Spent Per Session']=analyze_df_1['Total Time Spent']/analyze_df_1['Number of Sessions']
plt.figure(figsize=(10,5))
plt.title("Time Spent Per Session by Age Group and Gender")
sns.barplot(analyze_df_1,x="Age Group",y="Time Spent Per Session",hue="Gender")
plt.legend(loc=1)
plt.show()

# Second DataFrame will consist of Time Spent and Session Frequncy and their average over Location and Demographics
analyze_df_2=df.groupby(['Location','Demographics'])[['Total Time Spent','Number of Sessions']].sum().reset_index()
analyze_df_2['Time Spent Per Session']=analyze_df_2['Total Time Spent']/analyze_df_2['Number of Sessions']
plt.figure(figsize=(15,8))
plt.title("Average Duration Spent by Location and DemoGraphics")
sns.barplot(analyze_df_2,x="Location",y="Time Spent Per Session",hue="Demographics")
plt.legend(loc=1)
plt.show()