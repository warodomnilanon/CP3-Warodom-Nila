menuList = []
priceList = []

def showBill():
    print("---- My Food ----")
    for numberBill in range(len(menuList)):
        print(menuList[numberBill],priceList[numberBill])
    print("Total: ", sum(priceList))


while True:
    mennuName = input("Please Enter Menu : ")
    if  (mennuName.lower() == "exit"): # .lower() will make data in front of it all low
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(mennuName)   # add data in menuList
        priceList.append(menuPrice)   # add data in menuList
showBill()

