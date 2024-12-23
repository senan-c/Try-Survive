from functions import *

def zombie_horde_event(area, zombies_killed, day):
    game = True

    print("As you're walking through", area, "you hear the shuffling of many feet and a moaning of many mouths")

    chance = random.randint(10, 100)
    print("You've stumbled upon a horde of", chance, "zombies\n")
    print("You know it's too many to fight even with weapons as strong as your",character[4][-1], "...")
    print("Will you:\n1. Sneak past\n2. Run past\n3. Wait for them to pass")
    choice = make_choice()

    for i in range(1):
        temp_item = item_list[random.randint(0, len(item_list) - 1)]
        add_item(temp_item)

    if choice == 1:
        chance = random.randint(1, 2)
        if chance == 1:
            print("Hiding behind cars and bins, you manage to sneak past the horde")

            if len(zombie_survivors) > 1:
                chance = random.randint(1, 3)

                if chance == 1:
                    print("But as you look back, you get a glance of a eerily familiar face")
                    named_zombie = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)][0]
                    print("It almost looked like", named_zombie, "was in that horde...")

                    journal_entry(day, "Sneaked past a horde but I think I saw a familiar face")

                else:
                    chance = random.randint(1, 3)

                    if chance == 1:
                        print("With your good luck you stumble upon a", temp_item, "on your way home")
                        add_item(temp_item)

                        log = "Sneaked past a horde and managed to grab a " + temp_item
                        journal_entry(day, log)

                    else:
                        print("You didn't find anything of use today, but it's better than dying")
                        journal_entry(day, "Got cut off by a horde but managed to sneak past")

            else:
                chance = random.randint(1, 3)

                if chance == 1:
                    print("With your good luck you stumble upon a", temp_item, "on your way home")
                    add_item(temp_item)

                    log = "Sneaked past a horde and managed to grab a " + temp_item
                    journal_entry(day, log)

                else:
                    print("You didn't find anything of use today, but it's better than dying")
                    journal_entry(day, "Got cut off by a horde but managed to sneak past")

        elif chance == 2:
            print("You sneak past the horde, skirting on the edge of the street and almost out of sight")
            print("Suddenly a zombie lunges out in front of you, you'll have to fight it!")

            fight_result= fight(1,"zombies")

            if fight_result:
                zombies_killed += 1
                print("With the zombie dead you hurry home, glad you only had to fight one")

                if len(zombie_survivors) > 1:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("But as you look back, you get a glance of a eerily familiar face")
                        named_zombie = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)][0]
                        print("It almost looked like", named_zombie, "was in that horde...")

                        journal_entry(day, "I had to escape a horde, fight a zombie and I think I saw a familiar face")

                    else:
                        journal_entry(day, "I had to escape a horde and fight a zombie")

                else:
                    journal_entry(day, "I had to escape a horde and fight a zombie")

            else:
                game = False

    elif choice == 2:
        print("With the horde nearing your location you make a break for it")
        chance = random.randint(1, 2)
        if chance == 1:
            print("The zombies notice you, but with your fast pace you easily speed by them")

            print("In fact, you're so fast that you have time to grab a",temp_item,"off the ground.")
            add_item(temp_item)
            print("With a runner's high, you jog your way back to the",character[7][0])

            if len(zombie_survivors) > 1:
                chance = random.randint(1, 2)

                if chance == 1:
                    print("But as you look back, you get a glance of a eerily familiar face")
                    named_zombie = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)][0]
                    print("It almost looked like", named_zombie, "was in that horde...")

                    log = "I had to run past a horde and I think I saw " + named_zombie + " in it"
                    journal_entry(day, log)

                else:
                    log = "I had to run past a horde but at least I grabbed a " + temp_item
                    journal_entry(day, log)

            else:
                log = "I had to run past a horde but at least I grabbed a " + temp_item
                journal_entry(day, log)


        elif chance == 2:
            print("Unfortunately, as you didn't take time to warm up, you trip and fall right in front of the horde!")
            chance = random.randint(1,4)
            if chance == 1:
                print("You get up again only to realise you've broken your ankle")
                print("Before you can escape, the horde catches you and you're torn apart...\nYOU ARE DEAD")
                game = False

            elif chance != 1:
                print("You manage to get back up and somehow evade the horde, but you've sprained your ankle")
                print("\nYou have lost 10HP")
                status = add_affliction("sprained ankle", 10)

                if not status:
                    game = False

                if game:
                    print("Defeated, you hobble back to the", character[7][0])
                    journal_entry(day, "I somehow got away from a horde but twisted my ankle like an idiot")

    elif choice == 3:
        print("You find a fire escape on the side of one of the buildings overlooking the street and climb up")
        chance = random.randint(1, 2)
        if chance == 1:
            print("On your way back down you lose your grip and fall, landing on your shoulder")
            print("\nYou have lost 20HP")

            status = add_affliction("bruised shoulder", 20)

            if not status:
                game = False

            journal_entry(day, "Nearly got caught by a horde then proceeded to fall down a fire escape")

        else:
            journal_entry(day, "Nearly got caught by a horde but managed to climb a fire escape")

        if game:
            print("The horde passes by, oblivious to you, and you sneak off back to the",character[7][0])
    
    return [game, zombies_killed]