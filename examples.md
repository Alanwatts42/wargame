


You have chosen a great problem to begin with, however there 
are a few things you get wrong about OOP. OOP is not simply 
about using a class for "everything", it's a kind of way to 
think about a problem.

To begin with, it helped me a lot to think about a class as 
a prototype of a "thing". In your case the "thing" would be 
a Pokemon. A Pokemon can do certain things. In your 
simplified versions that would be 1. attack another Pokemon 
and 2. heal itself. Often these actions are reflected in the 
classes's methods. I think you mostly understood that. What 
else is there about the Pokemon/"thing" it has certain 
properties that describe it. I would say that's an aspect 
you did not think about. A property could be name, 
color, ... or it's health status. We also learn that the 
health can only be between 0 and 100.

So with this on our mind, let's think of a new design for 
class Pokemon:

```
`class Pokemon:
    """Blueprint for a new pokemon"""

    def __init__(self):
        self._health = 100
        #    ^--- the leading _ is a convention to mark internal values

    @property
    def health(self):
        """The health of the Pokemon which is between 0 and 100"""
        return self._health

    @health.setter
    def health(self, new_health):
        """Set the new heath value"""
        # here the health limits are enforced
        self._health = min(100, max(0, new_health))

    def attack(self, other, choice):
        """Attack another Pokemon with the chosen attack (1 or 2)

        This function also returns the raw amount of random damage dealt. The
        amount of damage dealt depends on the attack type.
        """
        if choice == 1:
            attack_points = random.randint(18, 25)
        elif choice == 2:
            attack_points = random.randint(10, 35)
        else:
            print("That is not a selection. You lost your turn!")
            attack_points = 0
        other.health -= attack_points
        return attack_points

    def heal(self):
        """Heal the Pokemon"""
        heal_points = random.randint(18, 35)
        self.health += heal_points
        return heal_points
```


<br>

No additional variables that need to track health status, no 
checking on the health limits. Everything is nicely 
encapsulated into the Pokemon class. As DaveMongoose pointed 
out in his comment, a drawback of this approach is that the 
Pokemon can not be defeated as long as it heals after an 
attack, no matter how much damage it took.

```
mew = Pokemon()
user = Pokemon()
mew.attack(user, 1)
print(f"User health after attack: {user.health}")
user.heal()
print(f"User health after heal: {user.health}")
mew.heal() # health should still only be 100
print(f"Mew's health after 'illegal' heal: {user.health}")
```

<br>

### Short break on style and other conventions

Another thing that has changed in contrast to your solution 
is the documentation I added to each function. Python has an 
"official" Style Guide (which is worth a read on its own) 
with a section on how to write these so called docstrings 
here.

It also features guidelines on where to use blank lines and 
where not to use them. In my oppinion the excessive use of 
blank lines in your code hinders readability more than it 
does help to structure the code.

I also used only a single leading underscore for my internal 
value instead of two as you did. The Style Guide also has 
you covered on this topic. In general you should always use 
a single leading underscore to mark functions and variables/
members as internal. For more details on what happens if you 
use two leading underscores, follow the link above.

After that short intermezzo, let's look on how the battle 
simulation looks with the new class:


```
def battle_simulation():
    """Run a simple interactive Pokemon battle simulation"""
    mew = Pokemon()
    user_pokemon = Pokemon()
    while True:
        print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
        attack_choice = int(input("\nSelect an attack: "))
        # DON'T use eval on user input, this can be dangerous!

        # Mew selects an attack, but focuses on attacking if health is full.
        mew_choice = random.randint(1, 2 if mew.health == 100 else 3)
        # this is your original distinction just condensed into a single line

        # Attacks by user and Mew are done simultaneously
        # with the changes to Pokemon, there is no need to save all the
        # intermediate damage/heal values -> nice and short code
        if attack_choice != 3:
            print(f"You dealt {user_pokemon.attack(mew, attack_choice)} damage.")

        if mew_choice != 3:
            print(f"Mew dealt {mew.attack(user_pokemon, mew_choice)} damage.")

        if attack_choice == 3:
            print(f"You healed {user_pokemon.heal()} health points.")

        if mew_choice == 3:
            print(f"Mew healed {mew.heal()} health points.")

        if mew.health == 0 or user_pokemon.health == 0:
            break

        print(f"Your current health is {user_pokemon.health}")
        print(f"Mew's current health is {mew.health}")

    print(f"Your final health is {user_pokemon.health}")
    print(f"Mew's final health is {mew.health}")

    if user_pokemon.health < mew.health:
        print("\nYou lost! Better luck next time!")
    else:
        print("\nYou won against Mew!")


if __name__ == "__main__":
    battle_simulation()
```



