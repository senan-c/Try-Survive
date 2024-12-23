from functions import *

def locked_safe_event(area, zombies_killed, character, day):
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

            if chance == 1 and day > 7:
                print("But he's slumped against the wall and in bad shape")
                print("Looks like he's hit his head pretty hard")

                raider_name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                print("\nHis speech is slurred, but he says his name is", raider_name)
                print("He used to be a part of a gang of raiders, but he split with them after seeing their brutality")
                print("He tells you he hit his head while escaping from a horde")
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
                        print("He promises to repay you in the future")
                        survivor_group = [raider_name]
                        character[6].append(survivor_group)
                        print(raider_name, "is now your Friend")

                        print("\nWith this good deed, you say goodbye and head on your way home")

                        log = "Found an injured Raider named " + raider_name + " and saved his life"
                        journal_entry(day, log)

                    elif choice == 2:
                        print(raider_name, "struggles to look up at you, then falls back against the wall")
                        print("You turn and leave him to his fate, he will not last long...\n")

                        journal_entry(day, "Found an injured Raider, but left him to his fate")

                else:
                    print("But you don't have any medicine and you cannot help")
                    print("You explain this to him and he nods, accepting his fate")
                    print("With nothing more to do or say, you leave him to die...\n")

                    journal_entry(day, "Found an injured raider, but didn't have enough meds to save him")

            else:
                print("He doesn't appreciate your presence in his home and you'll have to fight")
                describe_human("raider", 1)
                fight_result = fight(1,"humans")

                if not fight_result:
                    game = False

                else:
                    print("With the fight over, you can take a look around")

        elif chance == 2:
            zom_num = random.randint(2, 5)
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
            print("Input the numbers one-by-one:")
            for i in range(3):
                num = int(input("Press a number: "))
                guess_list.append(num)
            print(line_break)

            if guess_list == code_list:
                print("CODE CORRECT!")
                print("You open the safe and find:")
                chance = random.randint(1,10)

                if chance == 1:
                    item = ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)]
                    print(item)
                    add_item(item)

                else:
                    random_item(2,3, "special")

                print("\nLooks like you hit the jackpot!")
                print("You head home to the", character[7][0],", excited with your find")

                journal_entry(day, "Cracked a safe open and found some great loot")

            else:
                print("CODE INCORRECT!")
                print("Looks like you couldn't guess the code")
                print("You head home, still wondering what was in the safe...")

                journal_entry(day, "Found a safe but couldn't crack the code")

    else:
        print("You decide not to risk it and head home to the", character[7][0])
        journal_entry(day, "Saw an interesting looking building but didn't risk checking it out")

    return [game, zombies_killed]