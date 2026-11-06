import random

class Dog:
    def __init__(self, nickname):
        self.nickname = nickname
        self.satiety = 50
        self.health = 100
        self.alive = True
        self.gladness = 80
        self.endurance = 100
        self.strength = 100

    def to_sleep(self):
        print("Dog is sleeping")
        self.health += 10
        self.gladness += 10
        self.satiety -= 5
        self.strength += 5
        self.endurance += 5

        if self.health >= 100:
            self.health = 100
        if self.gladness >= 100:
            self.gladness = 100
        if self.strength >= 100:
            self.strength = 100
        if self.endurance >= 100:
            self.endurance = 100

        if self.satiety <= 0:
            print("Dog died of hunger")
            self.alive = False

    def to_eat(self):
        print("Dog is eating")
        eat_cube = random.randint(1, 3)

        if eat_cube == 1 or eat_cube == 2:
            print("The dog ate deliciously")
            self.health += 5
            self.satiety += 10
            self.gladness += 5

            if self.satiety >= 201:
                print("The dog has grade 3 obesity")
                print("The dog died...")
                self.alive = False

            elif self.satiety >= 151:
                print("The dog has grade 2 obesity")
                self.endurance = 50
                self.strength = 60

            elif self.satiety >= 101:
                print("The dog has grade 1 obesity")
                self.endurance = 80
                self.strength = 90

        elif eat_cube == 3:
            print("The dog was poisoned.")
            self.health -= 20
            self.gladness -= 5
            self.strength -= 5
            self.endurance -= 5

        if self.health <= 0:
            print("Dog died")
            self.alive = False

    def to_chill(self):
        print("Dog is chilling")
        self.health += 10
        self.gladness += 10
        self.satiety -= 5

        if self.health >= 100:
            self.health = 100
        if self.gladness >= 100:
            self.gladness = 100

        if self.satiety <= 0:
            print("Dog died of hunger")
            self.alive = False

    def to_fight(self):
        print("Dog is fighting")

        if self.strength >= 80:
            print("The dog won the fight")
            self.health -= 5
            self.satiety -= 10

        elif self.strength > 40:
            print("The dog lost the fight but survived")
            self.health -= 10
            self.gladness -= 5
            self.satiety -= 5
            self.strength -= 5
            self.endurance -= 5

        else:
            print("The dog died")
            self.alive = False

        if self.health <= 0:
            print("Dog died")
            self.alive = False

        if self.satiety <= 0:
            print("Dog died of hunger")
            self.alive = False

    def end_of_day(self):
        print(f"Health = {self.health}")
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {self.satiety}")
        print(f"Strength = {self.strength}")
        print(f"Endurance = {self.endurance}")

    def live(self, day):
        print(f"\nDay {day} of {self.nickname}'s life")

        live_cube = random.randint(1, 4)

        if live_cube == 1:
            self.to_sleep()

        elif live_cube == 2:
            self.to_eat()

        elif live_cube == 3:
            self.to_chill()

        elif live_cube == 4:
            self.to_fight()

        self.end_of_day()


animal = Dog(nickname="Bonya")

for day in range(1, 365):
    if animal.alive == False:
        break

    animal.live(day)

if animal.alive:
    print("\nBonya survived the whole year!")
