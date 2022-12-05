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

# SELECTION OF DEPARTURE TIME
genre = st.radio(
    "When would you need a ride?",
    ("8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "4 PM", "8 PM"))
 
if genre in driver_dictionary["Departure_Time"]:
    st.write("Slot secured.") 
          
else: 
    st.write("No drivers available.")

# SELECTION OF DESTINATION
genre = st.radio(
        "What is your destination?",
        ("Nova SBE", "Santos"))
if genre in driver_dictionary["Destination"]:
        st.write("Driver available for selected destination.")

else:
    st.write("No driver available for selected destination.")
        
        
        






        
