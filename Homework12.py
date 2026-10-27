codes = ["A12", "B15", "A12", "C20", "B15", "D10"]

unique_codes = set(codes)
count = len(unique_codes)

codes_str = ""
for code in unique_codes:
    codes_str += code + " "

print(f"Unique codes count: {count}")
print(f"Codes: {codes_str}")