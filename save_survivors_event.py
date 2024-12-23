from functions import *

def save_survivors_event(area, zombies_killed, character, day, bag_items):
    game = True

    print("You make your way into", area + ",", "while keeping low and quiet")
    print("You duck out of sight as a horde passes close by, but they're not looking for you")

    survivor_amount = random.randint(1, 2)

    if survivor_amount == 1:
        survivor = "survivor"

    else:
        survivor = "pair of survivors"

    print("You look to the end of the street and see a", survivor, "exit a building and begin desperately running away")
    print("\nWill you:\n1. Try help the survivors\n2. Don't help them")
    choice = make_choice()

    if choice == 1:
        print("You decide to at least try help the", survivor, "escape")
        print("You circle around, trying to get ahead of the horde")
        print("But you're not quick enough, and a zombie stumbles out in front of you\n")

        if len(zombie_survivors) > 0:
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

            print("It's " + named_zombie + "!")
            if missing_friend:
                print("Looks like", named_zombie2, "isn't here, though he probably met a similar fate...")

                enemy_group = [named_zombie2, named_zombie]
                enemy_list.append(enemy_group)

            if named_zombie == "the Thief":
                print("And it looks like he still has your bag on his back")
                print("This might just be your opportunity to finally get it back...")

            else:
                print("You look at him sadly, remembering when you last saw him")
                print("But he doesn't share the same sentiment and shuffles towards you...")
            fight_result = fight(1, "zombies", named_zombie)

            if fight_result:
                zombies_killed += 1
                zombie_survivors.remove(named_zombie_group)

                if named_zombie == "the Thief":
                    print("You grab your bag of its back and check the contents, everything's there")
                    print("But you've still got a job to do")

                    for i in bag_items:
                        add_item(i)
                        bag_items.remove(i)

                else:
                    print("You look at", named_zombie, "for the last time, but it's time to go")
                    print("You've still got a job to do")

        else:
            fight_result = fight(1, "zombies")

        if fight_result:
            zombies_killed += 1
            if survivor_amount == 1:
                print("You run onto the street with the horde right in front of you")
                print("The survivor is still alive!\n")
                print("You spot a zombie sneaking up behind him as he retreats")
                print("You jump fowards and take it out, joining his side")

                input("Press 1 to continue: ")
                print(line_break)

                survivor_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                print("He smiles, glad to see a friendly face, and introduces himself as", survivor_name)
                print("But the fight isn't over yet, you'll each have to cut through the horde")
                print("You nod at eachother, then each make a dash for weakspots in the wall of zombies!")
                print("This is going to be a tough fight!\n")

                zom_num = random.randint(3, 7)
                fight_result = fight(zom_num, "zombies")

                if fight_result:
                    zombies_killed += zom_num
                    chance = random.randint(1, 3)
                    print("Somehow you manage to battle through the horde unscathed")
                    print("You dash forward, then spin around to look for", survivor_name)

                    if chance == 1:
                        print("\nHe appears from the horde and you cheer, but celebration doesn't last long")
                        print("A hand grabs his ankle and teeth close around his leg, before he's pulled in, never to be seen again")
                        print("As the futility of your good deed tears at your heart as you stare at the crowd of zombies")
                        print("\nYou run all the way home, not wanting to think about", survivor_name, "ever again...")

                        journal_entry(day, "Almost saved a survivor but he was dragged into a horde")

                    else:
                        print("\nHe suddenly rolls out of the horde, dodging the sea of hands grabbing at him")
                        print("He races up beside you and give you a high-five")
                        print("As the two of you make your escape, he thanks you for saving him")
                        print("Before he goes, he promises to repay you for this good deed someday\n")
                        survivor_group = [survivor_name]
                        character[6].append(survivor_group)
                        print(survivor_name, "is now your Friend")

                        print("\nWith this done, you say goodbye and head on your way home")

                        log = "Saved a survivor named " + survivor_name + " and made a new friend"
                        journal_entry(day, log)

                else:
                    game = False

            else:
                print("You run out onto the street, with the horde pouring towards you")
                print("But just in front are the two survivors!")
                print("It looks like one of them has sprained their ankle and is limping, but the zombies are catching up!")
                print("\nA rotting hand reaches out for the survivors, but you jump in to defend them")
                print("They see this and cheer, you'll be fighting out of this together")
                print("The horde has almost surrounded you, but you point towards a weak spot and they make a run for it")

                print("\nBut while the survivors make their escape, you'll have to defend their backs")
                zom_num = random.randint(4,8)
                fight_result = fight(zom_num, "zombies")

                if fight_result:
                    zombies_killed += zom_num
                    print("With enough zombies dead, you're free to make a run for it")
                    chance = random.randint(1, 2)

                    survivor1_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                    survivor2_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                    if chance == 1:
                        print("It looks like the two survivors were successful as well, there's a path out of here!")
                        print("You sprint after them, catching up with them as they round a corner")
                        print("Once you've made sure you're clear of the horde, they introduce themselves as",survivor1_name, "and", survivor2_name)
                        print("\nThey're grateful for your rescue, knowing they wouldn't have made it without you")
                        print("Before they go, they promise to repay you for this good deed someday")
                        survivor_group = [survivor1_name, survivor2_name]
                        character[6].append(survivor_group)
                        print(survivor1_name + " and " + survivor2_name + " are now your Friends")

                        print("\nWith this done, you say goodbye and head on your way home")

                        log = "Saved a pair of survivors named " + survivor1_name + " and " + survivor2_name + " and made some new friends"
                        journal_entry(day, log)

                    else:
                        print("As you run past the swarms of zombies, you search for the two survivors")
                        print("You can't see them only the zombies milling like ants in the middle of the road")
                        print("They're too busy to notice you, and you sneak away")
                        print("\nRounding the corner onto the next street, you spot one of the survivors!")
                        print("He introduces himself as", survivor1_name, "but explains his friend", survivor2_name, "didn't make it")
                        print("You offer your sympathy, and he thanks you for saving his life and trying to help his friend")
                        print("Before he goes, he promises to repay his debt someday")
                        survivor_group = [survivor1_name]
                        print(survivor1_name, "is now your Friend\n")

                        chance = random.randint(1,2)

                        if chance == 1:
                            character[6].append(survivor_group)
                            print("\nWith this done, you say goodbye and head on your way home")

                            log = "Made a new friend named " + survivor1_name
                            journal_entry(day, log)

                        else:
                            zombie_survivors.append(survivor_group)
                            print("You say goodbye, and", survivor1_name, "walks away with a limp")
                            print("But as you leave, you can't shake the feeling that it was", survivor2_name, "who was limping...")

                            log = "Made a new friend named " + survivor1_name + " but something wasn't right"
                            journal_entry(day, log)

    else:
        print("You decide not to help the", survivor, "escape, and instead watch as the horde closes in")
        survivor1_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
        survivor2_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

        if survivor_amount == 1:
            print("The survivor spins in circles, looking for a way out over and over")
            print("\nHe tries desperately to fight his way towards a nearby building, but it's no use")
            print("There's a shift in the horde and a gap appears, and he makes a run for a sidestreet")
            print("But he suddenly turns around and locks eyes with you, he's seen you but it's too late")
            print("You lose sight of him in the mass of zombies, wondering if you could have saved him")
            print("But something about that look tells you you'll see him again...")

            survivor_group = [survivor1_name]
            zombie_survivors.append(survivor_group)

            log = "Spotted a survivor running from a horde, I didn't help but I think he spotted me"
            journal_entry(day, log)

        elif survivor_amount == 2:
            print("The survivors spin in circles, shouting each other's names")
            print("It seems like their names are", survivor1_name, "and", survivor2_name)
            print("\nThey try desperately to fight their way towards eachother, but it's no use")
            print(survivor2_name, "runs back into the building and", survivor1_name, "makes a run for a sidestreet")
            print("But", survivor1_name, "suddenly turns around and locks eyes with you, he's seen you but it's too late")
            print("You lose sight of both of them in the mass of zombies, wondering if you could have saved them")

            survivor_group = [survivor2_name, survivor1_name]
            zombie_survivors.append(survivor_group)

            log = "Spotted two survivors running from a horde, I didn't help but one of them named " + survivor1_name + " spotted me"
            journal_entry(day, log)
        
        print("\nYou decide this has been enough action for today, and head home...")

    return [game, zombies_killed]