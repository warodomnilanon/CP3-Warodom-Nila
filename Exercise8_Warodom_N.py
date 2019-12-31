applePrice = 20
orangePrice = 10
mangoPrice = 40
usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "warodom" and passwordInput == "456789":
    print("----------Welcome to the BG Shop----------")
    print("item 1. apple  20 THB per pic")
    print("item 2. orange 10 THB per pic")
    print("item 3. mango  40 THB per pic")
    print("------------------The End------------------")

    userSelect = input("Select item : ")
    if userSelect == "1" or userSelect == "apple":
        amountApple = int(input("How many pic : "))
        print("------------------------------")
        print("Total : ",applePrice*amountApple, "THB")
        print("----------Thank  You----------")

    elif userSelect == "2" or userSelect == "orange":
        amountOrange = int(input("How many pic : "))
        print("------------------------------")
        print("Total : ",orangePrice*amountOrange, "THB")
        print("----------Thank  You----------")

    elif userSelect == "3" or userSelect == "mango":
        amountMango = int(input("How many pic : "))
        print("------------------------------")
        print("Total : ",mangoPrice*amountMango, "THB")
        print("----------Thank  You----------")

    else:
        print("*** Don't have any item ***")

else:
    print("*** Incorrect Please try again ***")
