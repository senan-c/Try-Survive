from functions import *
import csv

#Events
from supply_crate_event import *
from zombie_horde_event import *
from dead_survivor_event import *
from unlooted_store_event import *
from surrounded_van_event import *
from blackjack_event import *
from locked_safe_event import *
from survivor_footprints_event import *
from save_survivors_event import *
from killer_within_event import *
from enemy_survivor_event import *
from untouched_house_event import *
from hunt_or_forage_event import *
from loot_cars_event import *
from group_loot_event import *
from thief_event import *
from free_supplies_event import *
from unlooted_pharmacy_event import *
from workshop_event import *
from get_your_bag_event import *
from zombie_patrol_event import *
from survivor_fuel_event import *
from crumbling_bridge_event import *

from start_mission import *

username_list = []

with open("scores.csv", "r") as prev_usernames:
    read_users = csv.reader(prev_usernames)
    for row in read_users:
        username_list.append(row[0])

prev_usernames.close()

for i in range(len(username_list)):
    username_list[i] = username_list[i].upper()

username = input("Enter your Username: ")

while len(username) > 10:
    print("That Username is too long\n")
    username = input("Enter your Username: ")

while username.upper() in username_list:
    print("That Username is already taken\n")
    username = input("Enter your Username: ")

    while len(username) >= 10:
        print("That Username is too long\n")
        username = input("Enter your Username: ")

print("\nThis game is played with the number keys corresponding to each choice\n")
play = input("Click 1 to Play: ")
print(line_break)

while play != "1":
    play = input("Click 1 to Play: ")
    print(line_break)

print("Choose your character:")
print("1. Survivor - Difficulty: Medium")
print("2. First Responder - Difficulty: Easy")
print("3. Patient - Difficulty: Hard")
choice = make_choice()

if choice == 1:
    character_type = "Survivor"

elif choice == 2:
    chance = random.randint(1, 3)

    if chance == 1:
        character_type = "Police Officer"

    elif chance == 2:
        character_type = "Firefighter"

    else:
        character_type = "Paramedic"

else:
    character_type = "Patient"

print("Welcome " + username + ", it looks like you're a " + character_type)

if character_type != "Patient":
    print("\nWould you like to skip the intro?\n1. Yes\n2. No")
    skip_choice = make_choice()

    if skip_choice == 1:
        print("Intro has been skipped")

    else:
        print("Your story begins...")

else:
    skip_choice = 2

