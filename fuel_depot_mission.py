from functions import *

def fuel_depot_mission(location, zombies_killed, day):
    game = True

    print("It looks like the", location, "has seen better days")
    print("Most of the people in the area must have come here to scavenge for fuel")
    print("Burnt out cars and buses full of skeletons litter the depot\n")
    print("It looks like the military must have used the fuel as a last ditch weapon")
    print("You'll have to hope there's some left")

    print("\nAs you navigate the complex, you see more and more bodies")
    print("You round the corner towards the centre of the depot and see an undamaged fuel tank")

    chance = random.randint(1, 3)

    if chance == 1:
        print("Suddenly a burning zombie clad in flame-proof gear rounds the corner!")
        print("If you want to scavenge at the", location, "you'll have to fight the Fuel Beast first...\n")

        fight_result = fight(1, "boss", "Fuel Beast")

        if not fight_result:
            game = False

        else:
            zombies_killed += 1
            print("With the Fuel Beast dead, you can loot the area")
            journal_entry(day, "Killed the Fuel Beast and found loads of fuel for my car")

    elif chance == 2:
        print("But as you move out from cover a horde of scorched zombies pours out into the open!")
        print("You run for some containers and they give chase")
        print("Will you:\n1. Hide and wait for them to pass\n2. Try lose them in the containers")
        choice = make_choice()

        if choice == 1:
            print("You've got a head start on the horde and are able to duck into an open container")
            chance = random.randint(1,4)

            if chance == 1:
                print("But instead of passing by, the horde pours in and tears you to shreds...\nYOU HAVE DIED")
                game = False

            else:
                print("As the horde passes by, you almost choke on the fumes and give yourself away")
                print("But you manage to hold yourself together and they don't notice you")
                print("You wait till they're long gone before you sneak back out and towards the fuel tank")

                journal_entry(day, "Dodged a horde and found loads of fuel for my car")

        elif choice == 2:
            print("With the horde hot on your tail you run left and right between the stacks of containers")
            chance = random.randint(1, 2)

            if chance == 1:
                zom_num = random.randint(5,10)
                print("You look back and see", zom_num, "zombies are still behind you")
                print("You'll have to fight them here...")
                fight_result = fight(zom_num,"zombies")

                if not fight_result:
                    game = False

                else:
                    zombies_killed += zom_num
                    print("With the horde gone and the zombies dealt with, you're free to scavenge")

                    journal_entry(day, "Fought some scorched zombies and found loads of fuel for my car")

            elif chance == 2:
                print("You run as fast as you can, and when you finally look back, there's nothing there")
                print("Looks like you outpaced the horde, and you'll be able to loop around")

                journal_entry(day, "Evaded a horde while exploring and found loads of fuel for my car")

    if game:
        print("\nYou make it to the undamaged fuel tanks and find:")
        random_item(5,8,"normal","fuel")

    return [game, zombies_killed]