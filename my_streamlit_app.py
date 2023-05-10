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

st.write("Tout d'abord une heatmap de corrélation :")

fig = make_subplots(rows = 1, cols = 1)

fig.add_trace(go.Heatmap(x=df_cars.columns[:-1],
		 	y = df_cars.columns[:-1],
			z = df_cars.corr(numeric_only=True),colorscale = 'Picnic'),				
			row = 1,
			col = 1)
st.plotly_chart(fig)

st.write("Ainsi qu'un pairplot des différentes données :")

fig0 = sns.pairplot(df_cars, hue = 'continent')	
st.pyplot(fig0)

st.write("D'un coup d'oeil on peut s'apercevoir que :")
st.write('- le volume (cubicinches), les Chevaux-Vapeur (HP) et le poids (weights) sont fortement corrélés')
st.write('- les véhicules américains se distinguent des japonais et des européens comme étant plus lourds, plus puissants et plus rapides')
st.write('Maintenant, fais-toi plaisir et choisis la région :')


col_1, col_2, col_3 = st.columns(3)
with col_2:
	with st.form('form_1'):
		region1 = st.selectbox("Region : ",[' Europe.', ' US.', ' Japan.'])
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

	fig = px.scatter(df_region, x = 'weightlbs', y ='mpg' )
	
	fig.update_traces(showlegend=True) #trendlines have showlegend=False by default
	

	st.plotly_chart(fig)
