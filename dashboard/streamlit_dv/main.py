import streamlit as st
import pandas as pd
import numpy as np
import requests
from streamlit_autorefresh import st_autorefresh

# Restart session variables
# for key in st.session_state.keys():
#     del st.session_state[key]

# Configure to wide page layout
st.set_page_config(layout="wide")

# Auto rerun this script every 5 seconds
st_autorefresh(interval=5000)

# Title
st.write("# Cacao Project by Oompa Loompas 👋")

# --- [START] Session variables --- #

## Starting indices
if 'box_one_start' not in st.session_state:
    st.session_state['box_one_start'] = 1

if 'box_two_start' not in st.session_state:
    st.session_state['box_two_start'] = 1

if 'box_three_start' not in st.session_state:
    st.session_state['box_three_start'] = 1

if 'box_four_start' not in st.session_state:
    st.session_state['box_four_start'] = 1

## Ending indices
if 'box_one_end' not in st.session_state:
    st.session_state['box_one_end'] = 3000

if 'box_two_end' not in st.session_state:
    st.session_state['box_two_end'] = 3000

if 'box_three_end' not in st.session_state:
    st.session_state['box_three_end'] = 3000

if 'box_four_end' not in st.session_state:
    st.session_state['box_four_end'] = 3000

## Data points
if 'box_one_data' not in st.session_state:
    st.session_state['box_one_data'] = {
        'MQ2': [],
        'MQ3': [],
        'MQ7': [],
        'MQ9': [],
        'MQ135': []
    }

if 'box_two_data' not in st.session_state:
    st.session_state['box_two_data'] = {
        'MQ2': [],
        'MQ3': [],
        'MQ7': [],
        'MQ9': [],
        'MQ135': []
    }

if 'box_three_data' not in st.session_state:
    st.session_state['box_three_data'] = {
        'MQ2': [],
        'MQ3': [],
        'MQ7': [],
        'MQ9': [],
        'MQ135': []
    }

if 'box_four_data' not in st.session_state:
    st.session_state['box_four_data'] = {
        'MQ2': [],
        'MQ3': [],
        'MQ7': [],
        'MQ9': [],
        'MQ135': []
    }
# --- [END] Session variables --- #

# --- [START] Helper functions for fetching data points for each box --- #

## Fetch data for box one (1)
def read_box_one_data():
    response = requests.get(f"http://127.0.0.1:8000/get_box_one_data/{st.session_state['box_one_start']}/{st.session_state['box_one_end']}/").json()
    if response['status'] == 'COMPLETE':
        st.session_state['box_one_data']['MQ2'].append(response['mq2_ave'])
        st.session_state['box_one_data']['MQ3'].append(response['mq3_ave'])
        st.session_state['box_one_data']['MQ7'].append(response['mq7_ave'])
        st.session_state['box_one_data']['MQ9'].append(response['mq9_ave'])
        st.session_state['box_one_data']['MQ135'].append(response['mq135_ave'])
        st.session_state['box_one_start'] = st.session_state['box_one_start'] + 1
        st.session_state['box_one_end'] = st.session_state['box_one_end'] + 1

## Fetch data for box two (2)
def read_box_two_data():
    response = requests.get(f"http://127.0.0.1:8000/get_box_two_data/{st.session_state['box_two_start']}/{st.session_state['box_two_end']}/").json()
    if response['status'] == 'COMPLETE':
        st.session_state['box_two_data']['MQ2'].append(response['mq2_ave'])
        st.session_state['box_two_data']['MQ3'].append(response['mq3_ave'])
        st.session_state['box_two_data']['MQ7'].append(response['mq7_ave'])
        st.session_state['box_two_data']['MQ9'].append(response['mq9_ave'])
        st.session_state['box_two_data']['MQ135'].append(response['mq135_ave'])
        st.session_state['box_two_start'] = st.session_state['box_two_start'] + 1
        st.session_state['box_two_end'] = st.session_state['box_two_end'] + 1

