from functions import *

def unlooted_store_event(area, zombies_killed, character, day, bag_items):
    game = True

    print("As you walk through", area, "you notice a seemingly unlooted store")
    print("You walk up and try the door, but it's locked")
    print("Will you:\n1. Try force the door open with your",character[4][-1],"\n2. Try find another way in\n3. Smash the window\n4. Don't risk it")
    choice = make_choice()

    if choice == 1:
        chance = random.randint(1,4)
        if chance == 1 or chance == 4:
            print("You force the door, and suddenly it cracks and gives way")
            print("The store definitely isn't as untouched as you thought, but you'll make do\n")
            print("You check the aisles and find:")
            random_item(4, 10, "normal")

            print("\nHappy with your score, you return home to the",character[7][0],"with a smile on your face")
            journal_entry(day, "Forced the door open and looted a store with no hassle")

        elif chance == 2:
            print("As you force the door inwards, it suddenly heaves out and a dozen hands grab for your clothes")
            print("You've stumbled upon a sleeping horde!")
            print("Which way do you run:\n1. Left\n2. Right")
            choice = make_choice()
            chance = random.randint(1,3)
            if choice == 1:
                direction = "left"

            elif choice == 2:
                direction = "right"

            print("You run to the",direction)
            if chance == 1:
                print("And straight into a mass of zombies!")
                chance = random.randint(1, 2)
                if chance == 1:
                    print("Luckily you're quick on your feet and manage to turn around and make a quick getaway")
                    if len(character[4]) > 1:
                        lost_weapon = character[4][random.randint(1, len(character[4]) - 1)]
                        print("But in the process you lose your",lost_weapon)
                        remove_item(lost_weapon)
                    print("When you get home to the",character[7][0],"you're just happy you're alive")

                    journal_entry(day, "Tried to loot a store and barely escaped a horde")

                elif chance == 2:
                    chance = random.randint(1, 2)

                    if len(character[6]) == 0 or chance == 1:
                        print("You slip as you try desperately to get away, and are pulled into the horde...\nYOU ARE DEAD")
                        game = False

                    else:
                        friends = character[6][random.randint(0, len(character[6]) - 1)]
                        friend1 = friends[0]

                        if len(friends) > 1:
                            friend2 = friends[1]
                            print("You slip and arms reach out and grab you, but " + friend1 + " and " + friend2 + " cut through them and pull you away!")
                            print("The three of you escape the horde, and they remind you of the favor they owed you")
                            print("\nYou thank them profusely and say goodbye, returning home to the", character[7][0])

                            log = "Almost died while looting but I was saved by my friends " + friend1 + " and " + friend2
                            journal_entry(day, log)

                        else:
                            print("You slip and arms reach out and grab you, but suddenly you're pulled back away from the horde")
                            print("It's", (friend1 + "!"), "he's rescued you!")
                            print("The two of you escape the horde, and he reminds you of the favor he owed you")
                            print("\nYou thank him profusely and say goodbye, returning home to the",character[7][0])

                            log = "Almost died while looting but I was saved by my friend " + friend1
                            journal_entry(day, log)

            else:
                print("You know you made the right choice by running to the",direction,"as you see a horde swarm through the street behind you")

                journal_entry(day, "I almost got caught by a horde while looting")

        elif chance == 3:
            print("As the door gives way the alarm activates")
            chance = random.randint(1,2)
            if chance == 1:
                print("But your quick reflexes allow you to get away before a horde arrives")
                print("Still terrified you sprint all the way home to the",character[7][0])

                journal_entry(day, "An alarm went off while I was looting, but I escaped easily")

            elif chance == 2:
                print("You jump back, hitting your head on the door frame and cutting it open")
                print("Clutching your head, you make a run for it, but you'll need to do something about your injury later")
                print("\nYou have lost 50HP")
                status = add_affliction("laceration on your head", 50)

                if not status:
                    game = False

                if game:
                    print("\nYour head is pounding when you reach the",character[7][0],"but it's a reminder you're alive")

                    journal_entry(day, "Made a mess of a scavenging trip and split my head open on a door frame")

    elif choice == 2:
        print("Not trying to make any noise messing with the locked door, you go look for a back entrance")
        print("You walk down an alleyway to find your way around")
        chance = random.randint(1,3)
        if chance == 1:
            print("You were correct and there is a back entrance, but it's been destroyed by a crashed van")
            print("There's no way through")

            chance = random.randint(1, 2)

            if chance == 1 or len(zombie_survivors) == 0:
                print("\nYou turn to try the front door but a horde is coming down the street, it's too late now")
                print("You make your way back to the",character[7][0],"wondering what might have been")
                journal_entry(day, "Tried looting a store but some idiot crashed his van and ruined it")

            else:
                print("You turn to leave, but there's a zombie standing in your path")
                missing_friend = False

                if len(zombie_survivors) > 1:
                    named_zombie_group = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)]
                    named_zombie = named_zombie_group[0]

                else:
                    named_zombie_group = zombie_survivors[0]
                    named_zombie = named_zombie_group[0]

                if len(named_zombie_group) > 1:
                    missing_friend = True
                    named_zombie2 = named_zombie_group[1]

                print("\nIt's " + named_zombie + "!")
                if missing_friend:
                    print("Looks like", named_zombie2, "isn't here, though he probably met a similar fate...")

                    enemy_group = [named_zombie2, named_zombie]
                    enemy_list.append(enemy_group)

                if named_zombie == "the Thief":
                    print("And it looks like he still has your bag on his back")
                    print("This might just be your opportunity to finally get it back...")

                else:
                    print("Reminding yourself that this zombie isn't a person anymore, you prepare for a fight")
                fight_result = fight(1, "zombies", named_zombie)

                if fight_result:
                    zombies_killed += 1
                    zombie_survivors.remove(named_zombie_group)

                    if named_zombie == "the Thief":
                        print("You grab your bag off its back and check the contents, everything's there")
                        for i in bag_items:
                            add_item(i)
                            bag_items.remove(i)

                    else:
                        print("You look down at", named_zombie, "but it's time to leave")

                    print("Circling around to the front of the building you see the street filled with zombies")
                    print(named_zombie, "must have brought a horde with him here, and now there's no way of getting in")
                    print("With nothing left to do, you decide to just head back to the", character[7][0], "instead")

                    journal_entry(day, "Tried to loot a store but was ambushed by a familiar face instead")


        elif chance == 2:
            print("You check the back, and there is indeed an unlocked door through to the store")

            chance = random.randint(1, 3)

            if chance == 1:
                zom_num = random.randint(2, 3)

                print("\nYou open the door but there are", zom_num, "zombies inside!")
                print("You're going to have to fight for this loot!\n")
                fight_result = fight(zom_num, "zombies")

                if fight_result:
                    zombies_killed += zom_num
                    print("With them out of the way, you're free to check out the store")

                else:
                    game = False
            
            if game:
                print("It's definitely not as full as it looked but it's good enough for you\n")
                print("You check the aisles and find:")
                random_item(3,8,"normal")

                print("\nFeeling smart and with your pockets full, you decide to head back to the",character[7][0])

                journal_entry(day, "Found the back door of an unlooted store and filled my pockets")

        elif chance == 3:
            print("You check around the corner of the alleyway, but it seems a bomb has gone off here")
            print("Skeletons litter the pavement, and you get a sick feeling in your stomach")
            print("You take another look and it seems a bag by the end of the alleyway has survived")
            print("\nWill you:\n1. Climb over the rubble to reach it\n2. Move on")
            choice = make_choice()
            if choice == 1:
                chance = random.randint(1,2)
                if chance == 1:
                    print("You climb up the mountain of rubble, bag in your sights")
                    print("But your foot slips and you fall, slicing your arm on some exposed rebar")
                    print("\nYou have lost 30HP")
                    status = add_affliction("gash on your arm", 30)

                    if not status:
                        game = False

                    if game:
                        print("You clutch your arm, unable to climb anymore, and head back to the",character[7][0])

                        journal_entry(day, "Cut my arm open while climbing like an idiot, wasn't worth it")

                elif chance == 2:
                    print("You slowly climb your way up the pile of rubble")
                    print("Once you reach the top, you slide your way down towards the bag")
                    print("You check the bag and find:")
                    random_item(1,3,"normal")

                    print("Happy with this, you carefully climb back over and head home to the",character[7][0])

                    journal_entry(day, " Spotted a bag and climbed over some rubble to get it, I'm basically spiderman now")

            if choice == 2:
                print("Sensibly, you decide all this rubble is too dangerous and head home to the",character[7][0])

                journal_entry(day, "Was scavenging and decided not to climb through rubble for a possibly empty bag")

    elif choice == 3:
        chance = random.randint(1,3)
        if chance == 1:
            print("As you go to smash the glass with your",character[4][-1],"you notice a spark plug on the ground")
            print("Thinking quickly, you throw it at the window")
            chance = random.randint(1,2)
            if chance == 1:
                print("The glass shatters instantly and better yet, there's no alarm")
                print("You're now able to help yourself to the contents of the store\n")
                print("You check the aisles and find:")
                random_item(3,10,"normal")

                journal_entry(day, "Found a store and shattered the window with a spark plug, easy loot")

            elif chance == 2:
                print("The glass shatter perfectly, but suddenly the alarm blares")
                print("A horde of zombies appears but you hide behind a car, far away after your throw")
                print("You thank your quick thinking and head home to the",character[7][0])

                journal_entry(day, "Had my scavenging trip ruined by an alarm")

        elif chance == 2:
            print("You crack the glass with your weapon, but it's too loud and zombies start to appear from all around")
            print("You can't risk looting the shop now with all these zombies nearby")
            print("Cursing your stupidity you jog back to the",character[7][0] + ",", "sure to lose the zombies on your tail")

            journal_entry(day, "Was too loud while looting and rang the zombie dinner bell")

        elif chance == 3:
            print("You bring your weapon down hard on the glass, but it shatters and cuts your hand")
            print("\nYou have lost 20HP")
            status = add_affliction("cut on your palm", 20)

            if not status:
                game = False

            if game:
                print("A horde starts to form, and you know you have to get out of here")
                chance = random.randint(1,2)
                if chance == 1:
                    print("You run for a gap in the crowd, but slip on your own blood and come crashing to the ground")
                    print("The horde closes around you, there is no escape...\nYOU ARE DEAD")
                    game = False

                elif chance == 2:
                    print("Holding your palm tight, you run for a gap in the growing number of zombies")
                    print("You make it through by the skin of your teeth, and run all the way home to the",character[7][0])

                    journal_entry(day, "Cut my hand open like an idiot and nearly died")

    if choice == 4:
        print("Thinking there must be a reason this store hasn't been looted, you decide not to try it")
        print("Though you feel like a bit of a coward, you don't entirely regret your decision as you head back to the",character[7][0])

        journal_entry(day, "Found an unlooted store but decided not to risk it")

    return [game, zombies_killed]