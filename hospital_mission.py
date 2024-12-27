from functions import *

def hospital_mission(zombies_killed, day):
    game = True

    print("There must have been a huge battle here recently, the hospital is in bad shape")
    print("The smell of gunpowder is still in the air as you creep through the main building")
    print("You follow the signs towards the storage rooms")

    chance = random.randint(1, 3)

    if chance == 1:
        zom_num = random.randint(8,10)

        print("\nYou find yourself in the waiting room, and it's full of undead patients!")
        enemy = "zombies"

        print("Will you:\n1. Attack them head on\n2. Try sneak past")
        choice = make_choice()

        if choice == 1:
            print("You sprint towards the group of",zom_num, "zombies and cut one down in a surprise attack")
            fight_result = fight(zom_num - 1, enemy)

            if not fight_result:
                game = False

            else:
                zombies_killed += zom_num
                print("With the", enemy, "dead, you can loot the area")

        elif choice == 2:
            chance = random.randint(1,4)
            print("You wait for a few minutes till you see a gap in the crowd, and then you move")

            if chance == 1:
                print("As quietly as possible you begin to inch forward towards the door on the other side")
                print("You're obscured by the shadows with fresh blood and gunpowder covering your scent")
                print("\nYou make it to the next room and continue on your way, unseen...")

            else:
                print("You stick to the shadows and try navigate around the group unseen")
                print("But as you reach the door, your shoe squeaks in a pool of blood")
                print("The zombies jolt towards the sound in unison and you know you'll have to fight...\n")

                fight_result = fight(zom_num, enemy)

                if not fight_result:
                    game = False

                else:
                    zombies_killed += zom_num
                    print("With the", enemy, "dead, you can loot the area")

                    journal_entry(day, "Had to kill some infected patients, but there were good meds at the hospital")

    else:
        print("\nYou find the storage room and without a single zombie in your way")
        print("As you push the door and it creaks open, you can't help but feel a sense of dread...")
        print("You make your way in and thankfully it's not pitch black")

        input("\nPress 1 to continue: ")
        print(line_break)

        print("But there's something else in here with you...")
        print("A Diseased Doctor snarls and jumps out from the shadows!")

        fight_result = fight(1, "boss", "Diseased Doctor")

        if not fight_result:
            game = False

        else:
            zombies_killed += 1
            print("With the Diseased Doctor dead, you can loot the area")

            journal_entry(day, "Had to kill a Diseased Doctor, but there were good meds at the hospital")

    if game:
        print("You scavenge thoroughly and find a chest of medical loot!")
        print("\nYou look inside and find:")
        random_item(5, 8, "normal","meds")
        random_item(1, 3, "special")

    return [game, zombies_killed]