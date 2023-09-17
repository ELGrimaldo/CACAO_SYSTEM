import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
#     df = pd.read_csv('../Databox_1_smoothened.csv')
    st.title("Streamlit App in Django")
    

    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

        # Streamlit app code here

if __name__ == "__main__":
    main()