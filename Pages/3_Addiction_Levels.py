import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
df = pd.read_csv('Time-Wasters on Social Media.csv')

# Set up Streamlit layout
st.title("Country-wise Addiction Levels by Demographics")

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

# Show a breakdown of the most common watch reasons for the filtered data
watch_reason_counts = filtered_data['Watch Reason'].value_counts()

st.subheader("Most Common Watch Reasons")
st.write(watch_reason_counts)