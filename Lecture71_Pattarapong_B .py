menulist = []
pricelist = []
def showBill():
    print("Por Shop".center(18,"-"))
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number],"THB")
def totalPrice():
    totalprice = 0
    for i in pricelist:
        totalprice = int(i)+totalprice
    print("Total Price:", totalprice,"THB")
while True:
    menuName = input("Enter your Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price: ")
        menulist.append(menuName)
        pricelist.append(menuPrice)
showBill()
totalPrice()