import streamlit as st
import pandas as pd
import datetime
from modules.formater import Title
# Title page and footer
title = "About"
Title().page_config(title)

st.markdown("## 📊 About")
st.markdown("### 👨🏼‍💻 Goal")
st.markdown("""
Analysis of job requirements for aspiring data analysts is necessary for data nerds to focus more efficiently on what skills they need to learn for their future job. This dashboard is only the beginning of that journey. \n 
""")

st.markdown("### 📈 Data")
st.markdown(f"""
            Data used from Kaggle dataset by Luke
Data is collected daily from Google job postings search results; specifically, [searching for Data Analyst in the United States](https://serpapi.com/playground?engine=google_jobs&q=Data+Analyst&location=United+States&gl=us&hl=en). 👇🏼 \n
Serpapi doesn't provide data for India region, planning to have a data pipeline for scraping Indian jobs to have a large dataset soon.
""")

st.markdown("### 🔗 Links")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### [🐙 GitHub](https://github.com/encrebidle)")
    # st.image('images/octocat.png', width=150)
    st.write("Source code for project")

with col2:
    st.markdown("### [🗂️ Kaggle](https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search)")
    # st.image('images/kaggle.png', width=125)
    st.write("Dataset used with further details")
