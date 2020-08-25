import streamlit as st
import plotly.express as px
import plotly.io as pio
import pandas as pd

# data
b1_data = pd.read_csv('../data/b1_2019.csv')

st.title('Bleagu Data')

# sidemenu
st.sidebar.markdown(
    "# Sidebar"
)
template = st.sidebar.selectbox(
    "Template", list(pio.templates.keys())
)

arena = st.sidebar.selectbox(
    "Arena", list(b1_data.arena.unique())
)

# body
# st.write(
#     px.bar(b1_data, x="home_team", y="attendance", color="home_victory", barmode="group", template=template)
# )

filtered_df = b1_data[b1_data.arena == arena]
st.write(
    px.bar(filtered_df, x="home_team", y="attendance", color="home_victory", barmode="group", template=template)
)
