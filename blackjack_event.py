from functions import *

def blackjack_event(area, character, day):
    game = True

    print("You're walking through", area, "when something catches your eye")
    print("It looks like someone is waving at you from the roof of a nearby building!")
    survivor_num = random.randint(1, 2)
    survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
    if survivor_num == 1:
        print("You make your way up, and sure enough there's a survivor waiting for you\n")
        describe_human("survivor", 1)
        print("He introduces himself as", survivor1)

    elif survivor_num == 2:
        print("You make your way up, and sure enough there are", survivor_num, "survivors waiting for you\n")
        describe_human("survivor", 2)
        survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
        print("They introduce themselves as", survivor1, "and", survivor2)

    if survivor_num == 1:
        print(survivor1, "offers you some water and you accept it gratefully")

    elif survivor_num == 2:
        print(survivor2, "offers you some water and you accept it gratefully")

    water_drank = True

    print("You start up some conversation, and", survivor1, "brags about how great he is at blackjack")
    item_check = False
    if len(character[3]) > 0:
        item_check = True

    elif len(character[4]) > 1:
        item_check = True

    elif len(character[5]) > 0:
        item_check = True

    if item_check == True:
        survivor_pool = []
        for i in range(22):
            survivor_item = item_list[random.randint(0, len(item_list) - 1)]

            while survivor_item == "(food) rotten food":
                    survivor_item = item_list[random.randint(0, len(item_list) - 1)]
            
            survivor_pool.append(survivor_item)

        for i in range(3):
            survivor_pool.append(special_item_list[random.randint(0, len(special_item_list) - 1)])

        your_item1 = select_random_item()
        while your_item1 is None:
            your_item1 = select_random_item()

        survivor_item1 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

        while your_item1 == survivor_item1:
            your_item1 = select_random_item()
            survivor_item1 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

        print("He wants to play you, your", your_item1, "for his", survivor_item1)
        print("Will you:\n1. Challenge him to a game\n2. Back down")
        choice = make_choice()

        if choice == 1:
            result = play_blackjack(survivor1)

            remove_item(your_item1)

            survivor_pool.remove(survivor_item1)

            second_game = True

            item_check = False
            if len(character[3]) > 0:
                item_check = True

            elif len(character[4]) > 1:
                item_check = True

            elif len(character[5]) > 0:
                item_check = True

            if item_check == True:
                your_item2 = select_random_item()
                survivor_item2 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

                while your_item2 == survivor_item2:
                    your_item2 = select_random_item()
                    survivor_item2 = survivor_pool[random.randint(0, len(survivor_pool) - 1)]

                if your_item2 is None:
                    second_game = False

            else:
                second_game = False

            if result == True:
                print("YOU WIN\n")
                if survivor_num == 1:
                    print("You take the", survivor_item1, "and", survivor1, "nods")

                elif survivor_num == 2:
                    print("You take the", survivor_item1, "and", survivor1, "grimaces while", survivor2, "laughs")

                if second_game:
                    print("As you get up to leave, he stops you and challenges you to a double or nothing game")
                    print("This time, you'll be staking your", your_item1, "and", your_item2, "against his",survivor_item1, "and", survivor_item2)
                    print("Will you:\n1. Go double or nothing\n2. Take your victory and leave")

            elif result == False:
                print(survivor1.upper(), "WINS\n")
                print(survivor1, "takes the", your_item1, "and smiles")

                if second_game:
                    print("As you get up to leave, he stops you and challenges you to a double or nothing game to win it back")
                    print("This time, you'll be staking your", your_item1, "and", your_item2, "against his", survivor_item1, "and", survivor_item2)
                    print("Will you:\n1. Go double or nothing\n2. Take the loss and leave")

            elif result == "Draw":
                print("DRAW")
                second_game = True

                print("As you get up to leave,", survivor1, "stops you and asks for another game")
                print("Will you:\n1. Play another game\n2. Take the draw and leave")

            if second_game:
                choice = make_choice()

            if choice == 1 and second_game:
                result2 = play_blackjack(survivor1)

                if result2 == True:
                    print("YOU WIN\n")
                    if result != "Draw":
                        if survivor_num == 1:
                            print(survivor1, "gasps in disbelief as you take the", survivor_item1, "and the", survivor_item2)
                            print("He looks at you sadly as you wish him farewell")

                        elif survivor_num == 2:
                            print("He looks on in dismay as you take the", survivor_item1, "and the", survivor_item2 + ",", "while", survivor2, "roars laughing")
                            print("You wish them goodbye, and can still hear", survivor2, "laughing as you leave")

                        add_item(survivor_item2)

                        log = "Played some blackjack and won " + survivor_item1 + " and " + survivor_item2
                        journal_entry(day, log)

                    else:
                        if survivor_num == 1:
                            print("You take the", survivor_item1, "and", survivor1, "nods")
                            print("He looks at you sadly as you wish him farewell")

                        elif survivor_num == 2:
                            print("You take the", survivor_item1, "and", survivor1, "grimaces while", survivor2, "laughs")
                            print("You wish them goodbye, and can still hear", survivor2,"laughing as you leave")

                        log = "Played some blackjack and won " + survivor_item1
                        journal_entry(day, log)

                    print("\nYou smile to yourself as you head home, your bag heavier and your mood happier")
                    add_item(survivor_item1)
                    add_item(your_item1)


                elif result2 == False:
                    print(survivor1.upper(), "WINS\n")
                    if result != "Draw":
                        print(survivor1, "takes your", your_item1, "and your", your_item2, "and grins ear to ear")

                        remove_item(your_item2)

                        log = "Played some blackjack and lost both my " + your_item1 + " and my " + your_item2
                        journal_entry(day, log)


                    else:
                        print(survivor1, "takes your", your_item1, "and grins")

                        log = "Played some blackjack and lost my " + your_item1
                        journal_entry(day, log)

                    if survivor_num == 1:
                        print("You get up with a lighter bag as he wishes you goodbye")

                    elif survivor_num == 2:
                        print(survivor2, "pats you on the back as you try not to think too much about the loss")
                        print("You wish them both goodbye and head home")

                    print("\nOn your way back to the", character[7][0], "you promise to yourself to get better at blackjack...")


                elif result2 == "Draw":
                    print("DRAW")
                    if result == "Draw":
                        print("You look at eachother in confusion as you manage to stalemate again")
                        print("He shakes your hand, thanks you for the games and you leave")
                        print("You make your way back to the", character[7][0], "still trying to calculate the odds of that happening...")

                        journal_entry(day, "Drew two blackjack games in a row and called it quits")

                    else:
                        print("The game ends in a stalemate and the item stays with its winner")

                        if result == True:
                            print(survivor1, "looks at his", survivor_item1, "for the last time as you throw it in your bag")
                            add_item(survivor_item1)

                            log = "Played some blackjack and won " + survivor_item1
                            journal_entry(day, log)


                        elif result == False:
                            print("You look at your", your_item1, "for the last time as he throws it in his bag")

                            log = "Played some blackjack and lost my " + your_item1
                            journal_entry(day, log)

            elif choice == 2 or not second_game:
                if result == True:
                    print("You decide to take your victory and leave, saying goodbye on your way")
                    add_item(your_item1)
                    add_item(survivor_item1)

                    log = "Played some blackjack and won " + survivor_item1
                    journal_entry(day, log)

                elif result == False:
                    print("You decide to stop now before you lose something else, saying goodbye on your way")

                    log = "Played some blackjack and lost my " + your_item1
                    journal_entry(day, log)

                else:
                    print("You take the draw, glad you didn't lose your", your_item1, "but also thinking about his", survivor_item1)
                    add_item(your_item1)

                    journal_entry(day, log = "Played a game of blackjack and called it evens")

                if second_game:
                    print("You head home, wondering what would have happened if you played a second game...")

        else:
            print("You choose not to gamble, for today at least")
            print(survivor1, "goes to argue but stops himself and nods")
            if survivor_num == 1:
                print("He says goodbye and wishes you good luck, even if you're not keen on testing it")

            elif survivor_num == 2:
                print("They say goodbye and wish you good luck, even if you're not keen on testing it")

            print("\nBut as you make your way back to the", character[7][0], "you wonder what could have happened if you played some blackjack...")
            journal_entry(day, "Was offered a game of blackjack but turned it down")

    else:
        print("\nHe offers to play you if you bet some items")
        print("But you explain to him you don't really have enough to bet right now")
        charity_item = item_list[random.randint(0, len(item_list) - 1)]
        print("He nods understandingly and gives you a", charity_item, "in a gesture of charity")
        print("You thank him and head home to the", character[7][0])
        add_item(charity_item)

        log = "Met some survivors and they gave me " + charity_item
        journal_entry(day, log)