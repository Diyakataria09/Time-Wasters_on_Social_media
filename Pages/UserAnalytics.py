import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import preprocessor

# Page Configuration
st.set_page_config(
    page_title="Social Media Usage Insights",
    layout="wide"
)

# Declaring font sizes for headers in HTML format
font_size = 60
subheaders_font_size=38

# Title of the Page
st.markdown(
    f"<h1 style='text-align: center; color: #003366; font-size: {font_size}px;'>Social Media Usage Insights Dashboard</h1>",
    unsafe_allow_html=True
)

# Load the dataset
df = pd.read_csv("Time-Wasters on Social Media.csv")

# Creating Age Groups
df=preprocessor.fetch_age_group(df)

# Strip any leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Sidebar Title
st.sidebar.markdown(
    f"<h3 style='text-align: center; color: #000000; font-size: 32px'>Filters</h3>",
    unsafe_allow_html=True
)

# Create filters for Location, Gender, and Platform
location = preprocessor.multiselect(
    "Select Location", df['Location'].unique().tolist()
    )

    
gender = preprocessor.multiselect(
        'Select Gender', df['Gender'].unique().tolist()
    )
    
platform = preprocessor.multiselect(
        'Select Platforms', df['Platform'].unique()
    )

# Filter the DataFrame based on user selection
filtered_data = df[
        (df['Location'].isin(location)) &
        (df['Gender'].isin(gender)) &
        (df['Platform'].isin(platform))
    ]

