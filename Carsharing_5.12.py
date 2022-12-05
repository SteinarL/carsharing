import streamlit as st

original_title = '<p style="font-family:Helvetica; color:#458B74; font-size: 30px;">Welcome to the NOVA rideshare platform!</p>'
st.markdown(original_title, unsafe_allow_html=True)

driver_dictionary = {
        "Departure": "Santos",
        "Destination": "Nova SBE",
        "Departure_Time": "4 PM",
        "Free_capacity": 4,
        "Passengers": [],
        "Full": False
        }


tabs = st.tabs(["Passengers", "Drivers"])

tab_passengers = tabs[0]
with tab_passengers:
        
        with st.form(key='my_form'): # <-- Everything is in a form to have a submission button. The button doesn't really do anything for now 
                                        # but could perhaps be used for sending a signal to check inputs with driver availability.
                
                st.write("Please select the wished time of departure and your destination.")
                # SELECTION OF DEPARTURE TIME
                passenger_dept_time = st.radio(
                    "When would you need a ride?",
                    ("8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "4 PM", "8 PM"))

                if passenger_dept_time in driver_dictionary["Departure_Time"]:
                    st.write("Slot secured.") 
                else: 
                    st.write("No drivers available.")

                # SELECTION OF DESTINATION
                passenger_destination = st.radio(
                        "What is your destination?",
                        ("Nova SBE", "Santos"))
                if passenger_destination in driver_dictionary["Destination"]:
                        st.write("Driver available for selected destination.")
                else:
                    st.write("No driver available for selected destination.")

                submit_button = st.form_submit_button(label='Submit your need')
                if submit_button:
                        st.write("Your need has been submitted.")
                
tab_drivers = tabs[1]
with tab_drivers:
        # SELECTION OF DRIVER AVAILABILITY
        # Just a copy form above. Hasn't been adapted to drivers yet. 
                # Trying to figure out how to append new times to dictionary when driver selects departure time. 
        driver_time = st.radio(
            "When are you driving?",
            ("8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "4 PM", "8 PM"))

        if driver_time in driver_dictionary["Destination"]:
                st.write("Driver available for selected destination.")

        else:
            st.write("No driver available for selected destination.")
