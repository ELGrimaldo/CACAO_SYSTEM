import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh

# Restart session variables
# for key in st.session_state.keys():
#     del st.session_state[key]

# Configure to wide page layout
st.set_page_config(layout="wide")

# Auto rerun this script every 5 seconds
st_autorefresh(interval=5000)

# --- [START] Session variables --- #
# Starting index
if 'box_start_idx' not in st.session_state:
    st.session_state['box_start_idx'] = 1

# Ending index
if 'box_end_idx' not in st.session_state:
    st.session_state['box_end_idx'] = 3000

# Data points
if 'box_data' not in st.session_state:
    st.session_state['box_data'] = {
        'MQ2': [],
        'MQ3': [],
        'MQ7': [],
        'MQ9': [],
        'MQ135': []
    }

# Prediction
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = 'UNFERMENTED'
# --- [END] Session variables --- #

# Fetch data from the box
def read_box_data():
    ip_add = "127.0.0.1"                      # IP address of URL
    port = "8000"                             # Port number
    start = st.session_state['box_start_idx'] # Query start index
    end = st.session_state['box_end_idx']     # Query end index

    # Make a request of sensor data and cacao beans fermentation degree prediction
    response = requests.get(f"http://{ip_add}:{port}/get_box_data/{start}/{end}/").json()

    # Store the response in session state so that it can be used to display data in chart and table
    if response['status'] == 'COMPLETE':
        # Store moving average data in session state
        st.session_state['box_data']['MQ2'].append(response['mq2_ave'])
        st.session_state['box_data']['MQ3'].append(response['mq3_ave'])
        st.session_state['box_data']['MQ7'].append(response['mq7_ave'])
        st.session_state['box_data']['MQ9'].append(response['mq9_ave'])
        st.session_state['box_data']['MQ135'].append(response['mq135_ave'])

        # Store prediction in session state
        if response['prediction'] == 0:
            st.session_state['prediction'] = 'UNFERMENTED'

        else:
            st.session_state['prediction'] = 'FERMENTED'

        # Move the moving average window by 1 step, so that the next moving average can be calculated
        st.session_state['box_start_idx'] = st.session_state['box_start_idx'] + 1
        st.session_state['box_end_idx'] = st.session_state['box_end_idx'] + 1
    
# Make a data request every 5 seconds
read_box_data()

# --- [START] Box chart --- #
st.write("# Box Data")

# Take 4 columns for chart, 2 columns for table
box_chart_col, box_table_col = st.columns([4, 2])

# Extract box data from session state, then put it in a data frame 
# so that it can be used for plotting and displaying in table
box_data = pd.DataFrame(st.session_state['box_data'])

# Display chart
box_chart_col.subheader("Cacao Beans Gas Levels")
box_chart_col.line_chart(box_data)

# Display table
box_table_col.subheader("Raw Readings")
box_table_col.write(box_data)

# Print out fermentation degree
st.write(f"Fermentation degree: {st.session_state['prediction']}")
# --- [END] Box chart --- #
