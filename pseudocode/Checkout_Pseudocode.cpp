int Checkout() {
    DISPLAY "Order Checkout";
    DISPLAY "goto Menu";

    for (int i = 0; i <= order_list.size(); i++) {
        DISPLAY order_list[i];
    }
    DISPLAY "Total: RM" + order_total;
    DISPLAY "Checkout";
    READ input;
    switch (input) {
        case "goto Menu": MainMenu();
        case "Checkout": {
            DISPLAY "Thank you";
            DISPLAY "Ordered Food:";
            for (int i = 0; i <= order_list.size(); i++) {
                DISPLAY order_list[i];
            }
            DISPLAY "Total: RM" + order_total;
            return 0;
        }
        default: DISPLAY "Error: unrecognized option";
                return 0;
    }
}
