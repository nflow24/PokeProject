import random
import math

# ---- Pokémon (BST = 400 each) ----
# ---- Pokémon (BST = 400 each) ----
pikachu = {
    "name": "Pikachu",
    "hp": 60,
    "atk": 45,
    "spa": 80,
    "def": 50,
    "spd": 75,
    "spe": 90,
}

bulbasaur = {
    "name": "Bulbasaur",
    "hp": 70,
    "atk": 65,
    "spa": 55,
    "def": 70,
    "spd": 80,
    "spe": 60,
}

charmander = {
    "name": "Charmander",
    "hp": 60,
    "atk": 60,
    "spa": 70,
    "def": 75,
    "spd": 70,
    "spe": 65,
}

squirtle = {
    "name": "Squirtle",
    "hp": 65,
    "atk": 75,
    "spa": 65,
    "def": 75,
    "spd": 65,
    "spe": 55,
}
# ---- Formula functions ----
def calc_offense(p):
    return (p["atk"] + p["spa"]) / 2

def calc_defense(p):
    return (p["def"] + p["spd"]) / 2

def calc_damage(attacker, defender, B=10):
    offense = calc_offense(attacker)
    defense = calc_defense(defender)

    # Softer defense scaling
    damage = B * (offense / (defense ** 0.78))

    # Random factor (0.8–1.2)
    damage *= random.uniform(0.8, 1.2)

    # Small speed influence
    speed_diff = (attacker["spe"] - defender["spe"]) / 30
    damage *= (1 + speed_diff / 1000)

    # Crit factor (10% chance, x2)
    if random.random() < 0.10:
        damage *= 1.5

    return max(1, int(damage))  # Minimum 1 damage

# ---- Battle simulation ----
def battle(p1, p2):
    hp1, hp2 = p1["hp"], p2["hp"]

    # Decide turn order by Speed
    if p1["spe"] >= p2["spe"]:
        order = [p1, p2]
    else:
        order = [p2, p1]

    while hp1 > 0 and hp2 > 0:
        for attacker in order:
            if attacker is p1:
                defender, defender_hp = p2, hp2
            else:
                defender, defender_hp = p1, hp1

            damage = calc_damage(attacker, defender)
            defender_hp -= damage

            if defender is p1:
                hp1 = defender_hp
            else:
                hp2 = defender_hp

            if defender_hp <= 0:
                return attacker["name"]

# ---- Round robin ----
def simulate_round_robin(n=10000):
    pokemons = [pikachu, bulbasaur, charmander, squirtle]

    for i in range(len(pokemons)):
        for j in range(i + 1, len(pokemons)):
            p1, p2 = pokemons[i], pokemons[j]
            wins = {p1["name"]: 0, p2["name"]: 0}

            for _ in range(n):
                winner = battle(p1, p2)
                wins[winner] += 1

            print(f"\n{p1['name']} vs {p2['name']} ({n} battles):")
            for name, count in wins.items():
                winrate = (count / n) * 100
                print(f"  {name}: {winrate:.2f}%")

# Run round robin
simulate_round_robin(10000)
