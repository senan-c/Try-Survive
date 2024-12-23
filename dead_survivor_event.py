from functions import *

def dead_survivor_event(area, zombies_killed, day):
    game = True

    zom_num = random.randint(3, 7)
    print("You've nearly arrived at the", area, "when you spot a group of", zom_num, "zombies gathered around a corpse")
    print("They haven't noticed you yet, but that body might have some good loot on it...")
    print("Will you:\n1. Fight the zombies\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("You walk closer to the zombies and clear your throat, alerting them")
        fight_result = fight(zom_num, "zombies")

        if fight_result:
            zombies_killed += zom_num
            print("After the fight, you turn over the mangled body of the survivor and check his pockets")
            print("You find:")
            random_item(2, 3, "normal")
            chance = random.randint(1,2)
            if chance == 1:
                random_item(0, 1, "special")

            print("\nWith this victory in hand you head home, wondering who the survivor once was... ")
            journal_entry(day, "I fought some zombies and looted a survivor's body, RIP")

        else:
            game = False

    else:
        print("Choosing not to risk it, and potentially end up like that guy, you head home")
        journal_entry(day, "Saw a guy getting munched on and got out of there")

    return [game, zombies_killed]