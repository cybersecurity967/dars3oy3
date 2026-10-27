votes = {"Ali": "Python", "Vali": "JavaScript", "Madina": "Python", "Jasur": "C++", "Aziza": "Python", "Sardor": "JavaScript"}

vote_counts = {}

for lang in votes.values():
    if lang in vote_counts:
        vote_counts[lang] += 1
    else:
        vote_counts[lang] = 1

max_votes = 0
winner = ""

for lang, count in vote_counts.items():
    print(f"{lang}: {count} votes")
    
    if count > max_votes:
        max_votes = count
        winner = lang

print(f"Winner: {winner}")