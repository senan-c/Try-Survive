from functions import *

def enemy_survivor_event(area, day, total_armour):
    game = True

    enemy_name = enemy_list[random.randint(0, len(enemy_list) - 1)]
    enemy_list.remove(enemy_name)
    print("You're on your way towards", area, "when a figure steps out in front of you")
    print("It's hard to see, but it doesn't look to be a Raider or a zombie")

    if len(enemy_name) == 1:
        if enemy_name[0] in killer_list:
            killer_list.remove(enemy_name[0])
            print("It's the killer", enemy_name[0], "he's tracked you down!")
            print("\nThis time you won't be able to escape...")

        else:
            print("It's", enemy_name[0], "back for revenge!")
            print("\nHe glowers at you, and promises to punish you for what you did")

    else:
        print("It's", enemy_name[0], "back for revenge!")
        print("\nHe snarls, promising revenge for the death of his friend " + enemy_name[1] + "\n")

    print()
    fight_result = fight(1, "humans", enemy_name[0], total_armour)

    if fight_result:
        print("With", enemy_name[0], "dead, you turn back home")

        if enemy_name[0] not in killer_list:
            print("You'll be thinking twice before you mess with a survivor again...")

        log = enemy_name[0] + " returned and I had to kill him or be killed"
        journal_entry(day, log)

    else:
        game = False

    return game