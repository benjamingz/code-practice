#This will be a videogame about a player and their cat who level up to fight bosses and eventually take over their kingdom
import time

healthStat = 0
jumpStat = 0
strengthStat = 0
speedStat = 0
mainPowername = "empty"


print("\n*You wake up in the ground. You do not remember how you got there, or why there is a cat next to you. You only remember your name. All of a sudden, a man in a horse-drawn carriage appears coming down the road.*")

name = input("\nJohn: Welcome- erm... Well, I suppose I don't know your name yet traveller. What should I call you?\n\n")
nameConfirm = input(f"\n{name}? Am I saying that right?\n\n")
nameConfirm = nameConfirm.upper()
while nameConfirm != "YES" and nameConfirm != "NO":
    nameConfirm = input("I'm sorry, was that a yes or a no?\n")
if nameConfirm == "NO":
    name = input("I'm sorry, for the mistake, what should I call you then?\n")
else:
    name = name

print(f"\nWell then {name}, let me show you around!")
time.sleep(4)
print("\nI see your cat has already chosen you. That is a lucky thing you know.")
time.sleep(4)
print("In this kingdom, cats can choose you as their owner, but this is something that can take a lifetime to occur.")
time.sleep(4)
print("You are lucky yours chose you so early in your life.")
time.sleep(4)
print("I reckon you don't know how you got here. That is very common in this place, though we do not know why.")
time.sleep(4)
print("In the village, we try not to challenge the existing order because the consequences here are deadly.")
time.sleep(4)
print("Though there are some scary beings out there in this forest, they only come out at night.")
time.sleep(4)
print("The real worry us villagers have is the king. He is vile and ruthless, and does not like newcomers.")
time.sleep(5)
print("You should really get used to the powers of your cat. Wait, did I mention your cat has powers?")
time.sleep(5)
print("Have you even chosen the powers yet? No? Well, hold your hand above the cat's head, yes like that, and choose its abilities.")
time.sleep(5)
charChoice = input("\nChoose what abilities your cat has. Press ENTER to cycle through them. Enter the name of the cat you want underneath its description.")
charChoice = "empty"
while charChoice =="empty":
    print("\nHulkat\nAbility: Strength\nWeaknesses: Poison Attacks, Speed Attacks")
    charChoice = input()
    charChoice = charChoice.lower()
    if charChoice == "hulkat":
        charChoice = charChoice.capitalize()
        break
    else:
        charChoice = "empty"
    print("\nSpeedster\nAbility: Speed\nWeaknesses: Ice Attacks, Fire Attacks")
    charChoice =  input()
    charChoice = charChoice.lower()
    if charChoice == "speedster":
        charChoice = charChoice.capitalize()
        break
    else:
        charChoice = "empty"
    print("\nHelikitty\nAbility: Flight\nWeaknesses: Water Attacks, Earth Attacks")
    charChoice = input()
    charChoice = charChoice.lower()
    if charChoice == "helikitty":
        charChoice = charChoice.capitalize()
        break
    else:
        charChoice = "empty"
    print("\nBrick\nAbility: Impenetrable Skin\nWeaknesses: Strength Attacks, Flight Attacks")
    charChoice = input()
    charChoice = charChoice.lower()
    if charChoice == "brick":
        charChoice = charChoice.capitalize()
        break
    else:
        charChoice = "empty"
print(f"\nYou have chosen {charChoice}!")












time.sleep(2)
dial = input("\nNow that you have chosen your cat, maybe you can help our village deal with some of the monsters that have been terrorizing us. Come with me!")
















