stock = 12

while stock > 0:
    sold = int(input("Sold: "))
    
    if sold <= stock:
        stock -= sold
        print(f"Left: {stock}")
    else:
        print("Not enough stock!")

print("Warehouse is empty")