from functions import *

def crumbling_bridge_event(area, character, zombies_killed, total_armour, day):
    game = True
    soldier_name = None

    print("You're on your way towards", area, "when something catches your eye")
    print("Directly ahead of you is smoke rising into the air")
    print("\nIf there's a fire you won't be able to reach", area, "today, but it could be worth checking out...")

    print("Will you:\n1. Investigate the smoke\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("You decide to risk it and take a closer look")
        print("Getting closer, you step off the road and into the trees")
        print("Following the smoke, you emerge from the forest and find yourself in front of a large bridge\n")
        print("It rained heavily last night and the river churns below you")

        bridge_chance = random.randint(1, 4)
        print("Scanning for the fire you spot the source of the smoke\n")

        input("Press 1 to continue: ")
        print(line_break)

        if bridge_chance == 1:
            goal = "the crashed helicopter"
            print("It's a crashed helicopter!\n")
            print("Looks like it hit the bridge hard and it's starting to give way, it won't be long till the helicopter falls too")

        else:
            goal = "the lost convoy"
            print("It's a lost convoy!\n")
            print("It looks like they made their final stand here, but the bridge took some heavy damage")

        print("As you're standing there, a chunk of concrete crumbles and breaks away before disappearing in the rushing water\n")

        print("If you can get up there, you might be able to find some good loot, but it's risky")
        print("There's no telling what's waiting for you, and a fall into the river could be fatal...")
        print("Will you:\n1. Begin crossing the bridge\n2. Head home")
        choice = make_choice()

        if choice == 1:
            print("It's worth the risk, and you begin making your way across")

            bridge_length = random.randint(4, 5)
            step = 1
            crossing = True
            fall = False

            while crossing and step <= bridge_length and game and not fall:
                if step == 1:
                    fall_chance = 0
                    print("You take your first step onto the bridge but it seems this area is stable")

                    chance = random.randint(1, 2)

                    if chance == 1:
                        zom_num = 2
                        print("But you're not alone, and", zom_num, "zombies lurch out in front of you!")

                        result = fight(zom_num, "zombies")

                        if result:
                            print("With the zombies dead, you're free to continue")
                            zombies_killed += zom_num

                        else:
                            game = False

                    else:
                        print("Bodies and burnt out cars litter the area, you'll have to be careful")
                        print("There's no telling what might be waiting for you further up the bridge\n")

                elif step < 4:
                    print("Deciding to continue on, you push further up the bridge\n")
                    fall_chance = random.randint(1, 8)

                    if fall_chance == 1:
                        fall = True

                        print("But as you set your foot down, the ground gives way and you fall through!\n")
                        input("Press 1 to continue: ")
                        print(line_break)

                        print("Thankfully you don't fall far, but to your horror the bridge begins to collapse above")

                        if step == 3:
                            print("You run for safety, but you went too far along the bridge and a piece of rubble catches your shoulder\n")

                            print("You've injured your shoulder!")
                            print("\nYou have lost 30HP")
                            status = add_affliction("injured shoulder", 30)

                            if not status:
                                game = False

                            print("You've hurt yourself and with this side of the bridge down, you'll be heading home empty handed")

                            journal_entry(day, "Fell from a crumbling bridge and badly injured my shoulder")

                        else:
                            print("Diving at the last second, you manage to avoid the falling rubble\n")
                            print("But now this side of the bridge is down, looks like you'll be heading home empty handed")

                            journal_entry(day, "Fell from a crumbling bridge but managed to escape unscathed")

                        print("On your way back home you wonder what might have been up there waiting for you...")

                    else:
                        chance = random.randint(1, 3)

                        if chance == 1:
                            car_types = ["Sedan", "Hatchback", "Van", "Truck", "Convertible"]
                            car_colours = ["Red", "Blue", "Yellow", "White", "Black", "Silver", "Grey", "Green", "Navy","Brown"]

                            car = car_colours[random.randint(0, len(car_colours) - 1)] + " " + car_types[random.randint(0, len(car_types) - 1)]

                            if step == 2:
                                print("Most of the cars are burnt out and destroyed, but you spot a", car, "that seems relatively unscathed")

                            else:
                                print("Further up the bridge is in a bad state, but you spot a", car, "that seems mostly intact")

                            print("Deciding to check it out, you walk over to take a look\n")

                            chance = random.randint(1, 3)

                            if chance != 1:
                                locked_chance = random.randint(1, 2)

                                if locked_chance == 1:
                                    print("But it's locked")
                                    print("Will you:\n1. Smash a window\n2. Leave it alone")
                                    choice = make_choice()

                                    if choice == 1:
                                        chance = random.randint(1, 2)

                                        print("You check around for any zombies, before smashing the driver's window")

                                        if chance == 1:
                                            print("Luckily the sound didn't alert any zombies, and you're free to loot the car\n")

                                        else:
                                            zom_num = random.randint(2, 3)
                                            print("You go to loot the", car, "but", zom_num, "zombies emerge from behind it!\n")
                                            result = fight(zom_num, "zombies")

                                            if result:
                                                zombies_killed += zom_num
                                                print("With the zombies dead, you take one last look around before looting the car\n")

                                            else:
                                                game = False

                                        if game:
                                            loot_car(car)

                                    else:
                                        print("You won't risk smashing the glass and attracting attention")
                                        print("Maybe you'll try work your way up the bridge instead")

                                else:
                                    print("Looks like it's unlocked!\n")

                                    input("Press 1 to continue: ")
                                    print(line_break)
                                    loot_car(car)

                            else:
                                input("Press 1 to continue: ")
                                print(line_break)

                                print("But as you walk up to the", car, "you hear the barricade behind it creak and groan")
                                print("You jump back, and just in time as the concrete gives way and the car falls into the river below")
                                print("Hopefully there's better stuff further up the bridge")

                        elif chance == 2:
                            print("Burned corpses litter the bridge, but you spot a ragged backpack hidden under some rubble\n")
                            print("You dig it out and inside you find:")
                            random_item(2, 3, "normal", "no fuel")

                            input("\nPress 1 to continue: ")
                            print(line_break)

                            print("Quickly checking around, there doesn't seem to be anything else left here")
                            print("You hope there's better stuff further up the bridge")

                        else:
                            chance = random.randint(1, 2)

                            if chance == 1:
                                zom_num = random.randint(3, 4)

                                if step == 2:
                                    print("You haven't walked much further up the bridge when a zombie lunges out from behind a car!\n")
                                    print("Barely avoiding it, you turn to see", zom_num - 1, "more zombies have circled behind you")

                                else:
                                    print("This bit of the bridge obviously saw a lot of action, and you hear something moving behind the wreckage of a bus")
                                    print("Taking a look, you see", zom_num, "zombies waiting for you!\n")

                                result = fight(zom_num, "zombies")

                                if result:
                                    print("With the zombies dead, you're free to continue up the bridge")
                                    zombies_killed += zom_num

                                else:
                                    game = False

                            else:
                                print("The bridge creaks and groans but the surface under your feet holds")
                                print("For now...")

                elif step == 4:
                    fall_chance = random.randint(1, 7)

                    if fall_chance == 1:
                        fall = True

                        print("But as you set your foot down, the ground gives way and you fall through!\n")
                        input("Press 1 to continue: ")
                        print(line_break)
                        chance = random.randint(1, 4)

                        print("The cold water is like ice in your veins, and you desperately thrash to the surface")

                        if chance == 1:
                            print("As you gasp for air you open your eyes to see the bridge collapse, concrete chunks raining down\n")
                            print("You claw desperately at the water, but it's no use")
                            print("Crushed under the debris you're dragged to the riverbed, never to be seen again...\nYOU DIED")

                            game = False

                        else:
                            print("As the bridge collapses above you, somehow you manage to swim to the shore")
                            print("Gasping for air, you seem to have escaped intact\n")
                            if len(character[4]) > 1:
                                lost_weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                print("But in the process you lost your",lost_weapon)
                                remove_item("(weapon) " + lost_weapon)

                                log = "Fell from a crumbling bridge and lost my " + lost_weapon
                                journal_entry(day, log)

                            else:
                                journal_entry(day, "Fell from a crumbling bridge but somehow managed to swim to safety")

                            print("Now this side of the bridge is down, looks like you'll be heading home empty handed\n")
                            print("On your way back home you wonder what might have been up there waiting for you...")
                    
                    else:
                        chance = random.randint(1, 2)

                        if chance == 1:
                            zom_num = random.randint(3, 4)

                            print("You're nearing the end of the bridge when", zom_num, "military zombies shamble out from behind a truck!")

                            if goal == "the lost convoy":
                                print("These must have been soldiers from the lost convoy!")

                            else:
                                print("You wonder if they had anything to do with the crashed helicopter")

                            print("There's nowhere to run, you'll have to fight!\n")

                            result = fight(zom_num, "military zombies")

                            if result:
                                print("With the undead soldiers defeated, you're free to continue up the bridge")

                            else:
                                game = False

                        elif chance == 2:
                            if goal == "the lost convoy":
                                print("You're getting closer to the lost convoy when something catches your eye")

                            else:
                                print("You're getting closer to the crashed helicopter when you spot something, or someone...")

                            print("It's a dead survivor, or what's left of him")
                            print("A horde must have come through here and taken him by surprise, but his backpack is still caught underneath a car\n")

                            input("Press 1 to continue: ")
                            print(line_break)

                            print("Pulling it out and checking inside, you find:")
                            random_item(3, 5, "normal")

                            print("\nAfter checking through the bag you continue up the bridge")

                elif step == 5:
                    fall_chance = random.randint(1, 6)

                    if fall_chance == 1:
                        fall = True

                        chance = random.randint(1, 3)
                        print("You've almost made it when the ground underneath you cracks and your heart drops")

                        if chance == 1:
                            print("Suddenly the concrete gives way and you fall straight through!\n")

                            input("Press 1 to continue: ")
                            print(line_break)

                            print("Trying desperately to grab onto something, you hit off a pillar and your vision goes black\n")
                            print("When you wake, pain shoots through your body, and you look down to see a piece of rebar skewering your torso")
                            print("Looking up, a slab of concrete tumbles down from the bridge straight towards you")
                            print("\nClosing your eyes you accept your fate and-\nYOU DIED")

                            game = False
                        
                        else:
                            print("You try to run back to safety, but it's too late!\n")

                            input("Press 1 to continue: ")
                            print(line_break)

                            print("The bridge begins to collapse around you, and you're dragged down with it")
                            print("Crashing into the river, the water churns around you and you're dragged under")
                            print("Somehow dodging falling debris, you make it to shore\n")

                            if len(character[4]) > 1:
                                lost_weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                remove_item(lost_weapon)
                                print("But when you check your bag, not everything is there")
                                print("Looks like you lost your", lost_weapon, "but at least you're alive\n")

                                log = "Fell from a crumbling bridge and lost my " + lost_weapon
                                journal_entry(day, log)

                            else:
                                journal_entry(day, "Fell from a crumbling bridge but somehow managed to swim to safety")

                            print("But with this side of the bridge down, it looks like you'll be heading home empty handed")
                            print("On your way back home you wonder what might have been up there waiting for you...")

                    else:
                        chance = random.randint(1, 4)

                        if chance == 1 or chance == 2:
                            chance = random.randint(1, 2)

                            car1 = car_colours[random.randint(0, len(car_colours) - 1)] + " " + car_types[random.randint(0, len(car_types) - 1)]
                            car2 = "Police Cruiser"

                            car_chance = random.randint(1, 5)

                            if car_chance == 1:
                                car = car1
                            
                            else:
                                car = car2

                            print("You're getting close now, and you spot a", car, "crashed into the barricades")
                            print("It seems to still be in one piece")

                            if chance == 1 or chance == 2:

                                locked_chance = random.randint(1, 2)

                                if locked_chance == 1:
                                    print("But it's locked")
                                    print("Will you:\n1. Smash a window\n2. Leave it alone")
                                    choice = make_choice()

                                    if choice == 1:
                                        chance = random.randint(1, 2)

                                        print("You check around for any zombies, before smashing the driver's window")

                                        if chance == 1:
                                            print("Luckily the sound didn't alert any zombies, and you're free to loot the car\n")

                                        else:
                                            zom_num = random.randint(2, 3)
                                            print("You go to loot the", car, "but", zom_num, "zombies emerge from behind it!\n")
                                            result = fight(zom_num, "zombies")

                                            if result:
                                                zombies_killed += zom_num
                                                print("With the zombies dead, you take one last look around before looting the car\n")

                                            else:
                                                game = False

                                        if game:
                                            loot_car(car)

                                    else:
                                        print("You won't risk smashing the glass and attracting attention")
                                        print("Maybe you'll try work your way up the bridge instead")

                                else:
                                    print("Looks like it's unlocked!\n")
                                    loot_car(car)

                            else:
                                print("But as you walk up to the", car, "you hear the barricade behind it creak and groan")
                                print("You jump back, and just in time as the concrete gives way and the car falls into the river below")

                        elif chance == 3:
                            print("You're almost there when you spot someone lying propped up against the barricades")
                            print("It's a dead survivor!")

                            print("Will you:\n1. Approach him\n2. Leave him be")
                            choice = make_choice()

                            if choice == 1:
                                print("Choosing to take a closer look, you approach the survivor's body")

                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("But suddenly the dead survivor lurches to his feet!")
                                    print("He must have been bit!\n")

                                    result = fight(1, "zombies")

                                    if result:
                                        print("Finally put to rest the zombie topples over the barricades and into the river below")
                                        zombies_killed += 1

                                        loot_chance = random.randint(1, 2)

                                        if loot_chance == 1:
                                            print("Checking around, you find his bag stashed under a car nearby")
                                            print("Inside you find:")
                                            random_item(2, 3, "normal")
                                            random_item(0, 1, "special")
                                            print()

                                        else:
                                            print("You check around but there doesn't seem to be anything else here")

                                    else:
                                        game = False

                                else:
                                    print("You approach the survivor's body, but he doesn't stir")
                                    print("Checking around, you find his bag stashed under a car nearby")
                                    print("Inside you find:")
                                    random_item(2, 3, "normal")
                                    random_item(0, 1, "special")
                                    print("\nYou wonder what happened to him, before heading on your way")

                            else:
                                print("You decide not to risk it and leave the body alone...")

                        else:
                            print("The cars are densely packed here, and it's hard to see through the wreckage")
                            print("Taking a look around you spot a path, but it's blocked by another human!")
                            print("You squint but can't make out his face, right as he charges towards you!\n")

                            input("Press 1 to continue: ")
                            print(line_break)

                            if len(enemy_list) > 0:
                                enemy_name = enemy_list[random.randint(0, len(enemy_list) - 1)]
                                enemy_list.remove(enemy_name)

                                if len(enemy_name) == 1:
                                    if enemy_name[0] in killer_list:
                                        killer_list.remove(enemy_name[0])
                                        print("It's the killer", enemy_name[0], "he's tracked you down!")
                                        print("This time you won't be able to escape...")

                                    else:
                                        print("It's", enemy_name[0], "back for revenge!")
                                        print("He glowers at you, and promises to punish you for what you did")

                                else:
                                    print("It's", enemy_name[0], "back for revenge!")
                                    print("He snarls, promising revenge for the death of his friend", enemy_name[1])
                            
                                print()
                                result = fight(1, "humans", enemy_name[0], total_armour)

                                if result:
                                    print("With", enemy_name[0], "dead, you can squeeze past the cars and continue up the bridge")

                                    if enemy_name[0] not in killer_list:
                                        print("You'll be thinking twice before you mess with a survivor again...")

                                    combat_heal()

                                else:
                                    game = False

                            else:
                                print("It's a raider and he's here to fight!\n")

                                result = fight(1, "humans", None, total_armour)

                                if result:
                                    print("With the raider dead, you're able to squeeze past the cars and continue up the bridge")

                                    combat_heal()

                                else:
                                    game = False

                if not fall and game and step <= bridge_length:
                    print("Will you:\n1. Continue up the bridge\n2. Head home")
                    choice = make_choice()

                    if choice == 2:
                        print("Deciding against reaching", goal, "you head back home instead")
                        crossing = False

                        log = "Explored a crumbling bridge but I couldn't reach " + goal
                        journal_entry(day, log)

                    else:
                        step += 1

            if crossing and game and not fall:
                print("Looks like you've made it to", goal)
                print()

                if goal == "the crashed helicopter":
                    print("It's in bad shape, and the bridge underneath is starting to give way")
                    
                    ranks = ["Corporal", "Sergeant", "Lieutenant", "Captain"]
                    name = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                    soldier_name = ranks[random.randint(0, len(ranks) - 1)] + " " + name

                    print("But it looks like there's someone moving around inside!")
                    print("Pulling the door open, you take a look within\n")

                    input("Press 1 to continue: ")
                    print(line_break)
                    
                    print("It must have been a hard landing, but one soldier is still alive!")
                    print("He's been cut up badly in the crash, but he's still breathing")
                    print("The frame of the helicopter groans and the bridge beneath begins to crack, you won't have long...")
                    print("Will you:\n1. Help him\n2. Leave him for dead and loot the helicopter")
                    choice = make_choice()

                    if choice == 1:
                        print("Deciding to help the soldier, you climb through the wreckage to his aid")
                        print("He blinks his eyes open and doesn't attack, introducing himself as", soldier_name)
                        print("The two of you are able to escape the helicopter, but it's clear he won't be able to go much further without help\n")

                        input("Press 1 to continue: ")
                        print(line_break)

                        if len(character[5]) > 0:
                            print("Will you:\n1. Give him some medical supplies\n2. Tell him you can't help")
                            choice = make_choice()

                            if choice == 1:
                                print("You've gotten this far, you can't leave him now")
                                print("Click the corresponding button to select an item")
                                print("You have:")
                                count = 1
                                for i in character[5]:
                                    print(str(count) + ". " + i)
                                    count += 1
                                choice = make_choice()
                                chosen_meds = character[5][choice - 1]
                                print("You give him", chosen_meds)
                                character[5].remove(chosen_meds)

                                if chosen_meds == "painkillers":
                                    print("He swallows the painkillers and thanks you, but he needs more help")
                                    print("Pointing back towards the helicopter, he tells you there's a first aid kit inside")
                                    print("You check, and sure enough there's one in his bag\n")

                                print("After bandaging him up, he thanks you and asks if anyone else survived")
                                print("You tell him he's the only one left, and he nods solemnly")
                                print("But you've saved his life today and he owes you his life\n")

                                input("Press 1 to continue: ")
                                print(line_break)

                                print("Thanking you for your help he offers you a (food) MRE")
                                add_item("(food) MRE")
                                print("You take it gratefully and toss it in your bag\n")

                                print("He turns back towards the wreckage, right as the bridge beneath gives way")
                                print("The pair of you manage to jump back, and make it back to the road unscathed")
                                print("Wishing you well", soldier_name, "promises to help you again someday before he heads off")

                                survivor_group = [soldier_name]
                                character[6].append(survivor_group)

                                print(soldier_name, "is now your friend\n")

                                print("Heading back to the", character[7][0], "you wonder if today's decision will pay off in the future...")
                                journal_entry(day, "Found a crashed helicopter and saved a soldier who promised to repay me")

                            else:
                                print("You tell him you don't have any medicine and he nods")
                                print("It seems this was his final mission, and he asks you to leave him here to rest")
                                print("Before you can respond, the bridge gives way and the helicopter falls into the river below\n")

                                print(soldier_name, "thanks you for at least rescuing him, before leaning against a car to rest")
                                print("Knowing you could have saved him, you leave him to his fate and head back to the", character[7][0])

                                journal_entry(day, "Found a crashed helicopter but chose not to give medicine to the surviving soldier")

                        else:
                            print("You don't have any medical supplies to help him and you tell him this")
                            print("He nods and thinks for a second before telling you to check the helicopter")
                            print("Will you:\n1. Check the helicopter\n2. Tell him you can't help")
                            choice = make_choice()

                            if choice == 1:
                                print("You've gotten this far, you can't leave him now")

                                chance = random.randint(1, 3)

                                if chance != 1:
                                    print("Checking inside, you can't see much and decide to check the cockpit")
                                    print("Looking around, you hear a shuffling noise behind you\n")
                                    print("Turning your head you see the furious eyes of an undead pilot!")
                                    print("He must have turned and caused the helicopter to crash!\n")

                                    result = fight(1, "military zombies")

                                    if result:
                                        zombies_killed += 1
                                        print("With the pilot put to rest, you check the cockpit and find a first aid kit")
                                        print("Carefully navigating your way back out to", soldier_name, "he thanks you and patches himself up")

                                        print("He goes to get up, but the bridge beneath the helicopter gives way and you both scramble for safety\n")
                                        print("Making it to safer ground, you head back to the road\n")

                                        print("Wishing you well", soldier_name, "promises to help you again someday before he heads off")

                                        survivor_group = [soldier_name]
                                        character[6].append(survivor_group)

                                        print(soldier_name, "is now your friend\n")

                                        print("Heading back to the", character[7][0], "you wonder if today's decision will pay off in the future...")
                                        journal_entry(day, "Found a crashed helicopter and saved a soldier who promised to repay me")

                                    else:
                                        game = False

                                else:
                                    print("The wreckage creaks as you duck inside, and you get an uneasy feeling in your gut")
                                    print("You begin to search around, and find a relatively intact first aid kit under one of the seats\n")

                                    print("But as you climb back towards the door, the ground underneath the helicopter gives way!")

                                    input("Press 1 to continue: ")
                                    print(line_break)
                                    print("Desperately scrambling towards the exit, you leap out but hit your head hard on the door!")
                                    print("Tumbling off the side of the bridge", soldier_name, "manages to grab you and pull you back up\n")
                                    
                                    print("You've hit your head and cut it open!")
                                    print("\nYou have lost 40HP")
                                    status = add_affliction("laceration on your head", 40)

                                    if not status:
                                        game = False
                                        print("YOU DIED")
                                    
                                    if game:
                                        print("Now it seems both of you will be needing the first aid kit...")
                                        print("Will you:\n1. Give the badly injured soldier the medkit\n2. Keep it for yourself")
                                        choice = make_choice()

                                        if choice == 1:
                                            print(soldier_name, "needs it more than you do, and you hand it over")
                                            print("Acknowledging what you've done for him, he shakes your hand and thanks you\n")

                                            print("Reaching into his pocket he offers you a (food) MRE")
                                            add_item("(food) MRE")
                                            print("You take it gratefully and toss it in your bag\n")

                                            print("The two of you head back to the main road, and before he leaves he promises to repay you someday\n")

                                            survivor_group = [soldier_name]
                                            character[6].append(survivor_group)

                                            print(soldier_name, "is now your friend\n")

                                            print("Heading back to the", character[7][0], "you wonder if today's decision will pay off in the future...")
                                            journal_entry(day, "Found a crashed helicopter and saved a soldier who promised to repay me")

                                        else:
                                            print("He helps you up and goes to ask for the medkit and you pull it away")
                                            print(soldier_name, "looks at you confused for a second, before he sees your head and his eyes narrow\n")

                                            print("But he's in no state to fight, and he instead struggles to his feet and limps away")
                                            print("Before he leaves, he turns and tells you you'll regret this someday...\n")

                                            print("On your way home, you wonder if you'll be seeing him again...")
                                            journal_entry(day, "Found a crashed helicopter and made a potential enemy")

                                            chance = random.randint(1, 3)

                                            if chance != 1:
                                                zombie_survivor = [soldier_name]
                                                zombie_survivors.append(zombie_survivor)

                                            else:
                                                enemy_group = [soldier_name]
                                                enemy_list.append(enemy_group)
                            
                            else:
                                print("You tell him you won't risk it and he slumps against a car and mutters something under his breath")
                                print("He clearly doesn't think much of you, but at least you rescued him from the helicopter")
                                print("You go to say something, but he waves you away with his hand and struggles to his feet\n")

                                print("It's clear he no longer wants anything to do with you, and he limps away as you head back to the road")
                                print("Feeling cowardly for not helping him, you head back to the", character[7][0], "wondering if you made the right choice...")

                                journal_entry(day, "Could've helped a soldier but decided not to risk it")

                    else:
                        print("This is a new world, and not everyone can be saved")
                        print("You decide against helping the soldier, and instead start taking a look around for anything useful")

                        chance = random.randint(1, 3)

                        if chance != 1:
                            print("Searching around in the destroyed helicopter, you squint your eyes as you scan for anything valuable\n")
                            print("Spotting a rucksack near the injured soldier and climb over to take a closer look\n")

                            input("Press 1 to continue: ")
                            print(line_break)
                            print("The bag is labeled 'Property of " + soldier_name + "' and as you read it aloud the soldier stirs")
                            print("It must have been his, and inside you find:")

                            bag_loot_normal = ["(food) MRE", "(ammo) *5 pistol bullets*", "(ammo) *3 pistol bullets*", "(fuel) 1 litre of fuel", "(food) protein bar", "(meds) first aid kit"]
                            bag_loot_weapon = ["(weapon) quality machete", "(weapon) hammer", "(gun) *pistol*", "(weapon) *sledgehammer*", "(ammo) **15 rifle bullets**"]
                            bag_loot_armour = ["(clothing) *army helmet*", "(clothing) *leather jacket*", "(clothing) *combat pants*", "(clothing) *body armour*"]

                            loot_taken = []

                            loot_amount = random.randint(2, 3)
                            for i in range(loot_amount):
                                loot = bag_loot_normal[random.randint(0, len(bag_loot_normal) - 1)]
                                print(loot)
                                add_item(loot)
                                loot_taken.append(loot)

                            chance = random.randint(1, 2)

                            if chance == 1:
                                loot = bag_loot_weapon[random.randint(0, len(bag_loot_weapon) - 1)]
                                print(loot)
                                add_item(loot)

                            else:
                                loot = bag_loot_armour[random.randint(0, len(bag_loot_armour) - 1)]
                                print(loot)
                                add_item(loot)

                            print("\nAfter filling your bag, you turn back to leave the helicopter")

                            if "(meds) first aid kit" in loot_taken:
                                print("But as you pass the injured soldier, he grunts and reaches out towards you")
                                print("He saw you take the first aid kit from his bag and he needs it badly")
                                print("Will you:\n1. Give him the medicine\n2. Keep it for yourself")
                                choice = make_choice()

                                if choice == 1:
                                    print("Faced with this life or death decision, you decide to help another person in need")
                                    print("It may be the apocalypse, but you'll hold onto your humanity in a world of undead")
                                    print("Helping him up, the pair of you leave the helicopter and he sits down to patch himself up\n")
                                    print("He doesn't say a word about the rest of his stuff you took, and instead offers you a silent nod before you head on your way")

                                    journal_entry(day, "Stole some supplies from a crashed helicopter but rescued a soldier in the process")

                                else:
                                    print("But you didn't come here to save him, and now you have everything you need")
                                    print("Looking at him coldly, you feel no remorse as you leave him behind")
                                    print("You exit the wreckage and head back towards the road, hearing the bridge groan behind you")
                                    print("\nIt won't be long till he meets his end in the river below...")

                                    journal_entry(day, "Stole from a crashed helicopter and left a surviving soldier for dead")

                            else:
                                print("The soldier doesn't stir as you leave, and part of you is glad you won't have to look him in the eyes")
                                print("\nAs you step out onto the bridge, the wreckage creaks behind you and the ground begins to split")
                                print("You run and leap forwards, managing to make it to safety but when you look back the helicopter is gone...")

                                journal_entry(day, "Looted a crashed helicopter and left a surviving soldier for dead")

                            print("\nHeading back to the", character[7][0], "you think long and hard about the decisions you made today...")

                        else:
                            print("Dangling wires fizz and broken glass cracks under your feet as you search the wreckage\n")
                            print("You spot a rucksack near the far end of the helicopter and begin to climb over")
                            print("But a sudden creaking groan from underneath you makes you stop in your tracks...")
                            print("The bridge is starting to give way!\n")
                            
                            input("Press 1 to continue: ")
                            print(line_break)
                            print("Desperately scrambling towards the exit, you leap out but hit your head hard on the door!")
                            print("Tumbling off the side of the bridge you manage to grab a piece of rebar and pull yourself back up")
                            
                            print("You've hit your head and cut it open!")
                            print("\nYou have lost 30HP")
                            status = add_affliction("laceration on your head", 30)

                            if not status:
                                game = False
                                print("YOU DIED")
                            
                            if game:
                                print("You've narrowly escaped, but now there's no soldier and no helicopter...")
                                print("With more of the bridge crumbling into the river, you have no choice but to head back home")
                                print("\nHeading back to the", character[7][0], "you think long and hard about the decisions you made today...")

                                journal_entry(day, "Tried to steal from a crashed helicopter but nearly died when it fell into the river")

                elif goal == "the lost convoy":
                    if day < 7:
                        print("They must have set out right as the quarantine zones collapsed")

                    elif day < 14:
                        print("They must have been fleeing a quarantine zone and ended up here")

                    elif day < 28:
                        print("They must have been survivors from the military guarding the quarantine zones")

                    else:
                        print("They survived the outbreak and collapse of the quarantine zones just to end up here...")

                    truck_num = random.randint(5, 7)

                    print("It looks like they met some fierce opposition on this road")
                    print("None of the", truck_num, "trucks seem to have made it through\n")

                    print("But you're not here to reminisce about the past, you're here for what's inside")
                    print("Creeping through the burnt-out battleground, you spot the first truck still in okay shape")

                    truck_type = random.randint(1, 2)

                    if truck_type == 1:
                        print("It has a medical insignia on the side")

                    else:
                        print("It looks like it was carrying food and supplies")

                    zombie_chance = random.randint(1, 2)

                    print("Will you:\n1. Loot the truck\n2. Keep searching")
                    truck_choice = make_choice()

                    if truck_choice == 1:
                        print("Choosing to loot the supply truck, you approach to take a closer look")
                        print("There's a dead soldier slumped over the wheel, but he's been shot in the head")
                        print("Wondering what happened here, you pull the two back doors open\n")
                        input("Press 1 to continue: ")
                        print(line_break)
                        if zombie_chance == 1:
                            zom_num = random.randint(2, 3)
                            print("Only to be face-to-face with", zom_num, "undead soldiers!\n")

                            result = fight(zom_num, "military zombies")

                            if result:
                                print("The zombies lie dead at your feet, but it seems they didn't manage to get into the supplies\n")
                                print("They've still made a mess of the interior, but you manage to find:")

                                if truck_type == 1:
                                    random_item(2, (truck_num - 1), "normal", "meds")

                                else:
                                    random_item(4, (truck_num + 1), "normal", "no rot")

                            else:
                                game = False

                        else:
                            print("But there's no one inside")
                            print("It looks like the truck took a hard hit, the side is crumpled in and the interior is a mess\n")
                            print("You take a look around and manage to find:")

                            if truck_type == 1:
                                random_item(2, (truck_num - 1), "normal", "meds")

                            else:
                                random_item(4, (truck_num), "normal", "no rot")
                    
                    else:
                        print("You decide you'll keep searching, and walk past this truck")

                    if game:
                        if truck_choice == 1:
                            print("\nStepping out of the truck with the loot in your bag, you check your surroundings")

                        print("You're halfway through the convoy now, and you assess the situation")
                        print("Will you:\n1. Take a look at the rear of the convoy\n2. Head back home")
                        choice = make_choice()

                        if choice == 1:
                            print("Deciding to see what awaits you at the end, you head onwards")
                            print("Creeping around the back of a wrecked truck, you spot what you came here for")
                            print("At the very back of the convoy is a larger, more armoured truck with a national guard insignia\n")
                            print("It's not clear what's inside, but it must be good\n")
                            input("Press 1 to continue: ")
                            print(line_break)

                            chance = random.randint(1, 3)

                            if chance != 1:
                                print("You creep closer, but suddenly two survivors run out from behind the truck!")
                                print("A zombie careers after them, but a single hit from a survivor kills it instantly")
                                print("It looks like these guys are good fighters...\n")
                                print("You watch from behind cover as they dispatch 4 more, and the threat is gone")
                                print("Will you:\n1. Approach them\n2. Leave them to loot the truck")
                                choice = make_choice()

                                if choice == 1:
                                    survivor = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]
                                    survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                                    while survivor == survivor2:
                                        survivor2 = survivors_male_list[random.randint(0, len(survivors_male_list) - 1)]

                                    print("Choosing to approach, you spin around as you come closer")
                                    print("Weapons drawn, they eye you cautiously before lowering their weapons")
                                    print("You introduce yourself, and they tell you their names are", survivor, "and", survivor2)
                                    print("\nThey explain they came here same as you, looking for loot")
                                    print("Peering over your shoulder", survivor2, "remarks on how you seem to have gone the hard way")
                                    print("Seeming to recognise your skill,", survivor, "says they could use your help\n")

                                    input("Press 1 to continue: ")
                                    print(line_break)

                                    print("Agreeing to split the loot,", survivor2, "watches your backs as the two of you heave the armoured doors open")
                                    
                                    if truck_choice == 1:
                                        print("This one is a mess too, it'll take a while to search")

                                    else:
                                        print("It's in a bad state and it'll take a while to search")

                                    print("Good thing you have", survivor, "to search with, but you'll have to split the loot after")
                                    print("You're peering into the back of the truck when", survivor2, "calls for backup from outside\n")
                                    print("He says there's zombies approaching and he could use some help")
                                    print(survivor, "tells you to keep searching, and he'll help him out")
                                    print("It looks like you'll be searching alone for a while...\n")

                                    input("Press 1 to continue: ")
                                    print(line_break)

                                    print("Hearing them fight off the zombies outside, something catches your eye")
                                    print("It looks like a large crate slid to the back of the truck and got stuck")

                                    input("Press 1 to continue: ")
                                    print(line_break)
                                    print("Managing to free it, you check inside and find:")

                                    truck_loot_normal = ["(food) MRE", "(ammo) *10 pistol bullets*", "(ammo) *5 pistol bullets*", "(fuel) 1 litre of fuel", "(fuel) 2 litres of fuel", "(food) protein bar", "(meds) first aid kit", "(meds) bandages"]
                                    truck_loot_special = ["(weapon) quality machete", "(weapon) hammer", "(weapon) *sledgehammer*", "(ammo) **10 rifle bullets**", "(weapon) *spiked baseball bat*"]
                                    truck_loot_armour = ["(clothing) *army helmet*", "(clothing) *leather jacket*", "(clothing) *combat pants*", "(clothing) *body armour*", "(ammo) **15 rifle bullets**"]

                                    crate_loot = [0]

                                    while len(crate_loot) %3 != 0:
                                        loot_count = random.randint(4, 8)
                                        crate_loot = []

                                        for i in range(loot_count):
                                            loot = truck_loot_normal[random.randint(0, len(truck_loot_normal) - 1)]
                                            crate_loot.append(loot)

                                        chance = random.randint(1, 3)

                                        special_loot = truck_loot_special[random.randint(0, len(truck_loot_special) - 1)]
                                        armour_loot = truck_loot_armour[random.randint(0, len(truck_loot_armour) - 1)]

                                        if chance == 1:
                                            crate_loot.append(special_loot)
                                            crate_loot.append(armour_loot)

                                        elif chance == 2:
                                            crate_loot.append(armour_loot)

                                        else:
                                            crate_loot.append(special_loot)

                                    for i in crate_loot:
                                        print(i)

                                    print("\nWill you:\n1. Tell the others\n2. Lie and keep it for yourself")
                                    choice = make_choice()

                                    lie_chance = random.randint(1, 3)

                                    if choice == 1:
                                        print("Listening for a second, the fighting outside seems to have stopped")
                                        print("Choosing to do the right thing you call the two survivors back into the truck")
                                        print("They're sweaty and panting heavily, but they seem unscathed\n")

                                        print(survivor, "takes a look inside the crate and his eyes widen")
                                        print("Grinning at", survivor2, "he tells him to take a look")
                                        print("The two survivors thank you, and agree to split the loot in three\n")

                                        input("Press 1 to continue: ")
                                        print(line_break)

                                        print("When all's said and done, you end up with:")
                                        your_loot = len(crate_loot) // 3
                                        for i in range(your_loot):
                                            loot = crate_loot[random.randint(0, len(crate_loot) - 1)]
                                            print(loot)
                                            add_item(loot)
                                            crate_loot.remove(loot)

                                        print("\nAfter packing up your bag, you thank them for their help, and they thank you for yours")
                                        print("Parting ways, you head back down the bridge and back to the", character[7][0])

                                        journal_entry(day, "Looted a lost convoy with two survivors and we split the loot between us")

                                    elif choice == 2:
                                        print("You decide you don't owe these survivors anything, and take the loot for yourself instead")
                                        print("Packing your bag up, the fighting outside seems to have stopped")
                                        print("Stepping out of the truck, you shake your head at the two survivors\n")

                                        print(survivor, "looks at you clearly disappointed and sighs before going to take a look for himself")
                                        print("However,", survivor2, "chooses to stay out here and keep watch")
                                        print("Taking a look around, you excuse yourself before heading for the road\n")

                                        input("Press 1 to continue: ")
                                        print(line_break)

                                        if lie_chance == 1:
                                            print("Expecting", survivor2, "to call out at any moment or", survivor, "to shout from within the truck, your whole body is tense")
                                            print("But they don't suspect a thing, and all", survivor, "does is offer a quick wave as you pass out of sight")
                                            print("Heart hammering in your chest, you run back to the road and head back home towards the", character[7][0])
                                            print("\nStopping briefly on your way, you check your bag and admire your haul...")

                                            journal_entry(day, "Looted a lost convoy with two survivors and kept the loot for myself without them noticing")

                                            for i in crate_loot:
                                                add_item(i)

                                        else:
                                            print("But as you leave, you hear", survivor2, "shout from behind you")
                                            print("It seems he wants to check your bag...")
                                            print("Will you:\n1. Hand it over\n2. Tell him to back off")
                                            choice = make_choice()

                                            if choice == 1:
                                                print("There's not much you can do, and you choose to hand over the bag")

                                                fight_chance = random.randint(1, 3)

                                                if fight_chance != 1:
                                                    print(survivor2, "grabs it from your hands and takes a look inside")
                                                    print("His eyes narrowing, he looks up at you angrily\n")
                                                    print("He's not just going to let you away with this...")

                                                    result = fight(1, "humans", survivor2, total_armour)

                                                    if result:
                                                        print("With", survivor2, "lying dead at your feet, you waste no time grabbing your bag")
                                                        print("Running past the wrecked trucks, you hear", survivor, "shout in despair as he finds the body of his friend")
                                                        print("But he doesn't give chase, and you manage to make it back to the", character[7][0], "before nightfall...")

                                                        survivor_group = [survivor, survivor2]
                                                        enemy_list.append(survivor_group)

                                                        for i in crate_loot:
                                                            add_item(i)

                                                        log = "Looted a lost convoy with two survivors and killed one named " + survivor2 + " so I could keep the loot"
                                                        journal_entry(day, log)

                                                    else:
                                                        game = False

                                                else:
                                                    print(survivor2, "takes a step back before calling for", survivor, "and looking inside")
                                                    print("As", survivor, "emerges from the truck, he sees the contents of the bag and his eyes widen")
                                                    print("He looks at you betrayed by this act, but he doesn't attack\n")

                                                    print("Instead he takes your bag and pours the loot out onto the ground")
                                                    print("You watch as the pair of survivors pack the loot into their own bags, before kicking yours back to you")
                                                    print("They tell you to get lost, and you reluctantly head back to the road\n")

                                                    print("Heading back to the", character[7][0], "you think long and hard about the decisions you made today...")
                                                    journal_entry(day, "Looted a lost convoy with two survivors but was caught stealing the spoils")

                                            else:
                                                print("Choosing to stand your ground, you tell him to back off")
                                                print("His eyes narrowing, it seems he isn't going to let you just walk away\n")

                                                print("But as he approaches you, a zombie stumbles out from behind the truck...")
                                                print("Will you:\n1. Warn", survivor2, "\n2. Do nothing")
                                                choice = make_choice()

                                                if choice == 1:
                                                    print("You can't just let him get bit, and you shout a warning and point at the undead attacker")
                                                    print("His eyes widening, ", survivor2, "spins around and manages to dodge the lunging zombie")
                                                    print("It turns for another strike but he's too quick and stops it dead with a clean hit\n")

                                                    input("Press 1 to continue: ")
                                                    print(line_break)

                                                    print("Facing back towards you, he reluctanctly thanks you for saving him")
                                                    print("But you've still stolen from him and he asks that you just return what you took")
                                                    print("As he tells you this", survivor, "appears from the truck, wondering what all the fuss is about")
                                                    print("Will you:\n1. Hand over the loot\n2. Attack them")
                                                    choice = make_choice()

                                                    if choice == 1:
                                                        print("Deciding not to risk it, you toss your bag over")
                                                        print("You watch as the pair of survivors pack the loot into their own bags, before kicking yours back to you")
                                                        print("They tell you to leave, and you make your way back to the road\n")

                                                        print("Heading back to the", character[7][0], "you think long and hard about the decisions you made today...")

                                                        journal_entry(day, "Looted a lost convoy with two survivors but was caught stealing the spoils")

                                                    else:
                                                        print("But as", survivor2, "explains the situation to", survivor, "you drop your bag and kick it behind you")
                                                        print("The two survivors look at you confused, then realise what's happening")
                                                        print("Dropping their bags, they prepare for battle...\n")

                                                        result = fight(2, "humans", survivor + " and " + survivor2)

                                                        if result:
                                                            print("The two survivors lie dead at your feet, but you've won")
                                                            print("Looks like the loot belonged to you after all...")
                                                            for i in crate_loot:
                                                                add_item(i)

                                                            print("\nLeaving them to rot you head home, satisfied that there are two less competitors out here scavenging now...")
                                                            journal_entry(day, "Killed two survivors on a crumbling bridge for some good loot")

                                                        else:
                                                            game = False

                                                else:
                                                    chance = random.randint(1, 2)

                                                    if chance == 1:
                                                        print(survivor2, "doesn't notice the it, he's too focused on you")
                                                        print("He reaches for his weapon and steps towards you, right as the zombie grabs him!")
                                                        print("Shouting and struggling he wrestles with the zombie, but it's not enough and it bites!\n")

                                                        input("Press 1 to continue: ")
                                                        print(line_break)

                                                        print("You make a run for it right as", survivor, "emerges and rushes to help his friend")
                                                        print("Hearing the two of them shouting, you race down the bridge and make your escape back to the", character[7][0])
                                                        print("\nYou check your bag on the way home, and sure enough all the loot is there...")

                                                        for i in crate_loot:
                                                            add_item(i)

                                                        zombie_survivors.append([survivor2, survivor])

                                                        log = "Pushed a survivor named " + survivor2 + " into a zombie so I could keep some military loot for myself"
                                                        journal_entry(day, log)

                                                    elif chance == 2:
                                                        print("But", survivor2, "notices the zombie and spins around to fight it off!")
                                                        print("Will you:\n1. Make a run for it\n2. Push him into the zombie")
                                                        choice = make_choice()

                                                        if choice == 1:
                                                            chance = random.randint(1, 2)
                                                            print("Deciding to make a run for it you turn to run down the bridge")

                                                            if chance == 1:
                                                                print(survivor2, "is busy fending off the zombie, and his friend emerges from the truck to help")
                                                                print("The two of them defeat the zombie, but you're nowhere to be seen")
                                                                print("\nRunning all the way back to the", character[7][0], "it seems you've gotten away with their loot...")

                                                                for i in crate_loot:
                                                                    add_item(i)

                                                                journal_entry(day, "I was caught stealing from two survivors but I caused a distraction and escaped with the loot")

                                                            else:
                                                                print("But", survivor, "steps out in front of you, right as", survivor2, "kills the zombie")
                                                                print("Will you:\n1. Hand over the loot\n2. Attack them")
                                                                choice = make_choice()

                                                                if choice == 1:
                                                                    print("Deciding not to risk it, you toss your bag over")
                                                                    print("You watch as the pair of survivors pack the loot into their own bags, before kicking yours back to you")
                                                                    print("They tell you to leave, and you make your way back to the road\n")

                                                                    print("Heading back to the", character[7][0], "you think long and hard about the decisions you made today...")

                                                                    journal_entry(day, "Looted a lost convoy with two survivors but was caught stealing the spoils")

                                                                else:
                                                                    print("But as", survivor2, "explains the situation to", survivor, "you drop your bag and kick it behind you")
                                                                    print("The two survivors turn to look at you, then realise what's happening")
                                                                    print("Dropping their bags, they prepare for battle...\n")

                                                                    result = fight(2, "humans", survivor + " and " + survivor2)

                                                                    if result:
                                                                        print("The two survivors lie dead at your feet, but you've won")
                                                                        print("Looks like the loot belonged to you after all...")
                                                                        for i in crate_loot:
                                                                            add_item(i)

                                                                        print("\nLeaving them to rot you head home, satisfied that there are two less competitors out here scavenging now...")
                                                                        journal_entry(day, "Killed two survivors on a crumbling bridge for some good loot")

                                                                    else:
                                                                        game = False

                                                        else:
                                                            print("Deciding not to take any chances, you send him sprawling into the zombie")
                                                            chance = random.randint(1, 3)

                                                            if chance == 1:
                                                                print("He tries to get to his feet, but the zombie pulls him down and bites!")
                                                                print(survivor, "emerges to see his friend under attack, and you make a run for it")
                                                                print("Hearing the screams of", survivor2, "echoing behind, nobody gives chase\n")

                                                                print("You check your bag on the way home, and sure enough all the loot is there...")
                                                                log = "Looted a lost convoy with two survivors and killed one named " + survivor2 + " so I could keep the loot"
                                                                journal_entry(day, log)

                                                                zombie_survivors.append([survivor2, survivor])
                                                                for i in crate_loot:
                                                                    add_item(i)

                                                            else:
                                                                print("Somehow me manages to keep the zombie's gnashing teeth at bay, while screaming for help")
                                                                print(survivor, "emerges from the truck and rushes to help, managing to kill the zombie before it can bite\n")

                                                                input("Press 1 to continue: ")
                                                                print(line_break)

                                                                print("But now the two of them are angry and they turn towards you ready for revenge...\n")

                                                                result = fight(2, "humans", survivor + " and " + survivor2)

                                                                if result:
                                                                    print("The two survivors lie dead at your feet, but you've won")
                                                                    print("Looks like the loot belonged to you after all...")
                                                                    for i in crate_loot:
                                                                        add_item(i)

                                                                    print("\nLeaving them to rot you head home, satisfied that there are two less competitors out here scavenging now...")
                                                                    journal_entry(day, "Killed two survivors on a crumbling bridge for some good loot")

                                                                else:
                                                                    game = False
                            
                            else:
                                print("A fierce battle must have taken place here, the ground is littered with bodies")
                                print("Creeping closer, a low growl stops you in your tracks...")
                                print("Some of the bodies are beginning to wake, you're surrounded by zombies!\n")

                                print("You still have a few seconds to run, but you'll miss out on that truck")
                                print("Will you:\n1. Fight off the military zombies\n2. Run for it")
                                choice = make_choice()

                                if choice == 1:
                                    print("As dangerous as it is, you won't leave without checking the truck")
                                    
                                    zom_num = random.randint(5, 8)

                                    print("Taking a look around, you see", zom_num, "military zombies have risen to their feet")
                                    print("This is going to be a tough fight...\n")

                                    result = fight(zom_num, "military zombies")

                                    if result:
                                        print("You're doubled over panting, but the zombies lie still once more")
                                        print("Once you've caught your breath you're free to take a look around")
                                        print("The area seems to be clear so you can take a look inside the truck\n")

                                        input("Press 1 to continue: ")
                                        print(line_break)

                                        if truck_choice == 1:
                                            print("This one is a mess too, it's in a sorry state")
                                            print("But something catches your eye")

                                        else:
                                            print("The interior is in a sorry state, but something catches your eye")
                                        
                                        loot_chance = random.randint(1, 2)

                                        if loot_chance == 1:
                                            print("Most of the contents are destroyed but it looks like there's some good stuff in the back")

                                        else:
                                            print("Most of the contents are destroyed but it looks like there's a crate left in the back")

                                        print("Crawling through the wreckage, you take a closer look...\n")

                                        input("Press 1 to continue: ")
                                        print(line_break)

                                        if loot_chance == 1:
                                            print("You've found a crate of supplies and a metal storage locker!")
                                            print("Inside the crate you find:")
                                            random_item(3, 5, "normal", "no rot")
                                            random_item(1, 2, "special")

                                            print("\nBut the locker is sealed tight and held shut by a heavy padlock")
                                            print("You'll need a crowbar to open this one")

                                            if "crowbar" in character[4]:
                                                print("Will you:\n1. Use the crowbar\n2. Leave it")
                                                if choice == 1:
                                                    no_health = 0
                                                    crowbar_found = False

                                                    for i in character[4]:
                                                        if not crowbar_found:
                                                            if i == "hands":
                                                                no_health += 1

                                                            elif i == "*pistol*" or i == "**assault rifle**":
                                                                no_health += 1

                                                            elif i == "crowbar":
                                                                crowbar_found = True

                                                    crowbar_current = weapon_durability[character[4].index("crowbar") - no_health]
                                                    crowbar_max = max_weapon_durability[character[4].index("crowbar") - no_health]

                                                    if crowbar_current > 0:
                                                        print("Utilising your crowbar, you manage to pry the locker open")

                                                        if crowbar_current <= 6:
                                                            c_damage = crowbar_current

                                                        else:
                                                            c_damage = random.randint(6, 10)

                                                        print("But in the process, it took", c_damage, "damage")

                                                        weapon_durability[character[4].index("crowbar") - no_health] -= c_damage

                                                        if weapon_durability[character[4].index("crowbar") - no_health] == 0:
                                                            print("Your crowbar has broken!")

                                                        else:
                                                            print("Your crowbar now has " + str(weapon_durability[character[4].index("crowbar") - no_health]) + "/" + str(max_weapon_durability[character[4].index("crowbar") - no_health]) + " durability")

                                                        print("\nInside you find:")
                                                        random_item(2, 3, "special")
                                                        chance = random.randint(1, 3)

                                                        if chance == 1:
                                                            item = ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)]
                                                            print(item)
                                                            add_item(item)

                                                    else:
                                                        print("But you can't use a broken crowbar...")

                                                else:
                                                    if len(character[4] == 2):
                                                        print("You're not going to risk damaging your only weapon")

                                                    print("Deciding to leave the locker alone, you're satisfied enough with the crate")

                                            else:
                                                print("But you don't have a crowbar, and despite your best effort you can't open it")
                                                print("Deciding to leave the locker alone, you're satisfied enough with the crate")

                                        else:
                                            print("You've found a crate of military supplies!")
                                            print("Inside the crate you find:")
                                            random_item(3, 5, "normal", "no rot")
                                            random_item(1, 2, "special")

                                        print("\nAfter packing up your bag, you hop out of the truck and check your surroundings")
                                        print("With the dangers of the bridge behind, you head back down the bridge and back to the", character[7][0])
                                        print("Reaching the", character[7][0], "you sit down and check your stuff, exhausted after today's work...")

                                        journal_entry(day, "Fought my way up a crumbling bridge and looted some military supplies")

                                    else:
                                        game = False

                                else:
                                    print("This many normal zombies would be bad enough, but these are undead soldiers")
                                    print("They're more dangerous than the average zombie, and you don't want to risk it")
                                    print("Turning and breaking into a sprint, you run down the bridge and make your escape\n")

                                    print("Once you've reached the safety of the", character[7][0], "you find yourself wondering what might have been inside the truck...")
                                    journal_entry(day, "Explored a crumbling bridge, but there were too many zombies to handle")
        else:
           print("Deciding not to risk it, you turn and head home instead")
           print("But on your way back to the", character[7][0], "you find yourself wondering what might've been waiting for you...")
           journal_entry(day, "Found myself at a crumbling bridge, but decided not to risk it")
    else:
        print("Deciding not to risk it, you turn and head back to the", character[7][0], "instead")
        print("But on your way home you find yourself wondering what was causing all that smoke...")
        journal_entry(day, "Saw some smoke in the distance, but decided not to investigate")
        
    return [game, zombies_killed]