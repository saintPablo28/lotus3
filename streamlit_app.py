from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Lotus 3


Teacher Dashboard


"""






total_points = st.slider("Number of AI Practice Questions", 1, 5000, 2000)
num_turns = st.slider("Difficulty of Practice Set", 1, 100, 9)

"""
Progression of practice questions on difficulty index [0.0-2.0]


"""



Point = namedtuple('Point', 'x y')
data = []

points_per_turn = total_points / num_turns

for curr_point_num in range(total_points):
    curr_turn, i = divmod(curr_point_num, points_per_turn)
    angle = (curr_turn + 1) * 2 * 2 * i / points_per_turn
    radius = curr_point_num / total_points
    x = radius * np.random.randint(1,3)
    y = radius * np.random.randint(1,3)
    data.append(Point(x, y))

st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    .mark_circle(color='#0068c9', opacity=0.5)
    .encode(x='x:Q', y='y:Q'))


st.write("Average Class Correct Response Rate:")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
    
    
st.write("Raw Student Response Data")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)




"""
Built in Collaboration with IBM Corporation and Palantir Inc.
---------------

© Ye Institute for Innovators 2022 

"""
