import streamlit as st

# Font size for the title
font_size = 60  # Can be changed to adjust size of text

# Font size for the subtitle
font_size_subtitle = 38  # Can be changed to adjust size of text

# Use the fixed font size in the HTML
st.markdown(
    f"<h1 style='text-align: center; color: #003366; font-size: {font_size}px;'>Welcome to the Time-Wasters on Social Media Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

st.write("")


# Use the fixed font size in the HTML for the subtitle
st.markdown(
    f"<h3 style='text-align: center; color: #666666; font-size: {font_size_subtitle}px;'>Select to go towards the Time-Wasters on Social Media Analytics Dashboard.</h3>",
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")
# Add a logo to the dashboard
# col1, col2  = st.columns([0.5, 2])

# with col1:
    # st.image("image/Black And White Modern Typographic Simple social Media logo.png", width=300)1

# with col2:
st.write("")
st.write("")
st.write("")
# st.write("")
    
# Define the font sizes for question and answers
font_size_question = 40  # Larger size for the question
font_size_answers = 29    # Smaller size for the answers

# Display the formatted text with sizes applied
st.markdown(
    f"""
    <h4 style='color: #4D4D4D; font-size: {font_size_question}px;'>What we will see ahead ?</h4>
    <ol>
        <li style='color: #000080; font-size: {font_size_answers}px;'>User Distribution and Addiction Level Analysis</li>
        <li style='color: #000080; font-size: {font_size_answers}px;'>Analysis of Time Spent over Social Media</li>
    </ol>
        
    """, 
    unsafe_allow_html=True
)