## Fetch data for box three (3)
def read_box_three_data():
    response = requests.get(f"http://127.0.0.1:8000/get_box_three_data/{st.session_state['box_three_start']}/{st.session_state['box_three_end']}/").json()
    if response['status'] == 'COMPLETE':
        st.session_state['box_three_data']['MQ2'].append(response['mq2_ave'])
        st.session_state['box_three_data']['MQ3'].append(response['mq3_ave'])
        st.session_state['box_three_data']['MQ7'].append(response['mq7_ave'])
        st.session_state['box_three_data']['MQ9'].append(response['mq9_ave'])
        st.session_state['box_three_data']['MQ135'].append(response['mq135_ave'])
        st.session_state['box_three_start'] = st.session_state['box_three_start'] + 1
        st.session_state['box_three_end'] = st.session_state['box_three_end'] + 1

## Fetch data for box four (4)
def read_box_four_data():
    response = requests.get(f"http://127.0.0.1:8000/get_box_four_data/{st.session_state['box_four_start']}/{st.session_state['box_four_end']}/").json()
    if response['status'] == 'COMPLETE':
        st.session_state['box_four_data']['MQ2'].append(response['mq2_ave'])
        st.session_state['box_four_data']['MQ3'].append(response['mq3_ave'])
        st.session_state['box_four_data']['MQ7'].append(response['mq7_ave'])
        st.session_state['box_four_data']['MQ9'].append(response['mq9_ave'])
        st.session_state['box_four_data']['MQ135'].append(response['mq135_ave'])
        st.session_state['box_four_start'] = st.session_state['box_four_start'] + 1
        st.session_state['box_four_end'] = st.session_state['box_four_end'] + 1

## Fetch data for all
def read_data():
    read_box_one_data()
    read_box_two_data()
    read_box_three_data()
    read_box_four_data()
# --- [END] Helper functions for fetching data points for each box --- #

read_data()

# --- [START] Box one chart --- #
st.write("# Box One")

box_1_col_1, box_1_col_2 = st.columns([4, 2])

box_one_chart_data = pd.DataFrame(st.session_state['box_one_data'])

box_1_col_1.subheader("Cacao Beans Gas Levels")
box_1_col_1.line_chart(box_one_chart_data)

box_1_col_2.subheader("Raw Readings")
box_1_col_2.write(box_one_chart_data)
# --- [END] Box one chart --- #

# --- [START] Box two chart --- #
st.write("# Box Two")

box_2_col_1, box_2_col_2 = st.columns([4, 2])

box_two_chart_data = pd.DataFrame(st.session_state['box_two_data'])

box_2_col_1.subheader("Cacao Beans Gas Levels")
box_2_col_1.line_chart(box_two_chart_data)

box_2_col_2.subheader("Raw Readings")
box_2_col_2.write(box_two_chart_data)
# --- [END] Box two chart --- #

# --- [START] Box three chart --- #
st.write("# Box Three")

box_3_col_1, box_3_col_2 = st.columns([4, 2])

box_three_chart_data = pd.DataFrame(st.session_state['box_three_data'])

box_3_col_1.subheader("Cacao Beans Gas Levels")
box_3_col_1.line_chart(box_three_chart_data)

box_3_col_2.subheader("Raw Readings")
box_3_col_2.write(box_three_chart_data)
# --- [END] Box three chart --- #

# --- [START] Box four chart --- #
st.write("# Box Four")

box_4_col_1, box_4_col_2 = st.columns([4, 2])

box_four_chart_data = pd.DataFrame(st.session_state['box_four_data'])

box_4_col_1.subheader("Cacao Beans Gas Levels")
box_4_col_1.line_chart(box_four_chart_data)

box_4_col_2.subheader("Raw Readings")
box_4_col_2.write(box_four_chart_data)
# --- [END] Box four chart --- #

# st.session_state
