from functions import *

def military_base_mission(zombies_killed, day):
    game = True

    print("\nYou walk by deserted barracks and empty offices, but something doesn't feel right")
    print("You make your way deeper and deeper into the complex")
    print("But you can't shake the feeling that you're not alone")
    chance = random.randint(1,2)

    if chance == 1:
        print("\nYou find yourself looking at a huge reinforced door, it's clearly hiding something...")
        print("You investigate and find it's unlocked, the army must have left in a hurry")
        print("As you struggle to open it you hear a roar and the door flies open!")

        enemy = "Infected Commander"
        fight_result = fight(1, "boss", enemy)
        if not fight_result:
            game = False

    else:
        print("\nYou find yourself at the storage depot")
        zom_num = random.randint(7,12)
        enemy = "military zombies"
        print("But as you prepare to enter, a group of", str(zom_num) + " " + enemy, "swarms out!")
        fight_result = fight(zom_num, "military zombies")

        if fight_result:
            zombies_killed += zom_num

        else:
            game = False

    if game:
        print("\nWith the", enemy, "dead, you're free to look around")
        print("You scavenge around the area and find a chest of military loot!")
        print("\nYou look inside and find:")
        random_item(1,5,"normal")
        random_item(1,3,"special")
        random_item(0,1, "ultra special")

        if chance == 1:
            journal_entry(day, "Had to fight an Infected Commander, but got some good loot for my trouble")

        else:
            journal_entry(day, "Had to fight some military zombies, but got some good loot for my trouble")

    return [game, zombies_killed]