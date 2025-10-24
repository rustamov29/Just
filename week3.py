print("=== Car Wash Service Calculator ===")
print("Enter service package: basic, deluxe, or premium")
print("Type 'done' when finished selecting services")

subtotal = 0.0

while True:
    service = input("\nEnter service package: ").lower()
    if service == "done":
        break
    elif service == "basic":
        price = 10.0
    elif service == "deluxe":
        price = 17.0
    elif service == "premium":
        price = 25.0
    else:
        print("Invalid input, try again.")
        continue

    subtotal += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${subtotal:.2f}")

if subtotal >= 45.0:
    membership_savings = 6.0
else:
    membership_savings = 0.0
final_total = subtotal - membership_savings

print("\n=== Service Summary ===")
print(f"Subtotal: ${subtotal:.2f}")
if membership_savings > 0:
    print(f"Membership Savings: -${membership_savings:.2f}")
else:
    print(f"Membership Savings: ${membership_savings}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for choosing our service!")