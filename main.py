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

while username.upper() in username_list:
    print("That username is already taken\n")
    username = input("Enter your Username: ")

print("\nThis game is played with the number keys corresponding to each choice\n")
print("Are you ready to Try Survive?")
play = input("Click 1 to Play: ")

while play != "1":
    play = input("Click 1 to Play: ")

while game:
    if day == rot_day:
        rotten_food = True

        item_list.remove("(food) apple")
        item_list.remove("(food) chicken")
        item_list.remove("(food) bread")
        item_list.remove("(food) sausages")
        item_list.remove("(food) carrots")
        item_list.remove("(food) banana")
        item_list.remove("(food) strawberries")
        item_list.remove("(food) pre-made meal")

        for i in range(8):
            item_list.append("(food) rotten food")

    calories_used = 0
    day += 1
    print(line_break)
    print("Day",str(day))
    print(line_break)
    if day == 1:
        print("You're driving home from work when the radio is interrupted by an emergency broadcast")
        print("The government is warning of a disease which makes the dead come back to life and attack the living\n")
        print("You realise you need to find shelter")
        print("Will you:\n1. Make your way home, but closer to the city\n2. Get back to the restaurant you work at\n3. Drive to the forest nearby and camp out in your car")
        choice = make_choice()

        if choice == 1:
            character[7].append("house")

            print("The city is in chaos but you manage to get back to your house in one piece")
            print("You hurry inside, but it seems the fighting hasn't reached this area, yet...\n")

            print("You have a glass of water and then get to work")
            print("You do a quick sweep of your house and find:")
            random_item(3, 5, "normal")

        elif choice == 2:
            character[7].append("restaurant")

            print("The city is in chaos but you manage to get back to the restaurant in one piece")
            print("You hurry inside but it seems everyone else has left, you wonder if you'll ever see them again...\n")

            print("You do a quick sweep of the restaurant and find:")
            random_item(3, 5, "normal")

        elif choice == 3:
            character[7].append("campground clearing")

            print("You drive out into the forest and it seems everyone else is still in the city")
            print("You pull up to a campground in a clearing, this will do nicely...\n")

            print("You find a spring nearby and have some water")
            print("You do a quick sweep of the campground and find:")
            random_item(1, 3, "normal")

        print()
        eat_food()

        print("You close your eyes and go to sleep")
    
        log = "I survived my first day at the " + character[7][0]
        journal_entry(day, log)

        input("\nPress 1 to continue to Day "  + str((day + 1)) + ": ")
        days_no_water = 0

    elif day > 1:
        count = 0
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

        elif day == 2 and character[7][0] != "campground clearing":
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
            item_chance = random.randint(1,7)

            if item_chance == 1:
                friend = character[6][random.randint(0, len(character[6]) - 1)]
                if len(friend) == 1:
                    friend_grammar = "friend"
                    print("\nIt looks like", friend[0], "visited while you were asleep!")
                    print("He left you:")

                else:
                    friend_grammar = "friends"
                    print("\nIt looks like " + friend[0] + " and " + friend[1] + " visited while you were asleep!")
                    print("They left you:")

                rarity_chance = random.randint(1,8)
                random_item(1,3, "normal")

                if rarity_chance == 1:
                    random_item(1,2, "special")

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

                result = start_mission(location, temp_location, possible_locations, day, zombies_killed, water_drank, days_no_water)

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
            chance = random.randint(1, 23)

            if len(latest_events) >= 7:
                latest_events.remove(latest_events[0])

            count = 20
            while chance in latest_events and count > 0:
                chance = random.randint(1, 23)
                count -= 1

            if chance < 17:
                latest_events.append(chance)

            if chance == 1:
                result = supply_crate_event(area, zombies_killed, character, day)

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
                result = surrounded_van_event(area, zombies_killed, character, day)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 6:
                blackjack_event(area, character, day)

            elif chance == 7:
                result = locked_safe_event(area, zombies_killed, character, day)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 8:
                result = survivor_footprints_event(area, zombies_killed, character, day)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]

            elif chance == 9:
                result = workshop_event(area, zombies_killed, character, day, weapon_parts, workshop_event_played)

                if result[0] == False:
                    game = False
                
                zombies_killed = result[1]
                weapon_parts = result[2]

            elif chance == 10:
                result = save_survivors_event(area, zombies_killed, character, day, bag_items)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif chance == 11:
                result = killer_within_event(area, zombies_killed, character, day, bag_items)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]
           
            elif chance == 12 and len(enemy_list) > 0:
                result = enemy_survivor_event(area, day)

                if result == False:
                    game = False

            elif chance == 13:
                result = untouched_house_event(area, zombies_killed, character, day)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

            elif chance == 14:
                if day >= rot_day:
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
                    result = hunt_or_forage_event(zombies_killed, character, day)

                    if result[0] == False:
                        game = False
            
                    zombies_killed = result[1]

                elif choice == 2:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        result = loot_cars_event(zombies_killed, character, day)

                        if result[0] == False:
                            game = False

                    elif chance == 2:
                        result = group_loot_event(zombies_killed, character, day)

                        if result[0] == False:
                            game = False
            
                        zombies_killed = result[1]

            elif chance == 15:
                item_check = False
                if len(character[3]) > 0:
                    item_check = True

                elif len(character[4]) > 1:
                    item_check = True

                elif len(character[5]) > 0:
                    item_check = True
                
                if item_check and len(bag_items) == 0:
                    if len(raider_bag_items) == 0:
                        result = thief_event(area, zombies_killed, character, day, item_check)

                        if result[0] == False:
                            game = False
            
                        zombies_killed = result[1]
                        raider_has_bag = result[3]

                        if raider_has_bag:
                            bag_raiders = result[2]
                            raider_bag_items = result[4]
                            bag_items = []

                    else:
                        result = get_your_bag_event(area, character, day, raider_bag_items, bag_raiders)

                        if result[0] == False:
                            game = False

                        raider_bag_items = []

                else:
                    free_supplies_event(area, day)

            elif chance == 16:
                result = unlooted_pharmacy_event(area, zombies_killed, character, day)

                if result[0] == False:
                    game = False
        
                zombies_killed = result[1]

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

                if character[0][0] < 100 or len(afflictions) > 0:
                    print("You have", character[0][0], "HP")
                print("Would you like to heal your wounds?\n1. Yes\n2. No")
                choice = make_choice()

                if choice == 1:
                    if len(character[5]) > 0:
                        print("What do you need to heal?")
                        count= 1
                        for i in afflictions:
                            print(str(count) + ". " + i)
                            count += 1
                        if character[0][0] < 100:
                            print(str(count) + ". " + "HP at " + str(character[0][0]))

                        print(str(count + 1) + ". Don't heal anything")

                        heal_choice = make_choice()

                        if heal_choice != count + 1:
                            print("What item will you use?")
                            if heal_choice!= count or character[0][0] == 100:
                                count= 1
                                for i in character[5]:
                                    if i == "bandages":
                                        heal_chance= "75%"

                                    elif i == "first aid kit":
                                        heal_chance= "100%"

                                    elif i == "painkillers":
                                        heal_chance= "25%"
                                    print(str(count) + ". " + i + " - chance of healing " + heal_chance)
                                    count += 1

                                choice = make_choice()

                                if character[5][choice - 1] == "bandages":
                                    chance = random.randint(1, 4)
                                    print("Your", afflictions[heal_choice - 1], "has been bandaged")

                                    if chance != 1:
                                        print("Your",afflictions[heal_choice-1],"has been healed")
                                        afflictions.remove(afflictions[heal_choice - 1])

                                    else:
                                        print("Your", afflictions[heal_choice - 1], "hasn't healed")

                                elif character[5][choice - 1] == "painkillers":
                                    chance = random.randint(1, 4)
                                    print("You have taken some painkillers")

                                    if chance == 1:
                                        print("Your", afflictions[heal_choice - 1], "has been healed")
                                        afflictions.remove(afflictions[heal_choice - 1])

                                    else:
                                        print("Your", afflictions[heal_choice - 1], "hasn't healed")

                                elif character[5][choice - 1] == "first aid kit":
                                    print("Your", afflictions[heal_choice - 1], "has been treated with a first aid kit")

                                    print("Your", afflictions[heal_choice - 1], "has been healed")
                                    afflictions.remove(afflictions[heal_choice - 1])

                                character[5].remove(character[5][choice - 1])

                            else:
                                count = 0
                                for i in character[5]:
                                    count += 1
                                    if i == "bandages":
                                        hp_healed = 50

                                    elif i == "first aid kit":
                                        hp_healed = 100

                                    elif i == "painkillers":
                                        hp_healed = 25
                                    print(str(count) + ". " + i + " - HP healed: " + str(hp_healed))

                                choice = make_choice()

                                if character[5][choice-1] == "bandages":
                                    print("You have used some bandages")
                                    hp_healed = 50

                                elif character[5][choice-1] == "first aid kit":
                                    print("You have used a first aid kit")
                                    hp_healed = 100

                                elif character[5][choice-1] == "painkillers":
                                    print("You have taken some painkillers")
                                    hp_healed = 25

                                character[0][0] += hp_healed
                                if character[0][0] > 100:
                                    character[0][0] = 100
                                    print("You gained", hp_healed, "HP")

                                print("You now have " + str(character[0][0]) + "/100 HP")
                                character[5].remove(character[5][choice -1])
                            print()

                        else:
                            print("You chose not to heal anything\n")

                    else:
                        print("You don't have any medicine\n")

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

            if len(character[8]) > 0:
                print("Would you like to open your inventory?\n1. Yes\n2. No")
                choice = make_choice()
                if choice == 1:
                    loop = True
                    while loop:
                        if len(character[8]) > 0:
                            print("Click the corresponding number to select an item")
                            print("You have:")
                            count = 1
                            for i in character[8]:
                                print(str(count) + ". " + i)
                                count += 1
                            print(str(count) + ". " + "Exit")
                            choice = make_choice()

                            if choice != count:
                                item_chosen = character[8][choice - 1]
                                if item_chosen[0:2] == "(c":
                                    total_armour = equip_armour(item_chosen[11:],total_armour)

                                elif item_chosen == "journal":
                                    print("Important Events:")
                                    if len(journal) > 0:
                                        for entry in journal:
                                            print(entry)

                                    else:
                                        print("You haven't written anything in your journal yet")

                                elif item_chosen == "crafting recipes":
                                    crafting_recipes()

                                elif item_chosen == "(mod) **suppressor**":
                                    mod_options = []

                                    for weapon in character[4]:
                                        if weapon[0:3] == "**a" or weapon[0:3] == "*pi":
                                            mod_options.append(weapon)

                                    if len(mod_options) == 0:
                                        print("No guns in your inventory")

                                    else:
                                        print("Choose a weapon to add the suppressor to:")
                                        count = 1
                                        for i in mod_options:
                                            print(str(count) + ". " + i)
                                            count += 1
                                        print(str(count) + ". " + "Exit")
                                        choice = make_choice()

                                        if mod_options[choice -1] == "**assault rifle**":
                                            rifle_supp = True
                                            print("Your **assault rifle** is now suppressed")
                                        
                                        else:
                                            pistol_supp = True
                                            print("Your *pistol* is now suppressed")

                                        character[9].remove("(mod) **suppressor**")

                                print(line_break)

                            elif choice == count:
                                loop = False

                        else:
                            loop = False

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
                print("Your body couldn't take it any more and in your sleep...\nYOU DIED")
                game= False

            elif character[2][0] > 2000:
                if character[0][0] < 100:
                    hp_healed = random.randint(5, 20)

                    if character[0][0] + hp_healed > 100:
                        hp_healed = 100 - character[0][0]

                    print(line_break)
                    print("Overnight you heal", hp_healed, "HP")
                    print("You now have", character[0][0] + hp_healed, "/100 HP")

            if not water_drank:
                days_no_water += 1

            else:
                days_no_water = 0

            loop = False

