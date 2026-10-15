from pathlib import Path
import sys
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent))
import button_formats as bf
import data_manager as dm

# Handle item removal via URL query parameters
remove_idx = st.query_params.get("remove")
if remove_idx is not None:
    try:
        idx = int(remove_idx)
        orders = dm.load_order()
        if 0 <= idx < len(orders):
            orders.pop(idx)
            dm.save_order(orders)
            st.query_params.clear()
            st.rerun()
    except ValueError:
        pass

st.title("Order Checkout")

orders = dm.load_order()

if not orders:
    st.info("Your cart is empty!")
else:
    html_rows = ""
    for idx, order_key in enumerate(orders):
        if order_key in dm.FOOD_ITEMS:
            item_name = dm.FOOD_ITEMS[order_key]["name"]
            item_price = f"RM{dm.FOOD_ITEMS[order_key]['price']:.2f}"

            html_rows += f"""
              <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.08); vertical-align: middle;">
                <td style="padding: 12px 8px; font-size: 16px; font-weight: 700; color: #ffffff;">{item_name}</td>
                <td style="padding: 12px 8px; font-size: 16px; color: #ffffff;">{item_price}</td>
                <td style="padding: 12px 8px; text-align: center;">
                    <a href="?remove={idx}" target="_self" style="
                        display: inline-block;
                        background-color: transparent;
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        color: #ff4d4d;
                        padding: 4px 10px;
                        border-radius: 6px;
                        text-decoration: none;
                        font-weight: bold;
                        font-size: 14px;
                    ">&#10005;</a>
                </td>
              </tr>
            """

    total_price = dm.get_total()

    complete_table = f"""
    <div style="width: 100%;">
        <table style="width:100%; border-collapse: collapse; font-family: sans-serif; margin-bottom: 20px;">
          <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.2); text-align: left;">
            <th style="padding: 12px 8px; font-size: 14px; font-weight: 600; color: #aaa;">Item</th>
            <th style="padding: 12px 8px; font-size: 14px; font-weight: 600; color: #aaa;">Price</th>
            <th style="padding: 12px 8px; font-size: 14px; font-weight: 600; color: #aaa; text-align: center; width: 80px;">Action</th>
          </tr>
          {html_rows}
          <tr style="border-top: 2px solid rgba(255, 255, 255, 0.2); vertical-align: middle;">
            <td style="padding: 15px 8px; font-size: 18px; font-weight: 800; color: #ffffff;">TOTAL</td>
            <td style="padding: 15px 8px; font-size: 18px; font-weight: 800; color: #ffffff;" colspan="2">RM{total_price:.2f}</td>
          </tr>
        </table>
    </div>
    """

    if hasattr(st, "html"):
        st.html(complete_table)
    else:
        st.markdown(f"<div>{complete_table}</div>", unsafe_allow_html=True)

if st.button("Checkout", type="primary", use_container_width=True):
    # Optional: clear the cart file here if you want
    # dm.save_order([])
    st.switch_page("pages/5_Final.py")
