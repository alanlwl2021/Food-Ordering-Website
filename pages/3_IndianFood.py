from pathlib import Path
import sys
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))
import button_formats as bf
import data_manager as dm


bf.apply_custom_layout()
selected_item = st.query_params.get("selected")


st.title("Indian Food")

if selected_item in dm.FOOD_ITEMS:
    st.query_params.clear()

    item = dm.FOOD_ITEMS[selected_item]
    bf.confirm_purchase(item["name"], item["price"], selected_item)

elif selected_item == "checkout":
    st.switch_page("pages/4_Checkout.py")
elif selected_item == "menu":
    st.switch_page("MainMenu.py")

bf.food_item_row(
    dm.FOOD_ITEMS["roti_canai"]["name"],
    "https://www.elmundoeats.com/wp-content/uploads/2017/11/Roti-Canai-3.jpg",
    "RM" + f"{dm.FOOD_ITEMS["roti_canai"]["price"]:.2f}",
    "roti_canai",
)
bf.food_item_row(
    dm.FOOD_ITEMS["biryani"]["name"],
    "https://holycowvegan.net/wp-content/uploads/2023/01/vegetable-biryani-32.jpg",
    "RM" + f"{dm.FOOD_ITEMS["biryani"]["price"]:.2f}",
    "biryani",
)

bf.food_item_row(
    dm.FOOD_ITEMS["samosas"]["name"],
    "https://www.recipetineats.com/tachyon/2021/02/Samosas.jpg?resize=900%2C1125&zoom=0.72",
    "RM" + f"{dm.FOOD_ITEMS["samosas"]["price"]:.2f}",
    "samosas",
)

bf.food_item_row(
    dm.FOOD_ITEMS["nasi_kandar"]["name"],
    "https://upload.wikimedia.org/wikipedia/commons/4/4c/Nasi_kandar_Al_hilal.jpg?utm_source=ban.wikipedia.org&utm_campaign=index&utm_content=original",
    "RM" + f"{dm.FOOD_ITEMS["nasi_kandar"]["price"]:.2f}",
    "nasi_kandar",
)

bf.food_item_row(
    dm.FOOD_ITEMS["thosai"]["name"],
    "https://assets.tmecosys.com/image/upload/t_web_rdp_recipe_584x480_1_5x/img/recipe/ras/Assets/F11196CB-3766-4B34-BE2D-6DA648378159/Derivates/f5e4e9b9-c2c2-4445-b196-5d536156e0ce.jpg",
    "RM" + f"{dm.FOOD_ITEMS["thosai"]["price"]:.2f}",
    "thosai",
)

bf.floating_checkout_button()
bf.floating_menu_button()
