import json

mock_battle_card = {
    "competitor": "folk",
    "potential_impact": "medium",
    "evidence_status": "hypothetical"
}

with open("mock_battle_card.json", "w") as file:
    json.dump(mock_battle_card, file, indent=2)

with open("mock_battle_card.json", "r") as file:
    loaded_battle_card = json.load(file)

assert loaded_battle_card == mock_battle_card