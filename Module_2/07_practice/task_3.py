players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

fixed_players = []
for key, value in players.items():
    fixed_players.append(key + value)
print(fixed_players)
