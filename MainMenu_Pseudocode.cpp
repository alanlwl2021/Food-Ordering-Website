START

string input;
float order_total;
vector<string> order_list;

string selected_food;
float selected_price;
int quantity;

string c1, c2, c3, c4, c5;
string m1, m2, m3, m4, m5;
string i1, i2, i3, i4, i5;
float c1p, c2p, c3p, c4p, c5p;
float m1p, m2p, m3p, m4p, m5p;
float i1p, i2p, i3p, i4p, i5p;

c1 = "Hokkien Mee", c1p = 7.5;
c2 = "Char Kuey Teow", c2p = 6.0;
c3 = "Bak Kut Teh", c3p = 10.0;
c4 = "Chicken Rice", c4p = 5.5;
c5 = "Laksa", c5p = 4.5;

m1 = "Nasi Lemak", m1p = 1.5;
m2 = "Rendang", m2p = 6.0;
m3 = "Nasi Goreng", m3p = 5.5;
m4 = "Sate", m4p = 1.0;
m5 = "Nasi Kerabu", m5p = 7.0;

i1 = "Roti Canai", i1p = 1.0;
i2 = "Biryani", i2p = 9.0;
i3 = "Samosas", i3p = 1.5;
i4 = "Nasi Kandar", i4p = 8.0;
i5 = "Thosai", i5p = 2.0;

order_total = 0

int MainMenu()
{
    DISPLAY "Malay Food", "Chinese Food", "Indian Food";
    DISPLAY "goto Checkout";

    READ input;
    switch(input) {
        case "Malay Food": MalayFood();
        case "Chinese Food": ChineseFood();
        case "Indian Food": IndianFood();
        case "goto Checkout": Checkout();
        default: DISPLAY "Error: unrecognized option";
                return 0;
    }
}


// MAIN CODE

MainMenu();
END
