allowed = {"math", "english", "it", "physics"}
chosen = {"english", "it", "history"}

approved = chosen & allowed

not_approved = chosen - allowed

approved_str = ""
for subject in approved:
    approved_str += subject + " "

not_approved_str = ""
for subject in not_approved:
    not_approved_str += subject + " "

print(f"Allowed: {approved_str}")
print(f"Not allowed: {not_approved_str}")