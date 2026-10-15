import streamlit as st
import button_formats as bf
import data_manager as dm


bf.apply_custom_layout()

selected_card = st.query_params.get("selected")


if selected_card:
    st.markdown("""
        <div style="
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: sans-serif;
        ">
            <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px;">Loading...</div>
        </div>
    """, unsafe_allow_html=True)

if selected_card == "chinese_food": st.switch_page("pages/1_ChineseFood.py")
elif selected_card == "malay_food": st.switch_page("pages/2_MalayFood.py")
elif selected_card == "indian_food": st.switch_page("pages/3_IndianFood.py")
elif selected_card == "checkout": st.switch_page("pages/4_Checkout.py")



st.title("Restaurant Name, ig")
st.header("Menu")

col1, col2, col3 = st.columns(3)

with col1:
    bf.vertical_button("CHINESE FOOD", "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8", "chinese_food")
with col2:
    bf.vertical_button("MALAY FOOD", "https://images.unsplash.com/photo-1552611052-33e04de081de", "malay_food")
with col3:
    bf.vertical_button("INDIAN FOOD", "https://images.unsplash.com/photo-1562967916-eb82221dfb92", "indian_food")

bf.floating_checkout_button(total_price="RM" + f"{dm.get_total():.2f}", key="checkout")

# https://images.getrecipekit.com/20231116072724-c2-a9andy_cooks_thumbnails_nasi_lemak_01.jpg?aspect_ratio=4:3&quality=90&
