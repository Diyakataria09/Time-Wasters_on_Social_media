import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Time-Wasters on Social Media.csv")
df

# Define age bins and labels
bins = [19,25, 35, 45, 55, 65]  # Adjust the upper limit based on your dataset
labels = ['19-25', '26-35', '36-45', '46-55', '56-65']

# Create a new column for Age Group
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

df.columns

# Number of diffirent video categories

df[["Video Category"]].groupby("Video Category").size()

# Average age of each video category

df[["Age","Video Category"]].groupby("Video Category").mean().reset_index()


# Number of video categories country wise
country = df[["Video Category","Location"]].groupby("Location").count().reset_index()
country

plt.figure(figsize = (10,7))
plt.title("Number of video categories country wise")
sns.barplot(data = country ,x="Location",y="Video Category")
sns.despine()

# Average satisfaction fof diffirent video categories
df1 = df[["Satisfaction","Video Category"]].groupby("Video Category").mean().reset_index()
df1

df2 = df[["Profession","Video Category"]].groupby("Profession").count().reset_index()
df2

plt.figure(figsize =(10,8))
plt.title("Number of diffirent video categories watched by diffirent profession")
sns.barplot(data = df2 ,x="Profession",y="Video Category")
sns.despine()

# Number of videos on diffirent platforms
df[["Platform","Video Category"]].groupby("Platform").count().reset_index()

# diffirent video categories maximum at which platform
df[["Platform","Video Category"]].groupby(["Platform","Video Category"]).size()

# video category in diffirent demographic locations
df[["Demographics","Video Category"]].groupby("Demographics").value_counts()

ad = df[["Age Group","Video Category"]].groupby("Age Group").count().reset_index()
ad

plt.figure(figsize = (8,6))
sns.barplot(data = ad ,x="Age Group",y="Video Category")
plt.show()

# Video Length¶

df[["Age Group","Video Length"]]
len = df[["Age Group","Video Length"]].groupby("Age Group").mean().reset_index()
len

plt.figure(figsize = (8,6))
sns.barplot(data = len , x= "Age Group",y="Video Length")
plt.show()

#Average video length age group wise and category wise 
df[["Age Group","Video Category","Video Length"]].groupby(["Age Group","Video Category"]).mean()

#average video length country wise 
df[["Location","Video Length"]].groupby("Location").mean()

#Average video length of diffierent countries category wise 
df[["Location","Video Category","Video Length"]].groupby(["Location","Video Category"]).mean()

# Average video length platform wise 
df[["Video Length","Platform"]].groupby("Platform").mean().reset_index()

#videos on diffirent categories and  platform and thier average length
df[["Platform","Video Length","Video Category"]].groupby(["Platform","Video Category"]).mean().reset_index()

df[["Platform","Video Category","Age Group","Video Length"]].groupby(["Platform","Video Category","Age Group"]).mean()

# Number of videos watched¶
df["Number of Videos Watched"]
vd = df[["Number of Videos Watched","Video Category"]].groupby("Video Category").sum().reset_index()
vd

plt.figure(figsize = (9,7))
plt.title("Total number of videos watched category wise")
sns.barplot(data = vd , x="Video Category",y="Number of Videos Watched")
sns.despine()

videos_watched = df[["Age Group","Number of Videos Watched"]].groupby("Age Group").sum().reset_index()
videos_watched


plt.figure(figsize = (10,8))
plt.title("Total Number of videos watched by diffirent age group")

sns.barplot(data = videos_watched , x="Age Group",y="Number of Videos Watched")
sns.despine()

#Total number of videos watched in diffirent countries 
loc = df[["Number of Videos Watched","Location"]].groupby("Location").sum().reset_index()
loc

plt.figure(figsize = (10,8))
plt.title("Total number of videos watched in diffirent countries")
sns.barplot(data = loc , x="Location",y="Number of Videos Watched")
sns.despine()

# Number of videos watched as per satisfaction level
df[["Number of Videos Watched","Satisfaction"]].groupby("Satisfaction").sum().reset_index()

# Total number of videos platform wise 
df[["Number of Videos Watched","Platform"]].groupby("Platform").sum().reset_index()

#Country and platform wise number of videos watched 
df[["Location","Number of Videos Watched","Platform"]].groupby(["Location","Platform"]).count()