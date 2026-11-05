inv = [["Apple",89,20],["Mango",99,20],["Orange",99,20]]
cart = [0,0,0]
balance = 5000.0
while True:
    print(f"""\n
    ___________________________________________
   |                    Menu                   |
   | __________________________________________|
   |Input 1 to view stock and add item to cart |
   |Input 2 to view bank balance cart items    |
   |Input any key to exit                      |
   |___________________________________________|""")
    a = input()
    if a == "1":
        while True:
            print("\n1. ",inv[0][0],"   Price =",inv[0][1],"  In Stock:",inv[0][2])
            print("2. ",inv[1][0],"   Price =",inv[1][1],"  In Stock:",inv[1][2])
            print("3. ",inv[2][0],"  Price =",inv[2][1],"  In Stock:",inv[2][2])
            print(f"\nInput 1 to add {inv[0][0]} to cart")
            print(f"Input 2 to add {inv[1][0]} to cart")
            print(f"Input 3 to add {inv[2][0]} to cart")
            print("\nInput any key to exit to main menu")
            b = input()
            if b == "1":
                if inv[0][2] != 0:
                    am = input("Enter the amount: ")
                    if am.isdigit():
                        if int(am) <= inv[0][2]:
                            cart[0] += int(am)
                            inv[0][2] -= int(am)
                            print(f"{int(am)} {inv[0][0]} added to cart")
                            continue
                        else:
                            print("Enter a valid amount")
                            continue
                    else:
                        print("Enter a valid amount")
                        continue
                else:
                    print("Out of stock\n")
                    continue
            elif b == "2":
                if inv[1][2] != 0:
                    am = input("Enter the amount: ")
                    if am.isdigit():
                        if int(am) <= inv[1][2]:
                            cart[1] += int(am)
                            inv[1][2] -= int(am)
                            print(f"{int(am)} {inv[1][0]} added to cart")
                            continue
                        else:
                            print("Enter a valid amount")
                            continue
                    else:
                        print("Enter a valid amount")
                        continue
                else:
                    print("Out of stock\n")
                    continue
            elif b == "3":
                if inv[2][2] != 0:
                    am = input("Enter the amount: ")
                    if am.isdigit():
                        if int(am) <= inv[2][2]:
                            cart[2] += int(am)
                            inv[2][2] -= int(am)
                            print(f"{int(am)} {inv[2][0]} added to cart")
                            continue
                        else:
                            print("Enter a valid amount")
                            continue
                    else:
                        print("Enter a valid amount")
                        continue
                else:
                    print("Out of stock\n")
                    continue
            else:
                break
    elif a == "2":
        while True:
            print("Bank Balance:",balance)
            print(f"\n{inv[0][0]}: {cart[0]}  Price = {inv[0][1]*cart[0]}")
            print(f"{inv[1][0]}: {cart[1]}  Price = {inv[1][1]*cart[1]}")
            print(f"{inv[2][0]}: {cart[2]}  Price = {inv[2][1]*cart[2]}\n")
            print("Total amount =",inv[0][1]*cart[0]+inv[1][1]*cart[1]+inv[2][1]*cart[2])
            print("Input 1 to buy")
            print("\nPress any key to exit to main menu")
            c = input()
            if c == "1":
                if cart[0] == 0 and cart[1] == 0 and cart[2] == 0:
                    print("Nothing in cart")
                    break
                elif balance >= inv[0][1]*cart[0]+inv[1][1]*cart[1]+inv[2][1]*cart[2]:
                    balance -= inv[0][1]*cart[0]+inv[1][1]*cart[1]+inv[2][1]*cart[2]
                    cart = [0,0,0]
                else:
                    print("Insufficient Funds")
                    break
            else:
                break
    if a == "1":
        continue
    elif a == "2":
        continue
    else:
        break
print("bye bye")