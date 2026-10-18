int MalayFood() {
    DISPLAY "Malay Food";
    DISPLAY m1, m1p, m2, m2p, m3, m3p, m4, m4p, m5, m5p;
    DISPLAY "goto Menu", "goto Checkout";

    while true {
        READ input;
        switch(input) {
            bool food_pressed = false;
            case "goto Menu":
                MainMenu();
                break;
            case "goto Checkout":
                Checkout();
                break;
            case m1: selected_food = m1;
                    selected_price = m1p;
            case m2: selected_food = m2;
                    selected_price = m2p;
            case m3: selected_food = m3;
                    selected_price = m3p;
            case m4: selected_food = m4;
                    selected_price = m4p;
            case m5: selected_food = m5;
                    selected_price = m5p;
            default: DISPLAY "Error: unrecognized option";
                    return 0;
                    break;
        }

        quantity = 1;
        DISPLAY "Confirm Order";
        DISPLAY "Add" + selected_food + "for RM" + selected_price + "each?";
        while true {
            DISPLAY "Quantity: " + quantity;
            DISPLAY "+", "-", "Confirm", "Cancel";
            DISPLAY "Subtotal: " + selected_price * quantity;
            READ input;
            switch(input) {
                case "+":
                    quantity++;
                case "-":
                    if (quantity>1) {
                        quantity--;
                    }
                case "cancel":
                    break;
                case "confirm":
                    order_total += selected_price*quantity;
                    order_list.insert(order_list.end(), quantity, selected_food);
                    DISPLAY "Successfully added " + quantity + selected_food + "for RM" + selected_price*quantity;
                    break;
            }
        }
    }


    return 0;
}
