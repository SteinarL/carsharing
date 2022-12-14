import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to Nova Carpool!")

tabs = st.tabs(["Drivers", "Passengers"])

tab_drivers = tabs[0]
with tab_drivers:

    st.header("Fill out details for your ride")
    with st.form("my_form"):
                          #4: Add the [] to the dictionary as Key, and add the inputs as values:
        driver_name = st.text_input("Please enter your name:")
        driver_departure = st.selectbox("From where do you want to leave?", ("Santos", "Nova SBE"))
        driver_arrival = st.selectbox("Where do you want to go?", ("Nova SBE", "Santos"))
        driver_time = st.selectbox("At what time will you leave?", ("12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM"))
        driver_cap = st.number_input("How many free spots do you have?", min_value=1, step=1)

        #5: Ask if all entered data was correct. If yes, we end the loop and inputs are added to drivers_input dictionary:
                  
        correct_input = st.form_submit_button(label="Publish ride")
        if correct_input:
            st.write("Your ride has been published and you will be notified if someone requests a seat.")

tab_passengers = tabs[1]
with tab_passengers:

    st.header("When and where do you want to go?")

    with st.form("my_form2"):
                          #4: Add the [] to the dictionary as Key, and add the inputs as values:
        passenger_departure = st.selectbox("From where do you want to leave?", ("Santos", "Nova SBE"))
        passenger_arrival = st.selectbox("Where do you want to go?", ("Nova SBE", "Santos"))
        passenger_time = st.selectbox("At what time will you leave?", ("12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM"))

        #5: Ask if all entered data was correct. If yes, we end the loop and inputs are added to drivers_input dictionary:
                  
        correct_input = st.form_submit_button(label="Request ride")
        if correct_input:
            st.write("Your ride has been requested.")