record = []
scoreboard = []

record.append(username)
record.append(day - 1)
record.append(zombies_killed)

with open("scores.csv", "a", newline = "") as score:
    add_score = csv.writer(score)
    add_score.writerow(record)

with open("scores.csv", "r") as prev_scores:
    read_scores = csv.reader(prev_scores)
    for row in read_scores:
        scoreboard.append(row)

scoreboard = scoreboard[1:]

for i in range(1, len(scoreboard)):
    key = scoreboard[i]
    count = i - 1

    while count >= 0 and int(key[1]) > int(scoreboard[count][1]):
        scoreboard[count + 1] = scoreboard[count]
        count -= 1

    scoreboard[count + 1] = key

scoreboard = scoreboard[:11]

print()
print("{:-^46}".format("HIGH SCORES"))
print("{0:15}".format("Player:"), ("Days Survived:"), ("Zombies Killed:"))
for index, player in enumerate(scoreboard):
    print("{0:15}".format(player[0]), "{0:14}".format(player[1]), player[2])
print("-" * 46)

print("\nClear the Scoreboard?\n1. Yes\n2. No")
choice = make_choice()

if choice == 1:
    with open("scores.csv", "w", newline = "") as score:
        clear_score = csv.writer(score)
        clear_score.writerow(" ")

    print("Scoreboard cleared")