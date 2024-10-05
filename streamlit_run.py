import streamlit as st

# -- Page Setup --
homepage=st.Page(
    page="Pages/Homepage.py",
    title="Home Page"
)

time_wasters=st.Page(
    page="Pages/1_Time_Wasters.py",
    title="Time Wasters"
)
engagement_levels=st.Page(
    page="Pages/2_Engagement_Levels.py",
    title="Engagement Levels"
)
addiction_levels=st.Page(
    page="Pages/3_Addiction_Levels.py",
    title="Addiction Levels"
)

# -- Navigation Setup [without Sections] --
pg=st.navigation(pages=[homepage,time_wasters,engagement_levels,addiction_levels])

# -- Run Navigation --
pg.run()