import random
import math

# ---- Pokémon (BST = 400 each) ----
class Pokemon:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money


# ---- Formula functions ----
def calc_offense(p):
    return (p.attack) / 2

def calc_defense(p):
    return (p.defense) / 2

def calc_damage(attacker, defender, B=10):
    offense = calc_offense(attacker)
    defense = calc_defense(defender)

    # Softer defense scaling
    damage = B * (offense / (defense ** 0.75))

    # Random factor (0.8–1.2)
    damage *= random.uniform(0.8, 1.2)

    # Small speed influence
    speed_diff = (attacker.speed - defender.speed) / 30
    damage *= (1 + speed_diff / 1000)

    # Crit factor (16% chance, x1.5)
    if random.random() < 0.16:
        damage *= 1.5

    return max(1, int(damage))  # Minimum 1 damage

# ---- Battle simulation ----
def battle(p1, p2):
    hp1, hp2 = p1.hp, p2.hp

    # Decide turn order by Speed
    if p1.speed >= p2.speed:
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
                return attacker.name

# ---- Round robin ----
def simulate_round_robin(n, pokemons):
    max = 0
    for i in range(len(pokemons)):
        for j in range(i + 1, len(pokemons)):
            p1, p2 = pokemons[i], pokemons[j]
            wins = {p1.name: 0, p2.name: 0}

            for _ in range(n):
                winner = battle(p1, p2)
                wins[winner] += 1

            print(f"\n{p1.name} vs {p2.name} ({n} battles):")
            for name, count in wins.items():
                winrate = (count / n) * 100
                print(f"  {name}: {winrate:.2f}%")
                if count > max:
                    max = count
                    overall_winner = name
                else:
                    continue
    return overall_winner
# Run round robin
def main():
    p = Pokemon("Pikachu", 60, 125, 125, 90)
    b = Pokemon("Bulbasaur", 70, 120, 150, 60)
    # c = Pokemon("Charmander", 60, 130, 145, 65)
    # s = Pokemon("Squirtle", 65, 140, 135, 60)
    battlers = [p, b]
    user = Player(input("What is your name? ").capitalize(), money=1000)

    for battler in battlers:
        print(battler.name)

    choice = input("Who do you think will win? ")
    bet = int(input("How much will you bet? "))
    w = simulate_round_robin(11, battlers)
    if w == choice:
        user.money += bet
        print(f"you won, balance is now ${user.money}")

    else:
        user.money -= bet
        print(f"you lost, balance is now ${user.money}")

main()


