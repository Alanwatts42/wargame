#!/usr/bin/python3


class Warrior:
    """Basic soldier class, any other such classes will be subclasses of this one"""
    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def attack(self, other):
        other.health -= self.attack
        return other.health

    def take_damage(self. other):
        self.health -= other.attack
        return self.health

    def __str__(self):
        return str(__class__.__name__)


class Knight(Warrior):
    """A subclass of Warrior which is similar but with better attack"""
    def __init__(self):
        super().__init__()
        self.attack = 7

    def __str__(self):
        return str(__class__.__name__)


class Army:
    """A group made up of Warriors and Knights, which will clash with other such groups"""
    def __init__(self):
        self.units = []
        self.deaths = 0

    def add_units(self, unit_type, unit_qty):
        if unit_type is Warrior:
            unit_type = Warrior()
        elif unit_type is Knight: unit_type = Knight()
        self.units += [unit_type for i in range(unit_qty)]
   
    def deployed_unit(self):
        for i in range(len(self.units)):
            while True: 
                if self.units[i].is_alive():
                    continue
                elif self.units[i].is_alive() is False:
                    break
            

    def is_defeated(self):
        i = set(i.is_alive() for i in self.units)
        if i == {False} and len(i) is 1:
            return True 
        else:
            return False

    def soundoff(self):
        names = [print(i) for i in self.units]
        return names


class Battle:
    """Defines the clash of two Army() objects, pits each of their 
    warriors against one another in sequence until one of the armies
    runs out of warriors, at which point that army is defeated."""
    def __init__(self):
        self.turn = 0

    def fight(self, army_1, army_2):
        
        units_1 = army_1.units
        units_2 = army_2.units

        deaths_1 = army_1.deaths
        deaths_2 = army_2.deaths

        unitcount_1 = len(units_1)-1
        unitcount_2 = len(units_2)-1

        while army_1.deaths < unitcount_1 is False and army_2.deaths > unitcount_2 is False:
            if self.turn % 2 == 0:
                units_2[deaths_2].health -= units_1[deaths_1].attack
                if units_2[deaths_2].is_alive() is True:
                    self.turn += 1
                elif units_2[deaths_2].is_alive() is False:
                    army_2.deaths += 1
                    self.turn += 1
            elif self.turn % 2 == 1:
                units_1[deaths_1].health -= units_2[deaths_2].attack
                if units_1[deaths_1].is_alive() is True:
                    self.turn += 1
                elif units_1[deaths_1].is_alive() is False:
                    army_1.deaths += 1
                    self.turn += 1

        if army_1.is_defeated() is False and army_2.is_defeated() is True:
            return True
        elif army_2.is_defeated() is False and army_1.is_defeated() is True:
            return False
        else:
            return print(army_1.is_defeated(), army_2.is_defeated(), army_1.deaths, army_2.deaths)
    

if __name__ == '__main__':

    goodguys = Army()
    badguys = Army()
    goodguys.add_units(Knight, 5)
    badguys.add_units(Warrior, 4)

    war = Battle()    

    print("\n")
    goodguys.soundoff()
    print("\n")
    badguys.soundoff()
    print("\n")
    war.fight(goodguys, badguys)
