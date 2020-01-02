def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("-----iShop---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculate(input())
    elif userSelected == 2:
        return priceCalculate()

def vatCalculate(totalPrice):
    vat = 7
    result = int(totalPrice) + (int(totalPrice) * vat / 100)
    return result

def priceCalculate():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatCalculate(price1 + price2)

while login() == False:
    login()
else: print(showMenu())
print("---Thank You---")

