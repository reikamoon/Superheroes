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

class Weapon(Ability):
    def __init__(self, name, attack_value):
        super().__init__(name, attack_value)
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        self.attack_value = random.randint(0, 1500)
        # TODO: Use what you learned to complete this method.
        damage = random.randint(0, self.attack_value)
        return damage // 2

class Hero:
    def __init__(self, name, deaths = 0, kills = 0, starting_health = 5000, defense_value = 50, attack_value = 50):
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
        self.deaths = 0
        self.kills = 0
        self.name = name
        self.defense_value = defense_value
        self.attack_value = attack_value
        self.starting_health = self.current_health = starting_health
        self.stats = self.deaths, self.kills
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use

    def begin_fight(self):
        print("Welcome to the arena!")
        user_input = input("Would you like to create your very own hero?\n")
        user_input = user_input.lower()
        while True:
            if user_input == "yes":
                self.hero_creation()
            elif user_input == "no":
                print("Then choose a pre-made hero to play as.")
                print("Your choices are: Double, Kiva, Kabuto, Groh, Dimitri, and Orochi.")
                user_input = input("Make your decision.\n")
                user_input = user_input.lower()
            while True:
                if user_input == "Double":
                    add_hero(my_hero)
                    remove_hero(default)
                    print("You have chosen {0}!".format(self.name))
                if user_input == "Kiva":
                    add_hero(my_hero2)
                    remove_hero(default)
                if user_input.lower() == "Kabuto":
                    add_hero(my_hero3)
                    remove_hero(default)
                if user_input.lower() == "Groh":
                    add_hero(my_hero4)
                    remove_hero(default)
                if user_input.lower() == "Dimitri":
                    add_hero(my_hero5)
                    remove_hero(default)
                if user_input.lower() == "Orochi":
                    add_hero(my_hero6)
                    remove_hero(default)

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

    def add_weapon(self, weapon):
         self.abilities.append(weapon)

    def add_kills(self, num_kills):
        ''' Update kills with num_kills'''
        # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths = num_deaths

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total:Int'''
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total
            # TODO: This method should run Ability.attack() on every ability
            # in self.abilities and returns the total as an integer.

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
            return False
        else:
            return True
            pass

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # If both heroes lack abilities, call a draw
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("{0} and {1} both lack abilities! It's a draw!".format(self.name, opponent.name))
                break
            # Fightin'
            damage = self.attack()
            opponentdamage = opponent.attack()
            opponent.take_damage(damage)
            self.take_damage(opponentdamage)

        # Print the victor's name to the screen.
        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight

        # Player Dies
            if self.is_alive() == False:
                print("{0} has fallen!".format(self.name))
                print("{0} wins!".format(opponent.name))
                # add stats
                self.add_deaths(1)
                opponent.add_kills(1)
                # victory quotes
                if opponent.name == "Double" and opponent.is_alive() == True:
                    print("Phillip: We are victorious.")
                    print("Shotaro: Excellent work, Phillip.")
                if opponent.name == "Kiva" and opponent.is_alive() == True:
                    print("Kivat: Wataru, nice work!")
                    print("Wataru: It's finally over...")
                if opponent.name == "Kabuto" and opponent.is_alive() == True:
                    print("Tendou: I am the one who walks the path to heaven.")
                if opponent.name == "Groh" and opponent.is_alive() == True:
                    print("Groh: Target eliminated. Moving on to next assignment.")
                if opponent.name == "Dimitri" and opponent.is_alive() == True:
                    print("Dimitri: I pray for a day in which needless bloodshed will cease.")
                if opponent.name == "Orochi" and opponent.is_alive() == True:
                    print("Orochi: Pathetic...I long for a real challenge...")

                # Opponent Dies
                if opponent.is_alive() == False:
                    print("{0} has fallen!".format(opponent.name))
                    print("{0} wins!".format(self.name))
                # add stats
                opponent.add_deaths(1)
                self.add_kills(1)
                # victory quotes
                if self.name == "Double" and self.is_alive() == True:
                    print("Phillip: We are victorious.")
                    print("Shotaro: Excellent work, Phillip.")
                if self.name == "Kiva" and self.is_alive() == True:
                    print("Kivat: Wataru, nice work!")
                    print("Wataru: It's finally over...")
                if self.name == "Kabuto" and self.is_alive() == True:
                    print("Tendou: I am the one who walks the path to heaven.")
                if self.name == "Groh" and self.is_alive() == True:
                    print("Groh: Target eliminated. Moving on to next assignment.")
                if self.name == "Dimitri" and self.is_alive() == True:
                    print("Dimitri: These hands are stained red once again.")
                if self.name == "Orochi" and self.is_alive() == True:
                    print("Orochi: Pathetic...I long for a real challenge...")

    def create_hero(self):
        # Create Hero
        print("Welcome! Let's create a hero.")
        print("First, we need a name.")
        print("Enter your hero's name:")
        hero_name = input()
        print("Okay, your hero's name is {0}.".format(hero_name))
        print("Now, choose a class for {0}.".format(hero_name))
        try:
            print("Your class choices are:")
            print("1) Warrior, 2) Mage, 3) Thief")
            print("Choose your class.")
            hero_class = input()
            if hero_class == "Warrior":
                print("You have chosen the Warrior Class!")
                print("You are an armed bruiser that deals nasty damage!")
                hero_class = "Warrior"
            if hero_class == "Mage":
                print("You have chosen the Mage Class!")
                print("You are an expert in the arcane arts!")
                hero_class = "Mage"
            if hero_class == "Thief":
                print("You have chosen the Thief Class!")
                print("You are a shadow in the night who excells in speed and stealth!")
                hero_class = "Thief"
        except ValueError:
            print("Sorry, integers only!")
            print("Entering default class...Warrior")
            hero_class = "Warrior"
            custom_hero = Hero("{0}".format(hero_name))
            self.name = custom_hero
            print("My hero's name is {0}, and is a {1}.\n".format(custom_hero.name, hero_class))
        custom_hero = Hero("{0}".format(hero_name))
        self.name = custom_hero
        print("My hero's name is {0}, and is a {1}.\n".format(custom_hero.name, hero_class))

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
            '''
            # TODO: This method will allow a user to create an ability.
            # Prompt the user for the necessary information to create a new ability object.
            # return the new ability object.
        print("Now, let's create a starting ability for your hero.")
        print("Choose a name for your ability:\n")
        ability_name = input()
        try:
            print("How strong is this ability?")
            ability_strength = int(input())
        except ValueError:
            print("Sorry, integers only!")
            print("Entering default value...100")
            ability_strength = 100
        self.add_ability(Ability(ability_name, ability_strength))
        print("Ability is called {0} and has {1} strength!".format(ability_name, ability_strength))
        print("{0} has gained the ability, {1}!\n".format(self.name, ability_name))

    def create_weapon(self):
        print("Okay, let's make your hero's trusted weapon!")
        print("What type of weapon you'd like to forge:")
        weapon_type = input()
        print("So your weapon is a mighty {0}?".format(weapon_type))
        print("Does this weapon have a name?")
        weapon_name = input()
        print("Your {0}'s name is {1}.".format(weapon_type, weapon_name))
        try:
            print("Now, how strong is the {0}?".format(weapon_name))
            weapon_strength = int(input())
        except ValueError:
            print("Sorry, integers only!")
            print("Entering default value...100")
            weapon_strength = 100
        self.add_weapon(Weapon(weapon_name, weapon_strength))
        print("Your {0} is called {1} and has {2} strength!".format(weapon_type, weapon_name, weapon_strength))
        print("Now, your hero needs some protection. Time to forge some armor!")

    def create_armor()

