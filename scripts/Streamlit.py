import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df_merged = pd.read_csv('../data/telecom_user_satisfaction_dataa.csv')  # Replace with your actual data path

# Set page configuration
st.set_page_config(page_title="Telecom User Analysis Dashboard", layout="wide")

# Sidebar for navigation
st.sidebar.title("Dashboard Navigation")
option = st.sidebar.selectbox("Choose a task", ["User Overview Analysis", "User Engagement Analysis", "Experience Analysis", "Satisfaction Analysis"])

# User Overview Analysis
if option == "User Overview Analysis":
    st.title("User Overview Analysis")
    st.markdown("### Engagement Distribution Overview")
    
    # Example of a histogram plot for engagement scores
    fig = px.histogram(df_merged, x='MSISDN/Number', y='engagement_score', title="User Engagement Distribution")
    st.plotly_chart(fig, use_container_width=True)

# User Engagement Analysis
if option == "User Engagement Analysis":
    st.title("User Engagement Analysis")
    st.markdown("### Detailed Engagement Scores")
    
    # Example of a scatter plot for engagement scores
    fig = px.scatter(df_merged, x='MSISDN/Number', y='engagement_score', color='engagement_score', title="User Engagement Scores")
    st.plotly_chart(fig, use_container_width=True)

# Experience Analysis
if option == "Experience Analysis":
    st.title("Experience Analysis")
    st.markdown("### Experience Scores Distribution")
    
    # Example of a box plot for experience scores
    fig = px.box(df_merged, x='MSISDN/Number', y='experience_score', color='experience_score', title="User Experience Scores")
    st.plotly_chart(fig, use_container_width=True)

# Satisfaction Analysis
if option == "Satisfaction Analysis":
    st.title("Satisfaction Analysis")
    st.markdown("### User Satisfaction Scores")
    
    # Example of a bar plot for satisfaction scores
    fig = px.bar(df_merged, x='MSISDN/Number', y='satisfaction_score', color='satisfaction_score', title="User Satisfaction Scores")
    st.plotly_chart(fig, use_container_width=True)
