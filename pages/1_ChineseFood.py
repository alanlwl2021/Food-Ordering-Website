from pathlib import Path
import sys
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))
import button_formats as bf
import data_manager as dm


bf.apply_custom_layout()
selected_item = st.query_params.get("selected")


st.title("Chinese Food")

if selected_item in dm.FOOD_ITEMS:
    st.query_params.clear()

    item = dm.FOOD_ITEMS[selected_item]
    bf.confirm_purchase(item["name"], item["price"], selected_item)

elif selected_item == "checkout":
    st.switch_page("pages/4_Checkout.py")
elif selected_item == "menu":
    st.switch_page("MainMenu.py")

bf.food_item_row(
    dm.FOOD_ITEMS["hokkien_mee"]["name"],
    "https://rasamalaysia.com/wp-content/uploads/2018/05/penang-hokkien-mee.jpg",
    "RM" + f"{dm.FOOD_ITEMS["hokkien_mee"]["price"]:.2f}",
    "hokkien_mee",
)
bf.food_item_row(
    dm.FOOD_ITEMS["ckt"]["name"],
    "https://www.sidechef.com/recipe/844c8140-fc58-42d5-8eff-997aab276bc9.jpeg?d=1408x1120",
    "RM" + f"{dm.FOOD_ITEMS["ckt"]["price"]:.2f}",
    "ckt",
)

bf.food_item_row(
    dm.FOOD_ITEMS["bkt"]["name"],
    "https://noobcook.com/wp-content/uploads/2012/09/klang.jpg",
    "RM" + f"{dm.FOOD_ITEMS["bkt"]["price"]:.2f}",
    "bkt",
)

bf.food_item_row(
    dm.FOOD_ITEMS["chicken_rice"]["name"],
    "https://rasamalaysia.com/wp-content/uploads/2024/11/chicken-rice2.jpg",
    "RM" + f"{dm.FOOD_ITEMS["chicken_rice"]["price"]:.2f}",
    "chicken_rice",
)

bf.food_item_row(
    dm.FOOD_ITEMS["laksa"]["name"],
    "https://www.recipetineats.com/tachyon/2016/09/Laksa.jpg?resize=900%2C1260&zoom=0.72",
    "RM" + f"{dm.FOOD_ITEMS["laksa"]["price"]:.2f}",
    "laksa",
)

bf.floating_checkout_button()
bf.floating_menu_button()
