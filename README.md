# WarGame

<br>

Python practice project, meant to get accustomed to working with 
OOP in Python.

<br>

# The Characters

<br>
<br>


### Warrior

Originally I began with a simple class for the generic soldier
which I called "Warrior()". As the generic soldier class, I gave
Warrior() an arbitrary, but now by definition the baseline number,
of both health and attack power, so every instance of the Warrior()
class is born with 50 health and 5 attack. Each time a Warrior 
performs an attack on another character, their opponent's health is 
decreased by 5, because the Warrior's attack power is 5. 


### Knight

Next, I created the Knight() class, which I subclassed from 
Warrior(), which avoids needlessly repeating code. The only real 
difference between the Warrior and the Knight (aside from the name)
is that a Knight's attack power is 7 instead of 5. Other than that, 
his other stats and characteristics are identical to that of the 
Warrior, hence why I made it a subclass of Warrior().


## THe Armies

Because making the two Character classes fight one on one is so 
boring and stupid as to cause my forehead to ache just thinking
about it, I decided to complicate the situation by creating a new
class called Army(). 

The Army() class would act as a purpose-built container for a group
of these units, and would govern most aspects of how they would go 
about clashing with another similar group made up of the same units
but perhaps in different numbers and proportions. This was not as
easy as I initially imagined. My first task was to create a method 
that would add units to an army by taking the type and quantity of
units being added i.e. (Warrior, 5) as args, which would of course
add that number of instances of the Warrior or Knight class to that
army by appening a list called self.units. The full unit roster
could be called up via army.units (army being an example instance 
of the Army() class), and each unit could be accessed by slicing
the army.units list i.e. army.units[0] would give you the first 
unit appended to the army.units list, which also meant that was 
the first unit added to the army by default. 

While this was all relatively helpful, I was still running into 
difficulties trying to figure out how to get the two armies to 
send out their soldiers one by one, take turns attacking, and then
switch out the fighting soldier with the next one in line only once
the first one had died, and then have the soldier that had won that
fight continue fighting the soldier that had just replaced the one
they'd defeated on the previous turn. Iterating over the soldiers 
is one thing, but iterating over the soldiers in both armies 
at the same time, and only upon the death of the first soldier sent
out to fight, and so on until one army or the other had no soldiers
left alive 


### Note to self:

It was bloody difficult trying to convince git to merge this repo
with the one you created locally containing all of the important
files. While it would have been much easier had I just elected
to create the .gitignore, README.md, and license files yourself 
locally and just override everything in the remote empty branch,
easy and right are rarely the same thing.

```bash`
git pull origin master --allow-unrelated-histories
```

In case it's not already obvious, you'd just replace "origin" with 
the particular repo you're working with and "master" with the 
remote branch you are trying to merge with the local branch you'd 
need to currently have selected or "checked out".

<a href="https://careerkarma.com/blog/git-fatal-refusing-to-mergeunrelated-histories/">
Source: Some Rando's Blog
</a>








