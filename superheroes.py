import random
class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
              name:String
              max_damage: Integer
          '''
        self.name = "Carnage"
        self.attack_strength = 20
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
        self.name = "Fallen King's Armor"
        self.max_block = 350
        #TODO: Create instance variables for the values passed in.
        pass

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        self.defense_value = random.randint(0,500)
        self.max_block = 500
        return self.defense_value

class Hero:
        def __init__(self, name, starting_health=1000):
            '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
            '''
            # TODO: Initialize instance variables values as instance variables
            self.abilities = []
            self.armors = []
            self.name = name
            self.starting_health = self.current_health = starting_health
            # (Some of these values are passed in above,
            # others will need to be set at a starting value)
            # abilities and armors are lists that will contain objects that we can use

         def add_ability(self, ability):
             ''' Add ability to abilities list '''
             # TODO: Add ability object to abilities:List
             self.abilities.append(ability)

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

        def take_damage(self, damage):
                '''Updates self.current_health to reflect the damage minus the defense.
                '''
                # TODO: Create a method that updates self.current_health to the current
                self.current_health = self.current_health - damage_amt
                # minus the the amount returned from calling self.defend(damage).
                pass

        def defend(self, damage_amt):
            '''Runs `block` method on each armor.
            Returns sum of all blocks
            '''
            total_armor = 100
            return total_armor

        def add_armor(self, armor, shield):
                '''Add armor to self.armors
                Armor: Armor Object
                '''
                self.shield = "Aegis"
                self.armors.append(armor)
                # TODO: Add armor object that is passed in to `self.armors`

        def fight(self, opponent):
            ''' Current Hero will take turns fighting the opponent hero passed in.
            '''
            # TODO: Fight each hero until a victor emerges.
            if self.current_health == 0
            print("{0} wins!".format(hero2))
            # Print the victor's name to the screen.
            pass

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Carnage", 50)
    another_ability = Ability("Heaven's Punishment", 190)
    hero = Hero("Ashen Demon", 500)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
    shield = Armor("Aegis", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
