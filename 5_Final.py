import streamlit as st

st.title("Checkout")

st.success("Thank you!")

if st.button("Return to Main Menu"):
    st.switch_page("MainMenu.py")