# Check if any data is available for the selected filters
if not filtered_data.empty:

    # Descriptive Statistics
    st.markdown(
        f"<h3 style='text-align: center; color: #666666; font-size: {subheaders_font_size}px;' >Summary Statistics</h3>",
        unsafe_allow_html=True
    )
    
    st.write("")
    st.write("")

    # Creating key metric Columns
    col1,col2=st.columns(2)
    st.write("")
    st.write("")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.write("")
    st.write("")
    
    with col1:
        st.metric(label="Total People", value=len(df['UserID'].unique().tolist()))
    # with col2:
        st.metric(label="Total Time Spent", value=int(df['Total Time Spent'].sum()))
    with col2:
        st.markdown("<h5>Gender Distribution:</h5>",unsafe_allow_html=True)
        gender_distribution=filtered_data['Gender'].value_counts(normalize=True).map(lambda x: f"{x:.1%}")
        # st.write(filtered_data['Gender'].value_counts(normalize=True).map(lambda x: f"{x:.1%}"))
        gender_counts_df=pd.DataFrame(gender_distribution).reset_index()
        gender_counts_df.columns=['Gender', 'Proportion']
        col1,col2=st.columns(2)
        with col1:
            st.write("**Gender**")
            for index, row in gender_counts_df.iterrows():
                st.write(row['Gender'])
        with col2:
            st.write("**Percentage**")
            for index, row in gender_counts_df.iterrows():
                st.write(row['Proportion'])
    
    #Column Distribution
    col3,col4 = st.columns(2)
    st.write("")
    st.write("")
    st.markdown("<hr>",unsafe_allow_html=True)
    col5,col6 = st.columns(2)
    st.write("")
    st.write("")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.write("")
    st.write("")
    col7,col8 = st.columns(2)
    st.write("")
    st.write("")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.write("")
    st.write("")
    col9,col10 = st.columns(2)
    st.write("")
    st.write("")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.write("")
    st.write("")

    with col3:
        st.markdown(
            f"<h3 style='text-align: left; color: #66666; font-size: {subheaders_font_size}px;' >Gender Distribution</h3>",
            unsafe_allow_html=True
        )
        gender_counts = filtered_data['Gender'].value_counts()
        fig1, ax1 = plt.subplots()
        sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='pastel', ax=ax1)
        st.write("")
        st.write("")
        ax1.set_title('Count of Users by Gender', fontsize=10, loc='left')
        ax1.set_xlabel('Gender', fontsize=10)
        ax1.set_ylabel('Count', fontsize=10)
        st.pyplot(fig1,use_container_width=True)

        st.write("")
        st.write("")

        st.markdown("""
                    <h1 style='font-size: 22px;'>Large proportion of Users spread accross different Social Media Apps are Males.</h1>""", 
                    unsafe_allow_html=True
        )

    


        
    with col4:
        st.markdown(f"<h3 style='text-align:left; color: #66666; font-size: {subheaders_font_size}px;'>Location Distribution</h3>",unsafe_allow_html=True)
        st.write("")
        st.write("")
        location_counts = filtered_data['Location'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
        ax2.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
        # ax2.set_title('Users by Location',font_size=10,loc='left')
        st.pyplot(fig2)
        st.markdown("""##""")

    with col5:
        st.markdown(f"<h3 style='text-align:left; color: #66666; font-size: {subheaders_font_size}px;'>Platform Usage</h3>",unsafe_allow_html=True)
        platform_counts = filtered_data['Platform'].value_counts()
        fig3, ax3 = plt.subplots()
        sns.barplot(x=platform_counts.index, y=platform_counts.values, palette='muted', ax=ax3)
        ax3.set_title('Count of Users by Platform', fontsize=10, loc='left')
        ax3.set_xlabel('Platform', fontsize=10)
        ax3.set_ylabel('Count', fontsize=10)
        st.pyplot(fig3)

    with col6:
        st.markdown(f"<h3 style='text-align:left; color: #66666; font-size: {subheaders_font_size}px;'>Gender vs. Platform</h3>",unsafe_allow_html=True)
        gender_platform_counts = filtered_data.groupby(['Gender', 'Platform']).size().unstack()
        fig4, ax4 = plt.subplots()
        gender_platform_counts.plot(kind='bar', stacked=True, ax=ax4, cmap='Paired')
        ax4.set_title('User Distribution by Gender and Platform', fontsize=10, loc='left')
        ax4.set_xlabel('Gender', fontsize=10)
        ax4.set_ylabel('Count', fontsize=10)
        st.pyplot(fig4)

    with col7:
        st.markdown("""
        ## Key Insights from Average Engagement Levels on Social media by Age Groups
                    
        - ### Higher Social Media Usage in Younger Age Groups: 
          The 18-24 and 25-34 age groups spend the most time on social media across all genders, averaging around 140-160 minutes per day.

        - ### Gender Comparison Across Age Groups:
          Across all age groups, females generally seem to spend slightly more time on social media than males, while the "Other" gender category is consistently lower but follows a similar trend.

        - ### Decline in Usage with Age: 
          Social media usage tends to decline with increasing age. The 55-64 age group spends less time on social media compared to younger groups, averaging around 100-120 minutes.
  
        - ### Similar Patterns for Males and Females in Middle Age: 
          In the 35-44 and 45-54 age groups, the time spent on social media by both males and females is relatively close, suggesting similar social media habits in middle-aged adults.                 
        """)

    engagement_by_gender_age = preprocessor.fetch_engagement_by_gender(filtered_data)

    with col8:
        # Create a bar plot for Average Engagement by Age Group and Gender
        fig5,ax5=plt.subplots(figsize=(10, 10))
        sns.barplot(data=engagement_by_gender_age, x='Age Group', y='Engagement', hue='Gender', palette='pastel')
        plt.title('Average Engagement Levels on Social Media by Age Group and Gender')
        plt.xlabel('Age Group')
        plt.ylabel('Average Engagement Level')
        plt.legend(title='Gender', loc=7)
        st.pyplot(fig5)

    with col9:
        st.markdown(
            f"<h1 style='text-align: center; color: #66666; font-size: {subheaders_font_size}px;'>KDE Plot of Addiction Level by Age Group</h1>",
            unsafe_allow_html=True
        )
        # KDE plot for Addiction Level by Age Group
        fig6,ax6=plt.subplots(figsize=(12,8))
        sns.kdeplot(df[df['Age Group'] == '18-24']['Addiction Level'], shade=True, label="18-24", color="#FFB6C1")
        sns.kdeplot(df[df['Age Group'] == '25-34']['Addiction Level'], shade=True, label="25-34", color="#FF69B4")
        sns.kdeplot(df[df['Age Group'] == '35-44']['Addiction Level'], shade=True, label="35-44", color="#DB7093")
        sns.kdeplot(df[df['Age Group'] == '45-54']['Addiction Level'], shade=True, label="45-54", color="#87CEFA")
        sns.kdeplot(df[df['Age Group'] == '55-64']['Addiction Level'], shade=True, label="55-64", color="#A3D5A1")
        # plt.title("Addiction Level by Age Group")
        ax6.set_title('Addiction Level by Age Group', fontsize=22, loc='left')
        st.write("")
        plt.xlabel("Addiction Level")
        plt.ylabel("Density")
        plt.legend()
        st.pyplot(fig6)

    with col10:
        st.markdown("""
        ## Key Insights from Addiction Level by Age Groups
                    
        - 1. The graph includes five age groups: 18-24 (pink), 25-34 (red), 35-44 (blue), 45-54 (green), and 55-64 (light green).
        
        - 2. Each curve has peaks that represent the most frequent addiction levels within that age group.

        - 3. The 36-45 age group (blue) has the highest peak, indicating that users in this age group are more likely to have an addiction level around 1-2. Other age groups show lower peaks, meaning that while addiction is present, it's not as concentrated or frequent at certain levels as for the 36-45 group.
        
        ## Distribution Spread:
        
        - 1. Younger groups (19-25, 26-35) show wider curves, indicating a more varied range of addiction levels.
        
        - 2. Older groups (46-55, 56-65) have more concentrated peaks and tend to show lower addiction levels compared to younger groups.

        ## Addiction Level Trends:
                    
        - 1. Most age groups have a primary peak at around 1-2 on the addiction scale.
                    
        - 2. For the older groups (46-65), addiction levels are generally lower, suggesting that younger users may be more prone to higher addiction levels.
        """)

     