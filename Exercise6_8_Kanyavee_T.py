
print("Please Login")
username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "1234" :
    print("Welcome to KV Shop")
    print("Please select My Product : ")
    notebookPrice = 20
    print("1. Notebook : @", notebookPrice)
    pencilPrice = 10
    print("2. Pencil : @", pencilPrice)
    bluePen = 5
    print("3. Pen Blue : @", bluePen)
    redPen = 5
    print("4. Pen Red : @", redPen)
    blackPen = 5
    print("5. Pen Black : @", blackPen)
    userSelected = int(input("select My Product  : >> "))
    userCount = int(input("Qty : >> "))
    if userSelected == 1 :
        price = userCount * notebookPrice
        print(price)
    elif userSelected == 2 :
        price = userCount * pencilPrice
        print(price)
    elif userSelected == 3 :
        price = userCount * bluePen
        print(price)
    elif userSelected == 4 :
        price = userCount * redPen
        print(price)
    elif userSelected == 5 :
        price = userCount * blackPen
        print(price)
else :
    print("username or password not correct!!!")


