from functions import *

def get_your_bag_event(area, character, day, raider_bag_items, raider_num, total_armour):
    game = True

    print("You're heading towards", area, "when something catches your eye")
    vehicles = ["tank", "bus", "truck"]
    vehicle = vehicles[random.randint(0, len(vehicles) - 1)]

    print("Down the street, you see a lone figure resting against a destroyed", vehicle)
    print("Ducking behind cover before taking another look, you recognise your lost bag on his back")
    
    if raider_num == 1:
        print("It's the raider who took your bag from the thief!")

    else:
        print("It's one of the raiders who took your bag from the thief!")

    print("\nHe won't give it up without a fight, but it's a second chance at getting your stuff back")
    print("Will you:\n1. Confront him for the bag\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("Deciding to make a stand and get your bag back, you think about how to approach the situation")
        print("Will you:\n1. Take him head on\n2. Try to sneak up on him")
        choice = make_choice()

        if choice == 1:
            print("Leaping out of cover, you charge towards the raider")
            print("You see the raider's eyes go wide as he spots you and jumps to his feet")

            chance = random.randint(1, 4)

            if chance == 1:
                print("But his laces get tangled and he crashes back to the ground!")
                print("Rolling over, he grabs for his weapon but this mistake has cost him his life")
                print("Before he can get up, you land a fatal blow...")

            else:
                print("Looks like it's going to be a fair fight!\n")

                result = fight(1, "humans", None, total_armour)

                if not result:
                    game = False

            print("With the raider dead, you're free to take your bag off his back")
            print("Checking the contents, it looks like everything's still there")
            print("Making sure there's nobody else around, you head back home to the", character[7][0])

        else:
            print("Deciding to sneak up on him, you spot a path between some crashed cars")
            print("Keeping your head low, you slowly make your way towards the raider")

            chance = random.randint(1, 4)

            if chance == 1:
                print("You've almost reached him when you hear a snarl come from behind the destroyed", vehicle)

                input("\nPress 1 to continue: ")
                print(line_break)
                print("It's a zombie!")
                print("It lumbers towards the raider and he laughs as it approaches, dropping your bag drawing his weapon")
                print("But as he goes to swing at the zombie you shove him in the back, sending him sprawling straight towards it!")
                print("\nHe shrieks as it grabs him, but his cries are cut short as it bites him in the neck...")
                print("The raider's body hits the ground as the zombie turns towards you, but you grab the bag and make your escape")
                print("Once you're clear, you check the bag, and sure enough, everything's still there")

                zombie_survivor = ["the Raider who took your bag"]
                zombie_survivors.append(zombie_survivor)

            else:
                print("But a misplaced step sends a rusty hubcap skittering across the ground, and the raider spins to face you!")
                print("Looks like it's going to be a fair fight after all...\n")

                result = fight(1, "humans")

                if result:
                    print("With the raider dead, you're free to take your bag off his back")
                    print("Checking the contents, it looks like everything's still there")
                    print("Making sure there's nobody else around, you head back home to the", character[7][0])

                else:
                    game = False

        if game:
            for i in raider_bag_items:
                add_item(i)

            journal_entry(day, "Spotted a raider with my lost bag, managed to get it back")

    else:
        print("Deciding against confronting the raider you throw away your second chance at your bag")
        print("Heading back home you feel defeated, and promise to one day stand up for yourself...")
        journal_entry(day, "Saw a raider with my lost bag but I decided not to confront him, again...")

    return[game]