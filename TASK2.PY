stocks = {"TATA":2000, "TOYOTA":2500, "BMW":3000}

total = 0

while True:
    name = input("Enter stock (or done): ").upper()
    if name == "DONE":
        break
    
    qty = int(input("Enter quantity: "))
    total += stocks[name] * qty

print("Total Investment =", total)
