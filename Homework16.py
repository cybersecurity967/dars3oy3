warehouse = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}

total = 0
max_qty = 0
max_item = ""
min_qty = 999  
min_item = ""

for item in warehouse:
    qty = warehouse[item]
    total += qty
    
    if qty > max_qty:
        max_qty = qty
        max_item = item
        
    if qty < min_qty:
        min_qty = qty
        min_item = item

print(f"Most: {max_item} ({max_qty} pcs)")
print(f"Least: {min_item} ({min_qty} pcs)")
print(f"Total products: {total} pcs")
