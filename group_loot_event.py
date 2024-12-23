from functions import *

def group_loot_event(zombies_killed, character, day):
    game = True

    possible_shops = ["bakery", "butchers", "supermarket"]
    shop = possible_shops[random.randint(0, len(possible_shops) - 1)]

    print("You walk for a bit and end up on a street lined with destroyed shops")
    print("Keeping your head low, you sneak behind overturned cars and crashed trucks, until you see a", shop)
    print("Unlike all the other buildings, it seems to still be in one piece")
    print("\nBut there are two people arguing outside!")
    print("Will you:\n1. Approach them\n2. Head back home")

    choice = make_choice()

    if choice == 1:
        survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
        survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

        print("They hear your footsteps and spin around, but they're not looking for a fight")
        print("You explain yourself and they relax, introducing themselves as", survivor1, "and", survivor2)
        print("They want to loot the", shop, "but are worried it could be too dangerous")
        print("If you helped them, they'd be sure to give you a share of the haul")
        print("Will you:\n1. Agree to help\n2. Head back home")

        choice = make_choice()

        if choice == 1:
            print("They smile as you agree to help, and you ready yourselves to open the doors")

            chance = random.randint(1, 2)
            if chance == 1:
                print("You push the doors open and a zombie rushes out, but", survivor2, "kills it before it can get you")
                print("Thanking him, you lead the trio into the interior")

            else:
                print("You push the door open, and nothing stirs inside")
                print(survivor1, "steps in, and you and", survivor2, "follow him")

            print("\nIt's dark and gloomy inside but the pair of survivors are eager to find some food")
            
            if shop == "butchers":
                if day >= rot_day:
                    print("Most meat has rotted away, but they think there could still be freezers here on backup power")

                else:
                    print("They think there could be some meat hidden away in the freezers here, and want to get to it before it rots")

            elif shop == "bakery":
                if day >= rot_day:
                    print("All the baked goods have rotted away, but they think their could be freezers here on backup power")

                else:
                    print("They think there could still be some food here, and want to get it before it rots")

            else:
                if day >= rot_day:
                    print("Most food has begun to rot, but they're in search of cans and non-perishables")

            print("The inside looks like it saw some fighting and is in poor shape, so you split up and check around for anything useful\n")

            input("Press 1 to continue: ")
            print(line_break)

            chance = random.randint(1, 3)

            if chance == 1:
                print("You're checking under a collapsed shelf when you hear a shuffling sound behind you!")
                zom_group = random.randint(6, 10)
                zom_num = random.randint(2, 4)
                print("It's a group of", zom_group, "zombies!")
                print(zom_num, "of them are right beside you, and the rest are approaching fast\n")
                print(survivor1, "and", survivor2, "are nowhere to be seen, it looks like you'll be fighting by yourself")

                result = fight(zom_num, "zombies")

                if result:
                    zombies_killed += zom_num
                    print("You've fought off the", zom_num, "zombies, when", survivor1, "and", survivor2, "come to your rescue!")
                    print("They catch the zombies by surprise and kill the rest without much trouble")
                    print("Now that the threat is gone, they tell you they've hit the jackpot")
                    print("They race off and head into the back of the", shop)

                else:
                    game = False

            elif chance == 2:
                print("You're checking under a collapsed shelf when you hear a shout come from the other side of the", shop)
                print("Running over and trying not to trip in the murk, you see the two survivors battling a group of zombies")
                print("As you turn the corner, you're spotted and some zombies shamble towards you\n")
                zom_num = random.randint(2, 3)

                result = fight(zom_num, "zombies")

                if result:
                    zombies_killed += zom_num
                    print("You've killed the zombies, and look up to see the two survivors have too")
                    print("They thank you and continue on into the back of the", shop)
                    print("You check around the area, but a few moments later, they call your name")

                else:
                    game = False

            else:
                print("You're checking around under broken displays when you hear the two survivors calling you")
                print("Checking around the corner, you see them beckoning you into the back of the", shop)

            if game:
                loot_amount = random.randint(5, 12)
                total_loot = []
                while loot_amount % 3 != 0:
                    loot_amount = random.randint(5, 12)
                
                if shop == "butchers":
                    print("\nYou step into the back of the butchers, and to your surprise there's the sound of a generator humming")
                    print("There must be some backup generators here that are still running\n")

                    input("Press 1 to continue:")
                    print(line_break)
                    butcher_loot = ["(food) chicken", "(food) venison", "(food) sausages"]
                    print(survivor1, "and", survivor2, "are gathered beside a large fridge, you look inside and see:")

                    for i in range(loot_amount):
                        food = butcher_loot[random.randint(0, len(butcher_loot) - 1)]
                        print(food)
                        total_loot.append(food)

                    print()

                elif shop == "bakery":
                    print("\nYou step into the back of the bakery, and to your surprise there's the sound of a generator humming")
                    print("There must be some backup generators here that are still running\n")

                    input("Press 1 to continue:")
                    print(line_break)

                    bakery_loot = ["(food) bread", "(food) cake", "(food) pastry"]
                    print(survivor1, "and", survivor2, "are standing grinning beside a large fridge, you look inside and see:")

                    for i in range(loot_amount):
                        food = bakery_loot[random.randint(0, len(bakery_loot) - 1)]
                        print(food)
                        total_loot.append(food)
                    
                    print()

                else:
                    print("\nYou step into the back of the supermarket, and see rows of destroyed shelves")
                    if day >= rot_day:
                        print("There's rotten food everywhere, what a waste")

                    supermarket_loot = ["(food) can of soup", "(food) condensed milk", "(food) can of peaches", "(food) can of beans", "(food) can of tuna", "(food) instant noodles"]
                    print("But", survivor1, "and", survivor2, "have pulled aside a collapsed shelf, and underneath you see:")

                    for i in range(loot_amount):
                        food = supermarket_loot[random.randint(0, len(supermarket_loot) - 1)]
                        print(food)
                        total_loot.append(food)

                    print()

                print(survivor1, "gathers the food and puts it in a bag, promising to share it out evenly after")
                print("You nod, and", survivor2, "goes to open the back door so the three of you can escape\n")

                input("Press 1 to continue: ")
                print(line_break)

                chance = random.randint(1, 3)

                if chance != 1:
                    print("As he opens the door an alarm blares, he must have tripped it!")
                    print("You all rush out into the alleyway out back and look for an escape")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("But the alleyway is swarming with zombies!")
                        print("They've surrounded you on both sides, and as you look back into the", shop, "they flood in")
                        print("Thinking quickly, you jump and grab hold of the top of the alley wall, barely hanging on\n")

                        input("Press 1 to continue:")
                        print(line_break)

                        print("The brick crumbles under your fingertips but you just about manage to pull yourself up")
                        print("Looking back down into the alleyway,", survivor1, "and", survivor2, "are still panicking below you")
                        print(survivor1, "notices you and reaches up for help with the bag in one hand, as the zombies rush towards him")
                        print("Will you:\n1. Help him up\n2. Grab the bag and leave him")

                        choice = make_choice()

                        if choice == 1:
                            print("With one hand steadying yourself on the wall, you reach down and pull him up")
                            print("He grabs hold of the wall and throws the bag over, before reaching down and helping up", survivor2)
                            print("With seconds to spare, both survivors are safe and thank you for your help")
                            print("\nYou've jumped into a residential area and find a quiet spot in the nearby park to split up the loot")

                            food_split = 3

                        elif choice == 2:
                            print("You reach down, but as he reaches out with his empty hand, you snatch the bag from his grip")
                            print("His eyes widen and he looks at you in disbelief, as the horde closes in on him and", survivor2)
                            print("You hop over the wall with the bag over your shoulder, and you hear them screaming out as you make your escape")
                            print("\nBefore you head home, you find a quiet spot to check what you got from the", shop)

                            survivor_group = [survivor2, survivor1]
                            zombie_survivors.append(survivor_group)

                            food_split = 1

                    elif chance == 2:
                        print("But there are zombies on all sides!\n")
                        print("You choose the smaller group of zombies and charge towards it")
                        zom_num = random.randint(3, 6)
                        print(survivor1, "and", survivor2, "follow your lead, and the three of you take on the zombies")
                        print("You're leading the charge, and you'll be taking on", zom_num, "zombies\n")

                        result = fight(zom_num, "zombies")

                        if result:
                            zombies_killed += zom_num
                            chance = random.randint(1, 2)

                            if chance == 1:
                                print("You've killed the zombies and the way is clear, but only you and", survivor2, "have gotten through")
                                print("You look back and see", survivor1, "surrounded by zombies before he disappears in the undead mass")
                                print(survivor2, "shouts out, but you drag him away before the rest of the zombies can catch up")

                                chance = random.randint(1, 2)

                                if chance == 1:
                                    survivor_group = [survivor1]
                                    zombie_survivors.append(survivor_group)

                                food_split = 2

                            else:
                                print("You've killed the zombies and the way is clear, looks like the three of you made it out okay")

                                food_split = 3
                            
                            print("You make your escape, and manage to avoid a horde coming from another direction")
                            
                            if food_split == 2:
                                print("The two of you search around and find a quiet spot to split up the loot\n")

                            else:
                                print("The three of you search around and find a quiet spot to split up the loot\n")

                        else:
                            game = False

                    if game:
                        if food_split != 1:
                            if food_split == 2:
                                print("You go to divvy up the loot but", survivor2, "stops you")
                                print("Because his friend died he thinks he should take his portion as well")
                                print("Will you:\n1. Challenge him for the split\n2. Accept his terms")

                                choice = make_choice()

                                if choice == 1:
                                    chance = random.randint(1, 2)

                                    if chance == 1:
                                        print(survivor2, "looks at you for a moment, then blinks away tears and agrees")
                                        print("He admits he's not thinking straight and apologises")
                                        print("You'll get a 50/50 share of the loot now")

                                    else:
                                        print(survivor2, "looks at you, then his eyes narrow and he draws his weapon")
                                        print("He's not thinking straight after the death of his friend, but you'll have to kill or be killed...")

                                        result = fight(1, "humans", survivor2)

                                        if result:
                                            print("With the fight over, you look down sadly at", survivor2 + "'s", "body, looks like you were the only survivor...")
                                            food_split = 1

                                        else:
                                            game = False

                                else:
                                    print("You look at him for a moment, before deciding to avoid conflict and accept his terms")
                                    print("He nods and thanks you")

                            else:
                                print("You all decide to split up the loot evenly so everyone gets a fair share")

                            if game:
                                if food_split != 1:
                                    print("When all's said and done, you end up with:")
                                    for i in range(loot_amount // food_split):
                                        food = total_loot[random.randint(0, len(total_loot) - 1)]
                                        print(food)
                                        add_item(food)
                                        total_loot.remove(food)

                                else:
                                    print("Opening the bag up, you find:")
                                    for i in total_loot:
                                        print(i)
                                        add_item(i)

                        else:
                            print("Opening the bag up, you find:")
                            for i in total_loot:
                                print(i)
                                add_item(i)

                        if food_split == 3:
                            print("With the food in your bag, you say goodbye to", survivor1, "and", survivor2)
                            print("They thank you for your help and you head home to the", character[7][0])
                            log = "Successfully looted a " + shop + " with a pair of survivors"
                            journal_entry(day, log)

                        elif food_split == 2:
                            print("With the food in your bag, you say goodbye to", survivor2)
                            print("He smiles at you sadly and you head home to the", character[7][0])
                            log = "Successfully looted a " + shop + " with a pair of survivors but one didn't make it"
                            journal_entry(day, log)

                        elif food_split == 1:
                            print("\nAs you make your way back to the", character[7][0], "you think about what it cost...")
                            log = "Successfully looted a " + shop + " with some survivors but I was the only one who made it out"
                            journal_entry(day, log)

                else:
                    print("He opens up the door and the three of you head out into the alleyway")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        zom_group = random.randint(6, 9)
                        print("You step outside but there are", zom_group, "zombies waiting for you!")

                        zom_num = random.randint(3, 5)
                        print("Since you're in the front, it looks like you'll be fighting", zom_num, "of them")
                        
                        result = fight(zom_num, "zombies")

                        if result:
                            zombies_killed += zom_num

                        else:
                            game = False

                    elif chance == 2:
                        zom_num = random.randint(2, 3)
                        print("Stepping outside, you see", zom_num, "zombies laying on the ground outside")
                        print("They stir and pull themselves up, but", survivor1, "and", survivor2, "cut them down before they can stand")
                    
                    if game:
                        print("That seems to be all of them, and you take the opportunity to split up the loot")
                        
                        print("\nWhen all's said and done, you end up with:")
                        for i in range(loot_amount // 3):
                            food = total_loot[random.randint(0, len(total_loot) - 1)]
                            print(food)
                            add_item(food)
                            total_loot.remove(food)

                        print("\nHappy with your share of the loot, you say goodbye to the pair of survivors and head home")
                        log = "Successfully looted a " + shop + " with a pair of survivors"
                        journal_entry(day, log)

        else:
            print("You think about their request, but it doesn't seem worth it")
            print("They're disappointed to hear you're not interested, and you go your seperate ways")
            print("On your way home, you consider the possibility that you might have saved their lives...")
            log = "Some survivors wanted my help looting a " + shop + " but I denied their request"
            journal_entry(day, log)

    else:
        print("You don't risk the chance of a confrontation with some other humans, and head back to the", character[7][0])
        log = "Spotted some humans outside of a " + shop + " but didn't approach them"
        journal_entry(day, log)

    return [game, zombies_killed]