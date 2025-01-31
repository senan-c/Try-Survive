from functions import *

def supply_crate_event(area, zombies_killed, character, day):
    game = True

    zom_num = random.randint(1,5)
    if zom_num == 1:
        zombie_grammar = "zombie"

    else:
        zombie_grammar = "zombies"

    if zom_num == 1:
        print("On your way through",area,"you spot a zombie walking near a crate of supplies")
        print("Will you:\n1. Fight the zombie\n2. Sneak away")

    else:
        print("On your way through the forest you spot",zom_num,"zombies walking near a crate of supplies")
        print("Will you:\n1. Fight the zombies\n2. Sneak away")
    
    fight_choice = make_choice()

    if zom_num == 1:
        zombie_grammar = "a zombie"

    else:
        zombie_grammar = "some zombies"

    if fight_choice == 1:
        if zom_num == 1:
            zombie_grammar = "a zombie"
            print("You approach the zombie and get ready to fight")

        else:
            zombie_grammar = "some zombies"
            print("You approach the zombies and get ready to fight")

        fight_result= fight(zom_num,"zombies")
        if not fight_result:
            game = False

    if game:
        if fight_choice == 1:
            zombies_killed += zom_num

            supplies_before = character
            print("After the battle, you go up and check the crate to see what's inside")

            print("You crack open the crate and find:")
            random_item(2,4,"normal")
            random_item(1, 2, "normal", "food")

            print()
            chance = random.randint(1, 8)

            if chance == 1 or chance == 2:
                print("You turn to head home, and see a desperate survivor standing behind you")
                survivor_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                print("He says his name is", survivor_name, "and begs you for some food\n")

                if len(character[3]) > 0:
                    print("Will you:\n1.Give", survivor_name, "some food\n2.Refuse")
                    choice = make_choice()

                    if choice == 1:
                        print("You choose to help", survivor_name)
                        print("Click the corresponding button to select an item")
                        print("You have:")
                        count = 1
                        for i in character[3]:
                            print(str(count) + ". " + i)
                            count += 1
                        choice = make_choice()
                        print("You give him (food)", character[3][choice - 1])
                        character[3].remove(character[3][choice - 1])

                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("He shakes your hand vigorously and stuffs the food in his bag")
                            print("Thanking you for his kindness, he promises to help you in the future")
                            survivor_group = [survivor_name]
                            character[6].append(survivor_group)
                            print(survivor_name, "is now your Friend")
                            print("\nWith this victory in hand and a new friend, you head home with a smile")

                            log = "I Killed " + zombie_grammar + " and made a new friend named " + survivor_name
                            journal_entry(day, log)

                        else:
                            print("He snatches the food from your hands and scurries away")
                            print("You go to stop him, but with this kind of behaviour, he probably needs it more than you do...")
                            print("You head home to the", character[7][0], "contemplating your decision...")

                            log = "I Killed " + zombie_grammar + " and fed some wierdo"
                            journal_entry(day, log)

                    else:
                        print("You refuse his request, but instead of attacking, he sobs and runs off")
                        print("He won't last long out there, and on your way home you wonder if it was worth keeping the food...")
                        chance = random.randint(1, 2)

                        if chance == 1:
                            zombie_survivor = [survivor_name]
                            zombie_survivors.append(zombie_survivor)

                        log = "I Killed " + zombie_grammar + " and didn't give a guy named " + survivor_name + "some food"
                        journal_entry(day, log)

            elif chance == 8:
                print("But as you the supplies into your bag, two Raiders step in front of you!")
                print("They draw their weapons and tell you to hand over your spoils")
                print("Will you:\n1. Fight the Raiders\n2. Give them the supplies")

                choice = make_choice()

                if choice == 1:
                    print("You briefly consider their offer, then drop your bag and draw your own weapon")
                    print("They snarl and the fight begins")

                    result = fight(2, "humans")

                    if not result:
                        game = False
                    
                    else:
                        print("The Raiders lie dead and the supplies are still yours\n")
                        print("You head home proud that you stood up for yourself")
                        journal_entry(day, "Looted a supply crate and killed some Raiders who wanted a piece")

                elif choice == 2:
                    print("You're not going to risk a fight with some Raiders, and you hand over the meat you worked so hard for")
                    print("Their eyes widen as they snatch it from your hands, and you hear them laughing as they walk off")
                    print("Your face burns with embarassment as you turn and head home...")

                    character = supplies_before

                    journal_entry(day, "Went looting but had my spoils stolen by Raiders")

            else:
                print("With this victory in hand, you head home with a smile")

                log = "Killed " + zombie_grammar + " and looted a crate"
                journal_entry(day, log)

        else:
            print("You don't feel great about sneaking away, but it's better than dying")
            print("On your way home you wonder about what might've been in the crate")

            log = "I ran into " + zombie_grammar + " but got away undetected"
            journal_entry(day, log)

    return [game, zombies_killed]