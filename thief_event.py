from functions import *

def thief_event(area, zombies_killed, character, day, item_check):
    game = True

    loot_spot = ["burnt out police station", "destroyed military checkpoint", "looted pharmacy", "burnt down petrol station"]
    event_location = loot_spot[random.randint(0, len(loot_spot) - 1)]
    raider_num = random.randint(1, 2)
    raider_has_bag = False

    print("You've arrived at", area, "and are taking a look around when you spot a", event_location)
    print("It looks to be in bad shape, but the area is deserted and you decide to take a look anyway")
    print("You set your bag down and begin to look around")
    print("But after a few minutes of searching, you've found nothing and decide to look somewhere else")
    print("\nYou turn to leave, but a stranger has walked in and picked up your bag!")
    print("You run towards the Thief, but he bolts out the door before you can catch up")

    bag_items = []

    count = 3
    
    while item_check and count > 0:
        if len(character[3]) > 0:
            item_check = True

        elif len(character[4]) > 1:
            item_check = True

        elif len(character[5]) > 0:
            item_check = True

        else:
            item_check = False

        if item_check:
            your_item = select_random_item()
            while your_item is None:
                your_item = select_random_item()

            bag_items.append(your_item)
            remove_item(your_item)
            count -= 1
    
    print("The contents of the bag were:")
    for i in bag_items:
        print(i)

    print()
    
    print("Will you:\n1. Chase after him\n2. Let him go")
    choice = make_choice()

    if choice == 1:
        thief_fear = False
        thief_zombie = False

        print("You know you can't afford to lose that bag, and sprint out after him")
        print("It's incredibly dangerous to run around like this, but you need that bag back")

        if area == "Downtown":
            print("You're a fast runner and you have the advantage in the narrow streets of Downtown")

        elif area == "the Suburbs":
            print("You grew up in these suburbs and are gaining on him fast")

        elif area == "the City Centre":
            print("You know the city streets well, and have the advantage on the the Thief")

        else:
            print("You're familiar with the Industrial Estate, and a shortcut saves you some time")

        chance = random.randint(1, 2)

        if chance == 1:
            print("\nYou've almost caught up with him when a horde of zombies crashes out in front of you!")

            chance = random.randint(1, 2)

            if chance == 1:
                print("You have enough time to get away, but the Thief still has your bag")
                print("Will you:\n1. Try and save him\n2. Let him die")
                choice = make_choice()

                if choice == 1:
                    print("He's surrounded by zombies, you're not getting to him without a fight!")

                    zom_num = random.randint(3, 6)
                    result = fight(zom_num, "zombies")

                    if result:
                        zombies_killed += zom_num
                        print("You've fought your way through, and the Thief has somehow stayed alive!")
                        print("He sees the gap in the horde and runs for it, and you run with him")

                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("But as you follow him, he pushes a zombie into your path!")

                            chance = random.randint(1, 2)

                            if chance == 1:
                                print("You barely dodge the zombie as it flings itself at you, and continue after the Thief")

                            elif chance == 2:
                                print("The zombie crashes into you and you both fall to the ground")
                                print("You hear the Thief laughing as he escapes, and the horde closes around you")

                                chance = random.randint(1, 3)

                                if chance != 1:
                                    print("\nYou shove the zombie off and narrowly avoid a bite, but you've got the horde to worry about now")
                                    print("A few of the zombies have broken off to chase the Thief, and now there's a weak spot in their ranks")
                                    print("Looks like you'll be fighting again, this time to get out of the horde...")

                                    zom_num = random.randint(4, 7)
                                    result = fight(zom_num, "zombies")

                                    if result:
                                        zombies_killed += zom_num
                                        print("The last zombie goes down, and you dodge your way through the grabbing hands and out the other side")

                                    else:
                                        game = False

                                else:
                                    print("\nYou manage to push the zombie off, but as you get up it grabs your leg and bites!")
                                    print("Pain shoots through your leg, and dozens of zombies shamble towards you")

                                    weapon = character[4][random.randint(0, len(character[4]) - 1)]
                                    print("You push them away with your", weapon, "but it's no use and you're lost to the horde...\nYOU DIED")
                                    game = False

                            if game:    
                                print("\nHe's really going to have to answer for this")
                                print("You get away from the pursuing zombies and sure enough the Thief is in a nearby building")
                                print("Stepping out from the shadows, you see his eyes widen, he thought you were dead!")

                                thief_fear = True

                        elif chance == 2:
                            print("He knocks a zombie down as it lunges for him and you jump over it, both of you have escaped the horde")
                            print("\nThe two of you manage to lose the pursuing zombies by hiding in a nearby building, and now you'll need to settle the bag problem")

                        if game:
                            print("Will you:\n1. Ask him for the bag\n2. Kill him")
                            choice = make_choice()

                            if choice == 1:
                                chance = random.randint(1, 2)

                                if thief_fear:
                                    chance = 1

                                if chance == 1:
                                    print("He hesitates for a second, before handing you back the bag")
                                    print("You check inside to make sure everything is there before leaving")
                                    print("Heading back home to the", character[7][0], "you making sure you're not followed")

                                    journal_entry(day, "A Thief tried to steal my bag, but I caught him and got it back")

                                    for i in bag_items:
                                        add_item(i)
                                        bag_items.remove(i)

                                else:
                                    print("The Thief thinks for a second then tells you he won't give it back")
                                    print("He insists that he needs it more than you do")
                                    print("Will you:\n1. Threaten him\n2. Let him have the bag")
                                    choice = make_choice()

                                    if choice == 1:
                                        chance = random.randint(1, 2)

                                        if chance == 1:
                                            print("You threaten the Thief, but his eyes narrow")
                                            print("It seems like he'd rather die than give back the bag")

                                            result = fight(1, "humans", "the Thief")

                                            if result:
                                                for i in bag_items:
                                                    add_item(i)
                                                    bag_items.remove(i)

                                                print("You pick the bag up off the floor and check everything is there, before heading back to the", character[7][0])
                                                journal_entry(day, "A Thief tried to steal my bag and I killed him to get it back")

                                            else:
                                                game = False
                                        
                                        else:
                                            print("You threaten him and his eyes widen")
                                            print("He hands the bag back to you and watches as you make sure everything is there")
                                            for i in bag_items:
                                                add_item(i)
                                                bag_items.remove(i)
                                            
                                            print("You glare at him before you leave, then head back home to the", character[7][0], "while making sure you're not followed")
                                            journal_entry(day, "A Thief tried to steal my bag but I scared him so bad he gave it back")
                                            

                                    elif choice == 2:
                                        print("You choose to let him have the bag, and he tries not to look shocked as you leave")
                                        print("He'll be fine for today, but you wonder how long it'll be before this lifestyle catches up with him")
                                        print("You head home, wondering if karma exists in the apocalypse...")
                                        journal_entry(day, "A Thief tried to steal my bag, but I let him keep it")

                                        chance = random.randint(1, 2)
                                        
                                        if chance == 1:
                                            zombie_survivor = ["the Thief"]
                                            zombie_survivors.append(zombie_survivor)
                            
                            elif choice == 2:
                                chance = random.randint(1, 3)

                                if chance == 1:
                                    print("He goes to say something, but you stop him")
                                    print("There'll be no negotiations today")

                                    result = fight(1, "humans", "the Thief")

                                    if result:
                                        for i in bag_items:
                                            add_item(i)
                                            bag_items.remove(i)
                                        print("You pick the bag up off the floor and check everything is there, before heading back to the", character[7][0])
                                        journal_entry(day, "A Thief tried to steal my bag and I showed him no mercy")

                                    else:
                                        game = False

                                else:
                                    if len(character[4]) > 1:
                                        print("You go to pull a weapon, but he tackles you before you can get to it")

                                    else:
                                        print("He goes to say something, but you tackle him before he can react")

                                    print("Slamming onto the ground, you wrestle and crash into a table")
                                    print("It seems you didn't lose the zombies after all, and they've heard the noise!")
                                    print("\nA dozen zombies burst into the room, and the pair of you struggle to your feet")
                                    print("Without thinking twice, you shove the thief into the horde, grab the bag, and make your escape")
                                    print("As you leave, you hear him scream out before falling silent...")
                                    print("\nYou check the bag on the way back to the", character[7][0], "looks like everything's there")

                                    journal_entry(day, "A Thief tried to steal my bag, so I shoved him into a horde of zombies")                 
                                    chance = random.randint(1, 2)
                                    if chance == 1:
                                        zombie_survivor = ["the Thief"]
                                        zombie_survivors.append(zombie_survivor)

                                    for i in bag_items:
                                        add_item(i)
                                        bag_items.remove(i)
                                        
                    else:
                        game = False

                elif choice == 2:
                    print("Deciding that your bag isn't worth dying for, you leave the Thief to die instead")
                    print("Taking a look back, you see him try desperately to escape before he's pulled into the horde")
                    print("\nIt looks like that's the last you'll see of that bag")
                    print("You head home, wondering if karma exists in the apocalypse...")
                    journal_entry(day, "A Thief tried to steal my bag and I lost him in a horde of zombies")

                    chance = random.randint(1, 3)

                    if chance == 1:
                        zombie_survivor = ["the Thief"]
                        zombie_survivors.append(zombie_survivor)

            elif chance == 2:
                input("\nPress 1 to continue: ")
                print(line_break)
                print("You have just enough time to turn on your heel and run, but the Thief is surrounded instantly")
                print("There's far too many zombies, and you see struggle for a second before he's pulled away")
                print("As you escape, he screams out before suddenly falling silent")
                print("\nIt looks like that's the last you'll see of that bag")
                print("You head home, wondering if karma exists in the apocalypse...")
                journal_entry(day, "Some Thief grabbbed my bag and got dragged into a horde of zombies")

                zombie_survivor = ["the Thief"]
                zombie_survivors.append(zombie_survivor)

        elif chance == 2:
            chance = random.randint(1, 2)

            if chance == 1:
                print("\nYou turn the corner and he's right in front of you")

                if raider_num == 1:
                    print("But so is a Raider!")
                    print("The Thief looks to be pleading with the Raider and offering your bag")
                    print("But the Raider laughs, and cuts him down where he stands")
                    print("\nIf you want your bag back, you'll have to fight the Raider for it")
                    print("Will you:\n1. Fight the Raider\n2. Head home")

                elif raider_num == 2:
                    print("But so are a pair of Raiders!")
                    print("The Thief looks to be pleading with the Raiders and offering them your bag")
                    print("But the Raiders laugh, and one cuts him down where he stands")
                    print("\nIf you want your bag back, you'll have to fight the Raiders for it")
                    print("Will you:\n1. Fight the Raiders\n2. Head home")

                choice = make_choice()

                if choice == 1:
                    print("That bag is yours, and you'll fight to the death for it")

                    result = fight(raider_num, "humans")

                    if result:
                        print("You grab your bag, then check the thief's body and find:")
                        random_item(1, 4, "normal")
                        print("\nWeary after the fighting, you decide to just head home...")
                        print("On your way back to the", character[7][0], "you wonder who those men were before all this...")
                        journal_entry(day, "A Thief tried to steal my bag and I had to kill some Raiders to get it back")

                        for i in bag_items:
                            add_item(i)
                            bag_items.remove(i)

                    else:
                        game = False

                else:
                    raider_has_bag = True

                    if raider_num == 1:
                        print("You're not going to risk fighting a Raider for that bag, and decide to just head home instead")
                        journal_entry(day, "A Thief grabbed my bag but a Raider got to him first")

                    else:
                        print("You're not going to fight a pair of Raiders for that bag, and instead you head back to the", character[7][0])
                        journal_entry(day, "A Thief grabbed my bag but some Raiders got to him first")

                    print("On your way home, you try not to think about what you left behind")

            elif chance == 2:
                print("\nThe bag is weighing the Thief down, and you've almost caught up with him")
                print("He tries to hop over a burnt out car but catches his foot and lands on his face")
                print("It looks like he's badly hurt his leg and can't run anymore!\n")
                print("The noise has alerted some nearby zombies and they'll be here soon")
                print("Will you:\n1. Take the bag and leave\n2. Help him")
                choice = make_choice()

                if choice == 1:
                    print("He writhes in pain on the ground, and you stoop over him to grab the bag")
                    print("Realising what you mean to do, he begs you to reconsider")
                    print("But you're not sticking around, and as the zombies emerge from nearby buildings you make your escape")
                    print("\nOn your way back to the", character[7][0], "you find yourself hoping his end was swift...")
                    journal_entry(day, "A Thief stole my bag and injured his leg, I left him for dead")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        zombie_survivor = ["the Thief"]
                        zombie_survivors.append(zombie_survivor)

                    else:
                        enemy_group = ["the Thief"]
                        enemy_list.append(enemy_group)

                    for i in bag_items:
                        add_item(i)
                        bag_items.remove(i)

                else:
                    print("You grab your bag off the ground, but you can't just leave him here")
                    print("Noticing you haven't left yet, the Thief looks up in disbelief")
                    print("He can't stand on his leg, but you help him to his feet as zombies begin to emerge from the dark buildings\n")
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("Somehow the two of you manage to outpace the zombies, but the Thief's leg is in bad shape")
                        print("You lose them down a nearby side street, and head into an abandoned building")

                    else:
                        zom_num = random.randint(2, 6)
                        print("The two of you make for a nearby side street, but your path is blocked by", zom_num, "zombies!")
                        print("The Thief won't be much use, looks like you're fighting on your own")

                        result = fight(zom_num, "zombies")

                        if result:
                            zombies_killed += zom_num
                            print("With the zombies out of the way and the Thief still alive, you head inside the building")

                        else:
                            game = False

                    if game:
                        print("\nThe interior is deserted and you set the Thief down, he'll be safe for now")
                        thief_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                        print("He thanks you profusely, and introduces himself as", thief_name)
                        print(thief_name, "still can't believe you saved him, but he needs something for his leg")
                        print("You've already done more than enough, but he says he won't survive long if he can't walk")

                        if len(character[5]) > 0:
                            print("Will you:\n1.Give", thief_name, "some medicine\n2.Refuse to help")
                            choice = make_choice()

                            if choice == 1:
                                print("You choose to help", thief_name)
                                print("Click the corresponding button to select an item")
                                print("You have:")
                                count = 1
                                for i in character[5]:
                                    print(str(count) + ". " + i)
                                    count += 1
                                choice = make_choice()
                                print("You give him", character[5][choice - 1])
                                character[5].remove(character[5][choice - 1])

                                print("He thanks you for saving his life, even though he tried to steal your bag")
                                print("He promises to try help you in the future")
                                survivor_group = [thief_name]
                                character[6].append(survivor_group)
                                print(thief_name, "is now your Friend")

                                print("\nWith this good deed, you say goodbye and head on your way")
                                journal_entry(day, "Decided to save a Thief, and made a new friend")

                            elif choice == 2:
                                print(thief_name, "looks at you sadly, but he understands")
                                print("He tried to steal your bag and you chose to save him, he shouldn't have asked for medicine as well")
                                journal_entry(day, "Saved a Thief from a horde, but didn't give him any medicine")

                                chance = random.randint(1, 2)

                                if chance == 1:
                                    zombie_survivor = [thief_name]
                                    zombie_survivors.append(zombie_survivor)

                        else:
                            print("But you don't have any medicine and you cannot help")
                            print("Before you leave he thanks you for saving him from the zombies, even if you couldn't give him any medicine")
                            journal_entry(day, "Saved a Thief from a horde, but couldn't give him any medicine")

                            chance = random.randint(1, 3)

                            if chance == 1:
                                zombie_survivor = [thief_name]
                                zombie_survivors.append(zombie_survivor)

                        print("On your way back to the", character[7][0], "you think about the decisions you made today, and wonder if anyone else would have done the same...")

    else:
        print("It isn't worth chasing a Thief through", area, "and you decide to just let him go")
        print("As you make your way home, you find yourself hoping someone else sorts him out")
        journal_entry(day, "A Thief stole my bag but I didn't risk chasing him")

    return [game, zombies_killed, raider_num, raider_has_bag, bag_items]