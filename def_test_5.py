def check_discount(total_price, ticket_quantity, coupon_code):
    if (coupon_code == "NONTONSERU" and ticket_quantity >= 2):
        print ("Harga tiket: ", total_price - 15000)
    else:
        print ("Harga tiket: ", total_price)
    return
total_price = 50000
ticket_quantity = 2
coupon_code = "NONTONSERU"
print(check_discount(total_price, ticket_quantity, coupon_code))