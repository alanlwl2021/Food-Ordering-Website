from pathlib import Path
import sys
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))
import button_formats as bf
import data_manager as dm


bf.apply_custom_layout()
selected_item = st.query_params.get("selected")


st.title("Malay Food")

if selected_item in dm.FOOD_ITEMS:
    st.query_params.clear()

    item = dm.FOOD_ITEMS[selected_item]
    bf.confirm_purchase(item["name"], item["price"], selected_item)

elif selected_item == "checkout":
    st.switch_page("pages/4_Checkout.py")
elif selected_item == "menu":
    st.switch_page("MainMenu.py")

bf.food_item_row(
    dm.FOOD_ITEMS["nasi_lemak"]["name"],
    "https://images.getrecipekit.com/20231116072724-c2-a9andy_cooks_thumbnails_nasi_lemak_01.jpg?aspect_ratio=4:3&quality=90&",
    "RM" + f"{dm.FOOD_ITEMS["nasi_lemak"]["price"]:.2f}",
    "nasi_lemak",
)

bf.food_item_row(
    dm.FOOD_ITEMS["rendang"]["name"],
    "https://www.dapurkobe.co.id/wp-content/uploads/rendang-daging.jpg",
    "RM" + f"{dm.FOOD_ITEMS["rendang"]["price"]:.2f}",
    "rendang",
)

bf.food_item_row(
    dm.FOOD_ITEMS["nasi_goreng"]["name"],
    "https://cdn.rasa.my/2025/06/Elina-Top-Image-22-696x385.jpg.webp",
    "RM" + f"{dm.FOOD_ITEMS["nasi_goreng"]["price"]:.2f}",
    "nasi_goreng",
)

bf.food_item_row(
    dm.FOOD_ITEMS["sate"]["name"],
    "https://themuddledpantry.com/wp-content/uploads/2015/10/img_2123_edited-480x640.jpg",
    "RM" + f"{dm.FOOD_ITEMS["sate"]["price"]:.2f}",
    "sate",
)

bf.food_item_row(
    dm.FOOD_ITEMS["nasi_kerabu"]["name"],
    "https://scontent-kul3-1.xx.fbcdn.net/v/t39.30808-6/650084796_1759263408578888_95547003031146076_n.jpg?stp=dst-jpg_tt6&cstp=mx1080x1440&ctp=s1080x1440&_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=aafV6AHZFxIQ7kNvwFkUvvz&_nc_oc=Adp6FtYs4Mq4lVIBZmLg05VW7xtb1Vv8VoIxrgOrFlp1RPb9DXFd6LtY8RdDj918Uys&_nc_zt=23&_nc_ht=scontent-kul3-1.xx&_nc_gid=EzDCkBqUDv1UOttHG2lVpw&_nc_ss=7b289&oh=00_AQN4MW6XVk42JqS16dWq6jT0oAoXrCBZd-T8N-j27m6Jcw&oe=6AD77F23",
    "RM" + f"{dm.FOOD_ITEMS["nasi_kerabu"]["price"]:.2f}",
    "nasi_kerabu",
)

bf.floating_checkout_button()
bf.floating_menu_button()
