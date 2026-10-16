from pathlib import Path
import sys
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))
import data_manager as dm

st.title("Checkout")

st.success(f"Thank you! Your total will be RM{dm.get_total():.2f}.")

if st.button("Return to Main Menu"):
    st.switch_page("MainMenu.py")
