import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataChart:
    
    def __init__(self) -> None:
        pass

def main():
#     df = pd.read_csv('../Databox_1_smoothened.csv')
    
    

    chart_data = pd.DataFrame(
    np.random.randn(20, 5),
    columns=['MQ-2', 'MQ-3', 'MQ-7', 'MQ-9', 'MQ-135'])

    st.title("Fermentation Box 1")
    st.line_chart(chart_data)
    
    st.title("Fermentation Box 2")
    st.line_chart(chart_data)
    
    st.title("Fermentation Box 3")
    st.line_chart(chart_data)
    
    st.title("Fermentation Box 4")
    st.line_chart(chart_data)
    

if __name__ == "__main__":
    main()