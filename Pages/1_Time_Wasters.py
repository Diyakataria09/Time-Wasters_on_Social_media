import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the app
st.title('Time Wasters on Social Media')


# Load your data
df = pd.read_csv('Time-Wasters on Social Media.csv')

# Set up Streamlit layout
st.subheader("Country-wise Addiction Levels by Demographics")

# Country Selection Dropdown
selected_country = st.selectbox("Select Country", df['Location'].unique().tolist())

# Gender Selection
selected_gender = st.selectbox("Select Gender", df['Gender'].unique().tolist())

# Age Slider (assuming 'Age' column is in the dataset)
min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
selected_age_range = st.slider("Select Age Range", min_age, max_age, (min_age, max_age))

# Platform Selection
selected_platform = st.selectbox("Select Platform", df['Platform'].unique().tolist())

# Filter Data based on user selections
filtered_data = df[
    (df['Location'] == selected_country) &
    (df['Gender'] == selected_gender) &
    (df['Age'] >= selected_age_range[0]) &
    (df['Age'] <= selected_age_range[1]) &
    (df['Platform'] == selected_platform)
]

# Show filtered data as a table (optional, for debugging purposes)
# st.write(filtered_data)


# Calculate average addiction level for the filtered data
avg_addiction_level = filtered_data['Addiction Level'].mean()

# Display the result
st.subheader(f"Average Addiction Level in {selected_country} for {selected_gender} users aged {selected_age_range[0]} to {selected_age_range[1]} on {selected_platform}:")
st.write(f"*{avg_addiction_level:.2f}*")

# Visualize the Addiction Level (you can use any type of plot, here we use a bar chart)
st.subheader("Addiction Level Distribution")

plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_data, x='Addiction Level', kde=True, bins=10, color='teal')
plt.title(f"Addiction Level Distribution in {selected_country} for {selected_gender} users")
plt.xlabel('Addiction Level')
plt.ylabel('Frequency')

# Display the plot in Streamlit
st.pyplot(plt)

#Time Spenditure Analysis
# platform=st.multiselect("Select Platforms",df['Platform'].unique().tolist())

# filter1_df= df[
#     (df['Platform'] == platform) & 
#     (df['Frequency']) & 
#     (df['Total Time Spent'])
# ]

# time_spent_on_platform=filter1_df[["Platform","Frequency","Total Time Spent"]].groupby(['Platform','Frequency']).sum().reset_index()
# pivot_time_spent_on_platform = pd.pivot(time_spent_on_platform,index='Frequency',columns='Platform',values='Total Time Spent')
# pivot_time_spent_on_platform.reset_index(inplace=True)
# pivot_time_spent_on_platform.set_index("Frequency", inplace=True)
# fig1,ax1=plt.subplots(figsize=(9, 7))
# ax1.plot(pivot_time_spent_on_platform,linestyle='--',marker='o')
# plt.xlabel('Frequency')
# plt.ylabel('Total Time Spent')
# plt.title('Multiline Line Plot from Pivot Table')
# plt.legend(df['Platform'],title='Platform',loc=2)
# ax1.grid(True)
# st.pyplot(fig1)
# st.write("")
# st.write("")
# st.markdown("<hr>",unsafe_allow_html=True)
# st.write("")
# st.write("")

# Show a breakdown of the most common watch reasons for the filtered data
watch_reason_counts = filtered_data['Watch Reason'].value_counts()

st.subheader("Most Common Watch Reasons")
st.write(watch_reason_counts)
st.subheader("Country-wise Engagement Levels")

# Average engagement per country
avg_engagement_by_country = df.groupby('Location')['Engagement'].mean().sort_values(ascending=False)

# Display bar chart
st.bar_chart(avg_engagement_by_country)

st.subheader("Addiction Level vs Age")

# Filter data by selected country and platform
selected_country = st.selectbox("Select Country", df['Location'].unique(), key='country_select_addiction')
selected_platform = st.selectbox("Select Platform", df['Platform'].unique(), key='platform_select_addiction')

# Filter the data
filtered_data = df[(df['Location'] == selected_country) & (df['Platform'] == selected_platform)]

# Line plot of addiction level vs age
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data, x='Age', y='Addiction Level', marker='o')
plt.title(f'Addiction Level vs Age in {selected_country} on {selected_platform}')
plt.xlabel('Age')
plt.ylabel('Addiction Level')
st.pyplot(plt)

st.subheader("Engagement Levels by Platform")

# Select age range
age_range = st.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (20, 40), key='age_slider_platform')

# Filter the data
filtered_data = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]

# Boxplot for engagement by platform
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='Platform', y='Engagement', palette='Set3')
plt.title(f'Engagement Levels for Age Group {age_range[0]} to {age_range[1]}')
st.pyplot(plt)

st.subheader("Gender-wise Comparison of Productivity Loss")

# Select platform
selected_platform = st.selectbox("Select Platform", df['Platform'].unique(), key='platform_select_prod_loss')

# Filter the data
filtered_data = df[df['Platform'] == selected_platform]

# Group by gender and calculate average productivity loss
gender_prod_loss = filtered_data.groupby('Gender')['ProductivityLoss'].mean()

# Bar chart
st.bar_chart(gender_prod_loss)

st.subheader("Engagement vs Productivity Loss")

# Scatter plot of engagement vs productivity loss
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Engagement', y='ProductivityLoss', hue='Platform', palette='viridis', s=100)
plt.title('Engagement vs Productivity Loss across Platforms')
st.pyplot(plt)


st.subheader("Watch Reasons per Demographic")

# Select country and age group
selected_country = st.selectbox("Select Country", df['Location'].unique(), key='country_select_watch_reason')
age_range = st.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (20, 40), key='age_slider_watch_reason')

# Filter the data
filtered_data = df[(df['Location'] == selected_country) & (df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]

# Bar chart of most common watch reasons
watch_reasons = filtered_data['Watch Reason'].value_counts()
st.bar_chart(watch_reasons)