class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.endurance = endurance
        self.power = power
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} sleeps")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} eats")
        self.power += 1

    def hit(self):
        print(f"{self.name} hits")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} walks")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Endurance: {self.endurance}")
        print(f"Power: {self.power}")
        print(f"Hair color: {self.hair_color}")