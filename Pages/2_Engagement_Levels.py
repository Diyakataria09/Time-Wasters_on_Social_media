import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
df = pd.read_csv('Time-Wasters on Social Media.csv')

# Set up Streamlit layout
st.title("Country-wise Engagement Levels by Demographics")

# Country Selection Dropdown
countries = df['Location'].unique()
selected_country = st.selectbox("Select Country", countries)

# Gender Selection
genders = df['Gender'].unique()
selected_gender = st.selectbox("Select Gender", genders)

# Age Slider (assuming 'Age' column is in the dataset)
min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
selected_age_range = st.slider("Select Age Range", min_age, max_age, (min_age, max_age))

# Platform Selection
platforms = df['Platform'].unique()
selected_platform = st.selectbox("Select Platform", platforms)

# Filter Data based on user selections
filtered_data = df[
    (df['Location'] == selected_country) &
    (df['Gender'] == selected_gender) &
    (df['Age'] >= selected_age_range[0]) &
    (df['Age'] <= selected_age_range[1]) &
    (df['Platform'] == selected_platform)
]

# Show filtered data as a table (optional for debugging)
# st.write(filtered_data)

# Calculate average engagement level for the filtered data
avg_engagement_level = filtered_data['Engagement'].mean()

# Display the result
st.subheader(f"Average Engagement Level in {selected_country} for {selected_gender} users aged {selected_age_range[0]} to {selected_age_range[1]} on {selected_platform}:")
st.write(f"*{avg_engagement_level:.2f}*")

# Visualize the Engagement Level (you can use any type of plot, here we use a histogram)
st.subheader("Engagement Level Distribution")

plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_data, x='Engagement', kde=True, bins=10, color='green')
plt.title(f"Engagement Level Distribution in {selected_country} for {selected_gender} users")
plt.xlabel('Engagement Level')
plt.ylabel('Frequency')

# Display the plot in Streamlit
st.pyplot(plt)

# Show a breakdown of the most common watch reasons for the filtered data
watch_reason_counts = filtered_data['Watch Reason'].value_counts()

st.subheader("Most Common Watch Reasons")
st.write(watch_reason_counts)