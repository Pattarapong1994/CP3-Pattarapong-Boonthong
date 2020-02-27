user_login = input("User ID: ")
password_login = input("PASSWORD: ")
if user_login == "admin" and password_login == "123456":
    print("----Welcom to Porz Shop----")
    Banana_price = 10
    Apple_price = 15
    Orange_price = 7
    Mango_price = 16
    print("1.Banana Price:", Banana_price, "THB")
    print("2.Apple Price:", Apple_price, "THB")
    print("3.Orange Price:", Orange_price, "THB")
    print("4.Mango Price:", Mango_price, "THB")
    user_Select = int(input("Select Number: "))
    amount = int(input("Amount:"))
    if user_Select == 1:
        print("Banana Amount:", amount, "ea", "Total Price:", Banana_price * amount, "THB")
    elif user_Select == 2:
        print("Apple Amount:", amount,"ea", "Total Price:", Apple_price * amount, "THB")
    elif user_Select == 3:
        print("Orange Amount:", amount,"ea", "Total Price:", Orange_price * amount, "THB")
    elif user_Select == 4:
        print("Mongo Amount:", amount,"ea", "Total Price:", Mango_price * amount, "THB")
else:
    print("USER or PASSWORD is wrong!!")