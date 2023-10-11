import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import streamlit as st


df = pd.read_csv("https://github.com/Makram57/Streamlit1/blob/main/housing.csv",encoding='utf-8')


st.header("The following plot shows the average house price in America per location",divider='rainbow')
st.markdown("<span style='font-size: 20px;'>:red[Use the below filters to filter the results for a better visual]</span>", unsafe_allow_html=True)


selected_proximity = st.selectbox("Select Ocean Proximity", df['ocean_proximity'].unique())


min_age = int(df['housing_median_age'].min())
max_age = int(df['housing_median_age'].max())
selected_age_range = st.slider("Select Housing Median Age Range", min_age, max_age, (min_age, max_age))


filtered_df = df[(df['ocean_proximity'] == selected_proximity) & (df['housing_median_age'] >= selected_age_range[0]) & (df['housing_median_age'] <= selected_age_range[1])]

fig = px.scatter_mapbox(filtered_df,
                        lon='longitude',
                        lat='latitude',
                        color='median_house_value',
                        size='population',
                        mapbox_style='carto-positron',
                        center={'lat': 37.5, 'lon': 240},
                        zoom=4.5)

fig.update_layout(mapbox=dict(
    bearing=70,
    pitch=30,
))


sea_layer = {
    'below': 'traces',
    'sourcetype': 'raster',
    'source': [
        'https://basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}.png'
    ],
    'opacity': 1,
    'type': 'raster',
}

land_layer = {
    'below': 'traces',
    'sourcetype': 'raster',
    'source': [
        'https://basemaps.cartocdn.com/rastertiles/voyager_labels/{z}/{x}/{y}.png'
    ],
    'opacity': 1,
    'type': 'raster',
}

fig.update_layout(mapbox_layers=[sea_layer, land_layer])
fig.update_layout(title=f"Average House price per location in America - Ocean Proximity: {selected_proximity}")

st.header("",divider='rainbow')
st.plotly_chart(fig, use_container_width=True)

