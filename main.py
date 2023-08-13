import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_mock_data():
    hours = list(range(24))
    traffic = [np.random.randint(50, 200) if 6 < hour < 19 else np.random.randint(10, 50) for hour in hours]
    temperature = [np.random.randint(10, 20) if 0 <= hour <= 6 or 18 <= hour <= 23 else np.random.randint(20, 30) for hour in hours]
    noise_levels = [np.random.randint(40, 70) if 6 < hour < 19 else np.random.randint(20, 40) for hour in hours]
    airbnb_density = np.random.randint(5, 50)
    years = list(range(2018, 2028))
    appreciation = np.random.randint(3, 7, 5).tolist() + np.random.randint(2, 6, 5).tolist()
    sun_shade = [np.random.randint(60, 100) if 6 < hour < 19 else np.random.randint(0, 20) for hour in hours]
    
    return {
        'traffic': pd.DataFrame({'Hour': hours, 'Traffic': traffic}),
        'weather': pd.DataFrame({'Hour': hours, 'Temperature': temperature}),
        'noise': pd.DataFrame({'Hour': hours, 'Noise Level': noise_levels}),
        'airbnb_density': airbnb_density,
        'appreciation': pd.DataFrame({'Year': years, 'Appreciation (%)': appreciation}),
        'sun_shade': pd.DataFrame({'Hour': hours, 'Sun Exposure (%)': sun_shade}),
    }

np.random.seed(42)
num_properties = 10
central_latitude, central_longitude = 37.7749, -122.4194
latitudes = [central_latitude + np.random.uniform(-0.1, 0.1) for _ in range(num_properties)]
longitudes = [central_longitude + np.random.uniform(-0.2, 0.2) for _ in range(num_properties)]
properties_data = []
for lat, lon in zip(latitudes, longitudes):
    property_data = generate_mock_data()
    property_data['latitude'] = lat
    property_data['longitude'] = lon
    properties_data.append(property_data)

st.set_page_config('wide')

st.title('Residential Real Estate Dashboard')

# Property Map
st.header('Property Locations')
locations = [(prop['latitude'], prop['longitude']) for prop in properties_data]
map_data = pd.DataFrame(locations, columns=['lat', 'lon'])
st.map(map_data)

# Select a property
property_index = st.selectbox('Select a property to view details:', range(num_properties))
selected_property = properties_data[property_index]

# Create two columns for visualizations
col1, col2 = st.columns(2)

# Display data in Column 1
with col1:
    st.header('Hyper Local Traffic')
    st.bar_chart(selected_property['traffic'].set_index('Hour'))

    st.header('Weather Data')
    st.table(selected_property['weather'][6:15].set_index('Hour'))

    st.header('Airbnb Density')
    st.write(f'Number of Airbnb properties in the vicinity: {selected_property["airbnb_density"]}')

# Display data in Column 2
with col2:
    st.header('Noise Level Data')
    st.line_chart(selected_property['noise'].set_index('Hour'))

    st.header('Property Appreciation')
    st.line_chart(selected_property['appreciation'].set_index('Year'))

    st.header('Sun/Shade Projection')
    st.line_chart(selected_property['sun_shade'].set_index('Hour'))
