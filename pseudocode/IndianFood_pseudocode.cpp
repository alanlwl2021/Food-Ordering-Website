int IndianFood() {
    DISPLAY "Indian Food";
    DISPLAY i1, i1p, i2, i2p, i3, i3p, i4, i4p, i5, i5p;
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
            case i1: selected_food = i1;
                    selected_price = i1p;
            case i2: selected_food = i2;
                    selected_price = i2p;
            case i3: selected_food = i3;
                    selected_price = i3p;
            case i4: selected_food = i4;
                    selected_price = i4p;
            case i5: selected_food = i5;
                    selected_price = i5p;
            default: DISPLAY "Error: unrecognized option";
                    return 0;
                    break;
        }

        quantity = 1;
        while true {
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
                    DISPLAY "Successfully ordered " + quantity + selected_food + "for RM" + selected_price*quantity;
                    break;
            }
        }
    }


    return 0;
}
