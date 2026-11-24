for i in range(3):
    pin = input("Enter your pin:")

    if pin == "1234":
        print("Welcome Jaffar")
        balance = 5000

        while True:

            print("\n1. Check balance")
            print("2. Withdraw cash")
            print("3. deposit money")
            print("4. Exit")

            try:
              choice = int(input("\nChoose an option:"))

            except ValueError:
               print("Please enter numbers only!")     
               continue      
            
            if choice == 1:
                print(f"Your Balance is :{balance}")

            elif choice == 2:
                
                try:
                  amount = float(input("Enter withdrawl amount:"))
                
                except ValueError:
                    print("Please enter numbers only!")
                    continue
                
                if amount <= balance and amount > 0:
                    
                    balance -= amount
                    print(f"\nYour amount {amount} has been withdrawled")

                elif amount > balance:
                    print("Insufficent Funds")

                else:
                    print("Amount must be greater than zero")

            elif choice == 3:
                try:
                  amount = float(input("Enter deposit amount:"))

                except ValueError:
                    print("Please enter numbers only!")
                    continue
                
                if amount <= 20000 and amount > 0:
                    balance += amount
                    print("Please insert the cash amount in the ATM")

                elif amount > 20000:
                    print("This amount cannot be deposited \n Please Enter a lesser amount: ")

                else:
                    print("Amount must be greater than Zero")

            elif choice == 4:
                print("\n Thank you for using this ATM!")
                break


            else:
                print("Please choose a correct option")

    else:
        print("Please Enter a valid pin")

else:
    print("Too many attempts")