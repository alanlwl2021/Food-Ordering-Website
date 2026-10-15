from pathlib import Path
import sys
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))
import button_formats as bf
import data_manager as dm

FOOD_ITEMS = {
    "nasi_lemak": {"name": "NASI LEMAK", "price": 10.50},
    "ckt": {"name": "CHAR KWAY TEOW", "price": 8.90},
}

bf.apply_custom_layout()
selected_item = st.query_params.get("selected")


st.title("Chinese Food")

if selected_item in dm.FOOD_ITEMS:
    st.query_params.clear()

    item = dm.FOOD_ITEMS[selected_item]
    bf.confirm_purchase(item["name"], item["price"], selected_item)

elif selected_item == "checkout":
    st.switch_page("pages/4_Checkout.py")

bf.food_item_row(
    dm.FOOD_ITEMS["nasi_lemak"]["name"],
    "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8",
    "RM" + f"{dm.FOOD_ITEMS["nasi_lemak"]["price"]:.2f}",
    "nasi_lemak",
)
bf.food_item_row(
    dm.FOOD_ITEMS["ckt"]["name"],
    "https://images.unsplash.com/photo-1552611052-33e04de081de",
    "RM" + f"{dm.FOOD_ITEMS["ckt"]["price"]:.2f}",
    "ckt",
)

bf.floating_checkout_button(total_price="RM" + f"{dm.get_total():.2f}", key="checkout")
