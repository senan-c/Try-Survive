from functions import *

def surrounded_van_event(area, zombies_killed, character, day):
    game = True

    print("As you're busy checking the streets of",area,"you hear a commotion nearby")
    event= random.randint(1,10)
    if event == 1:
        van = "Survivor's Van"

    elif event == 2 or event == 3:
        van = "Ambulance"

    else:
        van = "Food Truck"

    print("You turn the corner, and spot an abandoned",van,"surrounded by dozens of zombies")
    print("From this distance you can't see if it's been looted or not")
    print("A horde of this size is very dangerous, but it could be worth it...")
    print("Will you:\n1. Distract the horde\n2. Lead the horde away\n3. Leave the horde alone")
    choice = make_choice()

    if choice == 1:
        chance = random.randint(1,2)
        print("You sneak behind a car and grab a rock from the pavement")
        if chance == 1:
            print("You throw the rock as far as you can and it strikes a window down the street")
            print("The horde of zombies lift their heads as one, and trundle towards the sound")

            print("\nWith them out of the way, you're free to check out the",van)
            chance = random.randint(1,3)
            if chance != 1:
                print("The",van,"seems completely intact!\n")
                print("You open the doors and find:")
                if van == "Survivor's Van":
                    random_item(1,2,"special")
                    random_item(2,5,"normal")

                    log = "Lured a horde away and looted a " + van
                    journal_entry(day, log)

                elif van == "Ambulance":
                    random_item(3, 6, "normal", "meds")

                    log = "Lured a horde away and looted an " + van
                    journal_entry(day, log)

                elif van == "Food Truck":
                    random_item(5, 10, "normal", "food")

                    log = "Lured a horde away and looted a " + van
                    journal_entry(day, log)

                print("\nHappy with today's score, you head home, wishing every day was like this")

            elif chance == 2:
                print("But it looks like the horde got to the van first")
                print("Disappointed, you head back to the",character[7][0])

                journal_entry(day, "Found a promising van but a horde got to it first")

        elif chance == 2:
            print("You throw the rock and the window smashes, but suddenly the alarm blares, this is way too loud!")
            print("Your distraction has worked too well and another horde of zombies appears from behind you")
            print("You need to escape, and quickly!")
            print("Will you:\n1. Fight your way through a weak spot in the hordes\n2. Make a run for a side street")
            choice = make_choice()

            if choice == 1:
                chance = random.randint(1,3)
                print("You run straight for the weakest zombies in the horde behind you")
                if chance != 1:
                    print("As they reach out to grab you, you use your",character[4][-1],"to fight them off")
                    print("Somehow you fight your way through without a scratch and head back to the",character[7][0])

                    journal_entry(day, "Ended up fighting my way through a horde, wouldn't recommend")

                else:
                    print("But as you prepare to burst through, a zombie jumps out from behind a car")
                    print("It throws you off balance and you tumble right into the horde...\nYOU ARE DEAD")
                    game = False

            elif choice == 2:
                chance = random.randint(1,2)
                print("You make a dash for the side street to your left, and through the hordes")
                if chance == 1:
                    print("The zombies at the front of both hordes reach out for you...")
                    print("But you somehow make it through the gap")
                    print("After this close call you decide to head home to the",character[7][0])

                    journal_entry(day, "Nearly died while trying to lure a horde")

                elif chance == 2:
                    print("You've almost made it through when a zombie gets hold of your bag")
                    print("It yanks you back, and your head lashes back with it")
                    print("With adrenaline rushing through you, you manage to wrestle free and escape")
                    item_lost = ""
                    if len(character[3]) > 1:
                        lost_item = character[3][random.randint(1, len(character[4]) - 1)]
                        item_lost = "and lost a " + lost_item

                    elif len(character[5]) > 1:
                        lost_item = character[5][random.randint(1, len(character[5]) - 1)]
                        item_lost = "and lost a " + lost_item

                    print("You make your way back, but you've hurt your neck " + item_lost)
                    print("\nYou have lost 15HP")
                    status = add_affliction("sprained neck", 15)

                    if not status:
                        game = False

                journal_entry(day, "Nearly died while scavenging, sprained my neck instead")

    elif choice == 2:
        print("You decide to lead the horde away, shouting and waving your arms")
        chance = random.randint(1, 2)
        if chance == 1:
            print("The horde gives chase, following you down the street and away from the",van)
            print("Will you:\n1. Double back around\n2. Hide and wait for the horde to pass")
            choice = make_choice()

            if choice == 1:
                print("You double back around through a dark alley")
                chance = random.randint(1, 2)
                if chance == 1:
                    print("You were quick enough that the horde hasn't noticed and they trod straight past")
                    print("You make your way back and find the",van,"now deserted\n")
                    chance = random.randint(1,3)

                    if chance != 1:
                        print("The", van, "looks like it hasn't been looted!\n")
                        print("You open the doors and find:")
                        if van == "Survivor's Van":
                            random_item(1, 2, "special")
                            random_item(2, 5, "normal")

                            log = "Lured a horde away and looted a " + van
                            journal_entry(day, log)

                        elif van == "Ambulance":
                            random_item(3, 6, "normal", "meds")

                            log = "Lured a horde away and looted an " + van
                            journal_entry(day, log)

                        elif van == "Food Truck":
                            random_item(5, 10, "normal", "food")

                            log = "Lured a horde away and looted a " + van
                            journal_entry(day, log)
                        
                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("\nProud of your horde evading abilities, you head home with the loot")

                        elif len(enemy_list) > 0 and chance == 2:
                            enemy_name = enemy_list[random.randint(0, len(enemy_list) - 1)]
                            enemy_list.remove(enemy_name)

                            print("\nProud of your horde evading abilities, you turn to head home with the loot")
                            print("But there's someone standing behind you")

                            if len(enemy_name) == 1:
                                if enemy_name[0] in killer_list:
                                    killer_list.remove(enemy_name[0])
                                    print("It's the killer", enemy_name[0], "he's tracked you down!")
                                    print("This time you won't be able to escape...")

                                else:
                                    print("It's", enemy_name[0], "back for revenge!")
                                    print("He glowers at you, and promises to punish you for what you did")

                            else:
                                print("He snarls, promising revenge for the death of his friend", enemy_name[1])
                            
                            print()
                            fight_result = fight(1, "humans", enemy_name[0])

                            if fight_result:
                                print("With", enemy_name[0], "dead, you make your way back to the", character[7][0])

                                if enemy_name[0] not in killer_list:
                                    print("You'll be thinking twice before you mess with a survivor again...")

                                log = enemy_name[0] + " returned and I had to kill him or be killed"
                                journal_entry

                            else:
                                game = False

                    else:
                        print("Looks like the horde got to the van first, but it was worth a try")
                        print("Disappointed, you head back to the", character[7][0])

                        journal_entry(day, "Had my loot stolen from me by a horde")

                elif chance == 2:
                    print("You try and duck in quickly, but the horde spots you!")
                    chance = random.randint(1,2)
                    if chance == 1:
                        print("You break into a sprint and manage to get away before it closes around you")
                        print("But the horde heads back towards the",van,"and you've lost your chance")
                        print("You head home, glad you escaped but annoyed about wasting this opportunity")

                        journal_entry(day, "Horde almost got me while looting")

                    elif chance == 2:
                        kills = random.randint(2,10)
                        print("You try make your getaway but another group of zombies has circled around!")
                        print("Trapped in the alley, you manage to kill",kills,"zombies with your", character[4][-1])
                        print("But the numbers are overwhelming and the horde envelops you...\nYOU ARE DEAD")
                        game = False

            elif choice == 2:
                print("With the horde closing in, you run for a damaged shop window to hide in")
                print("You dive through the broken glass and take cover behind a display")
                chance = random.randint(1,2)
                if chance == 1:
                    print("The horde passes by, oblivious to your hiding spot and you make your way back to the",van)
                    print("It looks like you managed to lure the whole horde, the",van,"is now abandoned\n")
                    chance = random.randint(1, 2)
                    if chance == 1:
                        print("It looks like it hasn't been looted!\n")
                        print("You open the doors and find:")
                        if van == "Survivor's Van":
                            random_item(1, 2, "special")
                            random_item(2, 5, "normal")

                            log = "Lured a horde away and looted a " + van
                            journal_entry(day, log)

                        elif van == "Ambulance":
                            random_item(3, 6, "normal", "meds")

                            log = "Lured a horde away and looted an " + van
                            journal_entry(day, log)

                        elif van == "Food Truck":
                            random_item(5, 10, "normal", "food")

                            log = "Lured a horde away and looted a " + van
                            journal_entry(day, log)

                        print("\nProud of your horde evading abilities, you head home with the loot")

                    else:
                        print("Seems like the van has been picked clean, it's completely empty")
                        print("Disappointed, you head back to the", character[7][0])

                        journal_entry(day, "Lured a horde away but they picked the place clean")

                elif chance == 2:
                    print("But you jump too short and catch yourself on the glass, cutting deep!")
                    print("\nYou have lost 30HP")
                    status = add_affliction("deep cut", 30)

                    if not status:
                        game = False

                    if game:
                        chance = random.randint(1,2)
                        if chance == 1:
                            print("Practising extreme control, you don't make a sound and the horde goes by")
                            print("But you've injured yourself and you decide to just head back to the", character[7][0])

                            journal_entry(day, "I cut myself on some glass and almost alerted a horde")

                        elif chance == 2:
                            print("\nYou shout in pain, and the horde stops as they hear your cries")
                            print("You raise your hands weakly to defend yourself")
                            print("But the horde floods in and you're ripped apart almost instantly...\nYOU HAVE DIED")
                            game = False

        elif chance == 2:
            print("The horde surrounding the",van,"gives chase, but so does another horde from the opposite direction")
            print("It looks like you're pinned")
            print("Will you:\n1.Make a run for it\n2.Fight your way out")
            choice = make_choice()
            if choice == 1:
                print("You break into a sprint, trying to outpace the legions of undead")
                chance = random.randint(1,2)
                if chance == 1:
                    print("Their undead flesh is no match for your speed and you get away unscathed")
                    print("You loop back to the van but it's still covered in zombies")
                    print("You'll have to leave before it gets dark,",van,"or not")

                    journal_entry(day, "Had to outrun a horde, scavenging run not successful")

                elif chance == 2:
                    print("You make a run for it but you aren't fast enough, you try fight back but there are too many...")
                    print("YOU ARE DEAD")
                    game = False

            elif choice == 2:
                zom_num = random.randint(3,10)
                print("You decide to fight your way out with",zom_num,"zombies in your way")
                fight_result = fight(zom_num, "zombies")
                if fight_result == False:
                    game = False

                else:
                    zombies_killed += zom_num
                    print("With the zombies defeated, you make your escape, heading back to the",character[7][0])

                    journal_entry(day, "Got cornered by a horde but killed a good few zombies and escaped")

    elif choice == 3:
        print("You make the safe decision, telling yourself it's the smart one")
        print("But as you head home to the",character[7][0],"you can't help but wonder what was in the",van)

        journal_entry(day, "Spotted a van surrounded by zombies but didn't test my luck")

    return [game, zombies_killed]