from functions import *

def zombie_patrol_event(area, character, zombies_killed, day):
    game = True

    print("You've reached the streets of", area, "and begin to look around")
    print("The telltale shuffle of zombies alerts you to their presence, and you dive for cover")
    zom_num = random.randint(4, 7)
    print("Peering over the rubble from a collapsed building, you spot the group of", zom_num, "undead\n")

    print("But these are no ordinary zombies, it looks like you've stumbled across a patrol that never returned...")
    print("Their fatigues are tattered and covered in blood, their weapons either missing or destroyed\n")
    print("But just as you're about to turn and leave, you spot a promising looking rucksack on one of their backs")
    print("There could be some excellent loot inside that bag...")
    print("Will you:\n1. Fight the military zombies\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("You want that bag, and you're willing to risk fighting some zombies for it")
        print("Hopefully whatever's inside is worth it...\n")

        result = fight(zom_num, "military zombies")

        if result:
            zombies_killed += zom_num

            print("With the lost patrol finally put to rest, you check out the rucksack and find:")
            chance = random.randint(1, 10)

            if chance < 7:
                chance = random.randint(1, 3)

                if chance == 1:
                    rucksack_loot = ["(ammo) *3 pistol bullets*", "(ammo) *5 pistol bullets*", "(ammo) *10 pistol bullets*", "(ammo) **10 rifle bullets**", "(ammo) **15 rifle bullets**"]
                    loot_amount = random.randint(3, 5)

                    for i in range(loot_amount):
                        loot = rucksack_loot[random.randint(0, len(rucksack_loot) - 1)]
                        print(loot)
                        add_item(loot)

                else:
                    loot_amount = random.randint(4, 6)

                    for i in range(loot_amount):
                        print("(food) MRE")
                        add_item("(food) MRE")

            elif chance == 10:
                print("(gun) **assault rifle**")
                print("(ammo) **20 rifle bullets**")

                add_item("(gun) **assault rifle**")
                add_item("(ammo) **20 rifle bullets**")

            elif chance >= 7:
                print("(gun) *pistol*")
                print("(ammo) *20 pistol bullets*")

                add_item("(gun) *pistol*")
                add_item("(ammo) *20 pistol bullets*")

            print("\nPacking your spoils into your own bag, you decide to end on a good note and head home")
            print("As you head back to the", character[7][0], "you wonder if that's the last you've seen of the military...")

            journal_entry(day, "Fought some military zombies and found some great loot")

        else:
            game = False

    else:
        print("Knowing the dangers of these hardened military zombies, you decide not to risk it")
        print("Heading back to the", character[7][0], "you find yourself wondering what might have been in that bag...")

        journal_entry(day, "Spotted a group of military zombies but decided not to fight them")

    return [game, zombies_killed]