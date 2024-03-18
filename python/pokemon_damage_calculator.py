# https://www.codewars.com/kata/536e9a7973130a06eb000e9f/

def calculate_damage(your_type, opponent_type, attack, defense):
    modifier = {"fire": {"fire": .5, "water": .5, "grass": 2., "electric": 1.},
                "water": {"fire": 2., "water": .5, "grass": .5, "electric": .5},
                "grass": {"fire": .5, "water": 2., "grass": .5, "electric": 1.},
                "electric": {"fire": 1., "water": 2., "grass": 1., "electric": .5}}

    return 50 * (attack / defense) * modifier[your_type][opponent_type]

print(f"fire fire: {calculate_damage('fire', 'fire', 1, 50)}")
print(f"fire water: {calculate_damage('fire', 'water', 1, 50)}")
print(f"fire grass: {calculate_damage('fire', 'grass', 1, 50)}")
print(f"fire electric: {calculate_damage('fire', 'electric', 1, 50)}")
print(f"water fire: {calculate_damage('water', 'fire', 1, 50)}")
print(f"water water: {calculate_damage('water', 'water', 1, 50)}")
print(f"water grass: {calculate_damage('water', 'grass', 1, 50)}")
print(f"water electric: {calculate_damage('water', 'electric', 1, 50)}")
print(f"grass fire: {calculate_damage('grass', 'fire', 1, 50)}")
print(f"grass water: {calculate_damage('grass', 'water', 1, 50)}")
print(f"grass grass: {calculate_damage('grass', 'grass', 1, 50)}")
print(f"grass electric: {calculate_damage('grass', 'electric', 1, 50)}")
print(f"electric fire: {calculate_damage('electric', 'fire', 1, 50)}")
print(f"electric water: {calculate_damage('electric', 'water', 1, 50)}")
print(f"electric grass: {calculate_damage('electric', 'grass', 1, 50)}")
print(f"electric electric: {calculate_damage('electric', 'electric', 1, 50)}")