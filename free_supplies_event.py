from functions import *

def free_supplies_event(area, day):
    print("You're out scavenging near", area, "but things are looking pretty dismal")
    print("You have no food, medicine or weapons and the way things are going, you won't survive long out here")
    print("This area is almost destroyed, clearly there was a huge battle here recently\n")
    print("Your mouth is dry, and you have to squint your eyes to see in the harsh sunlight")
    print("But in front of you and lying in the middle of the road, there appears to be a duffel bag of supplies!\n")
    print("It might be a trap or even a mirage, but you think you should check it out")
    print("Will you:\n1. Check out the supplies\n2. Head home")
    choice = make_choice()

    if choice == 1:
        print("You sneak up to the duffel bag and find a note taped to it")
        print("It's from another survivor who got lucky recently, and they wanted to share with someone who needs it\n")
        print("Inside the bag you find:")
        random_item(3, 7, "normal", "no rot")
        print("\nYou take these items, thanking the unknown survivor as you head home")
        journal_entry(day, "Wasn't doing so great, but an unknown survivor left me some supplies")

    else:
        print("Even in this state, you won't risk a trap")
        print("You decide to head home instead, regardless of what's in the bag")
        journal_entry(day, "Saw some supplies in the middle of the road, but it looked like a trap")