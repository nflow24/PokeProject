class Pokemon:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
p = Pokemon("Pikachu", 60, 125, 125, 90)

for attr, value in p.__dict__.items():
    print(f"{attr}: {value}")
