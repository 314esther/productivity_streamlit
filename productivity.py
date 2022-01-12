import streamlit as st
import plotly.express as px
import math

st.markdown("""
    <style>
    .css-1d391kg{
        padding: 1em 1em;
    }
    .css-12oz5g7{
    	padding: 1rem 1rem 10rem;
    }
    </style>
""", unsafe_allow_html=True)

scarcity_slider = 50
incentive_slider = 50
intrinsic_slider = 50
automation_slider = 50

title="Simulating Economies Through the Ages"

st.header(title)


#st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">'+title+'</div>', unsafe_allow_html=True)


st.sidebar.header("INPUTS")
st.subheader("OUTPUTS")

#col1, col2, col3 = st.columns([1,1,1])

radio_value = st.sidebar.radio('Choose an Age:',('Testbed','🏭 Industrial Age','🖥️ Modern Age','🌏🖨️ Makerism Age'))

#st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


if radio_value == '🏭 Industrial Age':
	scarcity_slider = 75
	incentive_slider = 100
	intrinsic_slider = 100
	automation_slider = 20

if radio_value == '🖥️ Modern Age':
	scarcity_slider = 30
	incentive_slider = 100
	intrinsic_slider = 100
	automation_slider = 50

if radio_value == '🌏🖨️ Makerism Age':
	scarcity_slider = 0
	incentive_slider = 0
	intrinsic_slider = 100
	automation_slider = 100

categories = ["extrinsic motivation","productivity"]
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


values = [extrinsic_motivation, productivity]
df=px.data.tips()

fig = px.bar(df,x=values,y=categories, color=['not','highlight'], orientation='h')
fig.update_layout(xaxis=dict(
        range=[0,100],
    ),
	showlegend=False)

st.write(fig)

