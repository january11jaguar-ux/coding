def amount():
    try:
        bill = float(input("Enter the total bill amount: "))
        paid = float(input("Enter the amount paid by the customer: "))
        
        if paid >= bill:
            change = paid - bill
            print(f"Bill paid in full. Change to return: ${change:.2f}")
        else:
            remaining_due = bill - paid
            print(f"Partial payment received. Remaining due amount: ${remaining_due:.2f}")
            
    except ValueError:
        print("Please enter a valid number amount.")

amount()
