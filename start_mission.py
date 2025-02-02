from functions import *
#Missions
from military_base_mission import *
from fuel_depot_mission import *
from hospital_mission import *
from trader_mission import *
from radio_tower_mission import *

def start_mission(location, temp_location, possible_locations, day, zombies_killed, water_drank, days_no_water, total_armour):
    game = True

    kilometres = random.randint(20, 50)
    chance = random.randint(1, 3)

    if chance == 1:
        setting = "still daytime"

    elif chance == 2:
        setting = "getting late"

    else:
        setting = "the middle of the night"

    print("You drive roughly", kilometres, "kilometres, but when you arrive it's", setting)
    print("You're close by, but you park your car to avoid unwanted attention")
    if setting == "getting late":
        print("It'll be dangerous at night, so you better be quick")

    elif setting == "the middle of the night":
        print("You can't make out much in your pitch black surroundings")
        print("Will you:\n1. Push forward through the dark\n2. Take shelter till the morning")
        choice = make_choice()

        if choice == 1:
            chance = random.randint(1, 3)
            zom_num = random.randint(3, 8)
            if chance == 1:
                print("You narrowly avoid a group of", zom_num , "zombies, making it through without being seen")

            elif chance == 2:
                print("You make your way towards the", location, "but a group of",zom_num, "zombies cuts you off!")
                print("They've seen you, and you'll have to fight them")
                result = fight(zom_num, "zombies")

                if not result:
                    game = False

                if result:
                    print("After making sure nothing is following you, you head towards the", location)
                    zombies_killed += zom_num

        elif choice == 2:
            print("You decide to wait until morning to explore the", location)
            chosen_shelter = shelter[random.randint(0, 2)]
            print("You find a", chosen_shelter, "to sleep in till morning")

            chance = random.randint(1, 2)
            if chance == 1:
                zom_num = random.randint(2, 4)
                print("But inside are", zom_num, "zombies!\n")
                print("You'll have to fight them off quick before they attract attention")
                result = fight(zom_num, "zombies")

                if result:
                    zombies_killed += zom_num
                    print("You manage to fight off the zombies and secure the", chosen_shelter,"for the night")
                    print("You check around, and it looks like there's some clean water here to drink")

                    eat_food()
                    journal_entry(day, "Had to fight some zombies to secure shelter while exploring")
                    day += 1

                if not result:
                    game = False

            elif chance == 2:
                print("It's deserted thankfully, and you're able to set up for the night")
                print("You check around, and it looks like there's some clean water here to drink")

                eat_food()
                journal_entry(day, "Had to find shelter while exploring, will get there tomorrow")
                day += 1

            if game:
                if character[2][0] == 0:
                    print("You are now starving")
                    print("You have lost 5 HP, find some food soon...")
                    character[0][0] -= 5
                    print("\nYou now have", character[0][0], "HP")

                water_drank = True
                days_no_water = 0

                print("You close your eyes and go to sleep")
                input("\nPress 1 to continue to Day "  + str((day)) + ": ")

                if character[0][0] < 0:
                    character[0][0] = 0

                if character[0][0] == 0:
                    print("Your body couldn't take it any more and in your sleep...\nYOU DIED")
                    game= False

                if game:
                    print(line_break)
                    print("Day",str(day))
                    print(line_break)

                    water_drank = True
                    print("When you wake up you drink the rest of your water, and head to the", location)
                    print("You feel Hydrated")

    if game:
        print("\nYou walk for a bit, keeping your head low and your eyes up, but you meet nothing along the way")
        print("\nYou've arrived at the", location)
        print("It looks deserted, so you head inside")

        input("\nPress 1 to continue: ")
        print(line_break)

        chance = random.randint(1, 2)
        if chance == 1:
            human_amount = random.randint(1, 2)
            if human_amount == 1:
                print("You enter the", location, "but you hear someone moving around up ahead")

            else:
                print("As you enter the", location, "you hear some people talking up ahead")

            chance = random.randint(1, 2)
            if chance == 1:
                human = "survivor"

            elif chance == 2:
                human = "raider"

            print("As you get closer, you notice...")
            print(describe_human(human, human_amount))
            print()

            print("Will you:\n1. Try sneak past\n2. Approach them")
            choice = make_choice()

            if choice == 1:
                print("You stick to the shadows, hoping you aren't spotted")

                chance = random.randint(1, 2)
                if chance == 1:
                    print("As you pass by, they shout out and you come to a stop")
                    spotted = True

                elif chance == 2:
                    print("Your attempt at stealth succeeds, and you sneak by undetected")
                    spotted = False

            elif choice == 2:
                print("You take a quick breath and then step out of your cover")
                if human_amount == 1:
                    print("He spins around, alarmed at your presence and grabs for his weapon")

                else:
                    print("They spin around, alarmed at your presence and grab for their weapons")
                print("But you quickly explain you're not here to hurt anyone\n")
                spotted = True

            if spotted:
                if human == "survivor":
                    print("You prepare for the worst but instead they smile and greet you")
                    survivor1 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                    if human_amount == 1:
                        print("He introduces himself as", survivor1)
                    else:
                        survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                        print("They introduce themselves as", survivor1, "and", survivor2)

                        input("\nPress 1 to continue: ")
                        print(line_break)
                        print("They don't have any problem with you being here")

                    print("But", survivor1, "has hurt himself and really needs medicine\n")
                    if len(character[5]) > 0:
                        print("Will you:\n1.Give", survivor1, "some medicine\n2.Refuse")
                        choice = make_choice()

                        if choice == 1:
                            print("You choose to help", survivor1)
                            print("Click the corresponding button to select an item")
                            print("You have:")
                            count = 1
                            for i in character[5]:
                                print(str(count) + ". " + i)
                                count += 1
                            choice = make_choice()
                            print("You give him", character[5][choice - 1])
                            character[5].remove(character[5][choice - 1])

                            if human_amount == 1:
                                print("He thanks you as you have saved his life")
                                print("He promises to try help you in the future")
                                survivor_group = [survivor1]
                                character[6].append(survivor_group)
                                print(survivor1, "is now your Friend")
                                log = "Made a new friend named " + survivor1 + " while exploring"
                                journal_entry(day, log)

                            elif human_amount > 1:
                                print("They thank you as you have saved", survivor1 + "'s", "life")
                                print("They promise to try help you in the future")
                                survivor_group = [survivor1, survivor2]
                                character[6].append(survivor_group)
                                print(survivor1, "and", survivor2, "are now your Friends")

                                log = "Made some new friends named " + survivor1 + " and " + survivor2 + " while exploring"
                                journal_entry(day, log)

                            print("\nWith this good deed, you say goodbye and head on your way")

                        elif choice == 2:
                            if human_amount == 1:
                                print(survivor1, "looks at you sadly but doesn't speak")
                                print("You turn and leave him to die, he will not last long...")

                                journal_entry(day, "Found a survivor needing medicine but left him to die")

                            else:
                                print(survivor2, "goes to shout at you but he's stopped by", survivor1)
                                print("They look at you sadly as you walk away, he will not last long...")

                                journal_entry(day, "Found some survivors needing medicine but didn't help them")

                    else:
                        print("But you don't have any medicine and you cannot help")
                        print("You explain this to him and he nods, accepting his fate")
                        print("With nothing more to do or say, you leave him to die...")

                        journal_entry(day, "A survivor was in need of medicine but I couldn't help him")

                elif human == "raider":
                    print("You've fallen into a Raider trap!")
                    fight_result = fight(human_amount, "humans", None, total_armour)
                    if not fight_result:
                        game = False

                    else:
                        if character[0][0] > 20:
                            journal_entry(day, "Had to fight a Raider while exploring")

                        else:
                            journal_entry(day, "Had to fight a Raider while exploring, I barely survived")

        elif chance == 2:
            print("You tread lightly through the", location, "but it looks like there's nobody else here")

        if game:
            if location == "Radio Tower":
                result = radio_tower_mission(possible_locations, day)

                if result == False:
                    game = False

            elif location == "Military Base":
                result = military_base_mission(zombies_killed, day, total_armour)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif location == "Hospital":
                result = hospital_mission(zombies_killed, day, total_armour)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif location == "Fuel Depot":
                result = fuel_depot_mission(location, zombies_killed, day, total_armour)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif location == "Trader's Hideout":
                result = trader_mission(location, character, day, total_armour)

                if result[0] == False:
                    game = False

    if game:
        print("With this done, your mission is complete")
        print("You head back to your car and drive back to the", character[7][0])

        if location != "Radio Tower":
            explore_list.remove(temp_location)

    return[game, zombies_killed, water_drank, days_no_water]