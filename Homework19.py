cart = {"bread": 4000, "milk": 12000, "eggs": 18000, "oil": 25000}

initial_sum = sum(cart.values())
print(f"Initial sum: {initial_sum} UZS")

cart["sugar"] = 14000

new_sum = sum(cart.values())
print(f"After sugar: {new_sum} UZS")