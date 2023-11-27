import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh

SKIP_DAYS_REFRESH_RATE = 10000
NORM_REFRESH_RATE = 3000

# Restart session variables
# for key in st.session_state.keys():
#     del st.session_state[key]

# Configure to wide page layout
st.set_page_config(layout="wide")

# Starting index
if 'box_start_idx' not in st.session_state:
    st.session_state['box_start_idx'] = 1

# Ending index
if 'box_end_idx' not in st.session_state:
    st.session_state['box_end_idx'] = 3000

# Previously collected data index
if 'box_idx' not in st.session_state:
    st.session_state['box_idx'] = 169010

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

# Auto-refresh rate
if 'refresh_rate' not in st.session_state:
    st.session_state['refresh_rate'] = SKIP_DAYS_REFRESH_RATE

# Data source (Box or ESP32)
if 'data_source' not in st.session_state:
    st.session_state['data_source'] = 'box'

# If data source is box, are we gonna skip days?
if 'skip_days' not in st.session_state:
    st.session_state['skip_days'] = True

if ['box_chart_col', 'box_table_col'] not in st.session_state:
    st.write("# Box Data")
    st.session_state['box_chart_col'], st.session_state['box_table_col'] = st.columns([4, 2])
    st.session_state['box_chart_col'].subheader("Cacao Beans Gas Levels")
    st.session_state['box_table_col'].subheader("Raw Readings")

if 'box_chart' not in st.session_state:
    st.session_state['box_chart'] = st.session_state['box_chart_col'].line_chart()

# Auto rerun this script every x seconds (depends on refresh rate)
st_autorefresh(interval=st.session_state['refresh_rate'])

# Fetch data from the box
def read_box_data():
    ip_add = "127.0.0.1"                      # IP address of URL
    port = "8000"                             # Port number
    start = 0                                 # Query start index
    end = 0                                   # Query end index

    # Check where the data source is coming from
    # If the data source is from box, set the corresponding query index
    if st.session_state['data_source'] == 'box':
        start = st.session_state['box_idx']
    
    # Else, if data source is from ESP32, set the corresponding starting and ending query index
    else:
        start = st.session_state['box_start_idx']
        end = st.session_state['box_end_idx']

    # Make a request of sensor data and cacao beans fermentation degree prediction
    response = requests.get(f"http://{ip_add}:{port}/get_box_data/{start}/{end}/").json()

    # If response status returns COMPLETE, store the response in session state so that it can be used to display data in chart and table
    if response['status'] == 'COMPLETE':

        # If we skipped days, then store the data for those skipped days (this request is only made once)
        # (No prediction is made here)
        if response['skip_days'] == True:
            st.session_state['box_data']['MQ2'].extend(response['mq2_ave'])
            st.session_state['box_data']['MQ3'].extend(response['mq3_ave'])
            st.session_state['box_data']['MQ7'].extend(response['mq7_ave'])
            st.session_state['box_data']['MQ9'].extend(response['mq9_ave'])
            st.session_state['box_data']['MQ135'].extend(response['mq135_ave'])

            # Change the refresh rate back to normal after rendering the large amount of data to the chart and table
            st.session_state['refresh_rate'] = NORM_REFRESH_RATE
            st_autorefresh(interval=st.session_state['refresh_rate'])

        # Else, if we don't skip days, then store the moving average data in session state
        else:
            st.session_state['box_data']['MQ2'].append(response['mq2_ave'])
            st.session_state['box_data']['MQ3'].append(response['mq3_ave'])
            st.session_state['box_data']['MQ7'].append(response['mq7_ave'])
            st.session_state['box_data']['MQ9'].append(response['mq9_ave'])
            st.session_state['box_data']['MQ135'].append(response['mq135_ave'])

            # Then, the prediction in session state
            if response['prediction'] == 0:
                st.session_state['prediction'] = 'UNFERMENTED'

            else:
                st.session_state['prediction'] = 'FERMENTED'

            # Finally, increment the query index
            if st.session_state['data_source'] == 'box':
                st.session_state['box_idx'] = st.session_state['box_idx'] + 1

            else:
                st.session_state['box_start_idx'] = st.session_state['box_start_idx'] + 1
                st.session_state['box_end_idx'] = st.session_state['box_end_idx'] + 1
    
# Make a data request every x seconds (depends on refresh rate)
read_box_data()

# Extract box data from session state, then put it in a data frame 
# so that it can be used for plotting and displaying in table
if st.session_state['skip_days'] == True:
    box_data = pd.DataFrame(st.session_state['box_data'])

    # Display chart
    st.session_state['box_chart'].add_rows(box_data)

    # Display table
    st.session_state['box_table_col'].table(box_data.tail())

    # Set skip_days to False
    st.session_state['skip_days'] = False
    print('Skip days set to False.')

else:
    print('Appending new data to chart.')
    box_data = {
        'MQ2': [st.session_state['box_data']['MQ2'][-1]],
        'MQ3': [st.session_state['box_data']['MQ3'][-1]],
        'MQ7': [st.session_state['box_data']['MQ7'][-1]],
        'MQ9': [st.session_state['box_data']['MQ9'][-1]],
        'MQ135': [st.session_state['box_data']['MQ135'][-1]]
    }
    box_data = pd.DataFrame(box_data)
    st.session_state['box_chart'].add_rows(box_data)
    st.session_state['box_table_col'].table(pd.DataFrame(st.session_state['box_data']).tail())

# Print out fermentation degree
st.write(f"Fermentation degree: {st.session_state['prediction']}")
