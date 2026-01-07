import numpy as np
import streamlit as st
#e user inputs:- Weight (kg) (number input)- Height (cm) (number input)
#On button click, calculate BMI = weight / (height/100)^2.- Display:
 # - BMI Value
  #- A health category (Underweight, Normal, Overweight, Obese)- Show results in colored messages (st.success(), st.warning(), st.error())
  # .
st.set_page_config(
    page_title='BMI Calculator',
    page_icon='OIP.jfif',
    layout='wide'
  )
st.title('BMI Calculator App')
weight=st.number_input('Weight',20,250,65)
height=st.number_input('Height',55,300,165)
if st.button('Generate BMI on imput'):
    if height<0:
        st.error('Height cannot be zero')
    else:
        height_m=height/100
        bmi=weight/(height_m**2)
        st.success(f'Your bmi is:{bmi}')
        if bmi<18:
            st.warning('Underweight')
        elif 18<=bmi<24:
            st.success('Normal')
        elif 24<=bmi<30:
            st.warning('Overweight')
        else:
            st.error('Obese')