def calculate_bill(bill_text):
    lines = bill_text.split("\n")
    subtotal = 0
    voucher = 0
    tip_rate = 0

    for i in lines:
        clean = i.strip()
        if "TIP:" in clean:
            parts = clean.split(':')
            string = parts[1].strip()
            pct_number = string.replace('%', '')
            tip_rate = float(pct_number) / 100.0

        elif "VOUCHER:" in clean:
            parts = clean.split(':')
            amount = parts[1].strip()
            voucher = float(amount.replace('$', ''))

        elif "#" in clean and "@ $" in clean:
            before_at, after_at = clean.split('@')
            part = before_at.split('#')[1].strip()
            price_part = after_at.replace('$', '').strip()
            quantity = float(part)
            price = float(price_part)

            subtotal += quantity * price
    amount_after_voucher = subtotal - voucher
    grand_total = amount_after_voucher * (1.0 + tip_rate)

    return f"${grand_total:.2f}"

bill1 = """Burger # 2 @ $12.50
Fries # 2 @ $4.00
TIP: 15%
VOUCHER: $5.00"""
print(calculate_bill(bill1))

bill2 = """Steak # 1 @ $30.00
Wine # 1 @ $10.00
TIP: 20%"""
print(calculate_bill(bill2))

bill3 = """Pizza # 1 @ $18.00
Soda # 2 @ $2.50
VOUCHER: $3.00
TIP: 0%"""
print(calculate_bill(bill3))