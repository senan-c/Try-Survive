from functions import *

def survivor_footprints_event(area, zombies_killed, character, day, total_armour):
    game = True

    print("As you walk through", area, "you begin to notice the signs of another survivor")
    print("You spot some footprints leading off your usual path, and down a dark side street...")
    print("Will you:\n1. Follow the footprints\n2. Head home")
    choice = make_choice()

    if choice == 1:
        possible_hideouts = ["looted gunstore", "burnt out police station", "dismal house"]
        chance = random.randint(1,3)

        survivor_hideout = possible_hideouts[chance - 1]

        print("You choose to follow the footprints and set off after this survivor")
        print("Sticking to the shadows, you follow the trail to a", survivor_hideout)
        print("You sneak up and take a look through the window")

        survivor_type = random.randint(1,3)
        infected_survivor = random.randint(1, 2)

        if survivor_type != 1:
            if survivor_type == 2:
                human = "raider"

            else:
                human = "survivor"

            print("As your eyes adjust, you notice there's someone inside!")
            print(describe_human(human, 1))
            print("\nWill you:\n1. Approach them\n2. Attack them")
            choice = make_choice()

            if choice == 1:
                print("You take a deep breath, then stand up and walk in the door")

                if human == "raider":
                    print("It's a Raider!")
                    chance = random.randint(1, 2)

                    if chance == 1 and human[28:] in survivor_descriptions_list:
                        print("But to your surprise, the Raider doesn't attack you")
                        print("It looks like he's badly injured and can barely walk")

                        raider_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                        print("\nHe raises his hands and introduces himself as", raider_name)
                        print("You keep your guard up, but he quickly informs you he's not interested in a fight")
                        print("He tells you he got this wound from another Raider after abandoning his group")
                        print(raider_name, "asks for medicine, but realises you may not forgive his past...")

                        if len(character[5]) > 0:
                            print("Will you:\n1.Give", raider_name, "some medicine\n2.Refuse")
                            choice = make_choice()

                            if choice == 1:
                                print("You choose to help", raider_name)
                                print("Click the corresponding button to select an item")
                                print("You have:")
                                count = 1
                                for i in character[5]:
                                    print(str(count) + ". " + i)
                                    count += 1
                                choice = make_choice()
                                print("You give him the", character[5][choice - 1])
                                character[5].remove(character[5][choice - 1])

                                print(raider_name, "thanks you as you have saved his life")
                                print("He promises to make right with this second chance")
                                survivor_group = [raider_name]
                                character[6].append(survivor_group)
                                print(raider_name, "is now your Friend")

                                print("\nWith this good deed, you say goodbye and head on your way home")

                                log = "Found an injured Raider named " + raider_name + " and saved his life"
                                journal_entry(day, log)

                            elif choice == 2:
                                print(raider_name, "looks at you with sad understanding")
                                print("You turn and leave him to his fate, he will not last long...\n")

                                journal_entry(day, "Found an injured raider, but left him to his fate")

                        else:
                            print("But you don't have any medicine and you cannot help")
                            print("You explain this to him and he nods, accepting his fate")
                            print("With nothing more to do or say, you leave him to die...\n")

                            journal_entry(day, "Found an injured raider, but didn't have enough meds to save him")

                    else:
                        print("He snarls and glares at you")
                        print("Looks like there'll be no negotiations here...\n")
                        result = fight(1, "humans", None, total_armour)

                        if result:
                            print("With this fight over, you're free to take a look around the", survivor_hideout)
                            print("Looks like the Raider had a stash of food:")
                            random_item(2, 5, "normal", "food")
                            print("\nWith the food in your bag you head home, wondering if things could have gone differently")

                            journal_entry(day, "Killed a Raider and looted his stash")

                        else:
                            game = False

                elif human == "survivor":
                    print("You walk in and their head jolts towards you")
                    print("Looks like they're a survivor")
                    print("\nYou quickly explain you mean no harm, and the survivor concurs")

                    survivor_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                    print("He shakes your hand and introduces himself as", survivor_name)

                    if infected_survivor == 1:
                        print("But he looks ill and it seems like he's injured")

                    else:
                        print("But it seems like he's injured")

                    choice_line = "\nWill you:\n1. Ask about his wound"

                    if len(character[5]) > 0:
                        choice_line += "\n2. Offer him some medicine"

                    print(choice_line)
                    choice = make_choice()

                    if choice == 2:
                        print("You choose to offer medicine to", survivor_name)
                        print("Click the corresponding button to select an item")
                        print("You have:")
                        count = 1
                        for i in character[5]:
                            print(str(count) + ". " + i)
                            count += 1
                        choice = make_choice()

                        chosen_meds = character[5][choice - 1]
                        print("You give him the", chosen_meds)
                        character[5].remove(chosen_meds)

                        if infected_survivor == 1:
                                print("\nBut he looks at you strangely, the", chosen_meds, "may not be able to heal him")
                                print("Suddenly he collapses to the ground in front of you and lays still")
                                print("\nWill you:\n1. Check if he's ok\n2. Back away")
                                choice = make_choice()

                                if choice == 1:
                                    print("You kneel beside", survivor_name, "and check his pulse")
                                    print("Your heart drops, he's dead!")
                                    print("You look at him solemnly and wish you had gotten here earlier\n")
                                    print("But as you get up off the floor, something catches your eye")
                                    print(survivor_name + "'s", "eyes are wide open and staring at you!")
                                    print("He dives and tackles you, he must have been infected!\n")

                                    if len(character[4][0]) > 1:
                                        chance = random.randint(1,4)

                                        weapon = character[4][random.randint(1, len(character[4]) -1)]

                                        count = 20
                                        while weapon == "**assault rifle**" or weapon == "*pistol*" or count > 0:
                                            weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                            count -= 1

                                    else:
                                        chance = random.randint(1,2)
                                        weapon = "hands"

                                    if chance == 1:
                                        if weapon == "hands":
                                            print("You try push him off with your hands, but it's no use!")
                                            print("He overpowers you and bites...\nYOU DIED")

                                        else:
                                            print("You try push him back with your", weapon, "but there's not enough space!")
                                            print("He bites your arm and you shout in pain, before he lunges for your neck...\nYOU DIED")

                                        game = False

                                    else:
                                        if weapon == "hands":
                                            print("In a superhuman effort you heave his body off of you")
                                            print("He rolls back and jumps again, but you catch him with a kick to the ribs")
                                            print("He falls to the ground again and this time you stomp down, ending the fight...")

                                        else:
                                            print("He opens his mouth wide to bite you, but you stop his teeth with your", weapon)
                                            print("Recoiling back, he swipes at you and misses")
                                            print("You use this opportunity to put him down with your", weapon, "this time he won't get back up...")

                                else:
                                    print("You back away from", survivor_name, "as he lies still on the ground")
                                    print("You can barely hear over your heartbeat, as you battle the urge to help him")
                                    print("Suddenly he twitches, and slowly gets back up")

                                    print("\nBut as he turns to look at you, you realise this isn't", survivor_name, "anymore...")
                                    result = fight(1, "zombies")

                                    if not result:
                                        game = False

                                if game:
                                    zombies_killed += 1
                                    print("\n Shaken but alive you search his bag, retrieving your", chosen_meds, "and finding:")
                                    random_item(1, 3, "normal")
                                    random_item(1, 2, "crafting")
                                    print("\n You return home to the", character[7][0], "but vow to be more cautious next time...")

                                    journal_entry(day, "Tried to help a dying survivor but he turned and attacked me")

                        else:
                            print(survivor_name, "thanks you for your generosity")
                            print("He promises to pay you back someday, and shakes your hand again")
                            survivor_group = [survivor_name]
                            character[6].append(survivor_group)
                            print(survivor_name, "is now your Friend")

                            print("\nWith this done, you say goodbye and head on your way home")

                            log = "Helped a survivor named " + survivor_name + " and made a new friend"
                            journal_entry(day, log)

                    else:
                        print("You ask", survivor_name,"about his appearance mentioning your concerns about a wound")

                        if infected_survivor == 1:
                            print("He mutters something about a fall while scavenging for food")
                            print("He seems feverish and could use some medical help")

                            print("\nWill you:\n1. Check your bag for medical supplies\n2. Reach for a weapon")
                            choice = make_choice()

                            if choice == 1:
                                print("You tell him you can help him, and he looks at you in thinly veiled disbelief")
                                print("You place your bag down and begin to rummage through it for meds")
                                print("But when you look back up he's disappeared")
                                print("It seems he's run to a room in the back of the", survivor_hideout)

                                print("\nWill you:\n1. Go make sure he's ok\n2. Leave the",survivor_hideout)
                                choice = make_choice()

                                if choice == 1:
                                    print("You notice a door slightly ajar, but it's gloomy in here and the electricity has gone out")
                                    print("You call out", survivor_name + "'s", "name, and get no response...")
                                    print("You push the door open and see him standing in the dim light\n")

                                    input("Press 1 to continue: ")
                                    print(line_break)
                                    print("But it's not him anymore...")
                                    result = fight(1, "zombies")

                                    if result:
                                        zombies_killed += 1
                                        print("With the zombie dead you breathe a sigh of relief")
                                        print("\nShaken but alive, you search his body, finding:")
                                        random_item(1, 3, "normal")
                                        random_item(1, 2, "crafting")

                                        print("\nYou return home to the", character[7][0], "but vow to be more cautious next time...")

                                        journal_entry(day, "Tried to help a survivor and nearly got killed when he turned")

                                    else:
                                        game = False

                                else:
                                    print("You're not taking any chances, and you take this opportunity to run for the door")
                                    print("As you make your way home, you wonder what might have really happened to him...")
                                    zombie_survivor = [survivor_name]
                                    zombie_survivors.append(zombie_survivor)

                                    log = "Met a survivor named " + survivor_name + "but he didn't seem right, had to make a run for it"
                                    journal_entry(day, log)

                            else:
                                print("You make eye contact and he looks at you with an almost feral gaze")

                                if len(character[4][0]) > 1:
                                    weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                    print("You grab for your", weapon, "and he shrieks and runs")

                                else:
                                    print("You raise your hands and prepare to fight")
                                    print("But instead of fighting he shrieks and runs")

                                print("He's surprisingly fast, and you can't land a hit on him")
                                print("Kicking open the back door, he dashes out of sight and away from you")
                                print("\nThis escapade has made a lot of noise and to chase him would be too risky")
                                print("You decide to head back to the", character[7][0], "wondering what he was hiding...")
                                zombie_survivor = [survivor_name]
                                zombie_survivors.append(zombie_survivor)

                                log = "Met a survivor named " + survivor_name + "but he didn't seem right, when I reached for a weapon he bolted"

                        else:
                            chance = random.randint(1, 2)
                            if chance == 1:
                                print("He nods and tells you about his narrow escape with a group of masked soldiers")
                                print("Lifting up his shirt, he shows you a bleeding gash, presumably left by a bullet")

                            else:
                                print("He nods and tells you about his narrow escape from a group of Raiders")
                                print("Lifting up his shirt, he shows you a deep slash, presumably left by a raider's machete")

                            print("He notices your expression, and begs you for medical supplies")
                            if len(character[5]) > 0:
                                print("Will you:\n1.Give", survivor_name, "some medicine\n2.Refuse")
                                choice = make_choice()

                                if choice == 1:
                                    print("You choose to help", survivor_name)
                                    print("Click the corresponding button to select an item")
                                    print("You have:")
                                    count = 1
                                    for i in character[5]:
                                        print(str(count) + ". " + i)
                                        count += 1
                                    choice = make_choice()
                                    print("You give him the", character[5][choice - 1])
                                    character[5].remove(character[5][choice - 1])

                                    print(survivor_name, "thanks you as you have saved his life")
                                    print("He promises to return the favour if he sees you again")
                                    survivor_group = [survivor_name]
                                    character[6].append(survivor_group)
                                    print(survivor_name, "is now your Friend")

                                    print("\nWith this good deed, you say goodbye and head on your way home")

                                    log = "Gave a survivor named " + survivor_name + " some meds and made a new friend"
                                    journal_entry(day, log)

                                elif choice == 2:
                                    print(survivor_name, "looks at you with a mix of shock and fear")
                                    print("You turn and leave as he begs you again, he will not last long...\n")

                                    journal_entry(day, "Chose to ignore a survivor's request for medicine, he won't last long")

                            else:
                                print("But you don't have any medicine and you cannot help")
                                print("You explain this to him and tears appear in his eyes")
                                print("With nothing more to do or say, you leave him alone in the", survivor_hideout, "...")

                                journal_entry(day, "A survivor needed medicine, but I couldn't help him")

            else:
                print("You take a deep breath, then burst through the door")

                chance = random.randint(1, 2)

                if chance == 1:
                    if len(character[4][0]) > 1:
                        weapon = character[4][random.randint(1, len(character[4]) - 1)]

                    else:
                        weapon = "fists"

                    print("Taking him by surprise you land a lucky hit with your", weapon, "knocking him down")
                    print("You follow up with another, and he lies still and dead\n")

                    if human == "survivor":
                        print("You check the body and it looks like he was just an injured survivor")
                        journal_entry(day, "Killed a survivor today, don't know if he would have done the same")

                        if infected_survivor == 1:
                            print("But on closer inspection, it looks like he was bitten and infected")
                            print("Maybe it's for the better that you put him down")

                            journal_entry(day, "Killed a survivor today, he was infected anyway")

                    elif human == "raider":
                        print("You check the body and it looks like he was a raider")
                        print("Good thing you took him out")

                        journal_entry(day, "Took a Raider by surprise and killed him")

                    print("\nIt looks like he had:")
                    random_item(1, 3, "normal")
                    random_item(0, 1, "special")

                else:
                    print("But when you enter the", survivor_hideout, "he's looking right at you!")

                    if human == "survivor":
                        print("They're just a survivor, but now you'll have to fight them to the death...\n")

                    elif human == "raider":
                        print("He's a Raider, and Raiders are always ready to fight!\n")
                        journal_entry(day, "Had to fight a Raider to the death")

                    result = fight(1, "humans", None, total_armour)

                    if result:
                        if human == "survivor":
                            print("You've won the battle, and now another survivor lies dead")

                            if infected_survivor == 1:
                                print("As you go to check his corpse, you find an infected bite")
                                print("There isn't much he could have done anyway")

                                journal_entry(day, "Had to fight a survivor to the death, but turns out he was infected anyway")

                            else:
                                journal_entry(day, "Had to fight a survivor to the death")

                    else:
                        game = False

                if game:
                    print("\nYou fill your bag, and head home...")

        else:
            print("It looks like there's a dead survivor on the floor!")
            print("\nWill you:\n1. Go and check the body\n2. Leave the", survivor_hideout, "alone")
            choice = make_choice()

            if choice == 1:
                print("The door creaks as you push it open and step inside")
                print("The room is dimly lit, shadows playing tricks on your mind")
                print("As you check your surroundings, you start wishing this survivor had picked a better place to die\n")
                if infected_survivor == 1:
                    print("When your gaze settle on the body again, a wave of cold fear washes over you")
                    print("It's standing up, and it's shuffling towards you")
                    print("Looks like it wasn't quite dead after all...\n")

                    input("Press 1 to continue: ")
                    print(line_break)

                    zom_num = random.randint(2,4)
                    print("You try and make a run for it, but", zom_num, "more zombies have blocked your path")
                    print("This is going to be a tough fight")

                    result = fight(zom_num + 1, "zombies")

                    if result:
                        zombies_killed += zom_num
                        print("With the zombies dead, you're free to take a look around the room")
                        print("You spot the dead survivor's backpack, and inside you find:")
                        random_item(0, 1, "special")
                        random_item(2, 3, "normal")
                        random_item(1, 3, "crafting")

                        journal_entry(day, "Fought a recently deceased survivor and his friends")

                    else:
                        game = False

                else:
                    print("You go and check the body, it seems he died recently")
                    print("As you check his pockets, you think about what type of person he could have been\n")
                    print("You find nothing there, but spot a backpack in the corner")
                    print("Inside the backpack you find:")
                    random_item(2, 4, "normal")
                    random_item(1, 3, "crafting")

                    journal_entry(day, "Found a dead survivor and looted his backpack")

                if game:
                    print("\nWith this, you head back home to the", character[7][0])

    else:
        print("You've seen enough horror movies to know this is a bad idea, and head home to the", character[7][0], "without risking it")
        journal_entry(day, "Saw some footprints but decided not to follow them")

    return [game, zombies_killed]