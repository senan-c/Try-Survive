from functions import *

def loot_cars_event(zombies_killed, character, day, character_type):
    game = True

    print("This isn't your usual path and when you enter onto the highway, it appears to be deserted")
    print("You realise you've gone in the completely wrong direction")
    print("But this could an opportunity to search some cars")
    print("\nYou take a look around and though most of them are destroyed, a few cars remain untouched")
    print("Will you:\n1. Search the cars\n2. Head home")

    choice = make_choice()

    if choice == 1:
        check_cars = True

        print("You decide to check out the cars and select a few that look promising")
        print("But you'll to be careful, you're sure at least one of them will have an alarm...\n")

        car_types = ["Sedan", "Hatchback", "Van", "Truck", "Convertible"]
        car_colours = ["Red", "Blue", "Yellow", "White", "Black", "Silver", "Grey", "Green", "Navy","Brown"]

        cars = []
        car_alarms = []
        alarm_set = False
        second_alarm_set = False
        alarm = 5

        for i in range(5):
            car = car_colours[random.randint(0, len(car_colours) - 1)] + " " + car_types[random.randint(0, len(car_types) - 1)]

            police_car_chance = random.randint(1, 30)

            if police_car_chance == 1:
                car = "Police Cruiser"

            while car in cars:
                car = car_colours[random.randint(0, len(car_colours) - 1)] + " " + car_types[random.randint(0, len(car_types) - 1)]

            cars.append(car)

            if alarm_set == False:
                if alarm > 0:
                    alarm_chance = random.randint(1, alarm)

                else:
                    alarm_chance = 1

                if alarm_chance == 1:
                    alarm_set = True
                    car_alarms.append(1)

                else:
                    alarm -= 1
                    car_alarms.append(0)

            elif second_alarm_set == False:
                second_alarm = random.randint(1, 4)

                if second_alarm == 1:
                    second_alarm_set = True
                    car_alarms.append(1)

                else:
                    alarm -= 1
                    car_alarms.append(0)
            
            elif alarm > 0:
                alarm -= 1
                car_alarms.append(0)

        random.shuffle(car_alarms)

        while check_cars:
            print("Choose a car to search:")
            count= 1
            for i in cars:
                print(str(count) + ". " + i)
                count += 1
            print(str(count) + ". " + "Head home instead")
            choice = make_choice()

            if choice <= len(cars):
                chosen_car = cars[choice -1]
                cars.remove(chosen_car)
                print("You've taken your pick, and decide to check out the", chosen_car)

                if car_alarms[choice - 1] == 1:
                    print("The door is unlocked, but as you pull it open, the alarm blares!\n")
                    print("The noise is shockingly loud, and you see swarms of zombies emerging onto the highway around you")
                    print("Will you:\n1. Fight your way out\n2. Make a run for it")

                    choice = make_choice()

                    if choice == 1:
                        zom_num = random.randint(5,8)
                        print("Choosing to fight your way through, you spot", zom_num, "zombies in blocking an off ramp")
                        print("This will be your way out")
                        result = fight(zom_num, "zombies")

                        if result:
                            zombies_killed += zom_num
                            print("You've killed the zombies in your way, and without a second to spare you run down the off ramp")
                            print("As you take a look back, you see the hundreds of zombies pouring towards the sound of the alarm")

                        else:
                            game = False
                            check_cars = False

                    elif choice == 2:
                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("Fight or flight kicks in, and you make a dash for a nearby off ramp")
                            print("There are dozens of zombies on either side, and you see the horde begin to close around you")

                            chance = random.randint(1, 2)

                            if chance == 1:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    item_check = False
                                    if len(character[3]) > 0:
                                        item_check = True

                                    elif len(character[4]) > 1:
                                        item_check = True

                                    elif len(character[5]) > 0:
                                        item_check = True

                                    if item_check == True:
                                        your_item = select_random_item()
                                        while your_item is None:
                                            your_item = select_random_item()

                                    print("You run as fast as you can, but suddenly a zombie grabs your bag!")
                                    print("\nYou're dragged back towards the horde, but you manage to pull yourself free")
                                    print("But the chaos your", your_item, "fell and has been lost to the horde...")
                                    remove_item(your_item)
                                    
                                elif chance == 2:
                                    print("Your lungs burn as you sprint past the dozens of undead, but it looks like you're going to make it!\n")
                                    print("A zombie reaches out to grab your ankle but you kick its hand away and speed past")

                                print("Jumping over a barrier, you take a look back and see hundreds of zombies milling around the car")

                            elif chance == 2:
                                print("You run for the ramp, but as you get closer you see zombies lurching up towards you!")
                                print("Spinning around desperately, you make a run for a fence to escape over")
                                print("Zombies snarl and lunge at you, but you dodge and leap for the fence")
                                print("But you fall short, and the horde grabs hold of your legs and pulls you in...\nYOU DIED")

                                game = False
                                check_cars = False

                        elif chance == 2:
                            print("Dozens of zombies shamble and lurch towards you, and you look desperately for an escape")
                            print("You see a gap in the fencing and run for it")
                            zom_num = random.randint(2, 4)

                            print("But", zom_num, "zombies stumble out and block your path!\n")

                            result = fight(zom_num, "zombies")

                            if result:
                                zombies_killed += zom_num
                                print("You kill the zombies and dive through the gap in the fencing")
                                
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    print("You tumble down the embankment but somehow get up unscathed and escape")

                                else:
                                    print("You tumble down the embankment and land badly on your ankle")
                                    print("\nYou have lost 10HP")
                                    status = add_affliction("sprained ankle", 10)

                                    if not status:
                                        game = False

                                    if game:
                                        print("\nSomehow you manage to limp away and escape")

                    if game:
                        print("\nAfter this close call, you call it quits for the day and head back home...")
                        journal_entry(day, "Had a close call while looting cars and barely made it out")
                        check_cars = False

                else:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("But it's locked")
                        print("Will you:\n1. Smash a window\n2. Check a different car")
                        choice = make_choice()

                        if choice == 1:
                            chance = random.randint(1, 2)

                            if chosen_car == "Police Cruiser" and character_type == "Police Officer":
                                print("But this is the same model as your own Police Cruiser, and you know a few tricks")
                                print("With a bit of work you manage to get the door open")
                                chance = 1

                            else:
                                print("You check around for any zombies, before smashing the driver's window")

                            if chance == 1:
                                print("Luckily you haven't alerted any zombies, and you're free to loot the", chosen_car)
                                print()

                            else:
                                zom_num = random.randint(2, 3)
                                print("You go to loot the", chosen_car, "but", zom_num, "zombies emerge from behind it!\n")
                                result = fight(zom_num, "zombies")

                                if result:
                                    zombies_killed += zom_num
                                    print("With the zombies dead, you take one last look around before looting the car\n")

                                else:
                                    game = False
                                    check_cars = False

                            if game:
                                loot_car(chosen_car)

                        else:
                            print("You won't risk smashing the glass and attracting attention")
                            print("Maybe you'll try a different car instead")

                    else:
                        print("Looks like it's unlocked!\n")
                        loot_car(chosen_car)

            else:
                print("You choose not to risk an alarm, and head back to the", character[7][0], "instead")
                check_cars = False

                if len(cars) == 5:
                    journal_entry(day, "Found some cars to loot, but didn't want to risk setting off an alarm")

                else:
                    cars_looted = 5 - len(cars)

                    log = "Found some cars on the highway and looted " + str(cars_looted) + " of them"
                    journal_entry(day, log)

    return [game, zombies_killed]