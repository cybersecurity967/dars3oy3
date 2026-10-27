balance = int(input("Initial balance: "))
addition = int(input("Weekly addition: "))
weeks = 0

while balance <= 500000:
    balance += addition
    weeks += 1

print(f"Required weeks: {weeks}")