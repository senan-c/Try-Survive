from functions import *

def trader_mission(location, character, day, total_armour):
    game = True
    raider_hostage = False

    print("You enter the", location, "and find the Trader himself waiting for you\n")

    input("Press 1 to continue...")
    print(line_break)
    chance = random.randint(1, 2)

    if chance == 1:
        raider_hostage = True
        print("But he's not alone, looks like a Raider has taken him captive!")
        raider = describe_human("raider", 1)
        print(raider)

        if raider[28:] in survivor_descriptions_list:
            print("Perhaps this Raider can be reasoned with...")
            print("Will you:\n1. Negotiate with the Raider\n2. Fight the Raider")
            choice = make_choice()

            if choice == 1:
                print("\nYou try and reason with the Raider and he considers your proposal")
                print("He asks for some food, and in exchange he will leave without conflict")
                print("Will you:\n1. Give him some food\n2. Deny his request")
                choice = make_choice()

                if choice == 1:
                    print("\nClick the corresponding button to select an item")
                    print("You have:")
                    count = 1
                    for i in character[3]:
                        print(str(count) + ". " + i)
                        count += 1
                    choice = make_choice()
                    print("You give him (food)", character[3][choice - 1])
                    raider_hunger = random.randint(200, 800)

                    if get_cals(character[3][choice - 1]) < raider_hunger:
                        print("But the Raider is starving and unsatisfied with this offer")
                        print("He'd prefer to have his choice from your corpse!")
                        fight_result = fight(1, "humans", None, total_armour)

                        if not fight_result:
                            game  = False

                        else:
                            print("After the battle you pick back up your", character[3][choice - 1])
                            print("Seems you'll enjoy it more than him")

                            journal_entry(day, "Tried unsuccessfully to reason with a Raider and met with the Trader")

                    else:
                        print("He seems happy with this, and nods at you before leaving")
                        character[3].remove(character[3][choice - 1])

                        journal_entry(day, "Somehow managed to reason with a Raider and met with the Trader")

                elif choice == 2:
                    print("The Raider curses at you and his eyes narrow")
                    print("It looks like he'd rather fight you for your food anyway...")
                    fight_result = fight(1, "humans", None, total_armour)

                    if not fight_result:
                        game = False

                    journal_entry(day, "Fought with a Raider and met with a Trader")

            elif choice == 2:
                print("You don't negotiate with Raiders, time for him to die!")
                fight_result = fight(1, "humans", None, total_armour)

                if not fight_result:
                    game = False

                journal_entry(day, "Fought with a Raider and met with a Trader")

        else:
            print("This Raider can't be reasoned with...\n")
            print("You'll have to fight him instead")
            fight_result = fight(1, "humans", None, total_armour)

            if not fight_result:
                game = False

            journal_entry(day, "Fought with a Raider and met with a Trader")

        if game:
            print("\nWith the Raider dealt with, you're free to talk to the Trader")

    if game:
        print("He studies you for a second, then decides you're on his side\n")
        print("With this out of the way, he proposes his trades:")
        print(line_break)

        trader_pool = []
        for i in range(12):
            trader_pool.append(item_list[random.randint(0,len(item_list) -1)])

        for i in range(5):
            trader_pool.append(special_item_list[random.randint(0, len(special_item_list) - 1)])

        for i in range(1):
            trader_pool.append(ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)])

        count = 1
        none_count = 0
        your_item_list = []
        trader_item_list = []

        for i in range(3):
            your_item = select_random_item()
            if your_item is not None:
                if your_item[7:] in character[3]:
                    if your_item[7:] not in cal_list_800 and your_item[7:] not in cal_list_1000 and your_item[7:] not in cal_list_1500 and your_item[7:] not in cal_list_2500:
                        if len(character[5]) > 0:
                            category = character[5]
                            your_item = character[5][random.randint(0, len(character[5]) - 1)]

                        elif len(character[4]) > 1:
                            category = character[4]
                            your_item = character[4][random.randint(0, len(character[4]) - 1)]
                            while your_item == "hands":
                                your_item = character[4][random.randint(0, len(character[4]) - 1)]

                        else:
                            your_item = None

                        if your_item is not None:
                            if category[0] == character[4][0]:
                                your_item = "(weapon) " + your_item

                            elif category[0] == character[5][0]:
                                your_item = "(meds) " + your_item

            if your_item is not None:
                your_item_list.append(your_item)

            trader_item = trader_pool[random.randint(0, len(trader_pool) -1)]
            trader_item_list.append(trader_item)
            stored_trades = []
            if your_item is not None:
                trade = "Your " + your_item + " for his " + trader_item
                if trade not in stored_trades:
                    print(str(count) + ". " + trade)
                    count += 1
                stored_trades.append(trade)

            else:
                none_count += 1

        if none_count == 3:
            print("The Trader has no interest in your items")
            print("Come back next time with a better selection")

        else:
            print(str(count) + ".", "Reject all")
            line_break
            print("\n(You may only choose one trade)")
            choice = make_choice()

            if choice != count:
                print("You trade your", your_item_list[choice - 1], "for the Trader's", trader_item_list[choice - 1])
                add_item(trader_item_list[choice - 1])

                your_item = your_item_list[choice - 1]

                if your_item[0:2] == "(m":
                    character[5].remove(your_item[7:])

                elif your_item[0:2] == "(f":
                    character[3].remove(your_item[7:])

                elif your_item[0:2] == "(w":
                    character[4].remove(your_item[9:])

                if not raider_hostage:
                    log = "Traded with the Trader for a nice new " + trader_item_list[choice - 1]
                    journal_entry(day, log)

            else:
                print("You choose to reject the Trader's offers")
                if not raider_hostage:
                    journal_entry(day, "Met with the Trader but rejected his offers")

        print("\nBefore you leave, the Trader offers to play a game of Blackjack")

        trader_pool = []
        for i in range(20):
            trader_item = item_list[random.randint(0, len(item_list) - 1)]

            while trader_item == "(food) rotten food":
                trader_item = item_list[random.randint(0, len(item_list) - 1)]

            trader_pool.append(trader_item)

        for i in range(5):
            trader_pool.append(special_item_list[random.randint(0, len(special_item_list) - 1)])

        your_item = select_random_item()
        trader_item = trader_pool[random.randint(0, len(trader_pool) - 1)]

        while your_item == trader_item:
            your_item = select_random_item()
            trader_item = trader_pool[random.randint(0, len(trader_pool) - 1)]

        print("He proposes his", trader_item, "for your", your_item)
        print("Will you:\n1. Play Blackjack\n2. Head home")
        choice = make_choice()

        if choice == 1:
            result = play_blackjack("The Trader")

            if result == True:
                print("YOU WIN")
                print("You take the", trader_item, "and the Trader nods")
                print("He tells you he'll be sure to win next time, and you shake hands")
                add_item(trader_item)

            elif result == False:
                print("TRADER WINS")
                print("The Trader takes the", your_item, "and smiles")
                print("You tell him you want a rematch next time and he nods agreeingly")
                if your_item[0:2] == "(m":
                    character[5].remove(your_item[7:])

                elif your_item[0:2] == "(f":
                    character[3].remove(your_item[7:])

                elif your_item[0:2] == "(w":
                    character[4].remove(your_item[9:])

            elif result == "Draw":
                print("DRAW")
                print("Looks like you've stalemated, but you'll be sure to play again next time")

    return[game]