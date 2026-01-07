import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import datetime as dt
import time
#Build a Streamlit app with:- Sidebar to select a country from a dropdown (India, USA, UK, Canada)- Number input for Total Population- Number input for Vaccinated People- A button that, when clicked, calculates and displays the vaccination percentage- Display results with a progress bar and a success/warning message depending on whether the vaccination rate is above 
#70%
st.set_page_config(
    page_title='Vaccination Drive',
    page_icon='OIP.jfif',
    layout='wide'
)
st.sidebar.title('Vaccination Calculator')
st.title('Vaccination Drive for People')
s=st.sidebar.selectbox('Countries',['India','USA','Canada','UK'])
if s=='USA':
   pop=st.number_input('Enter USA population')
   vac=st.number_input('No of vaccinations completed')
   st.write(f"Total population is:{pop}")
   if st.button("Calculate Vacciantion Percentage:"):
      if pop<=0:
         st.error('Population cannot be zero')
      else:
         progress=st.progress(0)
         for i in range(101):
            time.sleep(0.01)
            progress.progress(i)
         per=(vac/pop)*100
         if per>=70:
            st.success(f"Good job:{per}")
         else:
            st.warning(f"Not good:{per}")     
