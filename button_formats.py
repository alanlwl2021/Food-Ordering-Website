import streamlit as st
import html
import textwrap
import json
import data_manager as dm

def apply_custom_layout():
    st.markdown(
        """
        <style>
        [data-testid="stMainBlockContainer"] {
            padding-right: 180px !important;
            padding-left: 20px !important;
            max-width: 90% !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def food_button(food_name, image_url, key):
    html_code = f"""
    <a href="?selected={key}" target="_self" style="text-decoration: none;">
        <div style="
            display: flex;
            width: 100%;
            height: 120px;
            background-color: #000000;
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            margin-bottom: 15px;
            border: 1px solid #222;
        ">
            <div style="
                flex: 1;
                background-image: linear-gradient(to right, rgba(0,0,0,0) 20%, rgba(0,0,0,1) 100%),
                                  url('{image_url}');
                background-size: cover;
                background-position: center;
            "></div>
            <div style="
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #ffffff;
                font-family: sans-serif;
                font-size: 20px;
                font-weight: 700;
                letter-spacing: 1px;
            ">{food_name}</div>
        </div>
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def vertical_button(food_name, image_url, key):
    formatted_name = food_name.replace('\n', '<br>')

    html_code = f"""
    <a href="?selected={key}" target="_self" style="text-decoration: none;">
        <div style="
            display: flex;
            flex-direction: column;
            width: 100%;
            height: 350px;
            background-color: #000000;
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            margin-bottom: 20px;
            border: 1px solid #333;
            transition: transform 0.2s ease;
            cursor: pointer;
        ">
            <div style="
                flex: 4;
                background-image: linear-gradient(to bottom, rgba(0,0,0,0) 50%, rgba(0,0,0,1) 100%), url('{image_url}');
                background-size: cover;
                background-position: center;
            "></div>
            <div style="
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                background-color: #000000;
                color: #ffffff;
                font-family: sans-serif;
                font-size: 16px;
                font-weight: 700;
                letter-spacing: 1px;
                padding: 0 10px;
                line-height: 1.3;
            ">{formatted_name}</div>
        </div>
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def floating_checkout_button(key="checkout"):
    total_price = f"RM{dm.get_total():.2f}"

    html_code = f"""
    <a href="?selected={key}" target="_self" style="text-decoration: none;">
        <div style="position: fixed; right: 0px; top: 45%; transform: translateY(-50%); width: 160px; height: 180px; background-color: #8B0000; border-top-left-radius: 30px; border-bottom-left-radius: 30px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: -4px 4px 15px rgba(0, 0, 0, 0.5); z-index: 9999; cursor: pointer;">
            <div style="position: absolute; left: 12px; writing-mode: vertical-rl; transform: rotate(180deg); color: #ff4d4d; font-family: sans-serif; font-size: 13px; font-weight: 800; letter-spacing: 2px;">CHECKOUT</div>
            <svg width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 20px; margin-bottom: 8px;">
                <circle cx="9" cy="21" r="1"></circle>
                <circle cx="20" cy="21" r="1"></circle>
                <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
            </svg>
            <div style="color: #ffffff; font-family: sans-serif; font-size: 16px; font-weight: 700; margin-left: 20px;">{total_price}</div>
        </div>
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def floating_menu_button(key="menu"):
    html_code = f"""
    <a href="?selected={key}" target="_self" style="text-decoration: none;">
        <div style="position: fixed; right: 0px; top: 66%; transform: translateY(-50%); width: 140px; height: 110px; background-color: #db6832; border-top-left-radius: 25px; border-bottom-left-radius: 25px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: -4px 4px 15px rgba(0, 0, 0, 0.5); z-index: 9998; cursor: pointer;">
            <div style="position: absolute; left: 12px; writing-mode: vertical-rl; transform: rotate(180deg); color: #ffd1b3; font-family: sans-serif; font-size: 11px; font-weight: 800; letter-spacing: 2px;">MENU</div>
            <svg width="35" height="35" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 15px; margin-bottom: 4px;">
                <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
        </div>
    </a>
    """
    st.markdown(html_code, unsafe_allow_html=True)

@st.dialog("Confirm Purchase")
def confirm_purchase(food_name, price, food_id):
    st.write(f"Add **{food_name}** to your order for **RM{price:.2f}** each?")

    qty = st.number_input(
        "Quantity", min_value=1, value=1, step=1, key="purchase_qty"
    )

    subtotal = price * qty
    st.write(f"Subtotal: **RM{subtotal:.2f}**")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Confirm", type="primary", use_container_width=True):
            for _ in range(int(qty)):
                dm.add_order(food_id)

            st.success(f"Added {int(qty)}x {food_name} to your order!")
            st.query_params.clear()
            st.rerun()

    with col2:
        if st.button("Cancel", use_container_width=True):
            st.query_params.clear()
            st.rerun()

def food_item_row(food_name, image_url, price, key):
    formatted_name = food_name.replace('\n', '<br>')

    col_card, col_price = st.columns([5, 1.2])

    with col_card:
        html_card = f"""<a href="?selected={key}" target="_self" style="text-decoration: none;">
<div style="
display: flex;
flex-direction: row;
width: 100%;
height: 140px;
background-color: #000000;
border-radius: 35px;
overflow: hidden;
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
margin-bottom: 15px;
border: 1px solid #333;
transition: transform 0.2s ease;
cursor: pointer;
">
<div style="
flex: 4;
background-image: linear-gradient(to right, rgba(0,0,0,0) 40%, rgba(0,0,0,1) 100%), url('{image_url}');
background-size: cover;
background-position: center;
"></div>
<div style="
flex: 6;
display: flex;
align-items: center;
justify-content: center;
text-align: center;
background-color: #000000;
color: #ffffff;
font-family: sans-serif;
font-size: 18px;
font-weight: 700;
letter-spacing: 1px;
padding: 0 15px;
line-height: 1.3;
">{formatted_name}</div>
</div>
</a>"""
        st.markdown(html_card, unsafe_allow_html=True)

    with col_price:
        html_price = f"""<div style="
display: flex;
align-items: center;
justify-content: center;
height: 140px;
background-color: #000000;
border-radius: 35px;
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
margin-bottom: 15px;
border: 1px solid #333;
color: #ffffff;
font-family: sans-serif;
font-size: 16px;
font-weight: 700;
">
{price}
</div>"""
        st.markdown(html_price, unsafe_allow_html=True)


