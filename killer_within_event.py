from functions import *

def killer_within_event(area, zombies_killed, character, day, bag_items):
    game = True

    print("You're walking towards", area, "when you pass by a large government building")
    print("Taking a closer look, you see a group of 4 survivors standing outside")
    print("Will you:\n1. Approach them\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("Curiosity gets the better of you, and you decide to see what's going on")
        print("You walk up to them, and surprisingly they turn towards you and smile")
        print("They're about to loot this building and could use an extra pair of hands")
        print("Will you:\n1. Agree to help\n2. Ask what they're looking for\n3. Head home")
        choice = make_choice()

        if choice != 3:
            plan_accepted = True

            taken_names = []
            event_friend_list = []
            event_survivor_list = []

            friend1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
            taken_names.append(friend1)
            event_friend_list.append(friend1)

            friend2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

            while friend2 in taken_names:
                friend2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
            taken_names.append(friend2)
            event_friend_list.append(friend2)

            survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

            while survivor1 in taken_names:
                survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
            taken_names.append(survivor1)
            event_survivor_list.append(survivor1)

            survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

            while survivor2 in taken_names:
                survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
            taken_names.append(survivor2)
            event_survivor_list.append(survivor2)

            zombie_liar = None
            not_zombie_liar = None

            if choice == 1:
                print("You agree to lend a hand and the group introduce themselves")
                print("Their names are " + friend1 + ", " + friend2 + ", " + survivor1 + " and " + survivor2)
                print(friend1, "and", friend2, "were friends before the apocalypse, but they met", survivor1, "and", survivor2, "after everything happened")
                print("You introduce yourself, and the group head inside")
                print("\nThe interior seems abandoned, and", friend2, "turns to you and explains the plan")
                print("They're here to look for guns, as this building used to have an armed security detail")
                print("They think some of the weapons and ammo could still be here somewhere")

            elif choice == 2:
                print("You ask them what they're looking for and they let you in on the plan")
                print("They're here to look for guns, as this building used to have an armed security detail")
                print("They think some of the weapons and ammo could still be here somewhere")
                print("Will you:\n1. Agree to help\n2. Head home")
                choice = make_choice()

                if choice == 1:
                    print("You agree to lend a hand and the group take the opportunity to introduce themselves")
                    print("Their names are " + friend1 + ", " + friend2 + ", " + survivor1 + " and " + survivor2)
                    print(friend1, "and", friend2, "were friends before the apocalypse, but they met", survivor1, "and", survivor2, "after everything happened")
                    print("You introduce yourself, and the group heads inside")
                    print("As you walk into the interior, you notice nothing out of the ordinary")
                    print("The place seems to be abandoned")

                else:
                    plan_accepted = False
                    print("They're surprised you aren't interested, but let you walk away")
                    print("You weren't going to risk walking into a huge building full of zombies just for the chance at a gun")
                    print("Heading back home, you wonder if the group had any luck...")

            if plan_accepted:
                print("\nNobody has a map, and instead the five of you find yourselves in the conference room")
                print("The building is huge, and you'll need to split up to search it properly")
                print(friend1, "suggests you all meet up in this room after 20 minutes of looking around")

                blackjack_player = taken_names[random.randint(0, len(taken_names) - 1)]

                print("\nBefore you go,", blackjack_player, "challenges you to a friendly game of blackjack")
                print("Will you:\n1. Play a game\n2. Stay focused on the search")
                choice = make_choice()

                if choice == 1:
                    result = play_blackjack(blackjack_player)

                    if result == True:
                        print("YOU WIN\n")
                        print(blackjack_player, "packs the cards up and shakes your hand congratulating you")

                    elif result == "Draw":
                        print("DRAW\n")
                        print(blackjack_player, "shrugs and packs up the cards, now it's time to have a look around")

                    else:
                        print(blackjack_player.upper() + " WINS\n")
                        print("He grins and packs up the cards, now it's time to take a look around")
                
                else:
                    print("You'd rather start searching for the weapons, but you might play a game later instead")

                print()
                print(friend1, "heads off with", friend2, "and the rest of you split up to search")

                killer_chance = random.randint(1, 7)
                if killer_chance == 1:
                    killer = "zombie"

                else:
                    killer = taken_names[random.randint(0, len(taken_names) - 1)]

                dead_survivors = []
                friend_split = False

                search_locations = ["north", "east", "south", "west"]
                search_floor = ["ground", "2nd", "3rd"]

                your_side = search_locations[random.randint(0, len(search_locations) - 1)]
                your_floor = search_floor[random.randint(0, len(search_floor) - 1)]

                your_location = your_side + " side of the building on the " + your_floor + " floor"

                print("\nYou'll be searching the", your_location)
                print("Once you're there, you start checking around for a security's office or an armory")
                print("Going door to door, you check through the dreary offices, full of desks and cubicles")

                input("\nPress 1 to continue: ")
                print(line_break)

                zom_chance = random.randint(1, 2)

                if zom_chance == 1:
                    print("But you're not alone!\n")
                    zom_num = random.randint(2, 3)
                    print("A door in front of you bursts open and out come", zom_num, "zombies")

                    result = fight(zom_num, "zombies")

                    if result:
                        zombies_killed += zom_num
                        print("The zombies lie dead and you check your watch")
                        print("Looks like your 20 minutes are up, it's time to head back")
                        zombies_found = True
                        input("\nPress 1 to continue: ")
                        print(line_break)

                    else:
                        game = False

                else:
                    zombies_found = False
                    print("After the 20 minutes have passed you've found nothing, and it's time to head back")
                    input("\nPress 1 to continue: ")
                    print(line_break)

                if game:
                    missing_friends = False
                    missing_survivors = False
                    missing_survivor = False
                    chance = random.randint(1, 3)

                    if chance == 1:
                        missing_friends = True  
                    
                    print("But when you arrive back at the conference room, not everyone is here")

                    if missing_friends:
                        print(friend1, "and", friend2, "haven't come back yet, it's just you and the two survivors", survivor1, "and", survivor2)
                        print(survivor1, "says the group should try and find them, and regroup in 15 minutes")

                        if killer != friend1:
                            if killer!= friend2:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    dead_friend = friend1
                                    friend1 = friend2
                        
                                else:
                                    dead_friend = friend2

                            else:
                                dead_friend = friend1
                                friend1 = friend2

                        else:
                            dead_friend = friend2

                        dead_survivors.append(dead_friend)
                        taken_names.remove(dead_friend)

                        print("\nBut before anyone can say anything,", friend1, "runs into the room")
                        print("He's sweating and panting heavily, and he says he was with", dead_friend, "but they were chased by zombies")

                        if killer != "zombie":
                            if zombies_found:
                                chance = random.randint(1, 4)

                                if chance == 1:
                                    killer = friend1

                            else:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    killer = friend1

                        print("But the two survivors say they haven't seen any zombies")

                        if zombies_found:
                            print("But you have seen some zombies here")
                            print("Will you:\n1. Tell the group\n2. Keep that to yourself")
                            choice = make_choice()

                            if choice == 1:
                                print("You tell the group that you had to fight off some zombies, and the two survivors relax")
                                print("They feel safer knowing", friend1, "might be telling the truth")
                                friend_split = True
                                not_zombie_liar = friend1
                            
                            else:
                                print("You decide not to tell the group, and now the two survivors aren't so sure about", friend1)

                        else:
                            print("You also haven't seen any zombies, and", friend1, "may not be telling the truth about what happened to", dead_friend)
                        
                            zombie_liar = friend1

                    else:
                        chance = random.randint(1, 2)

                        if chance == 1:
                            missing_survivor = True

                            dead_survivor = event_survivor_list[random.randint(0, len(event_survivor_list) - 1)]

                            while dead_survivor == killer:
                                dead_survivor = event_survivor_list[random.randint(0, len(event_survivor_list) - 1)]
                                
                            dead_survivors.append(dead_survivor)
                            taken_names.remove(dead_survivor)

                            print(dead_survivor, "hasn't come back yet, it's just you and the 3 others")
                            print(friend2, "says the group should try and find him, and regroup in 15 minutes")
                            print("You all agree, and head back out to search")
                            friend_split = False

                        else:
                            missing_survivors = True
                            print("Both of the survivors haven't come back yet, it's just you and the two friends,", friend1, "and", friend2)

                            if killer != survivor1:
                                if killer!= survivor2:
                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        dead_survivor = survivor1
                                        survivor1 = survivor2
                            
                                    else:
                                        dead_survivor = survivor2

                                else:
                                    dead_survivor = survivor1
                                    survivor1 = survivor2

                            else:
                                dead_survivor = survivor2
                            
                            dead_survivors.append(dead_survivor)
                            taken_names.remove(dead_survivor)

                            print(friend1, "says the group should try and find them, then regroup in 15 minutes")
                            print("\nBut before anyone can say anything,", survivor1, "runs into the room")
                            print("He's sweating and panting heavily, and he says he was with", dead_survivor, "but they were chased by zombies")

                            if killer != "zombie":
                                if zombies_found:
                                    chance = random.randint(1, 4)

                                    if chance == 1:
                                        killer = survivor1

                                else:
                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        killer = survivor1

                            print("But the two friends say they haven't seen any zombies")

                            if zombies_found:
                                print("But you have seen some zombies here")
                                print("Will you:\n1. Tell the group\n2. Keep that to yourself")
                                choice = make_choice()

                                if choice == 1:
                                    print("You tell the group that you had to fight some zombies, and the two friends relax")
                                    print("They feel safer knowing", survivor1, "might be telling the truth")
                                    friend_split = True

                                    not_zombie_liar = survivor1
                                
                                else:
                                    print("You decide not to tell the group, and now the two friends are now wary of", survivor1)
                                    print("They'll be sticking together this time")
                                    friend_split = False

                            else:
                                print("You also haven't seen any zombies, and", survivor1, "may not be telling the truth about what happened to", dead_survivor)
                                friend_split = False

                                zombie_liar = survivor1

                    print("\nThe four of you head back out to look for him")

                    if not friend_split:
                        if not missing_friends:
                            print("But the two friends aren't going to be splitting up")

                    else:
                        if not missing_friends:
                            print("Looks like the two friends are splitting up")
                    
                    input("\nPress 1 to continue: ")
                    print(line_break)

                    body_chance = random.randint(1, 2)
                    print("You're walking through the dull grey halls again, but this time you aren't looking for guns\n")
                    stick_together = False
                    event_group = []

                    if body_chance == 1:
                        body_found = True

                        if killer == "zombie":
                            print("You turn a corner and up ahead you spot someone crouched over a body")
                            print("It's a zombie!")

                            result = fight(1, "zombies")

                            if result:
                                print("With the zombie dead, you check the corpse and sure enough it's", dead_survivors[0])
                                print("After making sure he stays dead you head back to tell the others")
                                print("The 15 minutes are up, and you'll find them in the conference room\n")

                            else:
                                game = False

                        else:
                            print("Turning a corner, you spot a body in a pool of blood")
                            print("It's", dead_survivors[0], "and his throat has been slit!")

                            print("Your eyes widen and your blood goes cold")
                            print("Someone in your group killed him")

                            print("\nYou spin around as someone runs up the hallway behind you")

                            if not missing_friends:
                                if not friend_split:
                                    print("It's", friend1, "and he appears to be in a state of panic")
                                    print("This gets even worse when he looks over your should and sees the body")
                                    print("\nHe looks at you in shock and goes to defend himself")
                                    print("But there's no blood on your hands, and you wouldn't have had time to wash it off")
                                    print("He realises this and tells you he's lost his friend, and now he believes", survivor1, "might have killed him")
                                    print("\nBefore you can stop him, he runs off to search for his friend")
                                    
                                elif friend_split:
                                    print("It's", friend2, "and he stops in his tracks when he sees the body")
                                    print("But you quickly explain to him that you wouldn't have had time to wash away the blood")
                                    print("He thinks for a second then believes your innocence")
                                    print("But now he believes his friend", friend1, "is in trouble")
                                    print("\nBefore you can stop him, he runs off to search for his friend")

                            else:
                                if missing_survivor:
                                    survivor = taken_names[random.randint(0, len(taken_names) - 1)]

                                    print("It's", survivor, "and he stops in his tracks when he sees the body")
                                    print("But you quickly explain to him that you wouldn't have had time to wash away the blood")

                                    chance = random.randint(1, 2)

                                    if killer == survivor or chance == 1:
                                        print("He thinks for a second then believes your innocence")

                                        print("He promises you he had no part in this murder, so it must be one of the others")
                                        print("He suggests you stick together since you're both innocent")
                                        print("Will you:\n1. Agree to stick together\n2. Tell him you don't trust him")     
                                        choice = make_choice()

                                        if choice == 1:
                                            stick_together = True
                                            event_group.append(survivor1)     
                                            print("You choose to trust", survivor1, "and you both head off in search of the others")

                                        else:
                                            stick_together = False
                                            print("You don't trust him and he sighs before heading off down a different hallway")

                                    else:
                                        print("He doesn't trust you, and it doesn't look like you have any alibi")
                                        print("Taking one more look at the body, he runs of down the hallway")

                                elif missing_survivors or missing_friends:
                                    if missing_friends:
                                        survivor1 = friend1

                                    print("It's", survivor1, "and he stops in his tracks when he sees you")
                                    print("Looking over your shoulder, his eyes go wide when he sees the body")
                                    print("You quickly explain the situation, and show him there's no blood on your hands")

                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("It seems like he believes you, for now\n")

                                        if zombies_found and friend_split:
                                            print("He thanks you for backing him up earlier")
                                            print("He plans to get to the bottom of this, and offers to help you search")
                                            print("Will you:\n1. Agree to stick together\n2. Tell him you don't trust him")     
                                            choice = make_choice()

                                            if choice == 1:
                                                stick_together = True
                                                event_group.append(survivor1)     
                                                print("You choose to trust", survivor1, "and the two of you head off in search of the others")

                                            else:
                                                stick_together = False
                                                print("You don't trust him and he sighs before heading off down a different hallway")

                                        else:
                                            print("But this wasn't the work of the zombies he was talking about")
                                            print("Will you:\n1. Mention this to him\n2. Let it go")
                                            choice = make_choice()

                                            if choice == 1:
                                                print("You mention this to him and his eyes darken")
                                                if missing_survivors:
                                                    print("He asks if you're trying to accuse him of killing another survivor")
                                                else:
                                                    print("He asks if you're trying to accuse him of killing his friend")
                                                print("Will you:\n1. Accuse him\n2. Apologise")
                                                choice = make_choice()

                                                if choice == 1:
                                                    chance = random.randint(1, 2)
                                                    if (survivor1 == killer and chance == 1) or (killer in event_friend_list and chance == 2):
                                                        if friend1 == friend2:
                                                            friend1 = dead_survivors[0]

                                                        print("He shakes his head and says he has different suspicions")
                                                        if missing_survivors:
                                                            print("He thinks that either", friend1, "or", friend2, "killed the other survivor")

                                                        else:
                                                            print("He thinks that either", survivor1, "or", survivor2, "killed his friend")
                                                        if missing_survivors:
                                                            print("While running from the zombies,", dead_survivors[0], "ran towards where the two friends were looking")
                                                        
                                                        else:
                                                            print("While running from the zombies,", dead_survivors[0], "ran towards where the two survivors were looking")
                                                        print("\nHe thinks either one or both of them are responsible")
                                                        print("Taking another look at you, he runs off to try get to the bottom of this")

                                                    else:
                                                        print("He reminds you that neither of you were with the two friends when this happened")
                                                        print("With that in mind, it could be anyone")
                                                        print("Warning you not to throw around false info, he heads off down a hallway")

                                                else:
                                                    print("You apologise and he waves it away")
                                                    print("He says just stressed as he's already been chased by zombies and now someone's been murdered")
                                                    print("He plans to get to the bottom of this, and offers to help you search")
                                                    print("Will you:\n1. Agree to stick together\n2. Tell him you don't trust him")     
                                                    choice = make_choice()

                                                    if choice == 1:
                                                        stick_together = True
                                                        event_group.append(survivor1)     
                                                        print("You choose to trust", survivor1, "and the two of you head off in search of the others")

                                                    else:
                                                        print("You don't trust him and he sighs before heading off down a different hallway")

                                            else:
                                                print("You choose not to say anything, and he seems to breathe a sigh of relief")
                                                print("He tells you he's going to keep searching, and runs off down the hallway") 

                                    else:
                                        print("But he says he doesn't quite believe you, and backs away before running off")
                                        stick_together = False

                    else:
                        body_found = False
                        print("You haven't found anything yet, until you hear someone running up the hallway behind you")

                        if killer == "zombie":
                            if not missing_friends:
                                print("It's", friend1, "followed closely by", friend2)
                                print("They tell you that", dead_survivors[0], "was killed by a zombie, and it's time to regroup")

                            elif missing_friends:
                                print("It's", friend1, "followed closely by", survivor1)
                                print(friend1, "is somber, and he tells you his friend was killed by zombies")
                                print("They're on their way to regroup with", survivor2, "before they leave this place behind")

                            print("When you've all arrived at the conference room, the group decide what to do next\n")

                            if dead_survivor in event_friend_list:
                                print(friend1, "is mourning the loss of his friend and tells the others he'll be heading back to their camp")
                                taken_names.remove(friend1)

                                survivor = taken_names[random.randint(0, len(taken_names) -1)]
                                survivor2 = taken_names[random.randint(0, len(taken_names) -1)]

                                print("But before you leave,", survivor, "and", survivor2, "ask if you want to quickly check for any loot")

                            else: 
                                survivor = taken_names[random.randint(0, len(taken_names) -1)]
                                chance = random.randint(1, 2)
                                

                                if chance == 1:
                                    print(survivor, "says he's heading back to their camp, but the other stay to look around with you")
                                    taken_names.remove(survivor)

                                else:
                                    survivor2 = taken_names[random.randint(0, len(taken_names) -1)]
                                    taken_names.remove(survivor2)
                                    survivor3 = taken_names[random.randint(0, len(taken_names) -1)]
                                    print(survivor, "and", survivor2, "say they're heading back to camp, but", survivor3, "stays back to loot with you")

                                    taken_names = [survivor3]

                            input("\nPress 1 to continue: ")
                            print(line_break)
                            food_search(len(taken_names) + 1, taken_names, dead_survivors[0])

                        else:
                            if not missing_friends:
                                if not friend_split:
                                    if friend1 == killer:
                                        dead_survivor2 = friend2
                        
                                    else:
                                        if killer != friend2:
                                            dead_survivor2 = friend2

                                        else:
                                            dead_survivor2 = taken_names[random.randint(0, len(taken_names) - 1)]

                                    print("It's", friend1, "and he looks scared\n")
                                    print("Himself and", friend2, "were searching when they found the body of", dead_survivors[0])
                                    print("A zombie didn't kill him, his throat was slit")
                                    if missing_survivors:
                                        print("He tells you not to trust", survivor1)
                                        if not zombies_found:
                                            print("He thinks", survivor1, "was lying about the zombies")
                                    print("\nHe then tells you he's lost his friend, and he believes he's in danger too")
                                    print("But he doesn't trust you either and runs off down the hallway")

                                elif friend_split:
                                    print("It's", friend2, "and he appears to be in a state of panic")
                                    print("\nHe found " + dead_survivors[0] + "'s" + " body, but his throat was slit!")
                                    print("That means someone in the group killed him")
                                    print("Now he believes his friend", friend1, "is in trouble")
                                    if missing_survivors:
                                        print("He tells you not to trust", survivor1)
                                        if not zombies_found:
                                            print("He thinks", survivor1, "was lying about the zombies")
                                    print("\nBefore you can stop him, he runs off to search for his friend")

                                    if friend2 == killer:
                                        dead_survivor2 = survivor1
                        
                                    else:
                                        if killer != survivor1:
                                            dead_survivor2 = friend2

                                        else:
                                            dead_survivor2 = friend2

                            else:
                                if missing_survivor:
                                    survivor = taken_names[random.randint(0, len(taken_names) - 1)]

                                    print("It's", survivor, "and he stops in his tracks when he sees you")
                                    print("He tells you he found "  + dead_survivors[0] + "'s" + " body, but he wasn't killed by a zombie")
                                    print("His throat was slit!")
                                    print("That means someone in the group killed him")

                                    print("\nHe says he was keeping an eye on you, so it must be one of the others")
                                    print("He suggests you stick together since you're both innocent")
                                    print("Will you:\n1. Agree to stick together\n2. Tell him you don't trust him")     
                                    choice = make_choice()

                                    if choice == 1:
                                        stick_together = True
                                        event_group.append(survivor1)     
                                        print("You choose to trust", survivor1, "and the two of you head off in search of the others")

                                    else:
                                        stick_together = False
                                        print("You don't trust him and he sighs before heading off down a different hallway")

                                elif missing_survivors or missing_friends:
                                    if missing_friends:
                                        survivor1 = friend1

                                    print("It's", survivor1, "and he stops in his tracks when he sees you")
                                    if zombies_found and not friend_split:
                                        print("He was telling the truth about the zombies earlier")
                                        print("But he doesn't know that you ran into some zombies too")
                                        print("\nHe's stressed out and has no reason to trust you, running off before you can say anything")

                                    elif zombies_found and friend_split:
                                        print("He thanks you for backing him up earlier")
                                        print("He plans to get to the bottom of this, and offers to help you search")
                                        print("Will you:\n1. Agree to stick together\n2. Tell him you don't trust him")     
                                        choice = make_choice()

                                        if choice == 1:
                                            stick_together = True
                                            event_group.append(survivor1)     
                                            print("You choose to trust", survivor1, "and the two of you head off in search of the others")

                                        else:
                                            stick_together = False
                                            print("You don't trust him and he sighs before heading off down a different hallway")

                                    else:
                                        print("But so far you haven't seen any of the zombies he was talking about")
                                        print("Will you:\n1. Mention this to him\n2. Let it go")
                                        choice = make_choice()

                                        if choice == 1:
                                            print("You mention this to him and his eyes darken")
                                            if missing_survivors:
                                                print("He asks if you're trying to accuse him of doing something to the other survivor")
                                            else:
                                                print("He asks if you're trying to accuse him of doing something to his friend")
                                            print("Will you:\n1. Accuse him\n2. Apologise")
                                            choice = make_choice()

                                            if choice == 1:
                                                chance = random.randint(1, 2)
                                                if (survivor1 == killer and chance == 1) or (killer in event_friend_list and chance == 2):
                                                    print("He shakes his head and says he has different suspicions")
                                                    if missing_survivors:
                                                        print("He thinks that either", friend1, "or", friend2, "killed the other survivor")

                                                    else:
                                                        print("He thinks that either", survivor1, "or", survivor2, "killed his friend")
                                                    if missing_survivors:
                                                        print("While running from the zombies, the other survivor ran towards where the two friends were looking")
                                                    
                                                    else:
                                                        print("While running from the zombies, his friend ran towards where the two survivors were looking")

                                                    print("He thinks either one or both of them are responsible")
                                                    print("Taking another look at you, he runs off to try get to the bottom of this")

                                                else:
                                                    print("He reminds you that nobody knows what happened to him yet")
                                                    print("Warning you not to throw around false info, he heads off down a hallway")

                                            else:
                                                print("You apologise and he waves it away")
                                                if missing_survivors:
                                                    print("He says just stressed as he's already been chased by zombies and now the two friends think he's lying")
                                                
                                                else:
                                                    print("He says just stressed as he's already been chased by zombies and now the two survivors think he's lying")
                                                print("He plans to get to the bottom of this, and offers to help you search")
                                                print("Will you:\n1. Agree to stick together\n2. Tell him you don't trust him")     
                                                choice = make_choice()

                                                if choice == 1:
                                                    stick_together = True
                                                    event_group.append(survivor1)     
                                                    print("You choose to trust", survivor1, "and the two of you head off in search of the others")

                                                else:
                                                    stick_together = False
                                                    print("You don't trust him and he sighs before heading off down a different hallway")

                                        else:
                                            print("You choose not to say anything, and he seems to breathe a sigh of relief")
                                            print("He tells you he's going to keep searching, and runs off down the hallway")

                    if len(dead_survivors) == 1 and killer != "zombie":
                        dead_survivor2 = taken_names[random.randint(0, len(taken_names) - 1)]

                        while dead_survivor2 in dead_survivors or dead_survivor2 == killer:
                            dead_survivor2 = taken_names[random.randint(0, len(taken_names) - 1)]

                        dead_survivors.append(dead_survivor2)
                        taken_names.remove(dead_survivor2)

                    if stick_together:
                        if (missing_survivors or missing_friends) and body_found == False:
                            print("The two of you are walking down one of the many hallways when you come across the bodies of " + dead_survivors[0] + " and " + dead_survivors[1] + "!")

                        else:
                            print("The two of you are walking down one of the many hallways when you come across the body of " + dead_survivors[1] + "!")
                        survivor = event_group[0]
                        taken_names.remove(survivor)
                        print(survivor, "looks at you with a grim expression\n")
                        if (missing_survivors or missing_friends) and body_found == False:
                            print("The two of you check the bodies, and both their throats have been slit...")
                            print("It looks like", dead_survivors[1], "was killed when he found the body of", dead_survivors[0])

                        else:
                            print("The two of you check the body, and his throat has been slit...")
                        survivor2 = taken_names[0]

                        print(survivor, "says it was clearly", survivor2, "who did this")
                        print("\nBut you're not so sure if you can trust him")
                        if (survivor in event_survivor_list and missing_survivors) or (survivor in event_friend_list and missing_friends):
                            print("After all, he was with", dead_survivors[0], "when he went missing")

                            if zombie_liar == survivor:
                                print("You also haven't seen any zombies to back up his story...")
                        
                        print("Will you:\n1. Stick with", survivor, "\n2. Try and find", survivor2)
                        choice = make_choice()

                        if choice == 1:
                            print("Not wanting to risk being on your own in here, you decide to stick with", survivor)
                            print("You hope the killer really is", survivor2, "and head off to search for him")
                            print("\nThe two of you are searching around on the ground floor when", survivor, "says he's heard something ahead")
                            print("You didn't hear anything, but he seems pretty sure about it")
                            print("He asks if you want to check it out")
                            print("Will you:\n1. Stay here\n2. See what the noise was")
                            choice = make_choice()

                            if choice == 1:
                                print("You decide to stay here instead, and", survivor, "says he's going to check it out")
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("He walks off to check but a few minutes later,", survivor2, "turns the corner")
                                    chance = random.randint(1, 3)

                                    if chance == 1 or survivor2 == killer:
                                        print("He relaxes, glad to see you")
                                        print("\nYou look at him confused, but he explains he's been running from", survivor)
                                        print("He sees the shock on your face and explains that", survivor, "was chasing him and", dead_survivors[1], "when he managed to get away")
                                        print("You tell him that", dead_survivors[1], "is dead and his face drops, he looks devastated\n")

                                        if survivor2 in event_friend_list and dead_survivors[1] in event_friend_list:
                                            print("You understand how he must feel, they were good friends")

                                        else:
                                            print("You're not sure why he's so sad if he's only known him since the apocalypse started")
                                            print("But you have no idea how the two of them got on")

                                            if survivor2 != killer:
                                                chance = random.randint(1, 3)

                                                if chance == 1:
                                                    killer = survivor2

                                        print("He looks away and recovers himself before asking if you want to team up")
                                        print("Will you:\n1. Team up with " + survivor2 + "\n2. Try and find " + survivor + " instead")
                                        choice = make_choice()

                                        if choice == 1:
                                            print("You trust", survivor2, "more than you trust", survivor, "and the two of you decide to work together")
                                            print("Now that you're a team, you'll have to figure out what to do")

                                            result = tunnel_exit(survivor, survivor2, killer, not_zombie_liar)

                                            if not result:
                                                game = False
                                        
                                        else:
                                            print("You don't trust him, and decide to look for", survivor, "instead")
                                            print("He protests but seeing you've made your mind up, he tells you you're making a mistake and leaves")
                                            print("Taking care not to make too much noise, you begin your search of the old building\n")

                                            if zombie_liar != None:
                                                print("Suddenly, you hear something moving in a nearby room and as you sneak closer it gets louder")
                                                zom_num = 2
                                                print("\nWithout warning", zom_num, "zombies crash through the thin office wall to your left!")
                                                result = fight(zom_num, "zombies")

                                                if result:
                                                    zombies_killed += zom_num
                                                    print("Looks like", zombie_liar, "was right about the zombies after all...")

                                                else:
                                                    game = False

                                            else:
                                                print("The building is completely quiet and you check through office after office, finding nothing")

                                            print("\nYour gut tells you to look down the hallway, and you see a man's shadow on the wall")
                                            print("It looks like someone is creeping towards you!")
                                            print("You duck into cover behind a dusty vending machine and wait\n")

                                            input("Press 1 to continue: ")
                                            print(line_break)

                                            chance = random.randint(1, 2)
                                            survivor1 = survivor

                                            if chance == 1:
                                                survivor = survivor
                                                survivor2 = survivor2

                                            else:
                                                survivor = survivor2
                                                survivor2 = survivor

                                            print("It's " + survivor + "!")
                                            print("He must have come looking for you")
                                            print("Will you:\n1. Confront him\n2. Hide")
                                            choice = make_choice()

                                            if choice == 1:
                                                print("Choosing to confront him, you step out in front of him")
                                                chance = random.randint(1, 2)

                                                if survivor == killer and chance == 1:
                                                    print("But he doesn't panic, instead he flashes an evil grin")
                                                    print("He was the killer all along!")
                                                    print("You shout out " + survivor2 + "'s name, but " + killer + " tells you he's already dead\n")

                                                    result = fight(1, "humans", killer)

                                                    if result:
                                                        print(killer, "lies dead, but everyone else has shared his fate...")

                                                        print("\nThe old building is quiet now, and you decide to take another look around before you go")
                                                        weapon_search(killer)

                                                    else:
                                                        game = False

                                                else:   
                                                    if survivor == survivor1:
                                                        print(survivor, "jumps back, then looks at you with suspicion")
                                                        print("He asks you where you disappeared to earlier, and you tell him about your encounter with", survivor2)
                                                        print("His eyes narrow and he tells you he saw him along the way")
                                                        print(survivor, "thinks", survivor2, "must be the killer")

                                                    else:
                                                        print(survivor, "jumps back but relaxes when he sees it's you")
                                                        print(survivor, "insists he isn't following you, instead he thinks he's being followed by", survivor2)
                                                        print("He's glad to see you and you seem to have earned his trust")

                                                    print("\nBut now he wants to escape and you're not sure why he didn't just leave earlier")
                                                    print("Will you:\n1. Agree but ask him why he didn't leave already\n2. Find your own way out")
                                                    choice = make_choice()

                                                    if choice == 1:
                                                        result = window_exit(survivor, survivor2, killer)

                                                        if not result:
                                                            game = False

                                                    else:
                                                        print("Something about this doesn't add up, and you decide to escape by yourself instead")
                                                        print("Without warning you sprint off down a hallway and up a flight of stairs, losing him...\n")

                                                        result = result = fire_escape_exit(survivor, survivor2, killer, bag_items)

                                                        if result == 0:
                                                            result = -1

                                                        if not result:
                                                            game = False

                                                        else:
                                                            if result > 0:
                                                                zombies_killed += result

                                            else:
                                                print("You choose to remain hidden in the shadows and watch")

                                                chance = random.randint(1, 2)

                                                if chance == 1:
                                                    print("You're focused on", survivor, "and turn around just in time to see", survivor2, "coming up the other end of the hallway!")
                                                    print("With no other choice you jump out of hiding and stand between the two of them")
                                                    print("One of them has to be the killer")

                                                    print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
                                                    choice = make_choice()

                                                    if choice == 1:
                                                        ally = survivor
                                                        enemy = survivor2

                                                    elif choice == 2:
                                                        ally = survivor2
                                                        enemy = survivor

                                                    result = fight_killer(enemy, ally, killer)

                                                    if result:
                                                        weapon_search(killer)

                                                    else:
                                                        game = False

                                                elif chance == 2:
                                                    print("He hasn't seen you yet, but keeps searching")
                                                    print("Maybe he's searching for you to team up, or perhaps to kill you...\n")

                                                    if survivor == killer:
                                                        print("Suddenly he ducks down out of sight, and", survivor2, "emerges from an adjacent room")
                                                        print("You don't make a sound as", survivor2, "creeps through, only for", survivor, "to grab him and slit his throat!")
                                                        print("He drops the body to the floor and looks up, and directly at you!")

                                                    else:
                                                        print("He ducks into a dark room, then shouts and falls silent")
                                                        print("A moment passes then", survivor2, "walks out, covered in blood")
                                                        print("Horrified, you can only watch as he begins to walk towards your hiding spot...")
                                                    
                                                    print("\nYou have no choice you'll have to fight him!")

                                                    result = fight(1, "humans", killer)

                                                    if result:
                                                        print(killer, "lies dead, on his body you find the key for the front door")

                                                        print("\nBut the old building is quiet now, and you decide to take another look around before you go")
                                                        weapon_search(killer)

                                                    else:
                                                        game = False

                                    else:
                                        print("His eyes go wide when he sees you and he runs off")
                                        print("He must have thought you were the killer!")
                                        print("\nBut if you're both not the killer, then that leaves only", survivor)
                                        print("However,", survivor2, "could just be acting to get you to lose trust in", survivor)
                                        print("By splitting you up it'd be easier to kill both of you...")
                                        print("\nYou're trying to figure out what to do when", survivor, "emerges again")
                                        print("He says it was nothing and he must have been hearing things")
                                        print("Will you:\n1. Tell him you saw", survivor2, "\n2. Split up and look for", survivor2)
                                        choice = make_choice()

                                        if choice == 1:
                                            print("His face drops, and he thanks you for telling him")
                                            print("Since you're both together he says you should confront", survivor2)
                                            print("You agree, and the two of you run down the hallway he fled down")
                                            print("\nYou run past a dusty office, and he's waiting inside!")
                                            print("He tells you you're making a mistake and that", survivor, "is the killer")
                                            print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
                                            choice = make_choice()

                                            if choice == 1:
                                                ally = survivor
                                                enemy = survivor2

                                            elif choice == 2:
                                                ally = survivor2
                                                enemy = survivor

                                            result = fight_killer(enemy, ally, killer)

                                            if result:
                                                weapon_search(killer)

                                            else:
                                                game = False

                                        else:
                                            print("You no longer trust", survivor, "and he asks you what's changed")
                                            print("You're not going to tell him about", survivor2, "and instead you run off")
                                            print("He shouts after you desperately and tries to chase you, but you're too fast and he can't keep up")

                                            chance = random.randint(1, 2)

                                            if chance == 1:
                                                print("After around 15 minutes of searching you turn a corner and see", survivor2, "right in front of you")
                                                print("This time he doesn't run away, and he looks at you with suspicion")
                                                print("You explain to him that you believe what he said, and that you think", survivor, "is the killer")
                                                print("He asks if he can trust you and you show him your hands are clean, you haven't killed", survivor)

                                                print("\nHe thinks for a second before deciding to trust you")
                                                print(survivor2, "wants to escape but you're not sure why he didn't just leave earlier")
                                                print("Will you:\n1. Agree but ask him why he didn't leave already\n2. Find your own way out")
                                                choice = make_choice()

                                                if choice == 1:
                                                    result = window_exit(survivor, survivor2, killer)

                                                    if not result:
                                                        game = False

                                                else:
                                                    print("He hesitates, then nods and agrees")
                                                    print("You lead him back to where you last saw", survivor, "and start looking around\n")
                                                    print("The two of you are checking rooms when you hear a shout")
                                                    print("It's " + survivor2 + "'s" + " voice and you run into the room it came from")
                                                    print("Inside are", survivor2, "and", survivor, "facing off")
                                                    print("One of them has to be the killer")

                                                    chance = random.randint(1, 3)

                                                    if chance == 1:
                                                        killer = survivor

                                                    print("Will you:\n1. Side with " + survivor2 + "\n2. Side with " + survivor)
                                                    choice = make_choice()

                                                    if choice == 1:
                                                        ally = survivor2
                                                        enemy = survivor

                                                    elif choice == 2:
                                                        ally = survivor
                                                        enemy = survivor2

                                                    result = fight_killer(enemy, ally, killer)

                                                    if result:
                                                        weapon_search(killer)

                                                    else:
                                                        game = False

                                else:
                                    print("You decide to stay and after waiting for a few minutes, he's still not back")
                                    print("Will you:\n1. Continue to wait\n2. Make a run for it")
                                    escape = False
                                    killer_unknown = False
                                    choice = make_choice()

                                    if choice == 1:
                                        chance = random.randint(1, 3)

                                        if chance == 1 or survivor == killer:
                                            print("You choose to wait even longer, and he finally returns")
                                            print("He apologises for taking so long, it's dark back there and he got lost")
                                            print(survivor, "thinks it's too dangerous to stay here, you won't be able to see anything after dark")
                                            print("You agree and go to search for an exit")
                                            print("\nThe main door is locked, but he says he found the key earlier")

                                            if survivor == killer:
                                                print("He tosses it over to you, and you turn to open the door")
                                                input("\nPress 1 to continue: ")
                                                print("But as you turn your back to him, he grabs you and slices your throat with his knife...\nYOU DIED")
                                                game = False
                                            
                                            else:
                                                print("There's no sign of", killer, "and he steps past you to unlock the door")
                                                print("With the door open, you check to make sure the street is clear")
                                                print("There's nobody around and", survivor, "pats you on the shoulder and thanks you, before running off")
                                                print("As you run off in the opposite direction, you feel as if someone is watching you...")
                                                print("\nJust in case, you take a detour on your way home and you arrive before nightfall")

                                        else:
                                            print("You wait even longer but he still hasn't returned")
                                            print("Will you:\n1. Try and find him\n2. Try and escape")
                                            choice = make_choice()

                                            if choice == 1:
                                                print("You want to get to the bottom of this, and head towards where he disappeared")
                                                print("It's really dark back here, but you think you see something on the floor")
                                                if survivor == killer:
                                                    print("It's the body of", survivor2, "and it looks like his throat was cut too!")
                                                
                                                else:
                                                    print("It's the body of", survivor, "and it looks like his throat was cut too!")

                                                input("\nPress 1 to continue: ")
                                                print(line_break)

                                                chance = random.randint(1, 3)
                                                
                                                if chance != 1:
                                                    print("\nYou squint your eyes, and see bloody footsteps leading into an adjacent hallway")
                                                    print("It looks like", killer, "circled around to where you were waiting!")
                                                    print("Will you:\n1. Head back and confront him\n2. Make your escape")
                                                    choice = make_choice()

                                                    if choice == 1:
                                                        print("Stepping out of the dark offices,", killer, "is waiting for you")
                                                        print("He's covered in blood and says you're the last one he needs to kill")

                                                        result = fight(1, "humans", killer)

                                                        if result:
                                                            print(killer, "lies dead, on his body you find the key for the front door")

                                                            print("\nThe old building is quiet now, and you decide to take another look around before you go")
                                                            weapon_search(killer)

                                                        else:
                                                            game = False

                                                else:
                                                    print("\nSquinting your eyes, it looks like bloody footprints circle the room")
                                                    print("They seem to lead behind you and before you can react,", killer, "grabs you and slits your throat...\nYOU DIED")

                                            else:
                                                print("If he's innocent then you're leaving him for dead, but you're not risking your own life")
                                                escape = True
                                    
                                    else:
                                        print("If he's innocent then you're leaving him for dead, but you're not risking your own life")
                                        escape = True

                                    if escape:
                                        if zombies_found:
                                            print("You make for where you fought the zombies earlier, and sure enough there's a broken window they must have climbed through")
                                            print("Checking over your shoulder, you pull yourself up and through the window")
                                            chance = random.randint(1, 2)

                                            if chance == 1:
                                                print("But you've misjudged the height of the window, and you land badly on your ankle")
                                                status = add_affliction("sprained ankle", 10)

                                                if not status:
                                                    game = False

                                                print("\nLuckily nobody follows you from the building and you manage to sneak past any zombies on the way home")
                                                journal_entry(day, "Escaped a killer but sprained my ankle in the process")

                                                if killer_unknown:
                                                    print("Guess you'll never know who the killer was...")

                                            else:
                                                print("It's only a short drop and you you're up instantly before you run off")
                                                print("You arrive home with no hassle, and realise how lucky you were to escape")
                                                journal_entry(day, "Somehow escaped a killer unharmed")

                                            killer_return(killer)

                                        else:
                                            chance = random.randint(1, 2)

                                            if chance == 1:
                                                print("You head for the main door, and it's unlocked!")
                                                print("Heading out into an empty street you can't believe your luck and run off")
                                                print("But the killer is still out there, and you make sure to take a detour on your way home...")

                                            else:
                                                print("But the door doesn't budge, someone must have locked it!")
                                                print("You look back and", killer, "is across the foyer, covered in blood!")
                                                print("He flashes an evil grin and starts running towards you")

                                                print("\nThinking quick, you begin to climb towards a window above the door, maybe you can smash it!")
                                                print("Adrenaline pumps through your veins as you climb, hearing him get closer and closer")
                                                chance = random.randint(1, 2)

                                                if chance == 1:
                                                    print("You punch through the glass, but blood sprays from your hand")
                                                    status = add_affliction("laceration on your hand", 30)

                                                    if not status:
                                                        game = False

                                                    chance = random.randint(1, 2)

                                                    if chance == 1 and game:
                                                        print("\nBut somehow you manage to crawl through, and sprint away holding your injured hand")
                                                        print(killer, "pounds against the door but it's no use, he didn't have the key")
                                                        print("\nShocked you managed to survive, you head home as fast as you can...")

                                                        journal_entry(day, "Escaped a killer but injured my hand in the process")

                                                        killer_return(killer)

                                                    else:
                                                        print("Blood covers your fingers and you slip, falling backwards")
                                                        print("When you blink your eyes open he's staring down at you, and the last thing you see is the blade of his machete...\nYOU DIED")
                                                        game = False
                                                
                                                else:
                                                    print("You ball your t-shirt around your hand and punch through the glass")
                                                    print("Without a second to spare you're out the window and on the ground outside")
                                                    print("As you sprint away, you hear", killer, "pound against the door")
                                                    print("\nShocked you got away in one piece, you head home as fast as you can...")

                                                    journal_entry(day, "Managed to escape a killer, but it was close")

                                                    killer_return(killer)
                        else:
                            print("Deciding not to trust him, you head off on your own")
                            print("He protests but seeing you've made your mind up, he shrugs and walks off down a different hallway")
                            print("\nIt seems you'll have to try looking for", survivor2, "instead")
                            print("Despite " + survivor1 + "'s" + " warning...")
                            print("Taking care not to make too much noise, you begin your search of the old building\n")

                            if zombie_liar != None:
                                print("Suddenly, you hear something moving in a nearby room and as you sneak closer it gets louder")
                                zom_num = 2
                                print("\nWithout warning", zom_num, "zombies crash through the thin office wall to your left!")
                                result = fight(zom_num, "zombies")

                                if result:
                                    zombies_killed += zom_num
                                    print("Looks like", zombie_liar, "was right about the zombies after all...\n")

                                else:
                                    game = False

                            else:
                                print("The building is completely quiet and you check through office after office, finding nothing")

                            print("Your gut tells you to look down the hallway, and you see a man's shadow on the wall")
                            print("It looks like someone is creeping towards you!")
                            print("You duck into cover behind a dusty vending machine and wait\n")

                            chance = random.randint(1, 2)

                            if chance == 1:
                                survivor = survivor1
                                survivor2 = survivor2

                            else:
                                survivor = survivor2
                                survivor2 = survivor1

                            print("It's " + survivor + "!")
                            print("He must have come looking for you")
                            print("Will you:\n1. Confront him\n2. Hide")
                            choice = make_choice()

                            if choice == 1:
                                print("Choosing to confront him, you step out in front of him")

                                chance = random.randint(1, 2)

                                if survivor == killer and chance == 1:
                                    print("But he doesn't panic, instead he flashes an evil grin")
                                    print("He was the killer all along!")
                                    print("You shout out " + survivor2 + "'s name, but " + killer + " tells you he's already dead\n")
                                    print("Looks like you'll be on your own in this fight...")

                                    result = fight(1, "humans", killer)

                                    if result:
                                        print(killer, "lies dead, but everyone else has shared his fate...")

                                        print("\nThe old building is quiet now, and you decide to take another look around before you go")
                                        weapon_search(killer)

                                    else:
                                        game = False

                                else:
                                    print(survivor, "jumps back, then looks at you with suspicion")
                                    print("He asks if he can trust you and you show him your hands are clean, you haven't killed anyone\n")

                                    print("He thinks for a second before deciding to trust you")
                                    print(survivor, "wants to escape but you're not sure why he didn't just leave earlier")
                                    print("Will you:\n1. Agree but ask him why he didn't leave already\n2. Find your own way out")
                                    choice = make_choice()

                                    if choice == 1:
                                        result = window_exit(survivor2, survivor, killer)

                                        if not result:
                                            game = False

                                    else:
                                        print("Something about this doesn't add up, and you decide to escape by yourself instead")
                                        print("Without warning you sprint off down a hallway and up a flight of stairs, losing him...\n")

                                        result = result = fire_escape_exit(survivor, survivor2, killer, bag_items)

                                        if result == 0:
                                            result = -1

                                        if not result:
                                            game = False

                                        else:
                                            if result > 0:
                                                zombies_killed += result
                            else:
                                print("You choose to remain hidden in the shadows and watch")

                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("You're focused on", survivor, "and turn around just in time to see", survivor2, "coming up the other end of the hallway!")
                                    print("With no other choice you jump out of hiding and stand between the two of them")
                                    print("One of them has to be the killer")

                                    print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
                                    choice = make_choice()

                                    if choice == 1:
                                        ally = survivor
                                        enemy = survivor2

                                    elif choice == 2:
                                        ally = survivor2
                                        enemy = survivor

                                    result = fight_killer(enemy, ally, killer)

                                    if result:
                                        weapon_search(killer)

                                elif chance == 2:
                                    print("He hasn't seen you yet, but keeps searching")
                                    print("Maybe he's searching for you to team up, or perhaps to kill you...\n")

                                    if survivor == killer:
                                        print("Suddenly he ducks down out of sight, and", survivor2, "emerges from an adjacent room")
                                        print("You don't make a sound as", survivor2, "creeps through, only for", survivor, "to grab him and slit his throat!")
                                        print("He drops the body too the floor and looks up, and directly at you!")

                                    else:
                                        print("He ducks into a dark room, then shouts and falls silent")
                                        print("A moment passes then", survivor2, "walks out, covered in blood")
                                        print("Horrified, you can only watch as he begins to walk towards your hiding spot...")
                                    
                                    print("\nYou have no choice you'll have to fight him!")

                                    result = fight(1, "humans", killer)

                                    if result:
                                        print(killer, "lies dead, on his body you find the key for the front door")

                                        print("\nThe old building is quiet now, and you decide to take another look around before you go")
                                        weapon_search(killer)

                                    else:
                                        game = False

                    elif killer != "zombie":
                        print("\nYou're alone now, and maybe for the better")
                        print("But if you want to get out of here alive, you'll need to know who the killer is")
                        input("\nPress 1 to continue: ")
                        print(line_break)

                        print("Risking the dangers of the old building, you continue searching")
                        print("All of a sudden, you hear footsteps pounding nearby")
                        print("\nSomeone runs past the end of your hallway and you give chase!")
                        print("You get to the end and look, but there's nobody there")
                        print("\nChecking the other side, you see the body of", dead_survivors[1])

                        if body_found:
                            print("You run over, but his throat's been slit too...")

                        else:
                            print("You run over, but his throat's been slit!")

                        survivor = taken_names[random.randint(0, len(taken_names) - 1)]
                        taken_names.remove(survivor)
                        survivor2 = taken_names[0]

                        chance = random.randint(1, 2)

                        if chance == 1 or survivor == killer:
                            print("\nYou turn around, and", survivor, "is standing behind you!")
                            print("You go to explain yourself but he stops you")
                            print("He saw", survivor2, "run this way with blood on his hands, and he knows you're innocent\n")
                            print("He's eager to get out of here and he suggests the two of you team up")
                            print("Will you:\n1. Team up with him\n2. Find " + survivor2 + " on your own")
                            choice = make_choice()

                            if choice == 1:
                                print("You decide to team up with", survivor, "and head off in the direction of", survivor2)
                                print("The two of you search through the hallways and come across a bathroom")
                                print("The door is kicked ajar, and there are droplets of blood all over the floor")
                                print("This must have been where", survivor2, "washed the blood off his hands\n")

                                chance = random.randint(1, 3)

                                if survivor == killer or chance == 1:
                                    print("Suddenly", survivor, "ducks down beside a door and gestures for you to do the same")
                                    print("His eyes are wide and he whispers to you that he thinks", survivor2, "is inside")
                                    print("He gestures for you to go inside, but it's dark and you can't see anything from here")
                                    print("Will you:\n1. Take a look\n2. Tell him to go first")
                                    choice = make_choice()

                                    if choice == 1:
                                        if survivor == killer:
                                            print("The floor is covered in blood, and", survivor2, "is right in front of you")
                                            print("But he's lying down, and", survivor, "cackles as you realise", survivor2, "has been decapitated")
                                            print("Before you can react, he grabs you and slices your neck open with his knife...\nYOU DIED")
                                            game = False

                                        else:
                                            print("Your eyes adjust to the darkness, and you see", killer, "charging towards you!")
                                            print("You reach for your weapon but he stops suddenly in his tracks")
                                            print("A knife juts from his forehead and you spin around to see", survivor, "by your side")
                                            print("It looks like he saved your life with an excellent throw")

                                            print("The two of you head to the main door, and", survivor, "tells you he's not sticking around")
                                            print("You thank him for his help, then head back into the labyrinth of corridors to continue searching\n")

                                            input("Press 1 to continue: ")
                                            print(line_break)
                                            weapon_search(killer)
                                    else:
                                        if survivor == killer:
                                            print("His eyes narrow and he pulls his weapon")
                                            print("He wanted to lure you into that room so he could kill you!")
                                            print("There'll be no escape now, you'll have to fight\n")

                                            result = fight(1, "humans", survivor)

                                            if result:
                                                print(survivor + " lies dead, and when you check the room you find " + survivor2 + "'s body")
                                                print("You're sorry you couldn't save him, but what's done is done")

                                            else:
                                                game = False
                                        
                                        else:
                                            print("His eyes go wide, but he agrees and steps through the door")
                                            print("You go to follow him, but hear a scuffle then silence")
                                            print("Peeking around the doorway you see", killer, "standing over his body")
                                            print(killer, "was the killer all along and now", survivor, "is dead!")
                                            print("You've got no choice, you'll have to fight him\n")

                                            result = fight(1, "humans", killer)

                                            if result:
                                                print(killer, "lies dead, but so does", survivor, "and though you wished you could have saved him, you're glad it wasn't you")

                                                print("\nBut the old building is quiet now, and you decide to take another look around before you go")
                                                weapon_search(killer)

                                            else:
                                                game = False    

                                else:
                                    print("The two of you are checking rooms when you hear a shout")
                                    print("It's " + survivor + "'s" + " voice and you run into the room it came from")
                                    print("Inside are", survivor, "and", survivor2, "facing off")
                                    print("One of them has to be the killer")

                                    print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
                                    choice = make_choice()

                                    if choice == 1:
                                        ally = survivor
                                        enemy = survivor2

                                    elif choice == 2:
                                        ally = survivor2
                                        enemy = survivor

                                    result = fight_killer(enemy, ally, killer)

                                    if result:
                                        weapon_search(killer)

                                    else:
                                        game = False

                            else:
                                print("You don't trust", survivor, "and despite his warnings, you head off on your own")
                                print("Ascending the stairs to the next level, you find yourself staring down another identical hallway")

                                if zombie_liar != None:
                                    print("You hear something moving in a nearby room, and as you sneak closer it gets louder")
                                    zom_num = 2
                                    print("\nWithout warning", zom_num, "zombies crash through the thin office wall to your left!")
                                    result = fight(zom_num, "zombies")

                                    if result:
                                        zombies_killed += zom_num
                                        print("Looks like", zombie_liar, "was right about the zombies after all...\n")

                                    else:
                                        game = False

                                print("You continue walking down the hallway, checking each room but you're no further in your search\n")
                                print("Hearing someone walking up the stairs, you feel a strange desire to see who it is")

                                chance = random.randint(1, 3)

                                if chance == 1:
                                    print("Will you:\n1. Hide\n2. Wait at the top of the stairs")
                                    choice = make_choice()

                                else:
                                    print("You look around, but there's nowhere to hide anyway...\n")

                                    input("Press 1 to continue: ")
                                    print(line_break)
                                    choice = 2

                                if choice == 1:
                                    print("You dive into a cramped office, but you keep the door open to try and see who it is")
                                    print("You hear the footsteps get louder, then", killer, "peers into the room")
                                    print("His weapon glints as it catches the light, and he stares into the darkness before moving on")

                                    if killer == survivor:
                                        print("He's probably looking for", survivor2, "but you keep quiet just in case")

                                    else:
                                        print("You keep quiet, if", survivor, "was telling the truth, then he's the killer")
                                    
                                    input("\nPress 1 to continue: ")
                                    print(line_break)

                                    print("When he's moved on and the coast is clear, you creep out and go downstairs")

                                    if killer == survivor:
                                        print("But when you reach the floor below, you see", survivor2, "in a pool of blood")
                                        print("You run over to help but he's dead, and his throat is cut\n")
                                        print("The stairs creak, and to your horror", survivor, "is walking down with a huge grin")
                                        print("He was up there looking for you, not", survivor2, "and now he's found you")
                                        print("There'll be no escape this time, you'll have to fight...\n")
                                        result = fight(1, "humans", survivor)

                                    else:
                                        print("But when you reach the floor below, you see", survivor, "in a pool of blood")
                                        print("It seems he was telling the truth after all...")
                                        print("You hear the floorboards creak, and turn around to see", survivor2, "standing right behind you!\n")
                                        result = fight(1, "humans", survivor2)

                                    if result:
                                        print("You wipe the sweat off your brow, and realise it's only you left")
                                        print("Shocked by today's brutality, you head for the door")
                                    
                                    else:
                                        game = False

                                else:
                                    print("Deciding to follow your gut, you stand in the middle of the hallway and wait")
                                    print("Someone pokes their head up and looks at you")
                                    print("It's " + survivor2 + "!")

                                    chance = random.randint(1, 2)

                                    if chance == 1 or killer == survivor2:
                                        print("Surprisingly he smiles when he sees you")
                                        print("\nYou look at him confused, but he explains he's been running from", survivor)
                                        print("He sees the shock on your face and explains that", survivor, "was chasing him and", dead_survivors[1], "when he managed to get away")
                                        print("You tell him that", dead_survivors[1], "is dead and his face drops, he looks devastated\n")

                                        if survivor2 in event_friend_list and dead_survivors[1] in event_friend_list:
                                            print("You understand how he must feel, they were good friends")

                                        else:
                                            print("You're not sure why he's so sad if he's only known him since the apocalypse started")
                                            print("But you have no idea how the two of them got on")

                                            if survivor2 != killer:
                                                chance = random.randint(1, 3)

                                                if chance == 1:
                                                    killer = survivor2

                                        print("He looks away and recovers himself before asking if you want to team up")
                                        print("Will you:\n1. Team up with " + survivor2 + "\n2. Decide not to trust him either")
                                        choice = make_choice()

                                        if choice == 1:
                                            print("You trust", survivor2, "more than you trust", survivor, "and the two of you decide to work together")
                                            print("Now that you're a team, you'll have to figure out what to do")

                                            result = tunnel_exit(survivor, survivor2, killer, not_zombie_liar)

                                            if not result:
                                                game = False

                                        elif choice == 2:
                                            print("You don't quite buy " + survivor2 + "'s" + " story and decide to find a way out of here on your own")
                                            print("He protests against this decision, but all he can do is watch as you run off..\n")

                                            result = result = fire_escape_exit(survivor, survivor2, killer, bag_items)

                                            if result == 0:
                                                result = -1

                                            if not result:
                                                game = False

                                            else:
                                                if result > 0:
                                                    zombies_killed += result

                                    else:
                                        print("His eyes go wide when he sees you and he runs off")
                                        print("He must have thought you were the killer!")
                                        print("\nBut if you're both not the killer, then that leaves only", survivor)
                                        print("However,", survivor2, "could just be acting to get you to lose trust in", survivor)
                                        print("By splitting you up it'd be easier to kill both of you...")
                                        print("\nYou're trying to figure out what to do when", survivor, "emerges from the opposite staircase")
                                        print("It seems he came back up to look for you")
                                        print("Will you:\n1. Tell him you saw", survivor2, "\n2. Split up and look for", survivor2)
                                        choice = make_choice()

                                        if choice == 1:
                                            print("His face drops, and he thanks you for telling him")
                                            print("Since you're both together he says you should confront", survivor2)
                                            print("You agree, and the two of you run down the hallway he fled down")
                                            print("\nYou run past a dusty office, and he's waiting inside!")
                                            print("He tells you you're making a mistake and that", survivor, "is the killer")
                                            print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
                                            choice = make_choice()

                                            if choice == 1:
                                                ally = survivor
                                                enemy = survivor2

                                            elif choice == 2:
                                                ally = survivor2
                                                enemy = survivor

                                            result = fight_killer(enemy, ally, killer)

                                            if result:
                                                weapon_search(killer)

                                            else:
                                                game = False

                                        else:
                                            print("You no longer trust", survivor, "and he asks you what's changed")
                                            print("You're not going to tell him about", survivor2, "and instead you run off")
                                            print("He shouts after you desperately and tries to chase you, but you're too fast and he can't keep up")

                                            print("\nAfter around 15 minutes of searching you turn a corner and see", survivor2, "right in front of you")
                                            print("This time he doesn't run away, and he looks at you with suspicion")
                                            print("You explain to him that you believe what he said, and that you think", survivor, "is the killer")
                                            print("He asks if he can trust you and you show him your hands are clean, you haven't killed", survivor)

                                            print("\nHe thinks for a second before deciding to trust you")
                                            print(survivor2, "wants to escape but you're not sure why he didn't just leave earlier")
                                            print("Will you:\n1. Agree but ask him why he didn't leave already\n2. Find your own way out")
                                            choice = make_choice()

                                            if choice == 1:
                                                result = window_exit(survivor, survivor2, killer)

                                                if not result:
                                                    game = False

                                            else:
                                                print("Something about this doesn't add up, and you decide to escape by yourself instead")
                                                print("Without warning you sprint off down a hallway and up a flight of stairs, losing him...\n")

                                                result = fire_escape_exit(survivor, survivor2, killer, bag_items)

                                                if result == 0:
                                                    result = -1

                                                if not result:
                                                    game = False

                                                else:
                                                    if result > 0:
                                                        zombies_killed += result

                        else:
                            print("Will you:\n1. Go after the killer\n2. Find a way out")
                            choice = make_choice()

                            if choice == 1:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("You follow the trail of blood to a closed door and kick it open")
                                    print("Inside are", survivor, "and", survivor2, "facing off")
                                    print("One of them has to be the killer")

                                    if killer in event_friend_list:
                                        chance = random.randint(1, 3)

                                        if chance == 1:
                                            if killer == survivor:
                                                killer = survivor2

                                            else:
                                                killer = survivor

                                    print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
                                    choice = make_choice()

                                    if choice == 1:
                                        ally = survivor
                                        enemy = survivor2

                                    elif choice == 2:
                                        ally = survivor2
                                        enemy = survivor

                                    if choice == 1 or choice == 2:
                                        result = fight_killer(enemy, ally, killer)

                                        if result:
                                            weapon_search(killer)

                                        else:
                                            game = False

                                else:
                                    for i in dead_survivors:
                                        taken_names.remove(i)

                                    survivor = taken_names[random.randint(0, len(taken_names) - 1)]
                                    taken_names.remove(survivor)
                                    survivor2 = taken_names[0]

                                    print("After around 15 minutes of searching you turn a corner and see", survivor2, "right in front of you")
                                    print("But he looks at you with suspicion")
                                    print("He asks if he can trust you and you show him your hands are clean, you haven't killed anyone\n")
                                    print("Believing your innocence, he tells you he saw", survivor, "kill", dead_survivors[1])

                                    print(survivor2, "wants to escape but you're not sure why he didn't just leave earlier")
                                    print("Will you:\n1. Agree but ask him why he didn't leave already\n2. Find your own way out")
                                    choice = make_choice()

                                    if choice == 1:
                                        result = window_exit(survivor, survivor2, killer)

                                        if not result:
                                            game = False

                                    else:
                                        print("He hesitates, then nods and agrees")
                                        print("You lead him back to where you last saw", survivor, "and start looking around\n")
                                        print("The two of you are checking rooms when you hear a shout")
                                        print("It's " + survivor2 + "'s" + " voice and you run into the room it came from")
                                        print("Inside are", survivor2, "and", survivor, "facing off")
                                        print("One of them has to be the killer")

                                        chance = random.randint(1, 3)

                                        if chance == 1:
                                            killer = survivor

                                        print("Will you:\n1. Side with " + survivor2 + "\n2. Side with " + survivor)
                                        choice = make_choice()

                                        if choice == 1:
                                            ally = survivor2
                                            enemy = survivor

                                        elif choice == 2:
                                            ally = survivor
                                            enemy = survivor2

                                        result = fight_killer(enemy, ally, killer)

                                        if result:
                                            weapon_search(killer)

                                        else:
                                            game = False

                            elif choice == 2:
                                print("You've had enough of this killer, and have taken too many risks today")
                                print("You're going to try and escape instead")
                                print("Making your way to the door you entered earlier, you don't see anyone on your way")
                                print("But someone has locked the door\n")
                                input("Press 1 to continue: ")
                                print(line_break)

                                chance = random.randint(1, 2)

                                if survivor == killer:
                                    print("Looking back over your shoulder, you see", killer, "covered in blood and standing on the 2nd floor balcony!")
                                    print("He's grinning and staring right at you, dangling a key")
                                    print("You look in horror as he turns and sprints for the staircase\n")

                                    print("Thinking quick, you begin to climb towards a window above the door, maybe you can smash it!")

                                    print("Adrenaline pumps through your veins as you climb, hearing him get closer and closer")
                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("You punch through the glass, but blood sprays from your hand")
                                        status = add_affliction("laceration on your hand", 30)

                                        if not status:
                                            game = False

                                        chance = random.randint(1, 2)

                                        if chance == 1:
                                            print("\nBut somehow you manage to crawl through, and sprint away holding your injured hand")
                                            print("You make it home before nightfall, but you'll need to do something about your injury...")

                                            journal_entry(day, "Escaped a killer but badly hurt my hand")
                                            killer_return(killer)

                                        else:
                                            print("Blood covers your fingers and you slip, falling backwards")
                                            print("When you blink your eyes open his bloody face is staring down at you, and the last thing you see is the blade of his machete...\nYOU DIED")
                                            game = False
                                    
                                    else:
                                        print("You ball your t-shirt around your hand and punch through the glass")
                                        print("Without a second to spare you're out the window and on the ground outside")
                                        print("\nYou hear the key turning in the lock, but shout at the top of your lungs to draw zombies")
                                        print("Your plan works, and you sprint away as they emerge from the nearby buildings and attack", killer)
                                        print("You don't wait to see who wins, and instead run while he's distracted")
                                        print("\nRunning all the way home, you hope you never have to see him again...")

                                        journal_entry(day, "Escaped a killer with the help of some zombies")
                                        killer_return(killer)

                                else:
                                    print("You hear footsteps pounding the tiles and turn to see", survivor, "being chased by", survivor2)
                                    print("He's running as fast as he can and has the key in his hand")

                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print("He's almost reached you when he trips and falls on the keys\n")
                                        print("You've got no choice, you'll have to fight", survivor2)

                                        chance = random.randint(1, 3)

                                        if chance == 1:
                                            print("\nBut before you can reach " + survivor + ", " +  survivor2 + " chops down on his neck with his machete")
                                            print("You shout in frustration, and the fight begins")
                                            dead_survivors.append(survivor)

                                        else:
                                            print()
                                            print(survivor, "looks up to see you jump over him, and the fight begins!\n")

                                        result = fight(1, "humans", survivor2)

                                        if result:
                                            if survivor in dead_survivors:
                                                print("You couldn't save", survivor, "and you're the only one who survived this place")
                                                journal_entry(day, "Stopped a killer but I was the only one who survived")
                                            
                                            else:
                                                print("You've saved", survivor, "and he owes you his life")
                                                print("He opens up his bag and gives you:")
                                                random_item(3, 6, "normal", "no rot")
                                                print("\nAfter this you say goodbye and go your separate ways, glad to have escaped this place")
                                                journal_entry(day, "Stopped a killer and managed to save a survivor")
                                            
                                            print("Heading home, you think about the innocent men who were killed by", killer, "today...")

                                        else:
                                            game = False

                                    else:
                                        print("He's almost reached you when he trips and the keys fly out of his hand")
                                        print("Will you:\n1. Help him\n2. Grab the keys and escape")
                                        choice = make_choice()

                                        if choice == 1:
                                            print(survivor, "looks up to see you jump over him, and the fight begins!\n")
                                            result = fight(1, "humans", survivor2)
                                            print("You've saved", survivor, "and he owes you his life")
                                            print("He opens up his bag and gives you:")
                                            random_item(3, 6, "normal", "no rot")
                                            survivor_group = [survivor]
                                            character[6].append(survivor_group)
                                            print()
                                            print(survivor, "is now your Friend")
                                            print("\nAfter this you say goodbye and go your separate ways, glad to have escaped this place")
                                            print("Heading home, you think about the innocent men who were killed by", survivor2, "today...")

                                            journal_entry(day, "Stopped a killer and managed to save a survivor, making a new friend")

                                        else:
                                            print("You run towards", survivor, "and he reaches out for you, only to see you grab the keys instead")
                                            print("He shouts out but you ignore him and open the door")
                                            print("Screaming in horror as", survivor2, "pulls him back, he suddenly goes silent as you escape...")
                                            print("\nYou run home but " + survivor2 + " doesn't follow you, and you wonder if you could have saved " + survivor + "...")

                                            journal_entry(day, "Had a close call with a killer, and chose not to save a fellow survivor")

                if killer == "zombie" and game:
                    if body_found == True:
                        print("Sure enough, you find everyone in the conference room and explain the situation")
                        print("Following you to the place of death they see the body of", dead_survivor)

                        if dead_survivor in event_friend_list:
                            print(friend1, "mourns the loss of his friend and tells the others he'll be heading back to their camp")
                            taken_names.remove(friend1)

                            survivor = taken_names[random.randint(0, len(taken_names) -1)]
                            survivor2 = taken_names[random.randint(0, len(taken_names) -1)]

                            print("But before you leave,", survivor, "and", survivor2, "ask if you want to quickly check for any loot")

                        else:
                            print("\nSeeing the body, the group gets into a heated discussion")
                            
                            survivor = taken_names[random.randint(0, len(taken_names) -1)]
                            chance = random.randint(1, 2)
                            

                            if chance == 1:
                                print(survivor, "says he's heading back to their camp, but the other stay to look around with you")
                                taken_names.remove(survivor)

                            else:
                                survivor2 = taken_names[random.randint(0, len(taken_names) -1)]
                                taken_names.remove(survivor2)
                                survivor3 = taken_names[random.randint(0, len(taken_names) -1)]
                                print(survivor, "and", survivor2, "say they're heading back to camp, but", survivor3, "stays back to loot with you")

                                taken_names = [survivor3]

                        input("\nPress 1 to continue: ")
                        print(line_break)
                        food_search(len(taken_names) + 1, taken_names, dead_survivors[0])

            else:
                print("Though the thought of looting some guns is enticing, you won't risk it today")
                print("Explaining this to the group, you decide to head home instead...")
                journal_entry("Met a group of 4 survivors but didn't want to loot with them")

    else:
        print("But you aren't going to risk revealing yourself to a group this size")
        print("Odds are they're friendly, but if they're not you'd be in big trouble\n")
        print("On your way back to the", character[7][0], "you wonder what they were up to...")

        journal_entry("Saw a group of 4 survivors but didn't approach them")
    
    return [game, zombies_killed]