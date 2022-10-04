class Pokemon:
    def __init__(self, name, attack_power, health, abilities, type):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.abilities = abilities
        self.type = type
    def __str__(self):
        print(self.name, " is a ", self.type, " pokemon with ", )
    
#     def use_ability(a):
#         a.activate()

class Ability:
    def __init__(self, name, description, a_type):
        self.name = name
        self.description = description
        self.a_type = a_type
        def use():
            pass


# Class ability will contain information about abilities, name, description, etc
# Each pokemon will have a list of abilities that it can use. 