import streamlit as st
import plotly.express as px
import pandas as pd

#------------------------------------------------------------------------------------------------------------------
#Data

df = pd.read_csv("medical_cost.csv")

fig = px.pie(df, values='charges', names='region')

fig1 = px.bar(df.groupby('sex').charges.mean(), color= ['female', 'male'])

fig2 = px.bar(df.groupby('smoker').charges.mean(), color= ['yes', 'no'])

fig3 = px.line(df.groupby('age').charges.min())













#------------------------------------------------------------------------------------------------------------------

st.header("	:mag_right: Visualising the Data")
st.subheader("Visualizing the used data and trying to find reasonable conclusion.")

st.header("Average Cost of Expenses by Region 	:world_map: ")
st.write('The southeast region has the highest  cost for medical expenses, followed by the  northeast region, the northwest region, and the southwest region.')
st.plotly_chart(fig)

st.header("Average Cost of Expenses by Gender ⚥")
st.write('We can say that on an average that male has to spent a little more extra money for medical expenses.')
st.plotly_chart(fig1)

st.header("Can smoking increase the cost :smoking: ??")
st.write('We can see that on an average a smoker has to pay about 3X cost more as comaper to non-smoker.')
st.plotly_chart(fig2)

st.header("Do medical expenses increase overtime :timer_clock: ??")
st.write('We can see that as age increase the cost of bills also increases.')
st.plotly_chart(fig3)