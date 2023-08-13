
# Residential Real Estate Dashboard

This Streamlit application provides a visual overview of various metrics related to residential real estate properties, such as traffic, weather, noise levels, Airbnb density, property appreciation, and sun/shade projection.

## Features:
1. **Interactive Map**: Displays property locations. Users can select a specific property to view its detailed metrics.
2. **Dynamic Visualizations**: Line charts display the hourly variation of traffic, weather, noise levels, and sun/shade projection. A specific threshold for noise levels is highlighted, with values exceeding this threshold emphasized in red.
3. **Property Metrics**: Shows Airbnb density and yearly property appreciation for the selected property.

## Setup:

1. Ensure you have Python installed. You can download and install Python from [here](https://www.python.org/downloads/).
   
2. Install necessary libraries:
   ```
   pip install streamlit pandas numpy matplotlib
   ```

3. Clone or download this repository to your local machine.

## Usage:

1. Navigate to the directory containing the Streamlit script (`dashboard.py`).
   
2. Run the Streamlit application:
   ```
   streamlit run dashboard.py
   ```

3. The application will open in your default web browser. Interact with the map to select a property and view its detailed metrics.

---

