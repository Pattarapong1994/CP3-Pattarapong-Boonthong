hight = int(input("Please Enter a Height: "))
for i in range(hight):
    spece = " " * (hight - (i + 1))
    star = "*" * ((i * 2) + 1)
    print(spece + star)