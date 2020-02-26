user_login = input("User ID: ")
password_login = input("PASSWORD: ")
if user_login == "admin" and password_login == "123456":
    print("----Welcom to Porz Shop----")
    a = "Banana"
    a_price = 10
    b = "Apple"
    b_price = 15
    c = "Orange"
    c_price = 7
    d = "Mango"
    d_price = 16
    print("1.",a,"Price:",a_price,"THB")
    print("2.",b,"Price:",b_price,"THB")
    print("3.",c,"Price:",c_price,"THB")
    print("4.",d,"Price:",d_price,"THB")
    user_Select = int(input("Select Number: "))
    amount = int(input("Amount:"))
    if user_Select == 1:
        print(a,"Amount:", amount,"ea")
        print("Total Price:",a_price * amount,"THB")
    elif user_Select == 2:
        print(b,"Amount:", amount,"ea")
        print("Total Price:",b_price * amount,"THB")
    elif user_Select == 3:
        print(c,"Amount:", amount,"ea")
        print("Total Price:", c_price * amount,"THB")
    elif user_Select == 4:
        print(d,"Amount:", amount,"ea")
        print("Total Price:",d_price * amount,"THB")
else:
    print("USER or PASSWORD is wrong!!")