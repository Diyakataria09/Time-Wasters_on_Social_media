# Importing Libraries
import pandas as pd
import numpy as np
import streamlit as st

# Fetching the data
def fetch_data():
    df=pd.read_csv("Time-Wasters on Social Media.csv")
    return df

# Fetching Age Group data
def fetch_age_group(df):
    lower_bins=[18,24,34,44,54,64]
    labels=['18-24','25-34','35-44','45-54','55-64']
    df['Age Group'] = pd.cut(df['Age'], bins=lower_bins, labels=labels, right=False)
    return df

#Multiselect Function
def multiselect(title,options_list):
    
    select_all=st.sidebar.radio("Select All", ['Yes','No'], key=title)
    if select_all=='Yes':
        return options_list
    else:
        return st.sidebar.multiselect(title,options_list)

#Fetch Engagement by Gender   
def fetch_engagement_by_gender(df):
    engagement_by_gender=df.groupby(['Age Group', 'Gender'])['Engagement'].mean().reset_index()
    return engagement_by_gender

# Fetch Average Duration Spent by Age Group and Gender
def fetch_average_duration_age_gender(df):
    average_duration_age_gender=df.groupby(["Age Group","Gender"])[["Time Spent On Video","Number of Videos Watched"]].sum().reset_index()
    average_duration_age_gender['Average Duration Spent']=average_duration_age_gender["Time Spent On Video"]/average_duration_age_gender["Number of Videos Watched"]
    return average_duration_age_gender

# Fetch Average Duration Spent by Location and Demographics
def fetch_average_duration_loc_dem(df):
    average_duration_loc_dem=df.groupby(['Location','Demographics'])[['Total Time Spent','Number of Sessions']].sum().reset_index()
    average_duration_loc_dem['Time Spent Per Session']=average_duration_loc_dem['Total Time Spent']/average_duration_loc_dem['Number of Sessions']
    return average_duration_loc_dem

