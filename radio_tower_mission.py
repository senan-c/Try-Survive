from functions import *

def radio_tower_mission(possible_locations, day):
    game = True

    print("\nYou find the main terminal at the Radio Tower, and it's intact")
    print("On the terminal you find two possible locations to choose from:")

    temp_location_list = []
    count = 1
    for i in range(2):
        new_location = ""
        if new_location in temp_location_list:
            while new_location in temp_location_list:
                new_location = possible_locations[random.randint(0,len(possible_locations) - 1)]

            temp_location_list.append(new_location)

        else:
            new_location = possible_locations[random.randint(0, len(possible_locations) - 1)]
            temp_location_list.append(new_location)
        print(str(count) + ". " + new_location)
        possible_locations.remove(new_location)
        count += 1

    choice = make_choice()
    print("You have gathered info on the location of the",temp_location_list[choice - 1])
    fuel_required = random.randint(5,9)
    explore_list.append(temp_location_list[choice - 1] + " (" + str(fuel_required) + " Litres)")

    log = "Found a terminal at a Radio tower and got the location of the " + temp_location_list[choice - 1]
    journal_entry(day, log)

    return game