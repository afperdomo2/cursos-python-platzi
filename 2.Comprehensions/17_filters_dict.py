matches = [
    {"home": "Colombia", "away": "Brazil", "score": "1-1", "winner": "Draw"},
    {"home": "Argentina", "away": "Chile", "score": "3-0", "winner": "Local"},
    {"home": "Peru", "away": "Uruguay", "score": "0-1", "winner": "Away"},
    {"home": "Bolivia", "away": "Paraguay", "score": "2-2", "winner": "Draw"},
    {"home": "Ecuador", "away": "Venezuela", "score": "1-0", "winner": "Local"},
    {"home": "France", "away": "Germany", "score": "1-0", "winner": "Local"},
    {"home": "Italy", "away": "Spain", "score": "2-3", "winner": "Away"},
    {"home": "Portugal", "away": "England", "score": "2-2", "winner": "Draw"},
    {"home": "Netherlands", "away": "Belgium", "score": "1-1", "winner": "Draw"},
]

print("Matches: ", matches)
print("Matches count: ", len(matches))

draws = list(filter(lambda x: x["winner"] == "Draw", matches))
print("--------")
print("Draws: ", draws)
print("Draws count: ", len(draws))

print("--------")
locals_winners = list(filter(lambda x: x["winner"] == "Local", matches))
print("locals_winners: ", locals_winners)
print("Locals winners count: ", len(locals_winners))

print("--------")
aways_winners = list(filter(lambda x: x["winner"] == "Away", matches))
print("aways_winners: ", aways_winners)
print("Aways winners count: ", len(aways_winners))
