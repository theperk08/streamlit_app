import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello Wilders, bienvenue sur mon application !')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_cars = pd.read_csv(link)

df_cars


viz_correlation = sns.heatmap(df_cars.corr(), 

								center=0,

								cmap = sns.color_palette("vlag", as_cmap=True)

								)


st.pyplot(viz_correlation.figure)