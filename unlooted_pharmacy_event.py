from functions import *

def unlooted_pharmacy_event(area, zombies_killed, character, day):
    game = True

    print("You sneak through the zombie infested streets of", area, "before something catches your eye")
    print("It looks to be an unlooted pharmacy")
    print("There are a few zombies wandering around nearby, but nowhere near the amount you saw on the way over")
    print("Will you:\n1. Take a closer look\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("Eager to find out more about this pharmacy, you sneak closer")
        print("But when you get to the door, you realise why it hasn't been looted")
        print("There's a heavy duty alarm blinking behind the window, and the shutters have been pulled down")
        print("\nBut if you can find the key, you should be able to get in")
        print("There are a couple zombies nearby that might have it")
        print("Will you:\n1. Check the zombies\n2. Head home")
        choice = make_choice()

        if choice == 1:
            key_zombies = ["Police Officer", "Nurse", "Pharmacist","Pharmacist", "Doctor", "Civilian", "Civilian"]
            print("Deciding to check the nearby zombies, you spot a few nearby:")

            key_set = False
            key_num = 6
            keys = []
            present_zombies = []

            for i in range(key_num):
                key_zombie = key_zombies[random.randint(0, len(key_zombies) - 1)]
                present_zombies.append(key_zombie)

                if key_set == False:
                    if key_num > 0:
                        key_chance = random.randint(1, key_num)

                    else:
                        key_num = 1

                    if key_chance == 1:
                        key_set = True
                        keys.append(1)

                    else:
                        key_num -= 1
                        keys.append(0)

            random.shuffle(keys)

            no_key = True
            give_up = False

            while no_key and game:
                print("Choose a zombie:")
                count= 1
                for i in present_zombies:
                    print(str(count) + ". " + i)
                    count += 1
                print(str(count) + ". " + "Head home instead")
                choice = make_choice()

                if choice <= len(present_zombies):
                    chosen_zombie = present_zombies[choice -1]
                    present_zombies.remove(chosen_zombie)
                    print("You want that key and decide to fight the", chosen_zombie)

                    result = fight(1, "zombies")

                    if result:
                        zombies_killed += 1
                        if keys[choice - 1] == 1:
                            print("You check the pockets of the", chosen_zombie, "and this one has a key!")
                            print("Alongside the key is a crumpled note with the code for the alarm")
                            alarm_code = ""

                            for i in range(4):
                                num = random.randint(0, 9)
                                alarm_code += str(num)

                            print("The alarm code is:", alarm_code)
                            
                            no_key = False
                        
                        else:
                            print("You check its pockets, but there's no key to be found\n")

                    else:
                        game = False

                else:
                    if len(present_zombies) < key_num:
                        print("You're not going to risk fighting anymore zombies, and head back to the", character[7][0], "instead")

                    else:
                        print("You won't take the risk of fighting these zombies, and decide to head home instead")

                    journal_entry(day, "Tried finding the key to a pharmacy but it was too dangerous")

                    no_key = False
                    give_up = True

            if game and not give_up:
                print("\nYou try the key on the pharmacy door, and sure enough it clicks and opens")
                print("But you'll still need to put in the code!")
                print("Enter the numbers one-by-one:")
                entered_code = ""

                for i in range(4):
                    num = input("Press a number: ")
                    entered_code += num
                print(line_break)

                if entered_code == alarm_code:
                    print("The alarm deactivates and you breathe a sigh of relief")
                    print("Now you can take a look around\n")

                    chance = random.randint(1, 3)

                    if chance == 1 or chance == 2:
                        pharmacy_loot = ["(meds) bandages", "(meds) painkillers", "(meds) first aid kit"]
                        loot_taken = []

                        print("It's dark and gloomy in here, but there's still stock on the shelves")
                        print("You'll just have to take a look at what you've grabbed later")

                        loot_amount = random.randint(1, 3)

                        for i in range(loot_amount):
                            loot_taken.append(pharmacy_loot[random.randint(0, len(pharmacy_loot) - 1)])

                        chance = random.randint(1, 3)

                        if chance != 1:
                            print("But something stirs ahead, and knocks over a display")
                            print("In the aisle to your left, something answers with a guttaral groan")
                            print("\nYou're not alone in here!")
                            print("Will you:\n1. Keep looting\n2. Make your escape")
                            choice = make_choice()

                            if choice == 1:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("You try sneak between to the back of the pharmacy, but you've pushed your luck too far!")
                                    zom_num = random.randint(3, 6)

                                    print("In the dim light you see", zom_num, "zombies approaching you!")
                                    result = fight(zom_num, "zombies")

                                    if result:
                                        zombies_killed += zom_num
                                        print("That seems to be all of them, and you're free to loot behind the counters at the back")
                                        print("Grabbing everything you can find from the prescriptions section, you wonder if the owners will ever come looking for it")
                                        print("Hopefully some of it will be of use to you")

                                        loot_amount = random.randint(2, 4)

                                        for i in range(loot_amount):
                                            loot_taken.append(pharmacy_loot[random.randint(0, len(pharmacy_loot) - 1)])

                                        print("\nOnce you're happy you've looted everything, you head outside to check what you've got")
                                        print("You lay out the items and sort through them for anything useful")

                                    else:
                                        game = False

                                else:
                                    print("You can see dark shapes lurching between the aisles, but they can't see you")
                                    print("Sneaking past them, you make your way to the shelves at the back")
                                    print("It's too dark to see what you're picking up, but you fill your bag anyway")
                                    print("\nSpotting a gap in the zombies and your way out, you sneak back outside to check what you've got")
                                    print("You lock the door behind you and lay out the items to check for anything useful")

                            else:
                                print("You're not about to risk fighting some zombies in the dark and head back outside, locking the door behind you")
                                print("You lay out the items and sort through them for anything useful")

                        else:
                            print("It looks like it's only you, and you seize the opportunity to loot the cupboards in the back")
                            loot_amount = random.randint(2, 3)

                            for i in range(loot_amount):
                                loot_taken.append(pharmacy_loot[random.randint(0, len(pharmacy_loot) - 1)])

                            print("When you're sure you've check everything, you step outside")
                            print("It seems the coast is clear and you can check the items you grabbed")
                        
                        if game:
                                print("When you're finished you're left with:")
                                for i in loot_taken:
                                    print(i)
                                    add_item(i)

                                print("\nSatisfied with this, you check to make sure nothing has seen you before heading home")
                                journal_entry(day, "Looted a pharmacy and found some useful medical supplies")

                    else:
                        print("But there's a reason this pharmacy was left alone")
                        print("It was used as a morgue, and now the dead are waking back up!")
                        print("All around you, the undead rise in the darkness and lurch towards you")
                        chance = random.randint(1, 2)
                        zom_num = random.randint(3, 5)

                        if chance == 1:
                            print("You run for the door, but your path is blocked by", zom_num, "zombies!")
                            print("\nYou've got no choice, it's time to fight")
                            result = fight(zom_num, "zombies")

                            if result:
                                zombies_killed += zom_num
                                print("You've killed the zombies in your way, and barely manage to escape as hands grab at you from the murky shadows")
                                print("Slamming the door behind you, you run down the street and manage to avoid any other zombies on your way home")
                                print("That was a close call...")
                                journal_entry(day, "Tried to loot a morgue by mistake and nearly died")

                            else:
                                game = False

                        else:
                            print("You manage to get to the door before the zombies surround you, and slam it behind you")
                            chance = random.randint(1, 3)

                            if chance == 1:
                                print("Thankfully it's all clear outside, and you're able to get back to the", character[7][0], "without anymore hassle")
                                journal_entry(day, "Tried to loot a morgue by mistake but I got away in one piece")

                            else:
                                print("But you've shut the door too hard and the alarm blares!")

                                print("You run up the street, but", zom_num, "zombies stumble out in front of you")
                                print("There's no other way out of this, you'll have to fight!")
                                result = fight(zom_num, "zombies")

                                if result:
                                    zombies_killed += zom_num
                                    print("The zombies lie dead, and you make a run for it before the others can catch up")
                                    print("You have to take a detour, but you arrive at the", character[7][0], "before dark")
                                    journal_entry(day, "Tried to loot a morgue by mistake and nearly died")
                            
                            print("That was a close call...")

        else:
            print("But you can't risk it just on the hope of finding a key")
            print("You decide to just head home to the", character[7][0], "instead")
            journal_entry(day, "Saw an unlooted pharmacy but didn't risk trying to find a key")

    else:
        print("In the apocalypse, if something seems too good to be true then it probably is")
        print("You're not risking checking out the pharmacy, and decide to head home instead")
        journal_entry(day, "Saw an unlooted pharmacy but it looked too good to be true")

    return [game, zombies_killed]