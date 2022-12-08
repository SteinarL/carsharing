import streamlit as st
import numpy as np
import pandas as pd


# Setting up the tabs
tabs = st.tabs(["Drivers", "Passengers"])

tab_drivers = tabs[0]

     
    #4: Add the [] to the dictionary as Key, and add the inputs as values:
        drivers_input['Name'] = st.text_input("Please enter your name:", key=1)
        drivers_input['Departure'] = st.selectbox("From where do you want to leave?", ("Santos", "Nova SBE"))
        drivers_input['Arrival'] = st.selectbox("Where do you want to go?", ("Nova SBE", "Santos"))
        drivers_input['Departure_time'] = st.selectbox("At what time will you leave?", ("8 AM", "12 PM", "4 PM", "8 PM"))
        drivers_input['Free_capacity'] = st.number_input("How many free spots do you have?", min_value=1, max_value=10, step=1)

    #5: Ask if all entered data was correct. If yes, we end the loop and inputs are added to drivers_input dictionary:
       
        
tab_passengers = tabs[1]
        
      
        requests_input['Departure_P'] = st.selectbox("From where do you want to leave?", ("Santos", "Nova SBE"))
        requests_input['Arrival_P'] = st.selectbox("From where do you want to leave?", ("Nova SBE", "Santos"))
        requests_input['Departure_time_P'] = st.selectbox("At what time do you wish to leave?", ("8 AM", "12 PM", "4 PM", "8 PM"))
         
