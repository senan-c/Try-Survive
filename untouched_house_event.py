from functions import *

def untouched_house_event(area, zombies_killed, character, day):
    game = True

    horde_time = random.randint(5, 40)

    print("You're on your way towards", area, "when you spot a pretty much untouched row of houses")
    print("It looks like the perfect opportunity to do some looting")
    print("These houses should be full of stuff")
    print("But as you check the place out, you hear the sound of an approaching horde...\n")

    if horde_time >= 25:
        print("The horde is still far off and you should have some time to look around")

    elif horde_time >= 15:
        print("The horde isn't too far off but you could definitely risk taking a look around")

    else:
        print("The horde is really close, it'd be very risky to loot here")

    print("Will you:\n1. Loot one of the houses\n2. Leave and avoid the horde")
    choice = make_choice()

    if choice == 1:
        ground_floor = ["kitchen", "stairs", "living room", "bathroom", "garage"]
        first_floor = ["bedroom", "bedroom", "bathroom", "study"]

        print("You try the front door on one of the houses, and it's open")
        print("Luckily there's no alarm and you can make your way inside")
        print("You're in the hallway and can start looting")

        room_num = 1
        floor = 1
        exit_house = False

        print(line_break)
        while horde_time > 0 and exit_house == False:
            print("Room #" + str(room_num) + ":")
            input("Press 1 to search the room: ")
            print(line_break)

            if floor == 1:
                room = ground_floor[random.randint(0, len(ground_floor) - 1)]

                if room == "stairs":
                    print("You open a door and see stairs going up to the first floor")
                    horde_time -= random.randint(1, 2)
                    print("You walk up the stairs and are now on the first floor")

                    floor = 2

                else:
                    horde_time -= random.randint(4, 8)

                    if room == "kitchen":
                        print("You open a door and find yourself in the kitchen")
                        print("Spending a few minutes checking cupboards and shelves you find:")
                        random_item(3, 5, "normal", "food")

                    elif room == "bathroom":
                        print("You open a door and find yourself in the bathroom")
                        print("You check through the cabinets and find:")
                        random_item(1, 2, "normal", "meds")
                    
                    elif room == "living room":
                        print("You open a door and find yourself in the living room")
                        print("You check in drawers and behind couches and find:")
                        random_item(2, 3, "normal")

                    elif room == "garage":
                        print("You open a door and find yourself in a dusty garage")
                        chance = random.randint(1, 5)

                        if chance == 1:
                            garage_items = ["(weapon) *sledgehammer*", "(clothing) *motorbike helmet*", "(clothing) *work boots*"]

                            garage_loot = garage_items[random.randint(0, len(garage_items) - 1)]

                            print("\nYou take a look around the murky room, and spot a", garage_loot, "in the corner!")
                            add_item(garage_loot)

                            print("It seems like it was a good idea to loot here after all")

                        else:
                            print("\nYou around in the murky light, and find some fuel:")
                            random_item(1, 2, "normal", "fuel")

                ground_floor.remove(room)

            elif floor == 2:
                room = first_floor[random.randint(0, len(first_floor) - 1)]
                horde_time -= random.randint(6, 10)
                
                if room == "study":
                    chance = random.randint(1, 7)
                    print("You open a door and find yourself in the study")

                    if chance == 1:
                        print("You rifle through drawers and check under the desk, until something catches your eye")
                        print("There's a gun case under the desk!\n")
                        print("Inside it you find:")
                        print("(gun) *pistol*")
                        print("(ammo) *5 pistol bullets*\n")

                        add_item("(gun) *pistol*")
                        add_item("(ammo) *5 pistol bullets*")

                    else:
                        print("You check in drawers and between plant pots and find:")
                        random_item(3, 5, "normal")
                
                elif room == "bathroom":
                        print("You open a door and find yourself in the bathroom")
                        print("You check through the cabinets and find:")
                        random_item(1, 3, "normal", "meds")

                elif room == "bedroom":
                        print("You open a door and find yourself in a bedroom")
                        chance = random.randint(1, 5)

                        if chance == 1:
                            print("You check under the bed, then the wardrobe")
                            
                            bedroom_items = ["(clothing) *leather jacket*", "(clothing) *combat pants*", "(clothing) *body armour*", "(weapon) *katana*"]
                            bedroom_loot = bedroom_items[random.randint(0, len(bedroom_items) - 1)]

                            print("Looking through the wardrobe you see a", bedroom_loot, "in the back!")
                            add_item(bedroom_loot)

                        else:
                            print("You check shelves, drawers and under the bed and find:")
                            random_item(1, 3, "normal")

                first_floor.remove(room)

            if room != "stairs":
                print("\nYou're satisfied you've looted everything in this room and can move on")

        
            if len(first_floor) > 0:
                print("\nWill you:\n1. Check another room\n2. Leave and avoid the horde")
                choice = make_choice()

            else:
                if len(ground_floor) == 0:
                    print("Looks like you've checked everywhere, it's time to leave")
                    choice = 2
                    print(line_break)

                else:
                    print("Looks like you've checked the first floor, you'll head back downstairs")
                    floor = 1

                    print("\nWill you:\n1. Check another room\n2. Leave and avoid the horde")
                    choice = make_choice()
            
            if choice == 2:
                exit_house = True

            else:
                room_num += 1

        if horde_time <= 0:
            if exit_house == False:
                print("But as you go to check the next room, you hear the front door cave in")
            
            else:
                print("But as you go to leave, you hear the front door cave in")

            print("You took too long and the horde has arrived!")

            if floor == 1:
                print("Will you:\n1. Try escape through the back door")
                choice = make_choice()

            else:
                print("Will you:\n1. Try escape through a window")
                choice = make_choice()

            chance = random.randint(1, 3)
            if choice == 1 and floor == 1:
                print("You get to the kitchen and run for the back door")

                if chance == 1:
                    print("It's open!")
                    print("As you dash out into the garden, you look back and see zombies pouring into the kitchen after you")
                    print("You hop over the fence and head home, shocked by this lucky escape")

                    journal_entry(day, "Got greedy while looting but somehow escaped unharmed")

                else:
                    chance = random.randint(1, 2)
                    print("It's locked!")

                    if chance == 1:
                        print("You kick the door desperately and it gives in, but a shock goes through your knee")
                        print("You've injured your knee!")
                        print("\nYou have lost 20HP")
                        status = add_affliction("injured knee", 20)

                        if not status:
                            game = False

                        if game:
                            print("\nYou manage to make it out the door and slam it behind you as the horde pours into the kitchen")
                            print("Somehow you get over the garden fence before you get pulled into the mass of zombies")
                            print("As you hobble home, you curse yourself for being so greedy")

                            journal_entry(day, "Escaped a horde while looting but badly hurt my knee")

                    else:
                        print("You kick the door, but it doesn't budge")
                        print("As you go to kick it again, zombies pour into the kitchen!")
                        print("Undead hands grab you and drag you into the horde...\n YOU DIED")

                        game = False

            elif choice == 1 and floor == 2:
                print("You rush to one of the bedrooms and spot a window facing the back of the house")

                if chance == 1:
                    print("It's unlocked!")
                    print("You hear the horde coming up the stairs, and without a second thought you jump out the window")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("You roll as you land, avoiding injury and keeping your speed")
                        print("\nAs the horde of zombies pour out of the house, you hop the garden fence and escape")
                        print("As you head back to the", character[7][0], "you wonder what might have happened if the window was locked...")

                        journal_entry(day, "Had to jump out a window to escape a horde, but made it out okay")

                    else:
                        print("You land badly, hurting your ankle as you hit the ground")
                        print("You've sprained your ankle!")
                        print("\nYou have lost 10HP")
                        status = add_affliction("sprained ankle", 10)

                        if not status:
                            game = False

                        if game:
                            chance = random.randint(1, 2)

                            if chance == 1:
                                print("Somehow you manage to get over the garden fence before the zombies, but it's too close")
                                print("You can still feel their hands grabbing at your legs as you make your way home...")

                                journal_entry(day, "Sprained my ankle while escaping a horde and nearly died")

                            else:
                                print("You hobble towards the garden fence, but you're too slow!")
                                print("You lunge desperately forward and trip, the horde closes around you and it's over...\nYOU DIED")

                                game = False

                else:
                    print("The window's locked!")
                    print("You'll have no choice but to smash it\n")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("You punch your hand through the window shattering it, but cutting open your hand")
                        print("\nYou have lost 20HP")
                        status = add_affliction("laceration on your hand", 20)

                        if not status:
                            game = False

                        if game:
                            print("\nClutching your hand, you hop out the window and land in the grass")
                            print("Zombies crawl out the window after you, but you manage to clear the fence and get away")
                            print("As you head back to the", character[7][0], "you nurse your hand and curse your greediness")

                            journal_entry(day, "Cut my hand open while looting a house and almost died")

                    else:
                        print("You punch through the glass but it doesn't shatter fully and blood sprays from your hand")
                        print("Clutching your hand, you look for another way out, but it's too late")
                        print("Zombies rush into the room and you're torn apart...\nYOU DIED")

                        game = False

        else:
            print("You gather your loot and open the door to head home")

            if horde_time <= 3:
                print("But when you leave the house, the horde is right in front of you!")
                print("They've spotted you and you'll have to make a run for it\n")
                print("You get to the end of the street but a some zombies have cut you off")

                zom_num = random.randint(3, 6)

                fight_result = fight(zom_num, "zombies")

                if fight_result:
                    zombies_killed += zom_num
                    print("With the zombies dead, you're free to escape the horde and head home")
                    journal_entry(day, "Ran into some zombies while looting but managed to kill them all")

                else:
                    game = False

            elif horde_time < 10:
                print("You leave the house and check down the street, the horde is close but they won't reach you")

                chance = random.randint(1, 3)

                if chance == 1:
                    zom_num = random.randint(2, 4)

                    print("But as you go to escape down a side street,", zom_num, "zombies stumble in front of you")
                    print("If you want to avoid the horde, you'll have to take them out!")

                    fight_result = fight(zom_num, "zombies")

                    if fight_result:
                        zombies_killed += zom_num
                        print("With the zombies dead, you're free to escape the horde and head home")
                        journal_entry(day, "Had to escape a horde and killed some zombies in my way")

                    else:
                        game = False

                else:
                    print("There looks to be a lot of zombie activity from the horde, but you're able to slip through undetected")
                    print("You make it all the way back to the", character[7][0], "without anymore trouble")
                    journal_entry(day, "Saw a lot of zombies while looting a house, but they didn't see me")

            else:
                print("You exit the house and see you had time to spare, the horde is nowhere near")
                print("\nYou head back without any hassle, but you wonder if you could've taken a bit more loot with you...")
                journal_entry(day, "Looted a house and escaped a horde without being seen")

    return [game, zombies_killed]