import random
class Ability:
    def __init__(self, name, attack_strength):
        self.name = "Carnage"
        self.attack_strength = "150"
        '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
    def attack(self, attack_value):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        # TODO: Use random.randint(a, b) to select a random attack value.
        self.attack_value = random.randint(5,150)
      # Return an attack value between 0 and the full attack.
        return self.attack_value
      # Hint: The constructor initializes the maximum attack value.
        pass
if __name__ == "__main__
    ability = Ability("Carnage", 40)
    print
