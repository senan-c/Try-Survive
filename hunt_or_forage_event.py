from functions import *

def hunt_or_forage_event(zombies_killed, character, day):
    game = True

    print("You decide to try scavenging out in the wild today, and leaving the road you were walking on, you head off into nature")
    print("You hike through the trees, keeping and eye out for zombies and look around for anything interesting")

    forage_list = ["(food) apple", "(food) carrots", "(food) mushrooms", "(food) spring onions", "(food) strawberries"]
    noise = False
    forage_success = False
    hunt_success = False

    chance = random.randint(1, 2)
    if chance == 1:
        
        print("\nSuddenly some movement between the trees catches your eye")

        animal_chance = random.randint(1, 3)

        if animal_chance == 1:
            print("There's a flock of chickens just a few metres away!")
            print("Will you:\n1. Hunt the chickens\n2. Try and catch one")
            choice = make_choice()

            if choice == 1:
                print("\nYou reach in your bag for a weapon:")
                if len(character[4]) == 1:
                    print("But there's nothing there, you'll have to use your fists")
                weapon = choose_weapon()

                print("You break from cover and charge towards them")

                if weapon == "hands":
                    chance = random.randint(1, 6)
                    print("You chase after the chickens grabbing, swinging and kicking at them wildly")

                elif weapon == "**assault rifle**":
                    chance = 1
                    print("Switching your", weapon, "to single-fire you begin to shoot at the chickens")
                    character[10][1] -= random.randint(3, 6)
                    if character[10][1] < 0:
                        character[10][1] = 0

                    if not rifle_supp:
                        noise = True

                    chickens = random.randint(2, 5)

                elif weapon == "*pistol*":
                    chance = 1
                    print("You hold your", weapon, "in both hands and fire at the chickens")
                    character[10][0] -= random.randint(3, 6)
                    if character[10][0] < 0:
                        character[10][0] = 0

                    if not pistol_supp:
                        noise = True

                    chickens = random.randint(2, 5)

                else:
                    chance = random.randint(1, 2)
                    print("You chase after the chickens, swinging your", weapon, "with deadly intent")

                    chickens = random.randint(2, 3)

                if chance == 1:
                    hunt_success = True
                    hunt_items = []
                    if weapon == "hands":
                        print("Somehow you manage to catch a chicken, but you can't harvest it properly with just your hands")
                        print("You still manage to scrape up:")
                        print("(food) chicken")
                        add_item("(food) chicken")

                    elif weapon == "**assault rifle**" or weapon == "*pistol*":
                        print("You put your", weapon, "away and check your score")
                        print("Your bullets have made some of the meat unusable, but you harvest:")
                        for i in range(chickens):
                            print("(food) chicken")
                            add_item("(food) chicken")
                            hunt_items.append("(food) chicken")

                    else:
                        print("You stop to catch your breath, putting away your", weapon, "and checking your score")
                        print("After harvesting the slain chickens, you end up with:")
                        for i in range(chickens):
                            print("(food) chicken")
                            add_item("(food) chicken")
                            hunt_items.append("(food) chicken")

                else:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("As you run after the chickens, you trip over a tree root and fall flat on your face")

                    elif chance == 2:
                        print("Somehow they evade manage to evade you, and they escape into the bushes")

            elif choice == 2:
                print("You peer through the trees and select your favourite of the flock, before dashing out after it")

                chance = random.randint(1, 5)

                if chance == 1:
                    print("You've taken them by surprise and your chosen chicken barely has time to run before you scoop it up")
                    print("Seeming to realise you don't mean any harm, the chicken relaxes")
                    print("It looks like she's a hen, maybe she'll lay eggs")
                    print("\nWhat will you name your new chicken?")
                    count = 1
                    possible_names = []
                    for i in range(3):
                        name = chicken_name_list[random.randint(0, len(chicken_name_list) - 1)]
                        possible_names.append(name)
                        print(str(count) + ". " + name)
                        count += 1

                    choice = make_choice()
                    chickens.append(possible_names[choice - 1])
                    print("You now have a chicken named", possible_names[choice - 1])

                else:
                    print("The chickens scatter and you don't even get close to them")
                    print("Before you know it they've gotten away")

        elif animal_chance == 2:
            print("There's a deer just a few metres away!")
            print("Will you:\n1. Hunt the deer\n2. Leave it alone")
            choice = make_choice

            if choice == 1:
                if len(character[4]) > 1:
                    print("\nYou reach in your bag for a weapon:")
                    weapon = choose_weapon()

                    while weapon == "hands":
                        print("\nYou reach in your bag for a weapon:")
                        print("You can't use your hands to catch a deer...")
                        weapon = choose_weapon()

                    if weapon == "**assault rifle**":
                        chance = random.randint(1, 2)
                        print("Switching your", weapon, "to single-fire and fire a single shot at the deer")
                        character[10][1] -= 1

                        if not rifle_supp:
                            noise = True

                        deer = random.randint(2,4)

                    elif weapon == "*pistol*":
                        if len(character[10][0]) > 1:
                            print("You hold your", weapon, "in both hands and fire two shots at the deer")
                            character[10][0] -= 2
                            chance = random.randint(1, 2)
                        
                        else:
                            print("You hold your", weapon, "in both hands and fire a single shot at the deer")
                            character[10][0] -= 2
                            chance = random.randint(1, 3)

                        if not pistol_supp:
                            noise = True

                        deer = random.randint(1,3)

                    else:
                        chance = random.randint(1, 3)
                        print("You creep up behind the deer and dive out swinging your", weapon)

                        deer = random.randint(1, 3)

                    if chance == 1:
                        hunt_success = True
                        hunt_items = []

                        if weapon == "**assault rifle**" or weapon == "*pistol*":
                            print("You put your", weapon, "away and check your score")
                            if weapon == "*pistol*":
                                print("The", weapon, "has made some of the meat unusable")
                            
                            else:
                                print("It's a clean shot and the carcass is in good shape")

                            print("You don't have much time but you still manage to harvest:")
                            for i in range(deer):
                                print("(food) venison")
                                add_item("(food) venison")
                                hunt_items.append("(food) venison")

                        else:
                            print("You stop to catch your breath, putting away your", weapon, "and checking your score")
                            print("It wasn't a clean kill but you should be able to harvest some meat")
                            for i in range(deer):
                                print("(food) venison")
                                add_item("(food) venison")
                                hunt_items.append("(food) venison")

                    else:
                        if weapon == "**assault rifle**" or weapon == "*pistol*":
                            print("But you've missed, and before you can fire again the deer is gone")

                        else:
                            print("But the deer is too quick for you and it disappears into the trees")

                else:
                    print("You won't be able to catch a deer with just your hands")
                    print("Instead you forage around and find:")
                    forage_amount = random.randint(3, 6)

                    for i in range(forage_amount):
                        item = forage_list[random.randint(0, len(forage_list) - 1)]
                        print(item)
                        add_item(item)

                    forage_success = True

            else:
                print("You decide not to disturb the deer, and instead go foraging")
                forage_amount = random.randint(3, 8)
                print("You check around and find:")
                for i in range(forage_amount):
                    item = forage_list[random.randint(0, len(forage_list) - 1)]
                    print(item)
                    add_item(item)

                forage_success = True

        elif animal_chance == 3:
            military_zombies = True
            mil_zom_num = random.randint(1, 2)

            if mil_zom_num == 1:
                print("But it's not an animal, it's an undead soldier!")
                print("It's camouflage has let it get too close, you'll have to fight!")

            else:
                print("But it's not an animal, it's a pair of undead soldiers!")
                print("Their camouflage has let them get too close, you'll have to fight!")

            print()
            result = fight(mil_zom_num, "military zombies")

            if result:
                if mil_zom_num == 1:
                    print("You check the body, but it doesn't look like it was carrying any guns or ammo")

                else:
                    print("You check the bodies, but it doesn't look like they were carrying any guns or ammo")

            else:
                game = False
        
        if noise:
            zom_chance = random.randint(1, 2)

            if zom_chance == 1:
                print("You turn around to head home, but firing your gun has attracted some zombies!")
                zom_num = random.randint(2, 5)
                result = fight(zom_num, "zombies")

                if result:
                    zombies_killed += zom_num
                    print("With the zombies dead you'll be able to make your way back to the", character[7][0])

            else:
                ("You decide to head home, and luckily firing your", weapon, "didn't attract any undead attention")

    else:
        print("It seems the forest is quiet for today, you haven't been able to find anything to hunt")
        print("Instead, you decide to take a look around for something to eat\n")
        print("You forage around and find:")
        forage_amount = random.randint(5, 10)

        for i in range(forage_amount):
            item = forage_list[random.randint(0, len(forage_list) - 1)]
            print(item)
            add_item(item)

        forage_success = True

    if not noise:
        print("\nYou decide to get back before it gets late, and head off towards the", character[7][0])

        if hunt_success:
            chance = random.randint(1, 7)

            if chance == 1:
                print("But as you step out of the forest, two Raiders step in front of you!")
                print("They draw their weapons and tell you to hand over your spoils")
                print("It seems they know about your hunting expedition...")
                print("Will you:\n1. Fight the Raiders\n2. Give them the food")

                choice = make_choice

                if choice == 1:
                    print("You briefly consider their offer, then drop your bag and draw your own weapon")
                    print("They snarl and the fight begins")

                    result = fight(2, "humans")

                    if not result:
                        game = False
                    
                    else:
                        print("The Raiders lie dead and the food is still yours, looks like you've earned it...")
                        journal_entry(day, "Had a successful hunting trip and killed some Raiders who wanted a piece")

                elif choice == 2:
                    print("You're not going to risk a fight with some Raiders, and you hand over the meat you worked so hard for")
                    print("Their eyes widen as they snatch it from your hands, and you hear them laughing as they walk off")
                    print("Your face burns with embarassment as you turn and head home...")

                    for i in hunt_items:
                        remove_item(i)

                    journal_entry(day, "Went hunting but had my spoils stolen by Raiders")

            else:
                journal_entry(day, "Went hunting in the forest and brought back some food")

        else:
            if hunt_success:
                journal_entry(day, "Went hunting in the forest and brought back some food")

            else:
                if not forage_success and not military_zombies:
                    journal_entry(day, "Went on a hunt in the forest but wasn't successful")

                elif forage_success:
                    journal_entry(day, "Went foraging out in the forest")

                else:
                    if mil_zom_num == 1:
                        journal_entry(day, "Went on a hunt but found a military zombie instead")

                    else:
                        journal_entry(day, "Went on a hunt but found some military zombies instead")

    else:
        if hunt_success:
            journal_entry(day, "Went hunting in the forest and brought back some food")

        else:
            if not forage_success and not military_zombies:
                journal_entry(day, "Went on a hunt in the forest but wasn't successful")

            elif forage_success:
                journal_entry(day, "Went foraging out in the forest")

            else:
                if mil_zom_num == 1:
                    journal_entry(day, "Went on a hunt but found a military zombie instead")

                else:
                    journal_entry(day, "Went on a hunt but found some military zombies instead")

    return [game, zombies_killed]