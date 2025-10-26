 
import streamlit as st
from src.core.planner import TravelAssist
from dotenv import load_dotenv
load_dotenv(override=True)

st.set_page_config("AI Travel Assistant")
st.title("Travel Planner")

with st.form("Travel Form"):
    city = st.text_input("City Name")
    interest = st.text_input("Interest seprated by comma")
    submit_btn= st.form_submit_button("Plan for me")

    if(submit_btn):
        if city and interest:
            planner = TravelAssist()
            planner.set_city(city)
            planner.set_interest(interest)
            init= planner.create_init()

            st.subheader("Your Plan like this")
            st.markdown(init)
        else:
            st.warning("Enter Data")