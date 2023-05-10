import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import plotly.express as px
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
				z = df_cars.corr(numeric_only=True),colorscale = 'Picnic'),				
				row = 1,
				col = 1)
	st.plotly_chart(fig)

# mpg by year
with col_b:
	st.write("Ainsi qu'un scatterplot volume/nombre de cylindres :")
	fig2 = make_subplots(rows = 1, cols = 1)
	fig2.add_trace(go.Scatter(x=df_cars['cylinders'],
			 	y = df_cars['cubicinches'],
				mode = 'markers'),
				row = 1,
				col = 1)


	st.plotly_chart(fig2)

st.write('Maintenant, fais-toi plaisir et choisis la région :')



with st.form('form_1'):
	region1 = st.selectbox("Region : ",
	                           [' Europe.', ' US.', ' Japan.'])
	        
	submit1 = st.form_submit_button("OK !")
	    
if submit1:
	#st.write(region)
	st.write('''
	  - pour visualiser le nombre de chevaux-vapeur (CV)
	  en fonction du nombre de cylindres :
	  ''')
	df_region = df_cars[df_cars['continent'] == region1]
	df_region = df_region.sort_values(by = 'cylinders')	
	fig_bar1 = make_subplots(rows = 1, cols = 1)
	cylinders = [3, 4, 6, 8]
	for cylinder in cylinders:
		fig_bar1.add_trace(go.Violin(x = df_region['cylinders'][df_region['cylinders'] == cylinder],
			y = df_region['hp'][df_region['cylinders'] == cylinder],
			 ))
	fig_bar1.update_layout(title = dict({'text' : 'Chevaux-vapeur par nombre de cylindres', 'x' : 0.3}))
	fig_bar1.update_xaxes(title=dict({'text' : 'Nombre de cylindres'}))
	fig_bar1.update_yaxes(title=dict({'text' : 'Nombre de Chevaux-Vapeur'}))
	st.plotly_chart(fig_bar1)		


	st.write('''
	 - pour visualiser le temps d'accélaration de 0 à 60mph
	 en fonction des années :
	''')

	
		
	fig_bar2 = make_subplots(rows = 1, cols = 1)
	fig_bar2.add_trace(go.Scatter(x = df_region['year'], y = df_region['time-to-60'],
			 #labels = {'year' : 'Année', 'time-to-60': 'De 0 à 60 mph en ... secondes'}
			 mode = 'markers'))
	fig_bar2.update_layout(title = dict({'text' : "Temps d'accélaration de 0 à 60mph, par année", 'x' : 0.3}))
	fig_bar2.update_xaxes(title=dict({'text' : 'Année de production'}))
	fig_bar2.update_yaxes(title=dict({'text' : 'De 0 à 60 mph en ... secondes'}))

	st.plotly_chart(fig_bar2)


	st.write('''
	 - pour visualiser la distance parcourue (mpg)
	 en fonction du poids (en livres) :
	''')

	
		
	#fig_bar3 = make_subplots(rows = 1, cols = 1)
	#fig_bar3.add_trace(go.Scatter( x = df_region['weightlbs'], y = df_region['mpg'], mode = 'markers'))
	#fig_bar3.update_layout(title = dict({'text' : "Distance parcourue (mpg) en fonction du poids", 'x' : 0.3}))
	#fig_bar3.update_xaxes(title=dict({'text' : 'Poids (livres)'}))
	#fig_bar3.update_yaxes(title=dict({'text' : 'Distance parcourue (mpg)'}))

	fig = px.scatter(df_region, x = 'weightlbs', y ='mpg',  trendline="ols", trendline_scope="overall"
                )
	
	fig.update_traces(showlegend=True) #trendlines have showlegend=False by default
	

	st.plotly_chart(fig)