class Team:
    def __init__(self, teamname):
        ''' Initialize your team with its team name
        '''
    # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.heroes = []
        self.teamname = teamname

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
                return 1
            return 0

    def add_hero(self, hero):
          '''Add Hero object to self.heroes.'''
          # TODO: Add the Hero object that is passed in to the list of heroes in
          # self.heroes
          self.heroes.append(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print("{0}".format(hero.name))


    def revive_heroes(self, health = 5000):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print("Hero: {0} has died {1} time(s) and has killed {2} foe(s).".format(self.name, self.deaths, self.kills))

    def is_alive(self):
        if self.current_health < 0:
            return False
        else:
            return True


    def randomhero(self):
        while True:
            hero = random.choice(self.heroes)
            if hero.is_alive():
                return hero

    def attack(self, enemy_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        print("{0} vs. {1}! Only one shall emerge victorious!".format(my_team.name, enemy_team.name))
        while self.is_alive() and enemy_team.is_alive():
            my_team_hero = self.randomhero()
            enemy_team_hero = enemy_team.randomhero()
            my_team_hero.fight(enemy_team_hero)
            # Fightin'
            damage = self.attack()
            opponentdamage = opponent.attack()
            opponent.take_damage(damage)
            self.take_damage(opponentdamage)
            if enemy_team_hero ==  False:
                print("{0} has fallen! {1} is the victor!".format(my_team.name, enemy_team.name))
            if my_team_hero.is_alive() == False:
                print("{0} has fallen! {1} is the victor!".format(enemy_team.name, my_team.name))




class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
            '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        team_one: None
        team_two: None

    def create_team(self):
        team_one_name = input("Please choose a name for your team.\n")
        self.team_one = Team(team_one_name)
        return self.team_one

    def create_enemy_team(self):
        team_one_name = input("Please choose a name for the opposing team.\n")
        self.team_two = Team(team_two_name)
        return self.team_two

        def create_hero(self):
            '''Prompt user for Hero information
            return Hero with values from user input.
            '''
            # TODO: This method should allow a user to create a hero.
            # User should be able to specify if they want armors, weapons, and
            # abilities.
            # Call the methods you made above and use the return values to build
            # your hero.
            #
            # return the new hero object
            print("Choose a name for your hero:\n")
            default.name = Hero(name, 5000)

    def create_weapon(self):
         '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.

    def create_armor(self):
         '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # My Data
    # Weapons
    weapondouble = Weapon("CycloneJoker Double Blades",100)
    weaponkiva = Weapon("Zanbat Blade", 100)
    weaponkabuto = Weapon("Kabuto Kunai", 100)
    weapongroh = Weapon("Aerondight Replica", 100)
    weapondimitri = Weapon("Areadbhar", 100)
    weaponorochi = Weapon("Serpent King's Scythe", 100)
    # Abilities
    ability = Ability("Double Boiled Extreme", 350)
    ability2 = Ability("Flame Maximum Drive", 200)
    ability3 = Ability("Wake up Fever!", 350)
    ability4 = Ability("Break the Chain", 200)
    ability5 = Ability("Clock up", 200)
    ability6 = Ability("Hyper Kick", 350)
    ability7 = Ability("Chevalier Mal Fet", 200)
    ability8 = Ability("Super Chevalier Mal Fet", 350)
    ability9 = Ability("Atrocity", 350)
    ability10 = Ability("Vengeance of the King", 200)
    # Armor
    armor = Armor("Cyclone", 200)
    armor2 = Armor("Joker", 200)
    armor3 = Armor("Emperor's Garb", 200)
    shield = Armor("Emperor's Shield", 200)
    armor4 = Armor("ZECT Kabuto Armor", 200)
    armor5 = Armor("ZECT Kabuto Cast", 200)
    armor6 = Armor("Midnight Purge Uniform", 200)
    gauntlet = Armor("Limiter Gauntlet", 200)
    charm = Armor("Minerva's Ward", 15)
    armor7 = Armor("Fallen King's Armor", 200)
    armor8 = Armor("Lion's Cape", 200)
    armor9 = Armor("Serpent King's Garb", 200)
    shield2 = Armor("Aegis", 200)
    charm2 = Armor("Ouroboros Bracelet", 15)
    # Teams
    my_team = Team("Rider War")
    enemy_team = Team("Strike Force")
    # Team Rider War
    # Double
    my_hero = Hero("Double")
    my_hero.add_weapon(weapondouble)
    my_hero.add_armor(armor)
    my_hero.add_armor(armor2)
    my_hero.add_ability(ability)
    my_hero.add_ability(ability2)
    # Kiva
    my_hero2 = Hero("Kiva")
    my_hero2.add_weapon(weaponkiva)
    my_hero2.add_armor(armor3)
    my_hero2.add_armor(shield)
    my_hero2.add_ability(ability3)
    my_hero2.add_ability(ability4)
    # Kabuto
    my_hero3 = Hero("Kabuto")
    my_hero3.add_weapon(weaponkabuto)
    my_hero3.add_armor(armor4)
    my_hero3.add_armor(armor5)
    my_hero3.add_ability(ability5)
    my_hero3.add_ability(ability6)
    # Team Strike Force
    # Groh
    my_hero4 = Hero("Groh")
    my_hero4.add_weapon(weapongroh)
    my_hero4.add_armor(armor6)
    my_hero4.add_armor(gauntlet)
    my_hero4.add_armor(charm)
    my_hero4.add_ability(ability7)
    my_hero4.add_ability(ability8)
    # Dimitri
    my_hero5 = Hero("Dimitri")
    my_hero5.add_weapon(weapondimitri)
    my_hero5.add_armor(armor7)
    my_hero5.add_armor(armor8)
    my_hero5.add_ability(ability9)
    my_hero5.add_ability(ability10)
    # Orochi
    my_hero6 = Hero("Orochi")
    my_hero6.add_weapon(weaponorochi)
    my_hero6.add_armor(armor9)
    my_hero6.add_armor(shield2)
    my_hero6.add_armor(charm2)
    # Default Hero
    default = Hero("Default")
    # Begin Game
    #default.begin_fight()
    #my_hero5.fight(my_hero4)
    default.create_hero()
    default.create_ability()
