import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
  page_title = "Cars App",
  layout = "wide",
  page_icon = "🚗")

st.title('Hello Wilders, bienvenue sur mon application !')
st.write("Voici un exemple de dataset à analyser :")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_cars = pd.read_csv(link, sep=",")
df_cars

col_a, col_b = st.columns(2)
with col_a:
	st.write("Tout d'abord une heatmap de corrélation :")
	fig = make_subplots(rows = 1, cols = 1)

	fig.add_trace(go.Heatmap(x=df_cars.columns[:-1],
			 	y = df_cars.columns[:-1],
				z = df_cars.corr()),				
				row = 1,
				col = 1)
	st.plotly_chart(fig)
# mpg by year
with col_b:
	st.write("Ainsi qu'un scatterplot mpg/année :")
	fig2 = make_subplots(rows = 1, cols = 1)
	fig2.add_trace(go.Scatter(x=df_cars['year'],
			 	y = df_cars['mpg'],
				mode = 'markers'),
				row = 1,
				col = 1)

	st.plotly_chart(fig2)

st.write('Maintenant, fais-toi plaisir et choisis la région :')

col1, col2 = st.columns(2)

with col1:
	st.write('''
	  - pour visualiser le nombre de chevaux-vapeur (CV)
	  en fonction du nombre de cylindres :
	  ''')
	with st.form('form_1'):
	    region1 = st.selectbox("Region : ",
	                           [' Europe.', ' US.', ' Japan.'])
	        
	    submit1 = st.form_submit_button("OK !")
	    
	if submit1:
		#st.write(region)
		df_region1 = df_cars[df_cars['continent'] == region1]
		df_region1 = df_region1.sort_values(by = 'cylinders')	
		fig_bar1 = make_subplots(rows = 1, cols = 1)
		cylinders = [3, 4, 6, 8]
		for cylinder in cylinders:
			fig_bar1.add_trace(go.Violin(x = df_region1['cylinders'][df_region1['cylinders'] == cylinder],
				y = df_region1['hp'][df_region1['cylinders'] == cylinder],
				 ))
		fig_bar1.update_layout(title = dict({'text' : 'Chevaux-vapeur par nombre de cylindres', 'x' : 0.5}))

		st.plotly_chart(fig_bar1)		

with col2:
	st.write('''
	 - pour visualiser le temps d'accélaration de 0 à 60mph
	 en fonction des années :
	''')
	with st.form('form_2'):
	    region2 = st.selectbox("Region : ",
	                           [' Europe.', ' US.', ' Japan.'])
	        
	    submit2 = st.form_submit_button("OK !")
	    
	if submit2:		
		df_region2 = df_cars[df_cars['continent'] == region2]
		df_region2 = df_region2.sort_values(by = 'cylinders')	
		fig_bar2 = make_subplots(rows = 1, cols = 1)
		fig_bar2.add_trace(go.Scatter(x = df_region2['year'], y = df_region2['time-to-60'],
				 #labels = {'year' : 'Année', 'time-to-60': 'De 0 à 60 mph en ... secondes'}
				 mode = 'markers'),
				 row = 1,
				 col = 1)
		fig_bar2.update_layout(title = dict({'text' : "Temps d'accélaration de 0 à 60, par année", 'x' : 0.5}))

		st.plotly_chart(fig_bar2)
