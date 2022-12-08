import streamlit as st
import numpy as np
import pandas as pd



#1: Create a new bridging dictionary:
drivers_input = {}
drivers_list = []

#2: Loop or inputs will continue to run as long as it changes to False:
drivers_open = True

#3: While True it will:
#4: Add the [] to the dictionary as Key, and add the inputs as values:
while drivers_open:

tab1, tab2 = st.tabs(["Drivers", "Passengers"])
with tab1:
    #4: Add the [] to the dictionary as Key, and add the inputs as values:
    drivers_input['Name'] = st.text_input("Please enter your name:")
    drivers_input['Departure'] = st.selectbox("From where do you want to leave?", ("Santos", "Nova SBE"))
    drivers_input['Arrival'] = st.selectbox("Where do you want to go?", ("Nova SBE", "Santos"))
    drivers_input['Departure_time'] = st.selectbox("At what time will you leave?", ("8 AM", "12 PM", "4 PM", "8 PM"))
    drivers_input['Free_capacity'] = st.number_input("How many free spots do you have?", min_value=1, max_value=10, step=1)

    #5: Ask if all entered data was correct. If yes, we end the loop and inputs are added to drivers_input dictionary:
           
    
#5: Ask if all entered data was correct. If yes, we end the loop and inputs are added to drivers_input dictionary:
    #correct_input = st.button("Do you want to save and publish this ride?")
    #if correct_input:
        #drivers_open = False


#6: Now, we append the drivers_input dictionary to the drivers_list:
drivers_input_copy = drivers_input.copy()
drivers_list.append(drivers_input.copy())

#7: And can clear the drivers_input dictionary for a new entry. 
drivers_input.clear()

drivers_list = [
    {
        "Name" : "Max",
        "Departure": "Santos",
        "Arrival": "Nova_SBE",
        "Departure_time": "8AM",
        "Free_capacity": 0,
        "Passengers": [],
    },
    {
        "Name" : "Paul",
        "Departure": "Santos",
        "Arrival": "Nova_SBE",
        "Departure_time": "10AM",
        "Free_capacity": 4,
        "Passengers": [],
    }
]

