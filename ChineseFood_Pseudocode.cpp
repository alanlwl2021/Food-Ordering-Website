int ChineseFood() {
    DISPLAY "Chinese Food";
    DISPLAY c1, c1p, c2, c2p, c3, c3p, c4, c4p, c5, c5p;
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
            case c1: selected_food = c1;
                    selected_price = c1p;
            case c2: selected_food = c2;
                    selected_price = c2p;
            case c3: selected_food = c3;
                    selected_price = c3p;
            case c4: selected_food = c4;
                    selected_price = c4p;
            case c5: selected_food = c5;
                    selected_price = c5p;
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
