A = (3, 7)
B = (8, 2)

sum_A = sum(A)
sum_B = sum(B)

print(f"Sum of A: {sum_A}")
print(f"Sum of B: {sum_B}")

if sum_A > sum_B:
    print("Sum of A is greater")
elif sum_B > sum_A:
    print("Sum of B is greater")
else:
    print("Sums are equal")