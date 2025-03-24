from functions import *

def crumbling_bridge_event(area, character, zombies_killed):
    game = True

    print("You're on your way towards", area, "when something catches your eye")
    print("Directly ahead of you is smoke rising into the air")
    print("If there's a fire you won't be able to reach", area, "today, but it could be worth checking out...")

    print("Will you:\n1. Investigate the smoke\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("You decide to risk it and take a closer look")
        print("Getting closer, you step off the road and into the trees")
        print("Following the smoke, you emerge from the forest and find yourself in front of a large bridge")
        print("It rained heavily last night and the river churns below you")

        bridge_chance = random.randint(1, 5)
        print("Scanning for the fire you spot the source of the smoke")

        if bridge_chance == 1:
            goal = "the crashed helicopter"
            print("It's a crashed helicopter!")
            print("Looks like it hit the bridge hard and it's starting to give way, it won't be long till the helicopter falls too")

        else:
            goal = "the lost convoy"
            print("It's a lost convoy!")
            print("They must have been on their way to", area, "when the government lost control")
            print("It looks like they made their final stand here, but the bridge took some heavy damage")

        print("As you're standing there, a chunk of concrete crumbles and breaks away before disappearing in the rushing water\n")

        print("If you can get up there, you might be able to find some good loot, but it's risky")
        print("Will you:\n1. Begin crossing the bridge\n2. Head home")
        choice = make_choice()

        if choice == 1:
            print("It's worth the risk, and you begin making your way across")

            bridge_length = random.randint(4, 5)
            step = 1
            crossing = True
            fall = False

            while crossing and step < bridge_length and game and not fall:
                if step == 1:
                    fall_chance = 0
                    print("You take your first step onto the bridge but it seems this area is stable")

                    chance = random.randint(1, 3)

                    if chance == 1:
                        zom_num = 2
                        print("But you're not alone, and", zom_num, "lurch out in front of you!")

                        result = fight(zom_num, "zombies")

                        if result:
                            print("With the zombies dead, you're free to continue")

                        else:
                            game = False

                    else:
                        print("Bodies and burnt out cars litter the area, you'll have to be careful")

                elif step < 4:
                    print("Deciding to continue on, you push further up the bridge")
                    fall_chance = random.randint(1, 4)

                    if fall_chance == 1:
                        fall = True

                        print("But as you set your foot down, the concrete gives way and you fall through!")
                        print("Thankfully you don't fall far, but to your horror the bridge begins to collapse above")

                        if step == 3:
                            print("You run for safety, but you went too far along the bridge and a piece of rubble catches your shoulder")

                            print("You've injured your shoulder!")
                            print("\nYou have lost 30HP")
                            status = add_affliction("injured shoulder", 30)

                            if not status:
                                game = False

                            print("You've hurt yourself and with this side of the bridge down, you'll be heading home empty handed")

                        else:
                            print("Diving at the last second, you manage to avoid the falling rubble")
                            print("But now this side of the bridge is down, looks like you'll be heading home empty handed")

                    else:
                        chance = random.randint(1, 3)

                        if chance == 1:
                            car_types = ["Sedan", "Hatchback", "Van", "Truck", "Convertible"]
                            car_colours = ["Red", "Blue", "Yellow", "White", "Black", "Silver", "Grey", "Green", "Navy","Brown"]

                            car = car_colours[random.randint(0, len(car_colours) - 1)] + " " + car_types[random.randint(0, len(car_types) - 1)]

                            if step == 2:
                                print("Most of the cars are burnt out and destroyed, but you spot a ", car, "that seems relatively unscathed")

                            else:
                                print("Further up the bridge is in a bad state, but you spot a ", car, "that seems mostly intact")

                            print("Deciding to check it out, you walk over to take a look")

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
                                    loot_car(car)

                            else:
                                print("But as you walk up to the", car, "you hear the barricade behind it creak and groan")
                                print("You jump back, and just in time as the concrete gives way and the car falls into the river below")
                                print("Hopefully there's better stuff further up the bridge")

                        elif chance == 2:
                            print("Burned corpses litter the bridge, but you spot a ragged backpack hidden under some rubble")
                            print("You dig it out and inside you find:")
                            random_item(2, 3, "normal", "no fuel")

                            print("\nQuickly checking around, there doesn't seem to be anything else left here")
                            print("You hope there's better stuff further up the bridge")

                        else:
                            chance = random.randint(1, 2)

                            if chance == 1:
                                zom_num = random.randint(3, 4)

                                if step == 2:
                                    print("You haven't walked much further up the bridge when a zombie lunges out from behind a car!")
                                    print("Barely avoiding it, you turn to see", zom_num - 1, "more zombies have circled behind you")

                                else:
                                    print("This bit of the bridge obviously saw a lot of action, and you hear something moving behind the wreckage of a bus")
                                    print("Taking a look, you see", zom_num, "zombies waiting for you!")

                                result = fight(zom_num, "zombies")

                                if result:
                                    print("With the zombies dead, you're free to continue up the bridge")

                                else:
                                    game = False

                            else:
                                print("The bridge creaks and groans but the surface under your feet holds")
                                print("For now...")

                elif step == 4:
                    fall_chance = random.randint(1, 3)

                    if fall_chance == 1:
                        fall = True

                        print("But as you set your foot down, the ground gives way and you fall through!")
                        chance = random.randint(1, 3)

                        print("The cold water is like ice in your veins, and you desperately thrash to the surface")

                        if chance == 1:
                            print("As you gasp for air you open your eyes to see the bridge collapse, concrete chunks raining down\n")
                            print("You claw desperately at the water, but it's no use")
                            print("Crushed under the debris you're dragged to the riverbed, never to be seen again...\nYOU DIED")

                            game = False

                        else:
                            print("As the bridge collapses above you, somehow you manage to swim to the shore")
                            print("Gasping for air, you seem to have escaped intact")
                            if len(character[4]) > 1:
                                lost_weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                print("But in the process you lost your",lost_weapon)
                                remove_item(lost_weapon)

                            print("Now this side of the bridge is down, looks like you'll be heading home empty handed")
                    
                    else:
                        chance = random.randint(1, 2)

                        if chance == 1:
                            zom_num = random.randint(3, 5)

                            print("You're nearing the end of the bridge when", zom_num, "military zombies shamble out from behind a truck!")

                            if bridge_chance != 1:
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
                            if bridge_chance != 1:
                                print("You're getting closer to the lost convoy when something catches your eye")

                            else:
                                print("You're getting closer to the crashed helicopter when you spot something, or someone...")

                            print("It's a dead survivor, or what's left of him")
                            print("A horde must have come through here and taken him by surprise, but his backpack is still caught underneath a car\n")

                            print("Pulling it out and checking inside, you find:")
                            random_item(3, 5, "normal")

                            print("\nAfter checking through the bag you continue up the bridge")

                elif step == 5:
                    fall_chance = random.randint(1, 3)

                    if fall_chance == 1:
                        fall = True

                        chance = random.randint(1, 2)
                        print("You've almost made it when the ground underneath you cracks and your heart drops")

                        if chance == 1:
                            print("Suddenly the concrete gives way and you fall straight through!")
                            print("Trying desperately to grab onto something, you hit off a pillar and your vision goes black\n")
                            print("When you wake, pain shoots through your body, and you look down to see a piece of rebar skewering your torso")
                            print("Looking up, a slab of concrete tumbles down from the bridge straight towards you")
                            print("Closing your eyes you accept your fate and-\nYOU DIED")

                            game = False
                        
                        else:
                            print("You try to run back to safety, but it's too late!")
                            print("The bridge begins to collapse around you, and you're dragged down with it\n")
                            print("Crashing into the river, the water churns around you and you're dragged under")
                            print("Somehow dodging falling debris, you make it to shore\n")

                            if len(character[4]) > 1:
                                lost_weapon = character[4][random.randint(1, len(character[4]) - 1)]
                                remove_item(lost_weapon)
                                print("But when you check your bag, not everything is there")
                                print("Looks like you lost your", lost_weapon, "but at least you're alive\n")

                            print("But with this side of the bridge down, it looks like you'll be heading home empty handed")

                    else:
                        chance = random.randint(1, 4)

                        if chance == 1:
                            chance = random.randint(1, 2)

                            car1 = car_colours[random.randint(0, len(car_colours) - 1)] + " " + car_types[random.randint(0, len(car_types) - 1)]
                            car2 = "Police Cruiser"

                            car_chance = random.randint(1, 3)

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

                                else:
                                    game = False

                            else:
                                print("It's a raider and he's here to fight!\n")

                                result = fight(1, "humans", None, total_armour)

                                if result:
                                    print("With the raider dead, you're able to squeeze past the cars and continue up the bridge")

                if not fall and game:
                    print("Will you:\n1. Continue up the bridge\n2. Head home")
                    choice = make_choice()

                    if choice == 2:
                        print("Deciding against reaching", goal, "you head back home instead")
                        crossing = False

            if crossing and game and not fall:
                print("Looks like you've made it to", goal)