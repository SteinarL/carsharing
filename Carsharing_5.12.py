import streamlit as st
import numpy as np
import pandas as pd

private_gsheets_url = https://docs.google.com/spreadsheets/d/1yX5ncdE9e0fTgUcYQJ2RtBF3wg8TFd-cdTnBLh1V2T0/edit?usp=sharing
[gcp_service_account]
"type": "service_account",
"project_id": "phrasal-catwalk-371010",
"private_key_id": "a89dceeae8eeef024dfc7d6507cd524256258b42",
"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCLqd2cSdrtTz0+\nkNSexrGDgpv1aG270GtEs5cj4EcHZrE5z4mdbx82SghUhMPUv2YpjYRvuLD1vkO+\n3k7i+7WBvboDzJ24It5BwzpIXKKakACxSy74XV0aaUqVX73ueOjIm995nXjQpAAt\nxglygvAD/NlhdIbpPr6ovCnaZYq4c1gsjDm6IsAD+Yde1hAlVJEjvslreLoCB/Tu\nzkafb3TNwCxd0VQP73ibmlrcxANBez2Obvs7YUyMtCB1w93fY09H3gxrEJoyQQcs\nhUo9lI6QKefPbSbMSNNO4EbT+xdf96Dt62D0Rv3L/lztFcxJVus3dJFxyDR0KPMn\nP2R3oWS/AgMBAAECggEAApLTxSWGlcoDPanNNw/qcBKjOBGdYzvTHJgkUu8l9C8x\nahqp4hOd4y/pcqaWLVgN8j6JxXCWcNrw+8T4VCnSwubm7p9S2Z8lQz5+aCThYPkk\nREI3o5bXxTANtHsBmQ+m1v72cIpKeLtaPrDiNkhGZEnAtwjHXE52x81lbLR0gBmm\npZZLX9nZEOCPGjwRbGwSS7mE9AWpG7vp06bDgUqgpGEb9oPQe/WmyeLbqTuB/ndT\ni7bcmFcb/7RsAgBb2nqWpJU+/Tsx6MgJu4EWNmGESTnRd0rO9o1ROq4nscn7FcD/\nRMNawRGkBq2q1pEB794xR7YSOqOxMdD7eMkqSfXpZQKBgQC/vuVgPPpX/WNCBLnV\nDqbc4/ayn0AOjPQzx6RV1Xrt6k8tl5LYztdIFMR87HKM48GsHdn5Sqn5mOdGrU7h\noQl4Tmt9Y8G44DRGYn9o3OlkGGqHtiBPVFADCNC2Bm4gl9ZcbBQKfpbItfA83v6e\n756S0WRWglIFRAbXjGxzrtc7awKBgQC6dwxOfrNaDsOrEhzBaU3iFMJ0dw6bAimh\n8S/7++8vUOgUUGKh07BHSv8PSnQm0FABE5b77wMg68EnTtr7F0JVRFR4RfP48px7\no0Zu7UA0kDd+rAGVFyYBcpaI4SZ9LD108nTuQdLh0H9M6TPZ1WgyoRceRdV8Ssx7\nirDvvXoE/QKBgFo4A80IY/JKsw05FAb/YdvFFypsa8Ns5uoGIXiRfcm72Y1mKB4D\nFKBBxUHSLwPDljjZwtndG6TpIMjMerUHBGGq5ECXU2sdcvs7FR/N8bK7GkTImOM6\nlHsZBrrew6pqRt4trDBT57aAhIzfj4ZQ0JfcFg3uO5FmtKFu3QiBV5wJAoGAdPCm\nUjAZsPgjdI0WZaHyC0Bzt3DXQxV3IK3PJxwYJDd8ZQkI4m6NVhjNnzxVXeY01of/\nn56E+sd/ynQk12X93tXMl+VfHZih1NRQHs9B/fUYKKQdFfB/kFbZ25xAdC4jmM1Z\n0faMF7yXqZdzQkEZaO8oPX8UZS/P0Abp8mCFPs0CgYBR11dqXsi08X4S1ft5XrJh\nc9tiiV2Ol7bg87jGYptOmeY2svLMBmqAIW7Twour32DLKWps8FUMjxcOcCslC/MI\npBEG+eYpcjU7M2jiPkF/yvz5Ky4WLChzqS2tHYMn7OGyRf4xwpNKyEC5xg/gWKPc\n9dqZZmglJBn6yUwllq5Ykg==\n-----END PRIVATE KEY-----\n",
"client_email": "carsharing@phrasal-catwalk-371010.iam.gserviceaccount.com",
"client_id": "109636337076246681549",
"auth_uri": "https://accounts.google.com/o/oauth2/auth",
"token_uri": "https://oauth2.googleapis.com/token",
"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/carsharing%40phrasal-catwalk-371010.iam.gserviceaccount.com"


#1: Create a new bridging dictionary:
#drivers_input = {}
#drivers_list = []

#2: Loop or inputs will continue to run as long as it changes to False:
#drivers_open = True

#3: While True it will:
#4: Add the [] to the dictionary as Key, and add the inputs as values:
#while drivers_open:

    with st.form(key="my_form"):
#4: Add the [] to the dictionary as Key, and add the inputs as values:
        drivers_input['Name'] = st.text_input("Please enter your name:", key=1)
        drivers_input['Departure'] = st.selectbox("From where do you want to leave?", ("Santos", "Nova SBE"))
        drivers_input['Arrival'] = st.selectbox("Where do you want to go?", ("Nova SBE", "Santos"))
        drivers_input['Departure_time'] = st.selectbox("At what time will you leave?", ("8 AM", "12 PM", "4 PM", "8 PM"))
        drivers_input['Free_capacity'] = st.number_input("How many free spots do you have?", min_value=1, max_value=10, step=1)

#5: Ask if all entered data was correct. If yes, we end the loop and inputs are added to drivers_input dictionary:
        correct_input = st.form_submit_button(label="Publish ride")
        if correct_input: 
            drivers_open = False
    
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

