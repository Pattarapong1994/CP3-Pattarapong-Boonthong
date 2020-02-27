def login():
    user_login = input("User ID: ")
    password_login = input("PASSWORD: ")
    if user_login == "admin" and password_login == "123456":
        print("login Success !!")
        return showMenu()
    else:
        print("try Agian !!")
        return login()
def showMenu():
    print("----Porz_Shop----")
    print("1. vat calculator")
    print("2. price caculator")
    return munuSelect()
def munuSelect():
    User_Select = int(input("=>"))
    if User_Select == 1:
        return vatcalculate(int(input("price: ")))
    elif User_Select ==2:
        return pricecaclulate()
def vatcalculate(totalprice):
    vat = 7
    print("Total price: ", totalprice + (totalprice * 7 / 100))
def pricecaclulate():
    price01 = int(input("First Product Price: "))
    price02 = int(input("Second Product Price: "))
    return vatcalculate (price01 + price02)
login()