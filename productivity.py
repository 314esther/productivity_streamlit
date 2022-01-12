import streamlit as st
import plotly.express as px
import math

scarcity_slider = 50
incentive_slider = 50
intrinsic_slider = 50
automation_slider = 50

col1, col2, col3 = st.columns([1,1,1])
with col1:
	if st.button('Industrial Age'):
		scarcity_slider = 66
		incentive_slider = 85
		intrinsic_slider = 100
		automation_slider = 30
with col2:
	if st.button('Modern Age'):
		scarcity_slider = 30
		incentive_slider = 100
		intrinsic_slider = 100
		automation_slider = 50

with col3:
	if st.button('Makerism/Automation Age'):
		scarcity_slider = 0
		incentive_slider = 0
		intrinsic_slider = 100
		automation_slider = 100

categories = ["scarcity", "incentive", "extrinsic motivation", "intrinsic_motivation","automation","productivity"]
#category = st.selectbox("Category:", categories)
scarcity_value = st.sidebar.slider("scarcity", 0,100, scarcity_slider)
incentive_value = st.sidebar.slider("incentive", 0,100, incentive_slider)

scarcity = scarcity_value
incentive = incentive_value

intrinsic_motivation = st.sidebar.slider("intrinsic motivation", 0,100, intrinsic_slider)

extrinsic_motivation = ((scarcity/10)*(incentive/10))

automation = st.sidebar.slider("automation", 0,100, automation_slider)

routine_work = (extrinsic_motivation*((100-automation)/100)) + automation*(automation/100)


creative_work = intrinsic_motivation


x = (100-(scarcity))/100


raw_materials = 100-(scarcity)

#if x >= 0.75:
	#raw_materials = 100-(scarcity)
#else:
	#raw_materials = (-1*((2*x-1)**2)+1)*100
#100*math.sqrt(x)
#100*(x/(1+0.5*(1-x)))


productivity = (raw_materials/100)*(routine_work + creative_work)/2


values = [scarcity, incentive, extrinsic_motivation, intrinsic_motivation, automation, productivity]
df=px.data.tips()

fig = px.bar(df,x=values,y=categories, color=['not','not','not','not','not','highlight'], orientation='h')
fig.update_layout(xaxis=dict(
        range=[0,100],
    ),
	showlegend=False)

st.write(fig)

