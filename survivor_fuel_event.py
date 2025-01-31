from functions import *

def survivor_fuel_event(area, character, day, rot_day, zombies_killed):
    game = True
    fuel_traded = 0

    print("Your plans to scavenge in", area, "today are interrupted by a horde of zombies crossing your path")
    print("Thankfully they don't see you and you manage to get away")
    print("However, you are forced to take a detour and end up near the highway")

    print("\nYou're about to head home when you spot something moving out on the road")
    print("Sneaking closer, you spot two survivors chatting beside a seemingly operational car")
    print("Will you:\n1. Approach them\n2. Head back home")
    choice = make_choice()

    if choice == 1:
        print("Stepping out of the bush, you take a look around before calling out to the survivors")
        print("They spin around, clearly startled but relax when they see you mean no harm")
        
        survivor = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
        survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

        print("\nIntroducing themselves as", survivor, "and", survivor2, "they quickly explain their situation to you")
        print("They were scouting the area when they spotted a sign for a nearby petrol station")
        print("but they ran out of fuel before they reached it")
        print("This area is rife with zombies so they'd need your help getting there\n")
        print("But they also offer to trade some supplies for fuel")
        print("Will you:\n1. Help them loot the petrol station")

        if character[9][0] > 0:
            print("2. Trade some of your fuel")
            print("3. Head home")

        else:
            print("2. Head home")

        choice = make_choice()

        if choice == 2 and character[9][0] > 0:
            print("Deciding to help them out by trading some of your fuel, you check your bag")

            if character[9][0] == 1:
                trade_fuel = 1

            elif character[9][0] == 2:
                trade_fuel = 2

            else:
                trade_fuel = 3

            if character[9][0] == 1:
                print("It looks like you've brought", trade_fuel, "litre of fuel to trade with")

            else:
                print("It looks like you've brought", trade_fuel, "litres of fuel to trade with")

            print()

            print(survivor, "also opens his bag and takes out some items before proposing his trades")
            print("He will only trade for one item as they aren't far from home and don't need much fuel")

            trade_list = []
            fuel_costs = []

            for i in range(3):
                if character[9][0] == 1:
                    trade_list.append(item_list[random.randint(0,len(item_list) -1)])
                    fuel_costs.append(1)

                elif character[9][0] == 2:
                    chance = random.randint(1, 10)

                    if chance == 1:
                        trade_list.append(special_item_list[random.randint(0,len(special_item_list) -1)])
                        fuel_costs.append(2)

                    elif chance <= 5:
                        trade_list.append(item_list[random.randint(0,len(item_list) -1)])
                        fuel_costs.append(2)

                    else:
                        trade_list.append(item_list[random.randint(0,len(item_list) -1)])
                        fuel_costs.append(1)

                else:
                    chance = random.randint(1, 5)

                    if chance == 1:
                        trade_list.append(special_item_list[random.randint(0,len(special_item_list) -1)])
                        fuel_costs.append(3)

                    elif chance == 2:
                        trade_list.append(item_list[random.randint(0,len(item_list) -1)])
                        fuel_costs.append(2)

                    else:
                        trade_list.append(item_list[random.randint(0,len(item_list) -1)])
                        fuel_costs.append(1)

            print("\nHis trades are:")
            for i in range(3):
                if fuel_costs[i - 1] > 1:
                    print(str(i + 1) + ". " + str(fuel_costs[i - 1]) + " litres of fuel for 1x " + trade_list[i - 1])

                else:
                    print(str(i + 1) + ". 1 litre of fuel for 1x " + trade_list[i - 1])

            print("4. Reject all")
            choice = make_choice()

            if choice != 4:
                fuel_traded = fuel_costs[choice - 1]
                add_item(trade_list[choice - 1])
                print("You traded " + str(fuel_traded) + " litres of fuel for " + survivor + "'s " + trade_list[choice - 1])

            else:
                print("You chose not to trade with", survivor, "and he looks at you in dismay")
                print("He hesitates for a second, before asking you if you'd like to come help scavenge anyway")

                print("Will you:\n1. Agree to help\n2. Head home")
                choice = make_choice()

        if choice == 1:
            print("You agree to help the survivors and the three of you set off towards the petrol station")
            print("It's not too far and after 20 minutes or so of walking, you've almost arrived")

            chance = random.randint(1, 2)

            if chance == 1:
                zom_group = random.randint(8, 12)

                print("Right as you spot the petrol station, a group of", zom_group, "zombies spills out in front of you!")
                print("Looks like it's you and the pair of survivors against the undead\n")

                zom_num = random.randint(3, round(zom_group * 0.5))

                result = fight(zom_num, "zombies")

                if result:
                    print("The group of zombies lie dead, and the two survivors are still with you")
                    print("Sliding down a dusty embankment, the three of you approach the petrol station")

                else:
                    game = False

            else:
                print("Thankfully you aren't interrupted and the three of you reach the petrol station without issue")
                print("Sliding down a dusty embankment, the three of you keep your eyes peeled for any threats")

            print("\nGetting closer, the station is definitely in disrepair but it isn't destroyed like those in the city")
            print("Looters and panicked survivors must have been wiped out before they left the city...")
            print("The two survivors decide to split up,", survivor, "heading inside with you while", survivor2, "checks the pumps outside")

            input("Press 1 to continue:")
            print(line_break)

            print("The interior is a mess with shelves knocked over and broken glass littering the floor")
            print("The pair of you get to work, searching for anything left intact while", survivor2, "is busy outside\n")

            if day >= rot_day:
                print("Checking a pallet hidden underneath a collapsed shelf, you find only rotten food")
            
            else:
                produce_list = ["(food) carrots", "(food) banana", "(food) strawberries", "(food) mushrooms", "(food) apple", "(food) spring onions"]
                food_amount = random.randint(3, 5)

                print("You spot a pallet hidden underneath a collapsed shelf, and spot some produce that seems edible")
                print("You found:")

                for i in range(food_amount):
                    item = produce_list[random.randint(0, len(produce_list) - 1)]
                    print(item)
                    add_item(item)

            chance = random.randint(1, 2)

            if chance == 1:
                print("\nAs you pick your bag back up to continue searching, you hear glass crunch behind you")

                zom_num = random.randint(1, 2)

                if zom_num == 1:
                    print("Turning around you see a zombie shambling towards you!\n")

                else:
                    print("Turning around, you see", zom_num, "zombies shambling towards you!\n")
                
                result = fight(zom_num, "zombies")
                zombies_killed += zom_num

                if result:
                    print("With the fight over you turn around to see", survivor, "emerge from the back room holding some cans")
                    print("He says he heard the commotion but it seems you took care of it")

                else:
                    game = False

            else:
                print("\nYou pick your bag back up and turn to see", survivor, "emerge from the back room holding some cans")

            can_list = ["(food) condensed milk", "(food) can of beans", "(food) can of peaches", "(food) can of peaches"]
            your_can = can_list[random.randint(0, len(can_list) - 1)]

            print("He holds them up when he sees you, and throws you a", your_can)
            add_item(your_can)

            print("Accepting it gratefully, you toss it in your bag")

            input("Press 1 to continue:")
            print(line_break)

            chance = random.randint(1, 5)

            if chance == 1:
                print("With the interior searched, the two of you head outside to check on", survivor2)
                print("You emerge to find him holding a jerrycan full of fuel with a grin on his face")
                print("This will be more than enough for them, and he reaches in his bag to give you something in return")
                print(survivor2, "gave you:")
                random_item(2, 4, "normal", "no rot")
                random_item(0, 1, "special")

                print("\nAfter wishing you well the two survivors head back to their car and you make your way home")
                journal_entry(day, "Helped some survivors scavenge up some fuel without much trouble")

            else:
                print("But as you zip up your bag, you hear a shout come from outside")
                print(survivor2, "is in trouble!")

                print("You rush outside to see a horde of zombies approaching from the highway")
                print(survivor, "gasps as he sees", survivor2, "surrounded by undead")

                possible_weapons = ["machete", "hammer", "knife"]
                survivor_weapon = possible_weapons[random.randint(0, len(possible_weapons) - 1)]

                print("\nSomehow he hasn't been bitten yet, and he's swinging his", survivor_weapon, "around wildly")
                print("Time is running out, but", survivor, "shouts at you to help him save his friend")

                explosion_chance = random.randint(1, 2)

                print("Will you:\n1. Help him save his friend\n2. Make a run for it")
                choice = make_choice()

                if choice == 1:
                    print("You won't leave them here to die, and the two of you charge in to save", survivor2)
                    if explosion_chance == 1:
                        print("Hearing your footsteps, zombies spin around and one knocks over a jerrycan of fuel")

                    else:
                        print("It looks like he was able to scrounge up a jerrycan of fuel before he was ambushed by the zombies")

                    if explosion_chance == 1:
                        print(survivor, "rushes ahead of you and knocks a zombie to the ground, giving his friend enough space to fight")
                        print("But as", survivor2, "takes a swing at a zombie he slips on the spilled fuel, his", survivor_weapon, "sparking on the ground")
                        print("The group of zombies surrounding him are instantly alight in flames, and to your horror one stumbles straight into the fuel pumps")

                        print("\nThe explosion is deafening, throwing you backwards and off your feet")

                        injury_chance = random.randint(1, 2)

                        if injury_chance == 1:
                            print("Feeling a searing pain in your arm, you look down and see you're on fire!")
                            print("Rolling on the ground you manage to extinguish the flames, but the damage is already done")

                            print("\nYou have lost 30HP")
                            status = add_affliction("petrol burns", 30)

                            if not status:
                                game = False

                            if game:
                                print("You're burnt badly but alive")
                        
                        else:
                            print("You land hard, but you've somehow emerged unscathed")
                        
                        print("The same can't be said for", survivor2, "who is now scattered across the ground, alongside the zombies who surrounded him")
                        print("Hearing a scream behind you, you spin to see", survivor, "badly injured and crawling away from dozens of zombies")
                        print("\nBefore you can do anything he's dragged into the horde, and all you can do is run")

                        if injury_chance == 1:
                            print("Wincing from the pain of your burns, you make it back to the", character[7][0], "before dark")
                            journal_entry(day, "Tried to help some survivors grab some fuel, but got badly burnt and lost them both")

                        else:
                            print("Arriving home at the", character[7][0], "you try not to think about what happened today...")
                            journal_entry("Tried to help some survivors grab some fuel but it went terribly wrong")

                    else:
                        zom_group = random.randint(5, 8)
                        print("Most of the highway horde hasn't reached you yet, just these", zom_group, "zombies")
                        extra_num = random.randint(2, 3)
                        zom_num = random.randint(3, 5)
                        print(zom_num, "zombies turn and lumber towards you while", extra_num, "continue to surround", survivor2)
                        print(survivor, "charges ahead, taking on", (zom_group - zom_num), "zombies and leaving the rest for you\n")
                        
                        result = fight(zom_num, "zombies")

                        if result:
                            print("With the initial group of zombies lie dead there's no time to waste as the horde approaches")
                            print("The two survivors grab the jerrycan and the three of you escape in the nick of time")
                            print("You double back onto the highway and find the car intact and thankfully without any visitors\n")

                            print("Before they leave", survivor2, "thanks you for saving him, and reaches in his bag for a reward")
                            print(survivor2, "gave you:")
                            random_item(3, 4, "normal", "no rot")
                            random_item(0, 1, "special")

                            print("\nHeading home, you wonder if you'll end up seeing them again but glad you could help them")

                            journal_entry(day, "Helped some survivors scavenge fuel and fight off some zombies")

                        else:
                            game = False

                else:
                    print("Seeing his friend in trouble", survivor, "rushes forward to help, but you don't follow him")
                    print("He shouts as he sees you escape, dooming him and his friend to the horde...")

                    print("\nYou make it back to the", character[7][0], "unscathed, but you wonder if you could have saved those two survivors...")
                    journal_entry(day, "Escaped a horde, but I chose not to save two other survivors")

                    chance = random.randint(1, 3)

                    if chance == 1:
                        survivor_group = [survivor2, survivor]
                        zombie_survivors.append(survivor_group)

        elif choice == 2:
            print("You apologise, but you're not interested")
            print("They look at you disappointed and you wish them luck before heading home")

            if character[9][0] == 0:
                print("On your way back to the", character[7][0], "you wonder what will become of them...")

            else:
                print("On your way back to the", character[7][0], "you find yourself wishing you checked what they had for trade")

    return[game, zombies_killed, fuel_traded]
        