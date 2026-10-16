import json
from pathlib import Path

# CART_FILE = Path("cart_data.json")
ORDER_FILE = Path("order_data.json")

FOOD_ITEMS = {
    "hokkien_mee": {"name": "HOKKIEN MEE", "price": 7.50},
    "ckt": {"name": "CHAR KWAY TEOW", "price": 6.00},
    "bkt": {"name": "BAK KUT TEH", "price": 10.00},
    "chicken_rice": {"name": "CHICKEN RICE", "price": 5.50},
    "laksa": {"name": "LAKSA", "price": 4.50},

    "nasi_lemak": {"name": "NASI LEMAK", "price": 1.50},
    "rendang": {"name": "RENDANG", "price": 6.00},
    "nasi_goreng": {"name": "NASI GORENG", "price": 5.50},
    "sate": {"name": "SATE", "price": 1.00},
    "nasi_kerabu": {"name": "NASI KERABU", "price": 7.00},

    "roti_canai": {"name": "ROTI CANAI", "price": 1.00},
    "biryani": {"name": "BIRYANI", "price": 9.00},
    "samosas": {"name": "SAMOSAS", "price": 1.50},
    "nasi_kandar": {"name": "NASI KANDAR", "price": 8.00},
    "thosai": {"name": "THOSAI", "price": 2.00},
}

# def load_cart_total() -> float:
#     if CART_FILE.exists():
#         try:
#             with open(CART_FILE, "r") as f:
#                 data = json.load(f)
#                 return float(data.get("total_price", 0.0))
#         except (json.JSONDecodeError, ValueError):
#             return 0.0
#     return 0.0

# def save_cart_total(new_total: float):
#     with open(CART_FILE, "w") as f:
#         json.dump({"total_price": new_total}, f)

# def add_to_cart_total(amount: float):
#     current = load_cart_total()
#     save_cart_total(current + amount)



def load_order() -> list:
    if ORDER_FILE.exists():
        try:
            with open(ORDER_FILE, "r") as f:
                data = json.load(f)
                return data.get("items", [])
        except (json.JSONDecodeError, ValueError):
            return []
    return []

def add_order(food_name: str):
    items = load_order()
    items.append(food_name)
    save_order(items)

def save_order(items: list):
    with open(ORDER_FILE, "w") as f:
        json.dump({"items": items}, f, indent=4)

def get_total():
    total = 0
    orders = load_order()
    for o in orders:
        total += FOOD_ITEMS[o]["price"]
    return total
