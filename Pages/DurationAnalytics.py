import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import preprocessor

# Page Configuration
st.set_page_config(
    page_title="Time Spenditure Insights",
    layout="wide"
)

# Declaring font sizes for headers in HTML format
font_size = 60
subheaders_font_size=38

# Title of the Page
st.markdown(
    f"<h1 style='text-align: center; color: #003366; font-size: {font_size}px;'>Time Spent on Social Media Insights Dashboard</h1>",
    unsafe_allow_html=True
)

# Load the dataset
df = pd.read_csv("Time-Wasters on Social Media.csv")

# Creating Age Groups
df=preprocessor.fetch_age_group(df)

# Fetching Average Duration DataFrame
average_duration_age_gender=preprocessor.fetch_average_duration_age_gender(df)
average_duration_loc_dem=preprocessor.fetch_average_duration_loc_dem(df)

# Strip any leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Sidebar Title
st.sidebar.markdown(
    f"<h3 style='text-align: center; color: #000000; font-size: 32px'>Filters</h3>",
    unsafe_allow_html=True
)

#Platform Filter
platform = preprocessor.multiselect(
    "Select Platform", df["Platform"].unique().tolist()
    )

#Age Group Filter
age_group = preprocessor.multiselect(
    "Select Age Group", df["Age Group"].unique().tolist()
    )

#Gender Filter
gender= preprocessor.multiselect(
    "Select Gender",df['Gender'].unique().tolist()
    )

#Location Filter
location=preprocessor.multiselect(
    "Select Location",df['Location'].unique().tolist()
    )

#DemoGraphics Filter
demographics=preprocessor.multiselect(
    "Select Demographics",df['Demographics'].unique().tolist()
    )

#Global Filtering
filter1_df= df[
    (df['Platform'].isin(platform)) & 
    (df['Frequency']) & 
    (df['Total Time Spent'])
]

filter2_df=average_duration_age_gender[
    (average_duration_age_gender['Age Group'].isin(age_group)) & 
    (average_duration_age_gender['Gender'].isin(gender)) & 
    (average_duration_age_gender['Average Duration Spent'])
]

filter3_df=average_duration_loc_dem[
    (average_duration_loc_dem['Location'].isin(location)) &
    (average_duration_loc_dem['Demographics'].isin(demographics)) &
    (average_duration_loc_dem['Time Spent Per Session'])
]

# Creating key metric Columns
col1,col2,col3,col4=st.columns(4)
st.write("")
st.write("")
st.markdown("<hr>",unsafe_allow_html=True)
st.write("")
st.write("")

with col1:
    st.metric(label="Total People", value=len(df['UserID'].unique().tolist()))
with col2:
    st.metric(label="Total Time Spent", value=int(df['Total Time Spent'].sum()))
with col3:
    st.metric(label="Total Platforms", value=len(df['Platform'].unique().tolist()))
with col4:
    st.metric(label="Total Age Groups", value=len(df['Age Group'].unique().tolist()))

# Platform Analytics Chart

time_spent_on_platform=filter1_df[["Platform","Frequency","Total Time Spent"]].groupby(['Platform','Frequency']).sum().reset_index()
pivot_time_spent_on_platform = pd.pivot(time_spent_on_platform,index='Frequency',columns='Platform',values='Total Time Spent')
pivot_time_spent_on_platform.reset_index(inplace=True)
pivot_time_spent_on_platform.set_index("Frequency", inplace=True)
fig1,ax1=plt.subplots(figsize=(15, 5))
ax1.plot(pivot_time_spent_on_platform,linestyle='--',marker='o')
plt.xlabel('Frequency')
plt.ylabel('Total Time Spent')
plt.title('Multiline Line Plot from Pivot Table')
ax1.grid(True)
st.pyplot(fig1)
st.write("")
st.write("")
st.markdown("<hr>",unsafe_allow_html=True)
st.write("")
st.write("")

# Column Distribution
col5,col6=st.columns(2)
st.write("")
st.write("")
st.markdown("<hr>",unsafe_allow_html=True)
st.write("")
st.write("")
col7,col8=st.columns(2)
st.write("")
st.write("")
st.markdown("<hr>",unsafe_allow_html=True)
st.write("")
st.write("")

with col5:
    fig2,ax2=plt.subplots(figsize=(5, 5))
    sns.barplot(data=filter2_df, x='Age Group', y='Average Duration Spent', hue='Gender',ax=ax2)
    plt.title('Average Duration Spent Graph by Age Group and Gender')
    plt.xticks(rotation=75)
    plt.xlabel('Age Group')
    plt.ylabel('Average Duration Spent')
    plt.legend(title='Gender')
    st.pyplot(fig2)

with col6:
    st.markdown("""
        ## Key Insights from Average Duration Spent by Age Groups
                    
        - ### Higher Average Duration in Older Age Groups: 
          The 55-64 and 35-44 age groups spend the most time on social media across all genders.

        - ### Gender Comparison Across Age Groups:
          Across all age groups, 'Other' gender category generally seem to spend slightly more time on social media than males and females.

        - ### Increase in Usage with Age: 
          Social media usage tends to increase with increasing age. The 55-64 age group spends more time on social media compared to younger groups.
        """)

with col7:
    st.markdown("""
        ## Key Insights from Average Duration Spent by Location and Demographics
                    
        - ### Higher Average Duration in Rural Areas: 
          The average time spent on social media across all rural areas of different locations seem to be higher than Urban areas.

        - ### Consistent average Duration in Rural Areas:
          The average duration spent accross Social media seems to be conssitent accross different countries

        - ### Equal Proportion of Average Duration Spent in Indonesia: 
          The Average duration spent accross Social Media is almost similar in both Rural and Urban Areas, indicating highly active country on social media amongst it's country's population.
        """)

with col8:
    fig3,ax3=plt.subplots(figsize=(5,5))
    plt.title("Average Duration Spent by Location and Demographics")
    sns.barplot(filter3_df,x="Location",y="Time Spent Per Session",hue="Demographics")
    plt.xticks(rotation=75)
    plt.xlabel('Location')
    plt.ylabel('Average Duration per Session')
    plt.legend(title='Demographics')
    st.pyplot(fig3)