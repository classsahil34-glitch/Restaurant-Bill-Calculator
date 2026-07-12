name=input("Enter your name: ")
amount=float(input("Enter your Bill amount"))
if amount >= 5000:
    discount=amount*0.1
    result=amount-discount
    
    print("------Your Bill------")
    print("\nYour Name: ",name)
    print("\nyour bill: ",amount)
    print("\nYour final bill: ",result)
    
if amount<5000:
        print("------Your Bill------")
        print("\nYour Name: ",name)
        print("\nyour bill: ",amount)
        print("\nNo discount apply")
print("-----Thank you for uisng-----")