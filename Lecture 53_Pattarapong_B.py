def vatcalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatcalculate(int(input("Total Price: "))))