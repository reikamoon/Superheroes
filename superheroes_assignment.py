import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
              name:String
              max_damage: Integer
          '''
        self.name = name
        self.attack_strength = attack_strength
    # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
        pass
    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        self.attack_value = random.randint(0,1500)
        self.max_damage = 1500
         # Return an attack value between 0 and the full attack.
        return self.attack_value
         # Hint: The constructor initializes the maximum attack value.
class Armor:
    def __init__(self, name, max_block):
        #TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block
    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        self.defense_value = random.randint(0,500)
        self.max_block = 500
        return self.defense_value
class Hero:
    def __init__(self, name, starting_health = 5000, defense_value = 50):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        # TODO: Initialize instance variables values as instance variables
        self.abilities = []
        self.armor = []
        self.name = name
        self.defense_value = defense_value
        self.starting_health = self.current_health = starting_health
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities:List
        self.abilities.append(ability)

    def add_armor(self, armor):
         '''Add armor to self.armors
         Armor: Armor Object
         '''
         # TODO: Add armor object that is passed in to `self.armors`
         self.armor.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total:Int'''
        total = 0
        for ability in self.abilities:
            total += ability.attack()
            return total
            # TODO: This method should run Ability.attack() on every ability
            # in self.abilities and returns the total as an integer.
            pass

    def defend(self, damage_amt):
        '''Runs `block` method on each armor.
        Returns sum of all blocks
        '''
        total_armor = 0

        for armor in self.armors:
            block = armor.block()
            total_armor = total_armor + block
        return sum

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health = self.current_health - damage - self.defense_value
        return self.current_health
        print("Took damage! Remaining health: {0}".format(self.current_health))

    def is_alive(self):
        if self.current_health < 0:
            print("{0} has fallen!".format(self.name))
            if self.name == "Double":
                print("Phillip: Shotaro, now would be the time to make a strategic retreat.")
                print("Shotaro: Fine. But I won't forget this!")
            if self.name == "Kiva":
                print("Kivat: Wataru, we need to retreat!")
                print("Wataru: Too strong...")
            return False
        else:
            return True
            pass

    def begin_fight(self):
        user_input = input("Ready to battle?\n")
        user_input = user_input.lower()
        while True:
            if user_input == "yes":
                print("Beginning fight...")
                break
            elif user_input == "no":
                print("There's no use running!")
                user_input = input("Ready to battle?\n")
                user_input = user_input.lower()
            else:
                user_input = input("Ready to battle?\n")
                user_input = user_input.lower()

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("{0} and {1} both lack abilities! It's a draw!".format(self.name, opponent.name))
                break
            # Print the victor's name to the screen.
            if self.is_alive() == False:
                print("{0} wins!".format(opponent.name))
            if opponent.is_alive() == False:
                print("{0} wins!".format(self.name))
                pass
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Double")
    ability = Ability("Double Boiled Extreme", 350)
    ability2 = Ability("Flame Maximum Drive", 200)
    armor = Armor("Cyclone", 200)
    armor2 = Armor("Joker", 200)
    my_hero.add_armor(armor)
    my_hero.add_armor(armor2)
    my_hero.add_ability(ability)
    my_hero.add_ability(ability2)
    my_hero2 = Hero("Kiva")
    ability3 = Ability("Wake up Fever!", 350)
    ability4 = Ability("Break the Chain", 200)
    armor3 = Armor("Emperor's Garb", 200)
    shield = Armor("Emperor's Shield", 200)
    my_hero2.add_armor(armor3)
    my_hero2.add_armor(shield)
    my_hero2.add_ability(ability3)
    my_hero2.add_ability(ability4)
    my_hero.begin_fight()
    my_hero.fight(my_hero2)