while game:
    if (day == rot_day or character_type == "Patient") and rotten_food == False:
        rotten_food = True

        item_list.remove("(food) apple")
        item_list.remove("(food) chicken")
        item_list.remove("(food) bread")
        item_list.remove("(food) sausages")
        item_list.remove("(food) carrots")
        item_list.remove("(food) banana")
        item_list.remove("(food) strawberries")
        item_list.remove("(food) pre-made meal")
        item_list.remove("(food) carton of eggs")
        item_list.remove("(food) butter")
        item_list.remove("(food) mushrooms")

        for i in range(10):
            item_list.append("(food) rotten food")

    if "crowbar" in character[4] and "(weapon) crowbar" in item_list:
        item_list.remove("(weapon) crowbar")

    elif "(weapon) crowbar" not in item_list:
        item_list.append("(weapon) crowbar")

    calories_used = 0
    print(line_break)
    print("Days Survived:",str(day))
    day += 1
    print(line_break)
    if day == 1:
        if skip_choice == 2:
            if character_type != "Patient":
                print("The Quarantine Zones have fallen and now you find yourself in the middle of a city in chaos\n")
            if character_type == "Survivor":
                print("Your lungs burning, you risk a glance over your shoulder and your eyes widen in horror")
                print("Swarms of zombies pour into the street behind you, completely overwhelming everyone in their path")
                print("You parked your car nearby, but there's no telling if it's still there")
                print("If it's not, you'll surely die here, or worse...\n")
                input("Press 1 to continue: ")
                print(line_break)
                print("But thankfully you find it unscathed and you hop in before formulating a plan")
                print("You have a few options for where to go, but you'll need to make your decision quickly")
                print("Will you:\n1. Make your way home - Heal faster from injuries\n2. Get back to the restaurant you work at - Bonus calories when cooking\n3. Drive to the forest nearby and camp out in your car - Unlimited water from the spring")
                home_choice = make_choice()
                print("Pulling out of the car park, you narrowly avoid a group of zombies before speeding off towards your destination\n")

            elif character_type == "Police Officer":
                print("You fire your *pistol* indiscriminately into the crowd of zombies, but it's no use")
                print("A horde this big can't be stopped, all you can do is run")
                print("Looking around you see your fellow officers scatter and flee alongside you, there's no hope left for the city...\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("But as you turn back around, you run right into a fireman running the other way")
                print("You're knocked to the ground and your *pistol* flies out of your hand and skitters under a van")
                print("He apologises and helps you up, before a swarm of zombies rounds the corner and you both run for your lives\n")

                print("The fireman disappears down a neighbouring street, and you make a run for your Police Cruiser parked nearby\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Thankfully you find it unscathed and you hop in before formulating a plan")
                print("You have a few options for where to go, but you'll need to make your decision quickly")
                print("Will you:\n1. Make your way home - Heal faster from injuries\n2. Head for your local restaurant - Bonus calories when cooking\n3. Drive to the forest nearby and camp out in your Police Cruiser - Unlimited water from the spring")
                home_choice = make_choice()
                print("Tyres screeching, you narrowly avoid a group of zombies before speeding off towards your destination\n")

            elif character_type == "Firefighter":
                print("You pull desperately on your captain's arm, but it's no use")
                print("Watching in horror, he's pulled into the crowd of zombies and all you can do is run")
                print("A zombie lunges out to grab you, but you knock it back with your fire axe and keep moving\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Hearing gunshots ahead, you watch as police officers scatter and run from the undead army")
                print("Not paying attention, you run straight into an officer and both of you tumble to the ground")
                print("His *pistol* goes flying, but you help him up and the two of you run for your lives\n")

                print("He races off down the street, but the horde is coming and you decide to head in the opposite direction\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Spotting a car in the street ahead, you run towards it only to see the owner dragged out by a dozen zombies")
                print("He screams in pain, but there's nothing you can do as you hop inside the car and slide into the driver's seat")
                print("Undead hands claw at the windows, but you slam on the accelerator and take off down the street\n")
                print("Will you:\n1. Make your way home - Heal faster from injuries\n2. Head for your local restaurant - Bonus calories when cooking\n3. Drive to the forest nearby and camp out in the car - Unlimited water from the spring")
                home_choice = make_choice()

            elif character_type == "Paramedic":
                print("The hospital is has been overrun, and screams echo through the hallways as you make your escape")
                print("Doctors and patients alike run down the corridors, followed closely by hordes of undead")
                print("You won't be able to help anyone here, all you can do is run\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("You're cut off from the ambulance bay, but your car should still be parked outside")
                print("With more zombies on the way, it's your only hope of survival")
                print("Stopping to pack some medical supplies into your bag, you make a run for it\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("You burst out the hospital doors and spot half a dozen zombies in the parking lot")
                print("Somehow you manage to hop in the car and stamp on the accelerator before they can reach you\n")
                print("You have a few options for where to go, but you'll need to make your decision quickly")
                print("Will you:\n1. Make your way home - Heal faster from injuries\n2. Head for your local restaurant - Bonus calories when cooking\n3. Drive to the forest nearby and camp out in your car - Unlimited water from the spring")
                home_choice = make_choice()
                print("Pulling out of the car park, you narrowly avoid the group of zombies before speeding off towards your destination\n")

            elif character_type == "Patient":
                character[0][0] = 75
                character[1][0] = "Parched"
                character[2][0] = 0

                print("Blinking your eyes open, the first thing you notice is how dry your throat is")
                print("You've woken up in a hospital bed and light pours in from the window, illuminating the dusty air")
                print("The next thing you notice is how quiet the hospital is...\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Sitting up and pushing yourself out of bed, you almost collapse as your legs give way")
                print("It seems you've been asleep for quite a while...")
                print("After a few minutes you manage to get to your feet and make your way to the door")
                print("But a pool of dried blood on the floor catches your eye, and as the door creaks open, you see the hospital is in ruins\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("Exit signs still flicker green, and they guide your way through the carnage of the dusty hallways")
                print("You're shocked to see bodies strewn about, with some showing sign of having been mauled and eaten...")
                print("Reaching the front doors the sun almost blinds you, and through squinted eyes you see a figure staggering towards you...\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("With the sun still in your eyes, you can't make out their face, but something's not right")
                print("As they get closer their rotting face comes into view, and you jump back in horror")
                print("It's a person, but their skin is grey and rotting away, and their eyes are glazed over\n")

                input("Press 1 to continue: ")
                print(line_break)

                print("There's no other answer, it has to be a zombie!")
                print("You've got no other choice, if you want to survive you'll have to kill it...\n")

                result = fight(1, "zombies")

                if result:
                    print("Panting heavily, your hands shake as you look down at the corpse")
                    print("It's still now, and you take some respite from putting it out of its misery\n")
                    print("Checking its pockets, you find car keys which sure enough open a car parked outside")
                    print("Getting in, it looks like you have just enough fuel to get back to your house\n")
                    home_choice = 1

                else:
                    day -= 1
                    game = False

        else:
            if character_type != "Survivor":
                print("Where will you go after the fall of the Quarantine Zones?\n1. Make your way home - Heal faster from injuries\n2. Get back to the restaurant you work at - Bonus calories when cooking\n3. Drive to the forest nearby and camp out in your car - Unlimited water from the spring")

            else:
                print("Will you:\n1. Make your way home - Heal faster from injuries\n2. Head for your local restaurant - Bonus calories when cooking\n3. Drive to the forest nearby and camp out in your car - Unlimited water from the spring")
            home_choice = make_choice()

        if game:
            if home_choice == 1:
                character[7].append("house")

            elif home_choice == 2:
                character[7].append("restaurant")

            else:
                character[7].append("campground clearing")

            if home_choice == 1:
                if character_type != "Patient":
                    print("The city streets are in chaos, but you have just enough fuel to get back to your house")

                    print("With zombies everywhere, you hurry inside managing to avoid being seen")
                    print("With the door locked behind you, you feel at least a little bit safer\n")

                    print("Checking the cupboards, you pour yourself a glass of water before taking a look around")
                    print("You'll need to get used to searching for useful supplies, this is your new life...\n")

                    input("Press 1 to continue: ")
                    print(line_break)

                    print("After doing a sweep of your house, you've found:")
                    random_item(3, 5, "normal", "no fuel")

                    if character_type == "Police Officer":
                        print("\nGrabbing your bag from the Police Cruiser, you check inside and find:")
                        add_nightstick()

                        print("(clothing) *police vest*")
                        add_item("(clothing) *police vest*")

                else:
                    input("Press 1 to continue: ")
                    print(line_break)

                    print("Your neighbourhood is nothing like you remember, littered with bodies and burnt-out cars")
                    print("A couple houses on your street are burnt down completely, and in the distance more staggering figures can be seen...\n")
                    print("Parking the car and walking up to your house, you find the spare key under the mat")
                    print("Taking one last look around, it doesn't seem like you were followed")
                    print("After stepping inside you feel a little bit safer, but still on edge in this new world\n")

                    input("Press 1 to continue: ")
                    print(line_break)

                    print("You go to fill a glass of water, but the water's stopped and there's no electricity")
                    print("Checking through cabinets and cupboards, you try scrounge up what you can\n")
                    print("After checking the house you found:")
                    random_item(2, 3, "normal", "no fuel")

            elif home_choice == 2:
                print("The city streets are in chaos, but you have just enough fuel to get to the restaurant")
                print("Thankfully the area seems deserted, so you park your car and take a look\n")

                if character_type == "Survivor":
                    print("The door is unlocked, but the building seems to be empty as well")
                    print("It seems both customers and your coworkers alike fled to the quarantine zones")
                    print("After what you saw today, it seems unlikely any of them survived...")

                else:
                    print("Pushing the door, you're surprised to find it unlocked")
                    print("But the interior is a sharp contrast to what you remember from your visits before the apocalypse")
                    print("The once bustling and vibrant restaurant is still and quiet now, but it'll have to do...")

                input("\nPress 1 to continue: ")
                print(line_break)

                print("Now that you've escaped the fallen quarantine zone, you'll have to set up here\n")
                print("After grabbing a glass of water, you search the shelves and cabinets and find:")
                random_item(3, 5, "normal", "no fuel")

                if character_type == "Police Officer":
                    print("\nGrabbing your bag from the Police Cruiser, you check inside and find:")
                    add_nightstick()

                    print("(clothing) *police vest*")
                    add_item("(clothing) *police vest*")

            elif home_choice == 3:
                print("Deciding to head into the nearby forest, you keep driving until you enter a small clearing")
                print("It seems you've stumbled across a small campground you'll be able to stay at")
                print("With its isolated location and proximity to the city, it could be perfect...")

                input("\nPress 1 to continue: ")
                print(line_break)

                print("After parking your car you find a nearby spring to drink from, and begin taking a look around")
                print("Looks like whoever was here before you must have left in a hurry...\n")

                print("You do a quick sweep of the campground and find:")
                random_item(2, 3, "normal", "no fuel")

                if character_type == "Police Officer":
                    print("\nGrabbing your bag from the Police Cruiser, you check inside and find:")
                    add_nightstick()


                    print("(clothing) *police vest*")
                    add_item("(clothing) *police vest*")

            if character_type == "Firefighter":
                print("\nGrabbing your bag from the car, you check inside and find:")
                print("(weapon) *fire axe*")
                add_item("(weapon) *fire axe*")

            elif character_type == "Paramedic":
                print("\nGrabbing your bag from your car, you check inside and find:")
                random_item(2, 3, "normal", "meds")

            input("\nPress 1 to continue: ")
            print(line_break)

            check = open_inventory(rifle_supp, pistol_supp, total_armour)

            if check[0] == True:
                rifle_supp = True

            elif check[1] == True:
                pistol_supp = True
            
            total_armour = check[2]

            if character[0][0] < 100:
                heal(character_type)

            eat_food()

            print("You close your eyes and go to sleep")
            
            if character[7][0] != "house":
                log = "I survived my first day and set up at the " + character[7][0]

            else:
                log = "I survived my first day and set up at my " + character[7][0]
            journal_entry(day, log)

            input("\nPress 1 to continue to Day "  + str((day + 1)) + ": ")

            if character_type != "Patient":
                days_no_water = 0

            else:
                days_no_water = 3

    elif day > 1:
        count = 0
        character_rested = False
        card_list = []
        for i in range(4):
            suit = suits[count]
            for j in range(14):
                if j == 1:
                    card_list.append("ACE" + suit)

                elif j == 11:
                    card_list.append("KING" + suit)

                elif j == 12:
                    card_list.append("QUEEN" + suit)

                elif j == 13:
                    card_list.append("JACK" + suit)

                elif j != 0:
                    card_list.append(str(j) + suit)

            count += 1

        possible_locations = ["Military Base", "Fuel Depot", "Hospital", "Trader's Hideout"]
        water_drank = False
        print("You blink your eyes open and take a look around at your home at the",character[7][0])
        if character[7][0] == "campground clearing":
            print("You take a drink from the nearby spring")
            water_drank = True

        elif day == 2 and character[7][0] != "campground clearing" and character_type != "Patient":
            print("It looks like the electricity went out during the night, and the water's stopped too")

        if days_no_water == 0:
            character[1][0] = "Hydrated"

        elif days_no_water == 1:
            character[1][0] = "Thirsty"

        elif days_no_water == 2:
            character[1][0] = "Parched"

        elif days_no_water == 3:
            character[1][0] = "Dehydrated"

        elif days_no_water > 3:
            character[1][0] = "Severely Dehydrated"

        print("You feel", character[1][0])

        if len(character[6]) > 0:
            chances = len(character[6])
            chance_list = []

            for i in range(chances):
                item_chance = random.randint(1, 10)
                chance_list.append(item_chance)

            if 1 in chance_list:
                friend = character[6][random.randint(0, len(character[6]) - 1)]
                if len(friend) == 1:
                    friend_grammar = "friend"
                    print("\nIt looks like", friend[0], "visited while you were asleep!")
                    print("He left you:")

                else:
                    friend_grammar = "friends"
                    print("\nIt looks like " + friend[0] + " and " + friend[1] + " visited while you were asleep!")
                    print("They left you:")

                ranks = ["Corporal", "Sergeant", "Lieutenant", "Captain"]
                soldier = False

                for i in ranks:
                    if i in friend:
                        soldier = True

                if not soldier:
                    rarity_chance = random.randint(1,4)
                    random_item(2,3, "normal", "no rot")

                    if rarity_chance == 1:
                        random_item(0,1, "special")

                else:
                    bag_loot_normal = ["(ammo) *5 pistol bullets*", "(ammo) *3 pistol bullets*", "(meds) first aid kit"]
                    bag_loot_weapon = ["(weapon) quality machete", "(gun) *pistol*", "(weapon) *sledgehammer*", "(ammo) **15 rifle bullets**"]
                    bag_loot_armour = ["(clothing) *army helmet*", "(clothing) *combat pants*", "(clothing) *body armour*"]

                    chance = random.randint(1, 3)

                    if chance == 1:
                        item = bag_loot_normal[random.randint(0, len(bag_loot_normal) - 1)]

                    elif chance == 2:
                        item = bag_loot_weapon[random.randint(0, len(bag_loot_weapon) - 1)]

                    else:
                        item = bag_loot_armour[random.randint(0, len(bag_loot_armour) - 1)]

                    print(item)
                    add_item(item)

                if len(enemy_list) > 0:
                    print("\nBut it looks like someone else was here too")
                    print("They've left you a warning message...")
                    print("They weren't able to get you today with your", friend_grammar, "around, but they'll find you again soon...")

            if len(chickens) > 0:
                egg_chance = random.randint(1, 3)

                if egg_chance == 1:
                    if len(chickens) > 1:
                        hen = chickens[random.randint(0, len(chickens) - 1)]

                    else:
                        hen = chickens[0]

                    print("\nLooks like", hen, "laid an egg!")
                    add_item("(food) egg")
                    print("(food) egg has been added to your inventory")

        if character[9][0] == 1:
            print("\nYour car has 1 litre of fuel")

        else:
            print("\nYour car has", character[9][0], "litres of fuel")

        loop = True
        while loop:
            print("\nWhat will you choose to do today?\n1. Scavenge for supplies\n2. Explore\n3. Take some rest")
            choice = make_choice()
            if choice == 2 and len(afflictions) == 0:
                if character[9][0] < 5:
                    print("You don't have enough fuel to explore...")

                else:
                    loop = False

            else:
                loop = False

        if choice == 2 and len(afflictions) == 0:
            no_explore = False

            print("You decide to fuel up your car and explore")
            print("\nWhere will you travel to?")
            count = 1
            for i in explore_list:
                print(str(count) + ". " + i)
                count += 1
            print(str(count) + ". Exit")
            choice = make_choice()

            if choice != count:
                temp_location = explore_list[choice - 1]
                location = temp_location[0:-11]
                fuel_needed = int(explore_list[choice - 1][-9])

            else:
                fuel_needed = 0
                print("What will you choose to do today?\n1. Scavenge for supplies\n2. Take some rest")
                choice = make_choice()

                if choice == 2:
                    choice = 3

                no_explore = True

            while character[9][0] < fuel_needed:
                print("You don't have enough fuel to go this far...")
                print("\nWhere will you travel to?")
                count = 1
                for i in explore_list:
                    print(str(count) + ". " + i)
                    count += 1
                print(str(count) + ". Exit")
                choice = make_choice()

                if choice != count:
                    location = explore_list[choice - 1][0:-11]
                    fuel_needed = int(explore_list[choice - 1][-9])

                else:
                    print("What will you choose to do today?\n1. Scavenge for supplies\n2. Take some rest")
                    choice = make_choice()

                    if choice == 2:
                        choice = 3

                    no_explore = True

            if choice != count and not no_explore:
                result = True
                print("You decide to explore the", location)
                character[9][0] -= fuel_needed

                result = start_mission(location, temp_location, possible_locations, day, zombies_killed, water_drank, days_no_water, total_armour)

                if result[0] == False:
                    game = False

                else:
                    zombies_killed = result[1]
                    water_drank = result[2]
                    days_no_water = result[3]

            loop = False

        if choice == 1 and len(afflictions) == 0:
            area = areas[random.randint(0,len(areas)-1)]
            print("You decide to go scavenge in",area,"today\n")

            if day >= 14:
                chance = random.randint(1, 21)

            elif day >= 7:
                chance = random.randint(1, 19)

            else:
                chance = random.randint(1, 16)

            if len(latest_events) >= 14:
                latest_events.remove(latest_events[0])

            count = 50
            while chance in latest_events and count > 0:
                if day >= 14:
                    chance = random.randint(1, 21)

                elif day >= 7:
                    chance = random.randint(1, 19)

                else:
                    chance = random.randint(1, 16)
                count -= 1

            if chance < 19:
                latest_events.append(chance)

            if chance == 1:
                result = supply_crate_event(area, zombies_killed, character, day, total_armour)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 2:
                result = zombie_horde_event(area, zombies_killed, day)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 3:
                result = dead_survivor_event(area, zombies_killed, day)

                if result[0] == False:
                    game = False
            
                zombies_killed = result[1]

            elif chance == 4:
                result = unlooted_store_event(area, zombies_killed, character, day, bag_items)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 5:
                result = surrounded_van_event(area, zombies_killed, character, day, total_armour)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 6:
                blackjack_event(area, character, day)
                water_drank = True

            elif chance == 7:
                result = locked_safe_event(area, zombies_killed, character, day, total_armour)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 8 and day >= 7:
                result = survivor_footprints_event(area, zombies_killed, character, day, total_armour, character_type)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 9:
                result = workshop_event(area, zombies_killed, character, day, weapon_parts, workshop_event_played, workshop_satchel, total_armour)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]
                weapon_parts = result[2]
                workshop_satchel = result[3]

            elif chance == 10 and day >= 7:
                result = save_survivors_event(area, zombies_killed, character, day, bag_items)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif chance == 11 and day >= 14:
                event_chance = random.randint(1, 2)

                if event_chance == 1:
                    result = killer_within_event(area, zombies_killed, character, day, bag_items, total_armour, character_type)

                elif event_chance == 2:
                    event_chance = random.randint(1, 4)

                    if event_chance == 1:
                        result = zombie_patrol_event(area, character, zombies_killed, day)

                    else:
                        result = crumbling_bridge_event(area, character, zombies_killed, total_armour, day, character_type)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]
           
            elif chance == 12 and len(enemy_list) > 0:
                result = enemy_survivor_event(area, day, total_armour)

                if result == False:
                    game = False

            elif chance == 13:
                result = untouched_house_event(area, zombies_killed, character, day, character_type)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif chance == 14 and day >= 7:
                if rotten_food:
                    if first_hunt == True:
                        print("It's been", day, "days since the outbreak, and foods like chicken, apples and bread have rotted away")
                        print("If you want a solid supply of food, you'll have to go find it in the wild...\n")
                        first_hunt = False

                    chance = random.randint(1, 3)
                    if chance == 1:
                        print("You're heading towards", area, "when you see a path heading off into a wooded area")

                    elif chance == 2:
                        print("You're on your way to", area, "but you've spotted an interesting looking nature trail")

                    elif chance == 3:
                        print("While making your way towards", area, "you find yourself beside a large forest")

                    print("This could be a good opportunity to do some foraging, or even hunting!")
                    print("Will you:\n1. Investigate the forest trail\n2. Keep heading towards", area)
                    choice = make_choice()

                    if choice == 2:
                        print("Choosing to instead keep to your path, you walk on towards", area)

                else:
                    choice = 2
                    print("The weather is good today, and you decide to take a detour towards", area)

                if choice == 1:
                    result = hunt_or_forage_event(zombies_killed, character, day, total_armour)

                    if result[0] == False:
                        game = False
            
                    zombies_killed = result[1]

                elif choice == 2:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        result = loot_cars_event(zombies_killed, character, day, character_type)

                        if result[0] == False:
                            game = False

                    elif chance == 2:
                        result = group_loot_event(zombies_killed, character, day)

                        if result[0] == False:
                            game = False
            
                        zombies_killed = result[1]

            elif chance == 15 and day >= 7:
                item_check = False
                if len(character[3]) > 0:
                    item_check = True

                elif len(character[4]) > 1:
                    item_check = True

                elif len(character[5]) > 0:
                    item_check = True
                
                if item_check and len(bag_items) == 0:
                    if len(raider_bag_items) == 0:
                        result = thief_event(area, zombies_killed, character, day, item_check, total_armour, character_type)

                        if result[0] == False:
                            game = False
            
                        zombies_killed = result[1]
                        raider_has_bag = result[3]

                        if raider_has_bag:
                            bag_raiders = result[2]
                            raider_bag_items = result[4]
                            bag_items = []

                    else:
                        result = get_your_bag_event(area, character, day, raider_bag_items, bag_raiders, total_armour)

                        if result[0] == False:
                            game = False

                        raider_bag_items = []

                else:
                    free_supplies_event(area, day)

            elif chance == 16:
                result = unlooted_pharmacy_event(area, zombies_killed, character, day, character_type)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif chance == 17 and day >= 7:
                result = survivor_fuel_event(area, character, day, rot_day, zombies_killed, character_type)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]
                character[9][0] -= result[2]

            else:
                chance = random.randint(1, 20)
                
                if chance == 1:
                    print("As you journey towards", area, "you get an unsettling feeling in your gut")
                    print("You decide to tread carefully today, avoiding that area for now")
                    print("Better than to risk a fatal mistake")
                    print("Maybe tomorrow...")

                elif chance == 2:
                    print("It's too foggy to search for long, you can't risk a horde sneaking up on you")
                    print("Better safe than sorry...")

                elif chance == 3:
                    print("As you cross through a park on your way, you hear a horde nearby")
                    print("The sounds of moaning and shuffling remind you that your survival depends on more than just calories")
                    print("With that, your fear of being eaten beats out your hunger")
                    print("For now at least...")

                elif chance == 4:
                    print("One of your usual paths is a bridge across the nearby river, but it looks to have collapsed")
                    print("Upon closer inspection it seems someone blew it up during the night")
                    print("You're frustrated, but can't help but wonder what their motives were...")

                elif chance == 5:
                    survivor_num = random.randint(3, 15)
                    print("You've nearly reached", area, "when a group of", survivor_num, "raggedy survivors race out of a nearby building")
                    print("You duck into cover trying to remain unseen, just as they're cornered by a squad of soldiers in gas masks\n")
                    print("You're too far away to hear much but the survivors appear to be trying to reason")
                    print("Suddenly the leader of the soldiers barks an order, and his men raise their guns")
                    print("You watch in sudden horror as the survivors are gunned down in cold blood, and their bodies searched")
                    print("The soldiers set the corpses alight, and you use the distraction to make your escape...")

                elif chance == 6:
                    print("It rained heavily last night, and when you arrive at", area,"a flood has made the streets impassable")
                    print("Bodies float on the waters surface, and you don't even want to think about what lies below...")
                    print("You'll have to head home for today, but the flood should clear up soon")

                elif chance == 7:
                    zombies = random.randint(100,250)
                    print("As you leave the",character[7][0],"to head towards",area,"a huge horde of",zombies,"zombies walks in front of you")
                    print("You manage to avoid them and get away without being seen")
                    print("But you won't be able to scavenge in",area,"today")

                elif chance == 8:
                    print("As you're walking towards", area, "you hear hoots and shouting")
                    print("You dash to cover and a band of Raiders runs past")
                    print("It's a close call, and you can't risk scavenging out here today")
                    print("You'll have to head home and try tomorrow")

                elif chance == 9:
                    print("You round the corner towards", area, "but it looks like there's been a huge battle")
                    print("There are bodies strewn around, and the only movement comes from the hordes of undead scavengers")
                    print("You manage to stay out of sight, but you'll have to head home")

                elif chance == 10:
                    print("You arrive at", area, "with no hassle, but only because someone else beat you to it")
                    print("The promising area you marked on your map has already been looted")
                    print("It looks like it was recent enough, dead zombies lie here and there")
                    print("Doesn't look like they left anything interesting for you...")

                elif chance == 11:
                    print("You hear voices arguing up ahead, and while making sure to stay hidden, you take a look\n")
                    print("You peek over an overturned truck and see a two groups of Raiders arguing!")
                    print("It looks like they were waiting to ambush unsuspecting survivors, but couldn't decide who gets what")
                    print("You count yourself thankful for their incompetence, and head home")
                    
                elif chance == 12:
                    print("You're making your way down to", area, "when you hear gunfire ahead")
                    print("It continues briefly before stopping, but the damage has been done")
                    print("Dozens of zombies emerge from the streets around you, and you dive into cover")
                    print("Scavenging here is going to be a no-go today...")

                elif chance == 13:
                    print("You've nearly arrived at", area, "when you see smoke rising ahead...")
                    print("Deciding to check it out, you find a burning pile of dozens of bodies")
                    print("You're glad to see someone is sorting out all these zombies\n")
                    print("But as you make your way around, you realise not all of these bodies were undead")
                    print("One of the smouldering bodies on the edge of the pile is a survivor")
                    print("It looks like he was shot, and you make a quick exit")
                    print("\nOn your way home, you wonder what could have happened to him...")

                elif chance == 14:
                    print("You're on your way to", area, "when a chorus of shouts rings out")
                    print("You duck behind a billboard and watch a gang of Raiders descend on a group of zombies")
                    print("They're brutal fighters, and you find yourself learning new moves as you watch them")
                    print("\nThere's only one casualty on the Raider's side, and the zombies are dead")
                    print("With the action over, you stealthily creep away and head back to the", character[7][0])

                elif chance == 15:
                    chance = random.randint(1, 3)

                    if chance == 1:
                        print("RARE EVENT!\n")
                        print("You're walking up towards", area, "when a barricade in the street catches your eye")
                        soldier_num = random.randint(4, 10)
                        print("It's being patrolled by", soldier_num, "soldiers!")
                        print("Hopeful of some order being restored to society you creep closer, sticking to the shadows")
                        print("\nThe soldiers are wearing gas masks, and as you get near you begin to hear bits of conversation")
                        print("You're just about to reveal yourself when you hear an order from the soldier in command...")
                        print("He reminds his men to kill anything that moves, and putting aside your hopes, you head home")

                    else:
                        print("As you near", area,"the clouds above darken, and when you arrive it begins to pour rain")
                        print("You can barely see what's in front of you, and it'd be too dangerous to seek shelter")
                        print("You'll have to head back home for today...")

                elif chance == 16:
                    print("As you head down your usual road towards", area, "the smell of smoke drifts towards you")
                    print("You climb onto the roof of a smashed up store, and see a huge fire raging ahead")
                    print("The noise is drawing hundreds of zombies from all directions, you'll have to head home...")

                elif chance == 17:
                    print("You're checking around", area, "when you see signs leading to a fuel silo nearby")
                    print("You follow them for a few minutes, before finding the remains of the silo")
                    print("\nIt looks like the army lured a horde here before lighting the fuel on fire")
                    print("Ashen bones litter the wasteland, there's nothing here left to loot here")
                    print("Disappointed, you head back to the", character[7][0])

                elif chance == 18:
                    print("But something isn't right")
                    print("It feels like someone, or something is watching you...\n")

                    chance = random.randint(1, 3)

                    if chance == 1:
                        print("You keep walking straight, then dash off to the side")
                        print("Sprinting through sidestreets, you're taking a big risk, but your mind tells you it's the right decision")

                    elif chance == 2:
                        print("As you scavenge through some cars, you jump behind a van and run down a neighbouring alley")
                        print("You don't know what was watching you, but you've lost it")

                    else:
                        print("You keep moving towards your destination, when you feel a strange presence behind you")
                        print("Adrenaline fills your veins as you leap and jump over a fence, circling back down a different street")

                    print("As you head back to the", character[7][0], "you no longer feel that uneasy sensation...")

                elif chance == 19:
                    chance = random.randint(1, 3)
                    if chance == 1:
                        print("RARE EVENT!\n")
                        print("You've nearly reached", area, "and are taking a look around when a loud whir echoes through the streets")
                        print("It's a helicopter overhead!")
                        print("It's flying close to the ground but you can't make out the markings on the side")
                        print("\nBut it's not alone, it's being chased by hundreds of zombies!")
                        print("Thankfully they're too focused on the helicopter to notice you, and you're able to sneak away")
                        print("\nOn your way back home, you ponder who might have been flying, and where they were headed...")
                    
                    else:
                        print("You're close to", area, "when a sound stops you in your tracks")
                        print("Something is roaring up ahead, and screams echo through the streets")
                        print("Suddenly they're cut short, and you duck into cover as zombies lumber out of buildings and towards the noise")
                        print("You're not interested in whatever that was, and turn around to head back to the", character[7][0])

                elif chance == 20:
                    chance = random.randint(1, 3)

                    if chance == 1 and len(character[6]) > 0:
                        friends = character[6][random.randint(0, len(character[6]) - 1)]
                        friend1 = friends[0]
                        friend_count = 1

                        if len(friends) > 1:
                            friend2 = friends[1]
                            friend_count = 2

                        character[6].remove(friends)

                        print("RARE EVENT!\n")
                        print("You're on-route to your destination when you hear a commotion ahead")
                        print("You peek around some cars and spot a large group of Raiders")

                        if friend_count == 1:
                            print("You inch closer, and it looks like they have a human head on the end of a pike...")

                        else:
                            print("You inch closer, and it looks like they have two human head on the ends of pikes...")

                        print("Will you:\n1. Take a closer look\n2. Make a run for it")
                        choice = make_choice()

                        if choice == 1:
                            print("You sneak closer, moving between burnt out cars until you're close enough to see properly...\n")

                            if friend_count == 1:
                                print("It's", (friend1 + "'s"), "head on the pike")
                                print("Your friend", friend1, "is dead, killed by Raiders")

                                log = "Raiders killed my friend " + friend1
                                journal_entry(day, log)

                            else:
                                print("The heads belong to", friend1, "and", friend2)
                                print("The Raiders have killed your friends")

                                log = "Raiders killed my friends " + friend1 + " and " + friend2
                                journal_entry(day, log)

                            print("Shaking with rage, you hold yourself back")
                            print("There's no way you could take this many Raiders in a fight")
                            print("You walk home in the rain, plotting your revenge...")

                        else:
                            print("You don't risk the Raiders spotting you, not wanting to end up on a pike, so you make your exit")
                            print("As you walk home, you hope those heads didn't belong to anyone you knew...")

                            journal_entry(day, "Some Raiders had heads on pikes, hope it was nobody I knew")

                    else:
                        print("You're nearing", area, "when an eerie sight stops you in your tracks")
                        head_num = random.randint(3, 5)
                        print(head_num, "long wooden pikes stand upright in the center of the road, and each has a human head on top")
                        print("A gang of Raiders must have done this, looks like they're marking their territory")
                        print("You heed their warning, and head back home to the", character[7][0], "without scavenging...")

                filler_loot()

            if game:
                water_chance = random.randint(1,3)

                if water_chance == 1 and character[7][0] != "campground clearing":

                    if not water_drank:
                        print("\nYou find some water on your way home, enough for today")
                        water_drank = True

        elif choice == 3:
            count = 0
            medical_prompt = ""
            for i in afflictions:
                if count == 0:
                    medical_prompt += i

                elif count + 1 == len(afflictions):
                    medical_prompt += " and a " + i

                else:
                    medical_prompt += ", " + i

                    count += 1
            take_rest(medical_prompt)
            character_rested = True

        elif len(afflictions) > 0:
            count = 0
            medical_prompt = ""
            for i in afflictions:
                if count == 0:
                    medical_prompt += i

                elif count + 1 == len(afflictions):
                    medical_prompt += " and a " + i

                else:
                    medical_prompt += ", " + i

                    count += 1

            print("You wont be able to go out today because of your",medical_prompt)
            print("Will you?\n1. Take some rest")
            choice = make_choice()

            take_rest(medical_prompt)
            character_rested = True

        if game:
            print(line_break)

            count= 0
            medical_prompt= ""
            if len(afflictions) > 0 or character[0][0] < 100:
                if len(afflictions) > 0:
                    medical_prompt= "You have a "
                for i in afflictions:
                    if count == 0:
                        medical_prompt += i

                    elif count+1 == len(afflictions):
                        medical_prompt += " and a " + i

                    else:
                        medical_prompt += ", " + i

                    count += 1

                if medical_prompt != "":
                    print(medical_prompt)

                heal(character_type)

            damaged_weapon = False
            for i in range(len(weapon_durability)):
                if weapon_durability[i - 1] < max_weapon_durability[i - 1]:
                    damaged_weapon = True

            if damaged_weapon:
                print("Looks like one of your weapons is damaged")
                if len(weapon_durability) == 1 and weapon_parts == 0:
                    print("You'd better start looking for parts to repair it, or maybe a new weapon...\n")

                else:
                    count = 1
                    print("Will you:")
                    if weapon_parts > 0:
                        print(str(count) + ". Repair your weapon(s)")
                        count += 1

                    if len(weapon_durability) > 1:
                        print(str(count) + ". Scrap a weapon for parts")
                        count += 1

                    print(str(count) + ". Ignore")
                        
                    choice = make_choice()

                    if choice == 1 and weapon_parts > 0:
                        result = repair_weapon(weapon_parts)

                        weapon_parts = result

                    elif (choice == 2 and choice != count) or (weapon_parts == 0 and choice == 1):
                        scrap_loop = True

                        while scrap_loop:
                            result = scrap_weapon()
                            weapon_parts += result[1]

                            if not result[0]:
                                scrap_loop = False
                                count = 1
                                if weapon_parts > 0:
                                    print("Will you:")
                                    print(str(count) + ". Repair your weapon(s)")
                                    count += 1

                                    print(str(count) + ". Exit")
                                    choice = make_choice()

                                    if choice == 1: 
                                        result = repair_weapon(weapon_parts)

                                        weapon_parts = result           

            check = open_inventory(rifle_supp, pistol_supp, total_armour)

            if check[0] == True:
                rifle_supp = True

            elif check[1] == True:
                pistol_supp = True

            total_armour = check[2]
            
            if character_rested:
                eat_food(True)

            else:
                eat_food()

            if character[2][0] == 0:
                print("You are now starving")
                print("You have lost 5 HP, find some food soon...")
                character[0][0] -= 5
                if character[0][0] < 0:
                    character[0][0] = 0
                print("\nYou now have " + str(character[0][0]) + "/100 HP")

            if not water_drank:
                if character[1][0] == "Dehydrated":
                    print("\nYou are now dehydrated")
                    print("You have lost 10 HP, find some water soon...")
                    character[0][0] -= 10
                    if character[0][0] < 0:
                        character[0][0] = 0
                    print("\nYou now have " + str(character[0][0]) + "/100 HP")

                elif character[1][0] == "Severely Dehydrated":
                    print("\nYou are now severely dehydrated")
                    print("You have lost 20 HP, find some water URGENTLY...")
                    character[0][0] -= 20
                    if character[0][0] < 0:
                        character[0][0] = 0
                    print("\nYou now have " + str(character[0][0]) + "/100 HP")

            print("You close your eyes and go to sleep")
            input("\nPress 1 to continue to Day "  + str((day + 1)) + ": ")

            if character[0][0] == 0:
                print(line_break)
                print("Your body couldn't take it any more and in your sleep...\nYOU DIED")
                game= False

            elif character[2][0] >= 2000:
                if character[0][0] < 100:
                    hp_healed = random.randint(5, 20)

                    if character[0][0] + hp_healed > 100:
                        hp_healed = 100 - character[0][0]

                    print(line_break)
                    print("Overnight you heal", hp_healed, "HP")
                    character[0][0] = character[0][0] + hp_healed
                    if character[0][0] > 100:
                        character[0][0] = 100
                    print("You now have", character[0][0], "/100 HP")

            if not water_drank:
                days_no_water += 1

            else:
                days_no_water = 0

            loop = False

record = []
scoreboard = []
journal_list = []

record.append(username)
record.append(character_type)

if day < 1:
    day = 1

if day == 0:
    day = 1

record.append(day - 1)
record.append(zombies_killed)

with open("scores.csv", "a", newline = "") as score:
    add_score = csv.writer(score)
    add_score.writerow(record)

with open("journals.csv", "a", newline = "") as past_journal:
    add_past_journal = csv.writer(past_journal)

    if len(journal) == 0:
        journal.append("This journal is empty, nothing to read here...")
    add_past_journal.writerow(journal)

with open("scores.csv", "r") as prev_scores:
    read_scores = csv.reader(prev_scores)
    for row in read_scores:
        scoreboard.append(row)

with open("journals.csv", "r") as prev_journals:
    read_journals = csv.reader(prev_journals)
    count = 0
    for row in read_journals:
        if count != 0:
            journal_list.append(row)
        count += 1

scoreboard = scoreboard[1:]
scoreboard_unsorted = scoreboard.copy()

for i in range(1, len(scoreboard)):
    key = scoreboard[i]
    count = i - 1

    while count >= 0 and int(key[2]) > int(scoreboard[count][2]):
        scoreboard[count + 1] = scoreboard[count]
        count -= 1

    scoreboard[count + 1] = key

scoreboard = scoreboard[:11]

print()
print("{:-^63}".format("HIGH SCORES"))
print("{0:15} {1:15} {2:15} {3:15}".format("Player:", "Character:", "Days Survived:", "Zombies Killed:"))
for index, player in enumerate(scoreboard):
    print("{0:15} {1:15} {2:15} {3:15}".format(player[0], player[1], player[2], player[3]))
print("-" * 63)

print("Read a Past Journal?\n1. Yes\n2. No")
choice = make_choice()

if choice == 1:
    journal_loop = True

    while journal_loop:
        chosen_journal = input("Enter a player's name to read their journal: ")
        chosen_journal = chosen_journal.upper()

        found = False

        journal_num = 0
        for i in scoreboard_unsorted:
            if i[0].upper() == chosen_journal:
                found = True
                break
            else:
                journal_num += 1

        if not found:
            print("No journal found for that player...")

        else:
            journal = journal_list[journal_num]

            print(line_break)
            print(scoreboard_unsorted[journal_num][0] + "'s Journal:")

            for entry in journal:
                print(entry)

            if journal[0] != "This journal is empty, nothing to read here...":
                print("\n" + scoreboard_unsorted[journal_num][0] + " died on day " + str(int(scoreboard_unsorted[journal_num][2]) + 1) + " and the journal ends here...")
            print(line_break)

        print("Would you like to read another journal?\n1. Yes\n2. No")
        choice = make_choice()

        if choice == 2:
            journal_loop = False

print("Clear the Scoreboard?\n1. Yes\n2. No")
choice = make_choice()

if choice == 1:
    with open("scores.csv", "w", newline = "") as score:
        clear_score = csv.writer(score)
        clear_score.writerow(" ")

    with open("journals.csv", "w", newline = "") as prev_journals:
        clear_journals = csv.writer(prev_journals)
        clear_journals.writerow(" ")

    print("Scoreboard cleared")