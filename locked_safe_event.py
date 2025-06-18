from functions import *

def locked_safe_event(area, zombies_killed, character, day, total_armour):
    game = True

    print("You're exploring", area, "when a small office building catches your eye")
    print("This area is dangerous, so you'd better keep your eyes peeled...")
    print("Will you:\n1. Explore the building\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("Unsure of why, you decide to head inside and check the building")
        print("You go inside and head up a flight of stairs to a room above")
        print("Opening the door, it looks like there's a huge safe in the wall")

        chance = random.randint(1,3)

        if chance == 1:
            print("\nBut there's a Raider waiting for you too!")

            chance = random.randint(1, 3)

            if chance == 1 and day >= 7:
                print("But he's slumped against the wall and in bad shape")
                print("Looks like he's hit his head pretty hard\n")

                input("Press 1 to continue: ")
                print(line_break)

                raider_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                print("His speech is slurred, but he says his name is", raider_name)
                print("He used to be a part of a gang of raiders, but he split with them after seeing their brutality")
                print("He tells you he hit his head while escaping from a horde\n")
                print(raider_name, "needs medicine, but realises you may not believe his story..")

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
                        print("\nHe promises to repay you in the future")
                        survivor_group = [raider_name]
                        character[6].append(survivor_group)
                        print(raider_name, "is now your Friend")

                        print("\nWith this good deed, you say goodbye and he heads off on his own\n")

                    elif choice == 2:
                        print(raider_name, "struggles to look up at you, then falls back against the wall")
                        print("You turn and leave him to his fate, he will not last long...\n")

                else:
                    print("But you don't have any medicine and you cannot help")
                    print("You explain this to him and he nods, accepting his fate")
                    print("\nWith nothing more to do or say, you leave him to die...\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Now it's time to check out that safe")

            else:
                print("He doesn't appreciate your presence in his home and you'll have to fight\n")
                describe_human("raider", 1)
                fight_result = fight(1,"humans", None, total_armour)

                if not fight_result:
                    game = False

                else:
                    print("With the fight over, you can take a look around")

        elif chance == 2:
            zom_num = random.randint(2, 3)
            print("\nBut there are", zom_num, "zombies waiting for you too!")
            fight_result = fight(zom_num, "zombies")

            if not fight_result:
                game = False

            else:
                zombies_killed += zom_num
                print("With the fight over, you can take a look around")

        if game:
            print("\nYou take a closer look at the safe and it seems locked")
            print("It looks like the lock needs a 3-digit code")
            code_list = []
            guess_list = []
            for i in range(3):
                num = random.randint(1, 9)
                while num in code_list:
                    num = random.randint(1, 9)
                code_list.append(num)

            code_list_sorted = sorted(code_list)

            print("But the keypad is faded on the", str(code_list_sorted[0]) + ", " + str(code_list_sorted[1]) + " and " + str(code_list_sorted[2]) + " keys\n")
            print("Seems like you'll only get one chance before the safe locks permanently")

            choice = 1

            if "safe cracker" in character[4]:
                no_health = 0
                cracker_found = False

                for i in character[4]:
                    if not cracker_found:
                        if i == "hands":
                            no_health += 1

                        elif i == "*pistol*" or i == "**assault rifle**":
                            no_health += 1

                        elif i == "safe cracker":
                            cracker_found = True

                cracker_current = weapon_durability[character[4].index("safe cracker") - no_health]

                if cracker_current > 0:
                    safe_chance = random.randint(1, 2)
                    print("But your safe cracker might be of some use here...\n")

                    if safe_chance == 1:
                        print("Will you:\n1. Enter the code\n2. Try break the safe open - 25% chance")

                    else:
                        print("Will you:\n1. Enter the code\n2. Try break the safe open - 33% chance")

                    choice = make_choice()

            if choice == 1:
                print("Input the numbers one-by-one:")
                for i in range(3):
                    num = int(input("Press a number: "))
                    guess_list.append(num)
                print(line_break)

                if guess_list == code_list:
                    print("CODE CORRECT!\n")
                    print("You open the safe and find:")
                    chance = random.randint(1,10)

                    if chance == 1:
                        item = ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)]
                        print(item)
                        add_item(item)

                    if chance != 1:
                        random_item(2,3, "special")

                    else:
                        random_item(1,2, "special")

                    print("\nLooks like you hit the jackpot!")
                    print("You head home to the " + character[7][0] +", excited with your find")

                    journal_entry(day, "Cracked a safe open and found some great loot")

                else:
                    print("CODE INCORRECT!")
                    print("Looks like you couldn't guess the code")
                    print("You head home, still wondering what was in the safe...")

                    journal_entry(day, "Found a safe but couldn't crack the code")

            else:
                print("You decide to risk it and use the safe cracker instead")
                print("Sliding it into a gap in the door of the safe, you pull with all your might\n")

                input("Press 1 to continue: ")
                print(line_break)
                chance = random.randint(1, 100)
                safe_open = False

                if safe_chance == 1:
                    if chance <= 25:
                        safe_open = True
                
                elif safe_chance == 2:
                    if chance <= 33:
                        safe_open = True
                
                if safe_open:
                    print("It gives way suddenly and you fly backwards, but it's open!\n")
                    print("Inside you find:")
                    random_item(2,3, "special")

                    print("\nLooks like you hit the jackpot!\n")

                    if cracker_current <= 10:
                        c_damage = cracker_current

                    else:
                        c_damage = random.randint(10, 20)

                    print("But in the process, your safe cracker took", c_damage, "damage")

                    weapon_durability[character[4].index("safe cracker") - no_health] -= c_damage

                    if weapon_durability[character[4].index("safe cracker") - no_health] == 0:
                        print("Your safe cracker has broken!")

                    else:
                        print("Your safe cracker now has " + str(weapon_durability[character[4].index("safe cracker") - no_health]) + "/" + str(max_weapon_durability[character[4].index("safe cracker") - no_health]) + " durability")
                    
                    print("\nYou head home to the " + character[7][0] +", excited with your find")

                    journal_entry(day, "Cracked a safe open and found some great loot")

                else:
                    print("But instead of opening, the safe creaks and jams\n")

                    if cracker_current <= 10:
                        c_damage = cracker_current

                    else:
                        c_damage = random.randint(10, 20)

                    print("In the process, your safe cracker took", c_damage, "damage")

                    weapon_durability[character[4].index("safe cracker") - no_health] -= c_damage

                    if weapon_durability[character[4].index("safe cracker") - no_health] == 0:
                        print("Your safe cracker has broken!")

                    else:
                        print("Your safe cracker now has " + str(weapon_durability[character[4].index("safe cracker") - no_health]) + "/" + str(max_weapon_durability[character[4].index("safe cracker") - no_health]) + " durability")
                    
                    print("\nThere'll be no opening it now, you'll just have to head back to the", character[7][0])
                    journal_entry(day, "Tried to force open a safe but it ended up jamming shut")
                        
    else:
        print("You decide not to risk it and head home to the", character[7][0])
        journal_entry(day, "Saw an interesting looking building but didn't risk checking it out")

    return [game, zombies_killed]