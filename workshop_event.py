from functions import *

def workshop_event(area, zombies_killed, character, day, weapon_parts, workshop_event_played, workshop_satchel, total_armour):
    game = True
    noise = False

    print("On your way through " + area + " you catch sight of the local DIY store")
    print("It looks to be in relatively good shape, considering the circumstances...")
    print("Will you:\n1. Take a look inside\n2. Head back to the", character[7][0])
    choice = make_choice()

    if choice == 1:
        go_home = False
        print("Choosing to take a closer look, you make your way through a burnt out car park and up to the front entrance")

        chance = random.randint(1, 2)

        if chance == 1:
            print("Looks like the door is locked...")
            if len(character[4]) > 1:
                weapon = character[4][random.randint(1, len(character[4]) - 1)]

            else:
                weapon = "hands"
            print("Will you:\n1. Break a window with your", weapon, "\n2. Head back to the", character[7][0])
            choice = make_choice()

            if choice == 1:
                if weapon == "hands":
                    chance = random.randint(1, 2)
                    print("You've only got your hands to use, and you grit your teeth before striking a window")

                    if chance == 1:
                        print("The window shatters and luckily you don't hurt yourself in the process")
                    
                    else:
                        print("The window shatters, but you've cut open your hand!")
                        print("\nYou lost 20 HP")
                        status = add_affliction("cut on your hand", 20)

                        if not status:
                            game = False

                        else:
                            print("Ripping a piece of fabric, you wrap it tightly around the wound")
                            print("It'll have to do for now...\n")

                            input("Press 1 to continue:")
                            print(line_break)

                    if game:
                        print("You check to see if anything heard, but the coast is clear")

                else:
                    chance = random.randint(1, 2)
                    print("You strike the window with your", weapon, "and it shatters into a million pieces")

                    if chance == 1:
                        print("You check to see if anything heard, but the coast is clear")

                    else:
                        noise = True
                        zom_num = random.randint(3, 6)
                        print("You check to see if anything heard, and spot", zom_num, "zombies approaching you!\n")

                        result = fight(zom_num, "zombies")

                        if result:
                            zombies_killed += zom_num

                        else:
                            game = False

                if game:
                    print("Looks like you can explore the building now\n")
            
            else:
                if weapon == "hands":
                    print("You won't risk hurting yourself, and decide to head home instead")

                else:
                    print("You won't risk attracting zombies, and decide to head home instead")

                journal_entry(day, "Found a DIY store but decided against breaking in")

                go_home = True

        else:
            print("You try the main door, and it's unlocked\n")

        if not go_home and game:
            print("Stepping into the interior, it seems to be abandoned")

            survivor_chance = random.randint(1, 2)

            if survivor_chance == 1 and len(afflictions) == 0:
                print("But on closer inspection, there are dirty footprints leading into the back of the store...")
                print("You follow the tracks, sticking to the shadows, until you come face to face with two survivors!\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Their eyes go wide when they see you, but they don't attack")

                survivor = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                survivor_bag = []
                loot_amount = random.randint(5, 8)

                for i in range(loot_amount):
                    item = item_list[random.randint(0, len(item_list) - 1)]

                    if day < rot_day:
                        while item[1:5] == "meds" or item[1:5] == "weap":
                            item = item_list[random.randint(0, len(item_list) - 1)]

                    else:
                        while item == "(food) rotten food" or item[1:5] == "meds" or item[1:5] == "weap":
                            item = item_list[random.randint(0, len(item_list) - 1)]

                    survivor_bag.append(item)

                print("Seeing you're not a raider, they introduce themselves as", survivor, "and", survivor2)
                print("It looks like they were looting before they came here, but", survivor2, "has hurt himself badly\n")
                print(survivor, "offers you some of the loot in his bag in exchange for some medicine")

                if len(character[5]) > 0:
                    print("Will you:\n1. Give him some medicine\n2. Refuse his offer\n3. Refuse his offer and take the loot anyway")

                else:
                    print("Will you:\n1. Tell him you have no medicine\n2. Take the loot anyway")
                choice = make_choice()

                if choice == 1 and len(character[5]) > 0:
                    print("You think for a second, before deciding to give him some medicine\n")

                    print("Click the corresponding button to select an item")
                    print("You have:")
                    count = 1
                    for i in character[5]:
                        print(str(count) + ". " + i)
                        count += 1
                    choice = make_choice()
                    chosen_meds = character[5][choice - 1]
                    print("You give him", chosen_meds)
                    character[5].remove(chosen_meds)

                    print(survivor2, "thanks you for saving his life")
                    print("They both promise to try help you in the future\n")
                    survivor_group = [survivor, survivor2]
                    character[6].append(survivor_group)
                    print(survivor, "and", survivor2, "are now your Friends")

                    print("\nBefore they leave,", survivor, "reaches in his bag and gives you:")
                    if chosen_meds == "painkillers":
                        loot_amount = 2

                    elif chosen_meds == "bandages":
                        loot_amount = 3

                    else:
                        loot_amount = 4

                    for i in range(loot_amount):
                        item = survivor_bag[random.randint(0, len(survivor_bag) - 1)]
                        survivor_bag.remove(item)
                        print(item)
                        add_item(item)

                    input("\nPress 1 to continue: ")
                    print(line_break)
                    print("You've made some new friends, and now it's time to loot the building")

                elif choice == 1 and len(character[5]) == 0:
                    print("But you tell him you don't have any medicine, and his face drops")
                    print(survivor, "goes to comfort his friend, and you head off to loot the building\n")
                    
                    input("Press 1 to continue: ")
                    print(line_break)

                elif choice == 2 and len(character[5]) > 0:
                    print("You think for a second, then refuse his offer")
                    print("He looks at you in disbelief before his eyes narrow, turning his back on you to go comfort his friend")
                    print("With nothing else to say, you turn to go loot the building\n")

                    input("Press 1 to continue: ")
                    print(line_break)

                elif (choice == 2 and len(character[5]) == 0) or choice == 3:
                    print("You consider his offer, then tell him you'd rather just take all off his stuff")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("Both survivors look at you in shock, before", survivor, "drops his bag and kicks it over to", survivor2)
                        print("You won't be getting it without a fight!\n")

                        result = fight(1, "humans", survivor, total_armour)

                        if result:
                            print(survivor2 + " yells out as " + survivor + "'s body hits the ground")
                            print("He struggles, but he's unable to get up as you grab the bag\n")
                            print("Checking inside you find:")
                            for i in survivor_bag:
                                print(i)
                                add_item(i)

                            print("\nAfter taking these items for yourself you head off to loot the building, leaving", survivor2, "behind...\n")

                            input("Press 1 to continue: ")
                            print(line_break)

                        else:
                            game = False

                    else:
                        print("The two survivors look at you in shock, then", survivor, "looks at", survivor2, "and sighs before handing his bag over")
                        print("You thank him and his eyes narrow, but he doesn't attack")
                        print("Instead he turns to help his friend up before the two of them leave\n")

                        input("Press 1 to continue: ")
                        print(line_break)

                        print("Once they're gone, you search the bag and find:")
                        for i in survivor_bag:
                                print(i)
                                add_item(i)

                        print("\nAfter taking these items for yourself you decide to take a look around the building\n")

                        input("Press 1 to continue: ")
                        print(line_break)

            if game:
                print("After searching around for a couple of minutes, you find yourself in front of a room labeled 'Workshop'\n")

                input("Press 1 to continue: ")
                print(line_break)
                
                zom_chance = 0
                if survivor_chance == 2 or len(afflictions) > 0:
                    if len(character[4]) == 1:
                        zom_chance = random.randint(1, 2)

                    elif noise:
                        zom_chance = 2

                    else:
                        zom_chance = 1

                if zom_chance == 1:
                    zom_num = random.randint(2, 4)
                    print("You push open the doors, but there are", zom_num, "zombies inside!\n")

                    result = fight(zom_num, "zombies")

                    if result:
                        print("The zombies lie dead, and now you can look around")
                        zombies_killed += zom_num

                    else:
                        game = False

                else:
                    print("You push open the doors but there's nobody inside")

                if game:
                    print("The light is dim, but in the center of the room you spot a workbench you might be able to use")

                    input("\nPress 1 to continue: ")
                    print(line_break)
                    print("Checking the surface of the table you find:")
                    if not workshop_event_played:
                        print("(book) crafting recipes")
                        character[8].append("book of crafting recipes")
                    
                    chance = random.randint(1, 2)
                    if chance == 1:
                        print("(weapon) hammer")
                        add_item("(weapon) hammer")

                    random_item(3, 5, "crafting")
                    chance = random.randint(1, 2)
                    if chance == 1:
                        parts_found = random.randint(2, 3)
                        print("(material)", parts_found, "weapon parts")
                        weapon_parts += parts_found

                    if not workshop_event_played:
                        print("\nWould you like to read the (book) crafting recipes?\n1. Yes\n2. No")
                        choice = make_choice()

                        if choice == 1:
                            crafting_recipes()
                            print(line_break)

                    workshop_event_played = True
                    print("It looks like you'll be able to use this workbench")
                    print("Will you:\n1. Craft at the workbench\n2. Head home")        
                    choice = make_choice()

                    if choice == 1:
                        workshop_satchel = craft_item(weapon_parts, workshop_satchel) 
                        print("Once you've finished at the workbench, you head home to the", character[7][0])
                        journal_entry(day, "Found a workbench in a DIY store")

                    else:
                        print("Deciding not to use the workbench, you head home to the", character[7][0])
                        journal_entry(day, "Found a workbench in a DIY store but decided not to use it")

    return [game, zombies_killed, weapon_parts, workshop_satchel]