import random
import Zombie as z
import Human as h
import Boss as b

item_file = open("items/items.txt", "r")
item_list = item_file.readlines()
item_file.close()

special_item_file = open("items/special_items.txt", "r")
special_item_list = special_item_file.readlines()
special_item_file.close()

ultra_special_item_file = open("items/ultra_special_items.txt", "r")
ultra_special_item_list = ultra_special_item_file.readlines()
ultra_special_item_file.close()

boss_item_file= open("items/boss_items.txt", "r")
boss_item_list = boss_item_file.readlines()
boss_item_file.close()

crafting_item_file = open("items/crafting_items.txt", "r")
crafting_item_list = crafting_item_file.readlines()
crafting_item_file.close()

zom_descriptions_file = open("descriptions/zombie_descriptions.txt", "r")
zom_description_list = zom_descriptions_file.readlines()
zom_descriptions_file.close()

raider_descriptions_file = open("descriptions/raider_descriptions.txt", "r")
raider_descriptions_list = raider_descriptions_file.readlines()
raider_descriptions_file.close()

survivor_descriptions_file = open("descriptions/survivor_descriptions.txt", "r")
survivor_descriptions_list = survivor_descriptions_file.readlines()
survivor_descriptions_file.close()

military_descriptions_file = open("descriptions/military_descriptions.txt", "r")
military_descriptions_list = military_descriptions_file.readlines()
military_descriptions_file.close()

survivors_male_file = open("descriptions/survivor_names_male.txt", "r")
survivors_male_list = survivors_male_file.readlines()
survivors_male_file.close()

chicken_name_file = open("descriptions/chicken_names.txt")
chicken_name_list = chicken_name_file.readlines()
chicken_name_file.close()

items = item_list[0]
item_list = items.split(",")

count = 0
suits = ["D","C","H","S"]
card_list  = []
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

special_items = special_item_list[0]
special_item_list = special_items.split(",")

ultra_special_items = ultra_special_item_list[0]
ultra_special_item_list = ultra_special_items.split(",")

boss_items = boss_item_list[0]
boss_item_list = boss_items.split(",")

crafting_items = crafting_item_list[0]
crafting_item_list = crafting_items.split(",")

zom_descriptions = zom_description_list[0]
zom_description_list = zom_descriptions.split(",")

raider_descriptions = raider_descriptions_list[0]
raider_descriptions_list = raider_descriptions.split(",")

survivor_descriptions = survivor_descriptions_list[0]
survivor_descriptions_list = survivor_descriptions.split(",")

military_descriptions = military_descriptions_list[0]
military_description_list = military_descriptions.split(",")

survivors_male = survivors_male_list[0]
survivors_male_list = survivors_male.split(",")

chicken_names = chicken_name_list[0]
chicken_name_list = chicken_names.split(",")

raider_descriptions_list += survivor_descriptions_list

#0 HP, 1 Water, 2 Calories, 3 Food, 4 Weapons, 5 Meds, 6 Friends, 7 Home, 8 Bag, 9 Fuel, 10 Ammo
character = [[100], ["Hydrated"], [2000], [], ["hands"], [], [], [], ["journal", "material satchel"], [0], [0, 0]]
#0 Head, 1 Torso, 2 Hands, 3 Legs, 4 Feet
current_clothing = [[],[],[],[],[]]
total_armour = 0

temp_items = []
afflictions = []
enemy_list = []
zombie_survivors = []
latest_events = []
journal = []
bag_items = []
bag_raiders = 0
raider_bag_items = []

#0 Nails, 1 Rope, 2 Leather, 3 Wooden Poles
workshop_satchel = [0, 0, 0, 0]

areas = ["Downtown","the Suburbs","the City Centre","the Industrial Estate"]
zom_types = ["weak zombie","zombie","strong zombie"]
explore_list = ["Radio Tower (5 Litres)"]
shelter = ["small shop","lonely house","secluded shack"]

head_armour = ["*motorbike helmet*","*army helmet*"]
torso_armour = ["***commander's armor***","***doctor's labcoat***","*body armour*","*leather jacket*","*police vest*","**combat armour**", "*handmade armour*"]
leg_armour = ["*combat pants*"]
foot_armour = ["*work boots*", "*handmade boots*"]
hand_armour = ["***flame gloves***","*leather gloves*"]

bladed_weapons = ["machete", "knife", "*katana*", "*butterfly knife*", "basic spear", "heavy spear", "*tri-blade spear*"]

fight_list = []

game = True
day = 0
days_no_water = 0
zombies_killed = 0
water_drank = True

workshop_event_played = False

rifle_supp = False
pistol_supp = False

weapon_durability = []
max_weapon_durability = []
weapon_parts = 0

rotten_food = False
rot_day = random.randint(7, 14)
first_hunt = True

chickens = []
killer_list = []

line_break = ("-" * 120)


def add_item(x):
    if x[0:3] == "(me":
        character[5].append(x[7:])

    elif x[0:3] == "(fu":
        character[9][0] += int(x[7])

    elif x[0:2] == "(f":
        if x != "(food) rotten food":
            if x == "(food) carton of eggs":
                for i in range(6):
                    character[3].append("egg")

            else:
                character[3].append(x[7:])

    elif x[0:2] == "(w":
        weapon = x[9:]

        character[4].append(weapon)

        if weapon == "knife":
            weapon_durability.append(20)
            max_weapon_durability.append(20)

        elif weapon == "machete" or weapon == "basic spear" or weapon == "*butterfly knife*":
            weapon_durability.append(30)
            max_weapon_durability.append(30)

        elif weapon == "hammer" or weapon == "heavy spear" or weapon == "*spiked baseball bat*" or weapon == "*tri-blade spear*":
            weapon_durability.append(40)
            max_weapon_durability.append(40)

        elif weapon == "baseball bat" or weapon == "*katana*" or weapon == "***diseased scalpel***" or weapon == "quality machete":
            weapon_durability.append(45)
            max_weapon_durability.append(45)

        elif weapon == "crowbar":
            weapon_durability.append(50)
            max_weapon_durability.append(50)

        elif weapon == "heavy hammer":
            weapon_durability.append(55)
            max_weapon_durability.append(55)

        elif weapon == "*sledgehammer*" or weapon == "***flaming hand-axe***":
            weapon_durability.append(70)
            max_weapon_durability.append(70)

        elif weapon == "***commander's breaching hammer***":
            weapon_durability.append(90)
            max_weapon_durability.append(90)

    elif x[0:2] == "(c":
        character[8].append(x)

    elif x[0:3] == "(mo":
        character[8].append(x)

    elif x[0:3] == "(ma":
        value = int(x[11])

        if "nail" in x:
            workshop_satchel[0] += value

        elif "rope" in x:
            workshop_satchel[1] += value

        elif "leather" in x:
            workshop_satchel[2] += value

        else:
            workshop_satchel[3] += value

    elif x[0:3] == "(gu":
        character[4].append(x[6:])
        weapon_durability.append(1)
        max_weapon_durability.append(1)

    elif x[0:2] == "(a":
        if x[8] == "*":
            if x[10].isnumeric():
                character[10][1] += int(x[9:11])

            else:
                character[10][1] += int(x[9])

        else:
            if x[9].isnumeric():
                character[10][0] += int(x[8:10])

            else:
                character[10][0] += int(x[8])


def random_item(num1, num2, rarity, vers=None):
    temp_items = []
    for i in range(random.randint(num1,num2)):
        if rarity == "normal":
            temp_item = item_list[random.randint(0, len(item_list) - 1)]
            if vers == "meds":
                while temp_item[1:5] != "meds":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

            elif vers == "food":
                while temp_item[1:5] != "food":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

            elif vers == "fuel":
                while temp_item[1:5] != "fuel":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

            elif vers == "no fuel":
                while temp_item[1:5] == "fuel":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

                    if temp_item == "(weapon) crowbar" and "crowbar" in character[4]:
                        temp_item = item_list[random.randint(0, len(item_list) - 1)]

            elif vers == "no rot":
                while temp_item == "(food) rotten food" or temp_item[1:5] == "fuel" or temp_item[1:5] == "weap":
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

            else:
                while temp_item == "(weapon) crowbar" and "crowbar" in character[4]:
                    temp_item = item_list[random.randint(0, len(item_list) - 1)]

        elif rarity == "special":
            temp_item = special_item_list[random.randint(0, len(special_item_list) - 1)]

        elif rarity == "ultra special":
            temp_item = ultra_special_item_list[random.randint(0, len(ultra_special_item_list) - 1)]

        elif rarity == "crafting":
            temp_item = crafting_item_list[random.randint(0, len(crafting_item_list) - 1)]

        temp_items.append(temp_item)
        add_item(temp_item)
    for i in temp_items:
        print(i)


cal_list_100 = ["apple", "banana", "carrots", "mushrooms", "strawberries", "spring onions"]
cal_list_200 = ["egg", "can of sardines"]
cal_list_300 = ["bag of peach rings", "popcorn", "cereal", "instant noodles"]
cal_list_400 = ["protein bar", "bread", "flapjack", "honey", "tomato sauce", "granola bar", "pastry", "yoghurt"]
cal_list_600 = ["can of soup", "can of peaches", "can of beans", "can of tuna", "biscuits", "sausages", "oats", "bag of marshmallows", "bag of rice", "butter"]
cal_list_800 = ["chicken", "pasta", "beef jerky", "box of chocolates", "can of whipped cream", "cake"]
cal_list_1000 = ["pre-made meal", "venison"]
cal_list_1500 = ["condensed milk"]
cal_list_2500 = ["MRE"]

def get_cals(x):
    if x in cal_list_100:
        return 100

    elif x in cal_list_200:
        return 200

    elif x in cal_list_300:
        return 300

    elif x in cal_list_400:
        return 400

    elif x in cal_list_600:
        return 600

    elif x in cal_list_800:
        return 800

    elif x in cal_list_1000:
        return 1000

    elif x in cal_list_1500:
        return 1500

    elif x in cal_list_2500:
        return 2500

    else:
        if x == "chicken and pasta":
            cals = 1700 // 2

        elif x == "sausage and pasta":
            cals = 1500 // 2

        elif x == "chicken and beef sandwiches":
            cals = 2000 // 4

        elif x == "fruit and cream" or x == "tuna sandwiches":
            cals = 1000 // 2

        elif x == "mega MRE":
            cals = 3000

        elif x == "peaches and cream":
            cals = 1400 // 2

        elif x == "cereal treats":
            cals = 900 // 2

        elif x == "chicken stir-fry":
            cals = 1600 // 2

        elif x == "chicken casserole" or x == "venison stew":
            cals = 2500 // 2

        elif x == "venison casserole":
            cals = 2700 // 2

        elif x == "overnight oats":
            cals = 2600 // 4

        elif x == "rice pudding":
            cals = 2100 // 4
        
        elif x == "deluxe MRE":
            cals = 3500

        elif x == "smores":
            cals = 2000 // 4

        elif x == "omelette":
            cals = 1200

        if character[7][0] == "restaurant":
            cals += round(cals * 0.25)

        else:
            cals += round(cals * 0.10)

        return cals


def make_choice():
    while True:
        choice = input("Make your choice: ")
        if choice.isdigit():
            print(line_break)
            return int(choice)
        else:
            print(line_break)
            print("Please enter a valid number")
            print(line_break)


def add_affliction(injury, health):
    character[0][0] -= health
    afflictions.append(injury)
    print("You now have", character[0][0], "HP\n")

    if character[0][0] <= 0:
        print("\nYOU DIED")
        return False
    
    else:
        return True


def choose_weapon():
    count = 1
    durability_count = 0
    for i in character[4]:
        if i == "*pistol*":
            print(str(count) + ". " + i + " - ammo:", character[10][0])
            durability_count += 1

        elif i == "**assault rifle**":
            print(str(count) + ". " + i + " - ammo:", character[10][1])
            durability_count += 1

        else:
            if i != "hands":
                print(str(count) + ". " + i + " - condition: " + str(weapon_durability[durability_count]) + "/" + str(max_weapon_durability[durability_count]))
                durability_count += 1

            else:
                print(str(count) + ". " + i)
        count += 1

    weapon_choice = make_choice()

    while weapon_choice > len(character[4]):
        durability_count = 0
        print("SELECT A VALID OPTION")

        count = 1
        for i in character[4]:
            if i == "*pistol*":
                print(str(count) + ". " + i + " - ammo:", character[10][0])

            elif i == "**assault rifle**":
                print(str(count) + ". " + i + " - ammo:", character[10][1])

            else:
                if i != "hands":
                    print(str(count) + ". " + i + " - condition: " + str(weapon_durability[durability_count]) + "/" + str(max_weapon_durability[durability_count]))
                    durability_count += 1

                else:
                    print(str(count) + ". " + i)
            count += 1

        weapon_choice = make_choice()

    weapon_chosen = character[4][weapon_choice - 1]
    no_pistol_ammo = False
    no_rifle_ammo = False

    while weapon_chosen == "*pistol*" and character[10][0] == 0:
        no_pistol_ammo = True
        print("You don't have any ammo for this gun\n")
        count = 1
        print("Choose again!")

        count = 1
        durability_count = 0
        for i in character[4]:
            if i == "*pistol*":
                print(str(count) + ". " + i + " - ammo:", character[10][0])

            elif i == "**assault rifle**":
                print(str(count) + ". " + i + " - ammo:", character[10][1])

            else:
                if i != "hands":
                    print(str(count) + ". " + i + " - condition: " + str(weapon_durability[durability_count]) + "/" + str(max_weapon_durability[durability_count]))
                    durability_count += 1

                else:
                    print(str(count) + ". " + i)
            count += 1

        weapon_choice = make_choice()
        weapon_chosen = character[4][weapon_choice - 1]

    while (weapon_chosen == "**assault rifle**" and character[10][1] < 3) or (no_pistol_ammo and weapon_chosen == "*pistol*"):
        no_rifle_ammo = True
        print("You don't have enough ammo for this gun")
        print("Choose again!")

        count = 1
        durability_count = 0
        for i in character[4]:
            if i == "*pistol*":
                print(str(count) + ". " + i + " - ammo:", character[10][0])

            elif i == "**assault rifle**":
                print(str(count) + ". " + i + " - ammo:", character[10][1])

            else:
                if i != "hands":
                    print(str(count) + ". " + i + " - condition: " + str(weapon_durability[durability_count]) + "/" + str(max_weapon_durability[durability_count]))
                    durability_count += 1

                else:
                    print(str(count) + ". " + i)
            count += 1

        weapon_choice = make_choice()
        weapon_chosen = character[4][weapon_choice - 1]

    if weapon_chosen != "hands":
        if weapon_chosen == "**assault rifle**" or weapon_chosen == "*pistol*":
            temp_weapon_durability = 1

        else:
            temp_weapon_durability = weapon_durability[weapon_choice - 2]

        while (temp_weapon_durability == 0) or (no_pistol_ammo and weapon_chosen == "*pistol*") or (no_rifle_ammo and weapon_chosen == "**assault rifle**"):
            print("This weapon is broken")
            print("Choose again!")

            count = 1
            durability_count = 0
            for i in character[4]:
                if i == "*pistol*":
                    print(str(count) + ". " + i + " - ammo:", character[10][0])

                elif i == "**assault rifle**":
                    print(str(count) + ". " + i + " - ammo:", character[10][1])

                else:
                    if i != "hands":
                        print(str(count) + ". " + i + " - condition: " + str(weapon_durability[durability_count]) + "/" + str(max_weapon_durability[durability_count]))
                        durability_count += 1

                    else:
                        print(str(count) + ". " + i)
                count += 1

            weapon_choice = make_choice()
            weapon_chosen = character[4][weapon_choice - 1]

            if weapon_chosen != "hands":
                temp_weapon_durability = weapon_durability[weapon_choice - 2]

            else:
                temp_weapon_durability = 1

    return [weapon_chosen, weapon_choice]

def ranged_attack(weapon, enemy, health, armour=0):
    boss = False
    attack_missed = False

    if enemy == "Infected Commander" or enemy == "Diseased Doctor" or enemy == "Fuel Beast":
        enemy = "the " + enemy
        boss = True

    if weapon == "*pistol*":
        weapon = "pistol"
        ammo = character[10][0]
        chance = random.randint(1, 4)

    elif weapon == "**assault rifle**":
        weapon = "assault rifle"
        ammo = character[10][1]
        chance = random.randint(1, 5)

    while (weapon == "pistol" and ammo > 0) or (weapon == "assault rifle" and ammo > 3):
        if weapon == "pistol":
            shots_fired = random.randint(1, 3)

            while shots_fired > character[10][0]:
                shots_fired = random.randint(1, 3)
            character[10][0] -= shots_fired

        elif weapon == "assault rifle":
            shots_fired = random.randint(3, 5)

            while shots_fired > character[10][1]:
                shots_fired = random.randint(3, 5)
            character[10][1] -= shots_fired

        if shots_fired == 1:
            round = "round is"
            hit = "hits"
            strike = "strikes"
            miss = "misses"

        else:
            round = "rounds are"
            hit = "hit"
            strike = "strike"
            miss = "miss"

        if shots_fired == 1:
            print("You fire a shot at", enemy, "with your", weapon)

        else:
            print("You fire a burst of", shots_fired, "shots at", enemy, "with your", weapon)

        if chance != 1:
            killshot = random.randint(1, 3)

            if killshot == 1:
                print("The", round, "on target and", hit + " " + enemy, "in the head!\n")
                if boss == True:
                    damage = health//2.5

                    if (damage + 70) < health:
                        crit_chance = random.randint(1, 3)
                        if crit_chance == 1:
                            damage += 70

                    else:
                        damage = health

                else:
                    damage = health + armour

                if weapon == "**assault rifle**":
                    if (damage + 20) < health:
                        damage += 30

                print("Critical Hit! You hit", enemy, "for", int(damage), "damage")

            else:
                part_hit = random.randint(1, 3)
                if health < 60 and boss == False:
                    damage = health

                elif health < 80 and boss == True:
                    damage = health

                else:
                    if boss == True:
                        min_dam = health // 5

                        if health > 100:
                            max_dam = health // 2
                            damage = random.randint(int(min_dam), int(max_dam))

                        else:
                            damage = health

                    else:
                        min_dam = health // 2

                        damage = random.randint(int(min_dam), health)

                    if damage < 65 and health > 65 and (damage + 20) < health:
                        damage += 20

                    elif damage < 65 and health > 65 and (damage + 10) < health:
                        damage += 10

                if weapon == "**assault rifle**":
                    if (damage + 30) < health:
                        damage += 30

                    elif (damage + 20) < health:
                        damage += 20

                    elif (damage + 10) < health:
                        damage += 10

                if part_hit == 1:
                    print("The", round, "on target, but", strike + " " + enemy, "in the torso")
                    if (damage + 10) < health:
                        damage += 10

                    elif (damage + 5) < health:
                        damage += 5

                elif part_hit == 2:
                    print("The", round, "on target, but", strike + " " + enemy, "in the arm")

                else:
                    print("The", round, "on target, but", strike + " " + enemy, "in the leg")

                print("You hit", enemy, "for", int(damage), "damage")

        else:
            attack_missed = True

            if shots_fired == 1:
                round = "round"

            else:
                round = "rounds"

            print("The", round + " " + miss + " " + enemy + "!")

            damage = 0

        print()
        return [damage, attack_missed]


def fight_zombie(zombie, weapon_choice, bonus_dam, weapon_val):
    swapped_weapon = False

    count = 0
    while not zombie.health <= 0:
        damage = 0
        if count != 0:
            print(line_break)

        print("You attack the",zombie.character)

        if weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**":
            if weapon_choice == "*pistol*" and character[10][0] == 0 or weapon_choice == "**assault rifle**" and character[10][1] < 3:
                print("Looks like you don't have enough ammo!")
                print("You'll have to swap weapons\n")
                print("You back away from the zombie and quickly look in your bag")
                result = [0, False]

                select_weapon = choose_weapon()
                weapon_val = select_weapon[1] - 1
                weapon_choice = select_weapon[0]

                print("You swapped to your", weapon_choice)

            else:
                result = ranged_attack(weapon_choice, "the zombie", zombie.health)

                zombie.health -= result[0]

                if zombie.health < 0:
                    zombie.health = 0

                if result[1] == False:
                    print("The", zombie.character, "has", zombie.health, "HP left")
                    input("\nPress 1 to continue: ")
                    print(line_break)

            if result[1] == True:
                print("The zombie strikes!")
                chance = random.randint(1, 9)
                 
                if chance == 1:
                    escape_num = random.randint(1, 3)
                    print("It grabs you and goes for the kill!")
                    print("Choose a number between 1 and 3 to try break free")
                    choice = make_choice()

                    if choice == escape_num:
                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("Somehow you manage to push the zombie away and its gnashing teeth barely miss you")
                        
                        else:
                            print("You manage to land a kick on the zombie and its grip weakens")
                            print("Seizing the oppurtunity you twist and manage to get away")

                    else:
                        if weapon_choice == "hands":
                                print("You kick and punch at the", zombie.character, "but you can't break free")
                            
                        else:
                            print("Your", weapon_choice, "is trapped between you and the", zombie.character, "and you can't reach it!")

                        dead = False
                        
                        if len(current_clothing[1]) == 0:
                            dead = True

                        else:
                            if current_clothing[1][0] == "*leather jacket*":
                                chance = random.randint(1, 4)

                            elif current_clothing[1][0] == "*body armour*" or current_clothing[1][0] == "*police vest*":
                                chance = random.randint(1, 3)

                            elif current_clothing[1][0] == "**combat armour**":
                                chance = random.randint(1, 2)
                            
                            else:
                                chance = 2

                            if chance != 1:
                                dead = True

                        if dead:
                            print("\nWith a terrible groan the zombie pulls you in and bites!\nYOU ARE DEAD")
                            return False
                        
                        else:
                            print("\nThe zombie bites down hard, but it's stopped by your " + current_clothing[1][0] + "!")
                            print("Knocking the zombie back, you realise your", current_clothing[1][0], "has just saved your life")

                elif chance == 2 or chance == 3:
                    print("The zombie charges forward, but you knock back its attack with your", weapon_choice)

                else:
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("The zombie lunges for you, but you dodge and the fight continues")

                    else:
                        print("The zombie lunges towards you, but you push it back and the fight continues")

                input("\nPress 1 to continue: ")
                print(line_break)

        else:
            skip_turn = False

            if weapon_choice != "hands":
                if weapon_durability[weapon_val - 1] == 0:
                    print("But your", weapon_choice, "has broken!")
                    print("You'll have to swap weapons\n")
                    print("You back away from the zombie and quickly look in your bag")
                    select_weapon = choose_weapon()
                    weapon_val = select_weapon[1] - 1
                    weapon_choice = select_weapon[0]

                    skip_turn = True

                    print("You swapped to your", weapon_choice)

            if weapon_choice == "hands":
                miss_chance = random.randint(1,2)

            else:
                miss_chance = random.randint(1, 5)

                if zombies_killed >= 30:
                    miss_chance = random.randint(1, 8)

                elif zombies_killed >= 20:
                    miss_chance = random.randint(1, 7)

                elif zombies_killed >= 10:
                    miss_chance = random.randint(1, 6)

            if not skip_turn:
                if miss_chance != 1:
                    chance = random.randint(1, 2)

                    if weapon_choice in bladed_weapons:
                        bonus_dam += 5
                        if chance == 1:
                            print("You stab the", zombie.character, "with your",weapon_choice)

                        else:
                            print("You slash the", zombie.character, "with your",weapon_choice)

                        weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1

                    elif weapon_choice == "hands":
                        if chance == 1:
                            print("You swing and punch the", zombie.character, "in the head")

                        else:
                            print("You kick the", zombie.character, "as hard as you can")

                    else:
                        if chance == 1:
                            print("You whack the", zombie.character, "with your", weapon_choice)

                        else:
                            print("You club the", zombie.character, "with your", weapon_choice)

                        weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1

                    if zombie.health > 50:
                        damage = random.randint(50, zombie.health) + bonus_dam

                    elif zombie.health > 40:
                        damage = random.randint(40, zombie.health) + bonus_dam

                    elif zombie.health > 30:
                        damage = random.randint(30, zombie.health) + bonus_dam

                    else:
                        damage = zombie.health

                    if weapon_choice == "hands":
                        if zombie.health > 20:
                            if zombie.health//2 > 15:
                                damage = random.randint(15, zombie.health//2) + bonus_dam
                            
                            else:
                                damage = random.randint(15, 20)

                            if damage < 15:
                                damage = random.randint(15, 20)

                        else:
                            damage = zombie.health

                    if weapon_choice != "hands":
                        if "*" not in weapon_choice:
                            damage -= 5

                        else:
                            damage += 5

                        if damage < 20:
                            damage = random.randint(20, 25)

                    if damage > zombie.health:
                        damage = zombie.health

                    if damage < 0:
                        damage = 0

                    if damage > (zombie.health // 10) * 8:
                        print("Critical Hit! You hit the zombie for",damage,"damage")

                    else:
                        print("You hit the zombie for",damage,"damage")

                else:
                    chance = random.randint(1, 3)

                    if chance == 1:
                        print("You swing your",weapon_choice,"and miss")
                        print("\nThe zombie strikes!")

                    elif chance == 2:
                        if weapon_choice != "hands":
                            print("You swing your",weapon_choice,"but it only strikes a glancing blow")

                        else:
                            print("You swing your fist at the zombie, but the blow glances off")
                        
                        print("\nTaking the opportunity, the zombie strikes!")

                    else:
                        if weapon_choice != "hands":
                            print("You swing your", weapon_choice, "but it catches on the zombie's clothes and you almost lose it")

                        else:
                            print("Launching a kick at the zombie, it grabs for your leg and sends you stumbling back")

                        print("\nYou're off balance now, and the zombie strikes!")
                    
                    if weapon_choice == "hands":
                        chance = random.randint(1,6)

                    else:
                        if character[2][0] > 2000:
                            chance = random.randint(1,12)

                        elif character[2][0] > 1500:
                            chance = random.randint(1, 11)

                        else:
                            chance = random.randint(1, 10)

                    if chance == 1:
                        escape_num = random.randint(1, 3)
                        print("It grabs you and goes for the kill!\n")
                        print("Choose a number between 1 and 3 to try break free")
                        choice = make_choice()

                        if choice == escape_num:
                            chance = random.randint(1, 2)

                            if chance == 1:
                                print("Somehow you manage to push the zombie away and its gnashing teeth barely miss you")
                            
                            else:
                                print("You manage to land a kick on the zombie and its grip weakens")
                                print("Seizing the oppurtunity you twist and manage to get away")

                        else:
                            if weapon_choice == "hands":
                                print("You kick and punch at the", zombie.character, "but you can't break free")
                            
                            else:
                                print("Your", weapon_choice, "is trapped between you and the", zombie.character, "and you can't reach it!")

                            dead = False
                            
                            if len(current_clothing[1]) == 0:
                                dead = True

                            else:
                                if current_clothing[1][0] == "*leather jacket*":
                                    chance = random.randint(1, 4)

                                elif current_clothing[1][0] == "*body armour*" or current_clothing[1][0] == "*police vest*":
                                    chance = random.randint(1, 3)

                                elif current_clothing[1][0] == "**combat armour**":
                                    chance = random.randint(1, 2)
                                
                                else:
                                    chance = 2

                                if chance != 1:
                                    dead = True

                            if dead:
                                print("\nWith a terrible groan the zombie pulls you in and bites!\nYOU ARE DEAD")
                                return False
                            
                            else:
                                print("\nThe zombie bites down hard, but it's stopped by your " + current_clothing[1][0] + "!")
                                print("Knocking the zombie back, you're shaken at this close call")

                    elif (chance == 2 or chance == 3) and weapon_choice != "hands":
                        print("The zombie charges forward, but you block its attack with your",weapon_choice)
                        damage = random.randint(5, 20)

                        if damage > zombie.health:
                            damage = zombie.health
                        print("Looks like the zombie took",damage,"damage!")
                        zombie.health -= damage

                    else:
                        chance = random.randint(1, 2)

                        if chance == 1:
                            print("The zombie lunges for you, but you dodge and the fight continues")

                        else:
                            print("The zombie lunges towards you, but you push it back and the fight continues")

                if miss_chance != 1:
                    zombie.health -= damage
                    if zombie.health < 0:
                        zombie.health = 0
                    print("\nThe", zombie.character, "has", zombie.health, "HP left")

            input("\nPress 1 to continue: ")
            if zombie.health == 0:
                print(line_break)
            count += 1

    print("The zombie has been defeated!")
    chance = random.randint(1,5)
    if chance== 1:
        print("\nThe zombie dropped",zombie.loot_drop)
        add_item(zombie.loot_drop)
    print(line_break)

    if swapped_weapon == True:
        return [True, weapon_choice]

    else:
        return [True, False]


def fight_boss(boss, weapon_choice, bonus_dam, armour, weapon_val):
    punish_swap = True

    while boss.health > 0:
        print(line_break)
        boss.shout()
        print("You attack the", boss.name, "\n")
        miss_chance = random.randint(1, 4)
        result = [0, False]

        if weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**":
            if weapon_choice == "*pistol*" and character[10][0] == 0 or weapon_choice == "**assault rifle**" and character[10][1] < 3:
                print("Looks like you don't have enough ammo!")
                print("You'll have to swap weapons\n")
                print("You back away from the", boss.name, "and find space to look in your bag")
                
                weapon_choice = choose_weapon()

                chance = random.randint(1, 2)

                if chance == 1:
                    print("But", boss.name, "takes the opportunity to strike!\n")

                else:
                    print("Luckily you're back in the fight before", boss.name, "can strike")
                    punish_swap = False
                    
            else:
                result = ranged_attack(weapon_choice, boss.name, boss.health)

            damage = result[0]

            if result[1] == False:
                boss.health -= damage
                if boss.health < 0:
                    boss.health = 0

                print("It has", int(boss.health), "HP left\n")

        else:
            skip_turn = False
            punish_swap = True

            if weapon_choice != "hands":
                if weapon_durability[weapon_val - 1] == 0:
                    print("But your", weapon_choice, "has broken!")
                    print("You'll have to swap weapons\n")
                    print("You back away and quickly look in your bag")
                    select_weapon = choose_weapon()
                    weapon_val = select_weapon[1] - 1
                    weapon_choice = select_weapon[0]

                    skip_turn = True

                    print("You swapped to your", weapon_choice)

                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("But", boss.name, "takes the opportunity to strike!\n")

                    else:
                        print("Luckily you're back in the fight before", boss.name, "can strike")
                        punish_swap = False

            if not skip_turn:
                if weapon_choice == "hands":
                    miss_chance = random.randint(1, 2)

                if miss_chance != 1:
                    chance = random.randint(1, 2)
                    if weapon_choice in bladed_weapons:
                        bonus_dam += 5
                        if chance == 1:
                            print("You stab it with your", weapon_choice)

                        else:
                            print("You slash the", boss.name,"with your", weapon_choice)

                        weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1

                    elif weapon_choice == "hands":
                        if chance == 1:
                            print("You swing and punch the ", boss.name, "in the head")

                        else:
                            print("You kick the him as hard as you can")

                    else:
                        if chance == 1:
                            print("You whack it with your", weapon_choice)

                        else:
                            print("You club the ", boss.name, "with your", weapon_choice)

                        weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1

                    if "*" in weapon_choice:
                        bonus_dam += 20

                    if boss.health >= 20:
                        damage = random.randint(20, 150) + bonus_dam

                    else:
                        damage = boss.health

                    if weapon_choice == "hands":
                        if boss.health > 10:
                            damage = random.randint(10, 100) + bonus_dam
                            if damage == 0:
                                damage = 10

                        else:
                            damage = boss.health

                    if damage > boss.health // 2:
                        print("Critical Hit! You hit the", boss.name ,"for", int(damage), "damage\n")

                    else:
                        print("You hit the", boss.name ,"for", int(damage), "damage")

                    boss.health -= damage
                    if boss.health < 0:
                        boss.health = 0

                    print("It has", int(boss.health), "HP left\n")

                else:
                    chance = random.randint(1,3)
                    damage = 0
                    if chance == 1:
                        print("You swing your",weapon_choice,"and miss\n")

                    else:
                        boss.dodge()

        if boss.health > 0 and punish_swap == True:
            enemy_chance = random.randint(1, 4)

            if enemy_chance != 1:
                boss.attack()
                print()
                if character[0][0] >= 20:
                    enemy_damage = random.randint(50, 100)

                else:
                    enemy_damage = character[0][0]

                if enemy_damage > character[0][0]:
                    enemy_damage = character[0][0]

                if enemy_damage > character[0][0] // 2:
                    print("Critical Hit! The", boss.name,"hit you for", enemy_damage, "damage")

                else:
                    print("The", boss.name,"hit you for", enemy_damage, "damage")

                if armour < enemy_damage and armour > 0:
                    print("Your armour blocked", armour, "damage")
                    enemy_damage -= armour
                    armour = 0
                    character[0][0] -= enemy_damage
                    if character[0][0] < 0:
                        character[0][0] = 0

                    print("\nYou have", armour, "armour left")

                elif armour > enemy_damage and armour > 0:
                    og_armour = armour
                    armour -= enemy_damage

                    print("Your armour blocked",og_armour - armour, "damage")
                    print("\nYou have", armour, "armour left")

                else:
                    character[0][0] -= enemy_damage

                if character[0][0] < 0:
                    character[0][0] = 0

                print("You have", character[0][0], "HP left")

            else:
                boss.miss()

            if character[0][0] == 0:
                print("\nThe", boss.name, "Has killed you!\nYOU ARE DEAD")
                return False

        if boss.health != 0:
            input("\nPress 1 to continue: ")

    print("The", boss.name, "has been defeated!")
    print(line_break)
    return True


def fight_human(human_enemy, weapon_choice, bonus_dam, armour, weapon_val):
    swapped_weapon = False
    result = [0, True]
    punish_swap = True
    skip_turn = False

    while human_enemy.health > 0:
        print(line_break)
        print("You attack", human_enemy.name, "\n")
        miss_chance = random.randint(1, 4)

        if weapon_choice == "*pistol*" or weapon_choice == "**assault rifle**":
            miss_chance = 1

            if (weapon_choice == "*pistol*" and character[10][0] == 0) or (weapon_choice == "**assault rifle**" and character[10][1] < 3):
                print("Looks like you don't have enough ammo!")
                print("You'll have to swap weapons\n")
                print("You back away from", human_enemy.name, "and find space to look in your bag")
                result = [0, False]

                weapon_choice = choose_weapon()
                swapped_weapon = True

                chance = random.randint(1, 2)

                if chance == 1:
                    print("But", human_enemy.name, "takes the opportunity to strike!\n")

                else:
                    print("Luckily you're back in the fight before", human_enemy.name, "can strike")
                    punish_swap = False
            else:
                result = ranged_attack(weapon_choice, human_enemy.name, human_enemy.health, human_enemy.armour_val)

            damage = result[0]

        else:
            if weapon_choice != "hands":
                if weapon_durability[weapon_val - 1] == 0:
                    print("But your", weapon_choice, "has broken!")
                    print("You'll have to swap weapons\n")
                    print("You back away and quickly look in your bag")
                    select_weapon = choose_weapon()
                    weapon_val = select_weapon[1] - 1
                    weapon_choice = select_weapon[0]

                    skip_turn = True

                    print("You swapped to your", weapon_choice)

                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("But", human_enemy.name, "takes the opportunity to strike!\n")

                    else:
                        print("Luckily you're back in the fight before", human_enemy.name, "can strike")
                        punish_swap = False

            if not skip_turn:
                finisher = 0

                if weapon_choice == "hands":
                    miss_chance = random.randint(1, 2)

                elif "*" in weapon_choice:
                    if human_enemy.health >= 30:
                            finisher = random.randint(1, 7)

                    else:
                        finisher = random.randint(1, 3)

                if miss_chance != 1:
                    if finisher != 1:
                        chance = random.randint(1, 2)
                        if weapon_choice in bladed_weapons:
                            bonus_dam += 5
                            if chance == 1:
                                print("You stab him with your", weapon_choice)

                            else:
                                print("You slash", human_enemy.name,"with your", weapon_choice)
                            
                            weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1

                        elif weapon_choice == "hands":
                            if chance == 1:
                                print("You swing and punch", human_enemy.name, "in the head")

                            else:
                                print("You kick the him as hard as you can")

                        else:
                            if chance == 1:
                                print("You whack him with your", weapon_choice)

                            else:
                                print("You club", human_enemy.name, "with your", weapon_choice)
                            
                            weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1


                        if human_enemy.health >= 20:
                            damage = random.randint(20, human_enemy.health) + bonus_dam

                        else:
                            damage = human_enemy.health

                        if weapon_choice == "hands":
                            if human_enemy.health > 15:
                                damage = random.randint(15, 40) + bonus_dam
                                if damage == 0:
                                    damage = 15

                                elif damage > human_enemy.health:
                                    damage = human_enemy.health

                            else:
                                damage = human_enemy.health

                    else:
                        if finisher == 1:
                            damage = human_enemy.health + human_enemy.armour_val

                            if weapon_choice == "*katana*":
                                print("Your *katana* glints as it slices through the air,", human_enemy.name, "has no time to react before he is cut in half")

                            elif weapon_choice == "*sledgehammer*":
                                print("You bring your sledgehammer crashing down on his head, hearing bone splinter and crack")

                            elif weapon_choice == "*butterfly knife*":
                                print("Your *butterfly knife* blurs and dances as you slice at", human_enemy.name + ",", "and he falls back clutching his throat")

                            elif weapon_choice == "*spiked baseball bat*":
                                print("Driving your *spiked baseball bat* into his head with a sickening crunch,", human_enemy.name,"collapses and doesn't get back up")

                            elif weapon_choice == "*tri-blade spear*":
                                print("You slice your *tri-blade spear* across his face in a swift arc, before lunging forward and driving all three blades into his chest with lethal precision")


                            weapon_durability[weapon_val - 1] = weapon_durability[weapon_val - 1] - 1

                        else:
                            if human_enemy.health >= 20:
                                damage = random.randint(20, human_enemy.health) + bonus_dam

                            else:
                                damage = human_enemy.health

                    if damage <= 0:
                        damage = random.randint(5, 10)

                    elif damage < 20:
                        damage = random.randint(15, 20)

                    if damage > human_enemy.health // 2:
                        print("Critical Hit! You hit", human_enemy.name ,"for", damage, "damage")

                    else:
                        print("You hit him for", damage, "damage\n")

                elif miss_chance == 1:
                    chance = random.randint(1,3)
                    if chance == 1:
                        print("You swing your",weapon_choice,"and miss\n")

                    else:
                        human_enemy.dodge()

        if (miss_chance != 1 or result[1] == False) and not skip_turn:
            if human_enemy.armour_val > 0:
                print("His armour blocked", human_enemy.armour_val, "damage")

            if human_enemy.armour_val < damage and human_enemy.armour_val > 0:
                    damage -= human_enemy.armour_val
                    human_enemy.armour_val = 0
                    human_enemy.health -= damage

                    print("\nHe has", human_enemy.armour_val, "armour left")

            elif human_enemy.armour_val > damage and human_enemy.armour_val > 0:
                human_enemy.armour_val -= damage
                print("\nHe has", human_enemy.armour_val, "armour left")

            else:
                human_enemy.health -= damage
                
            if human_enemy.health < 0:
                human_enemy.health = 0
            
            if result[1] == False or miss_chance != 1:
                print("He has", human_enemy.health, "HP left\n")

        if human_enemy.health > 0 and punish_swap == True:
            enemy_chance = random.randint(1, 4)

            if human_enemy.weapon == "hands":
                enemy_chance = random.randint(1, 2)

            if enemy_chance != 1:
                human_enemy.attack()
                if character[0][0] >= 20:
                    chance = random.randint(1, 3)
                    if chance == 1:
                        enemy_damage = random.randint(20, 80)

                    else:
                        enemy_damage = random.randint(20, 50)

                else:
                    enemy_damage = character[0][0]

                if human_enemy.weapon == "hands":
                    if character[0][0] >= 20:
                        chance = random.randint(1, 3)
                        if chance == 1:
                            enemy_damage = random.randint(20, 60)

                        else:
                            enemy_damage = random.randint(20, 40)

                    else:
                        enemy_damage = character[0][0]

                if enemy_damage > character[0][0] // 2:
                    print("Critical Hit!", human_enemy.name,"hit you for", enemy_damage, "damage")

                else:
                    print(human_enemy.name,"hit you for", enemy_damage, "damage")

                if armour != 0:
                    if armour < enemy_damage and armour > 0:
                        print("\nYour armour blocked", armour, "damage")
                        enemy_damage -= armour
                        armour = 0
                        character[0][0] -= enemy_damage
                        if character[0][0] < 0:
                            character[0][0] = 0

                        print("You have", armour, "armour left")

                    elif armour > enemy_damage and armour > 0:
                        og_armour = armour
                        armour -= enemy_damage

                        print("\nYour armour blocked",og_armour - armour, "damage")
                        print("You have", armour, "armour left")

                else:
                    character[0][0] -= enemy_damage

                if character[0][0] < 0:
                    character[0][0] = 0

                print("You have", character[0][0], "HP left")

            else:
                human_enemy.miss()

            if character[0][0] == 0:
                print()
                print(human_enemy.name, "Has killed you!\nYOU ARE DEAD")
                return [False, False]

        if human_enemy.health != 0:
            input("\nPress 1 to continue: ")

    print(human_enemy.name, "has been killed!\n")
    input("Press 1 to continue: ")
    print(line_break)
    if swapped_weapon == True:
        return [True, weapon_choice]

    else:
        return [True, False]


def fight(num, battle, boss=None, total_armour=None):
    opp_list = []
    bonus_dam = 0
    if character[2][0] == 0:
        print("You're starving and you'll barely be able to fight!")
        bonus_dam -= 30

    elif character[2][0] < 500:
        print("You're almost starving and won't be able to fight as well")
        bonus_dam -= 25

    elif character[2][0] >= 500 and character[2][0] < 1000:
        print("You're very hungry and feel weak, you won't be able to fight as well")
        bonus_dam -= 20

    elif character[2][0] >= 1000 and character[2][0] < 1500:
        print("You're low on energy and won't be able to fight as well")
        bonus_dam -= 10

    elif character[2][0] >= 2000 and character[2][0] < 2500:
        print("You have enough energy and will fight well today")
        bonus_dam += 10

    elif character[2][0] >= 2500:
        print("You have plenty of energy and will fight well today")
        bonus_dam += 20

    if battle == "zombies":
        reg_count = 1
        strong_count = 1
        weak_count = 1

        for i in range(num):
            zom_type = zom_types[random.randint(0, len(zom_types) - 1)]
            fight_list.append("a " + zom_type)
            if "a " + zom_type not in opp_list:
                opp_list.append("a " + zom_type)

            else:
                if zom_type == "weak zombie":
                    weak_count += 1

                elif zom_type == "strong zombie":
                    strong_count += 1

                elif zom_type == "zombie":
                    reg_count += 1

        if weak_count > 1:
            opp_list.append(str(weak_count) + " weak zombies")
            for i in opp_list:
                if i == "a weak zombie":
                    opp_list.remove(i)

        if reg_count > 1:
            opp_list.append(str(reg_count) + " zombies")
            for i in opp_list:
                if i == "a zombie":
                    opp_list.remove(i)

        if strong_count > 1:
            opp_list.append(str(strong_count) + " strong zombies")
            for i in opp_list:
                if i == "a strong zombie":
                    opp_list.remove(i)

        count = 1
        if len(fight_list) == 1 and fight_list[0] == "a zombie":
            (fight_prompt) = "It looks like you'll be fighting a zombie"

        elif len(fight_list) > 1 or (len(fight_list) == 1 and (fight_list[0] == "a strong zombie" or fight_list[0] == "a weak zombie")):
            fight_prompt = "It looks like you'll be fighting "

            for i in opp_list:
                if count == 1:
                    fight_prompt += i

                elif count == len(opp_list):
                    fight_prompt += " and " + i

                else:
                    fight_prompt += ", " + i

                count += 1

    elif battle == "humans":
        if boss is None:
            for i in range(num):
                opp_list.append(survivors_male_list[random.randint(0, len(survivors_male_list) -1)])

            if num == 1:
                fight_prompt = "Looks like you'll be fighting 1 human, named " + opp_list[0]

            else:
                fight_prompt = "Looks like you'll be fighting " + str(len(opp_list)) + " humans, named "

                count = 0
                for i in opp_list:
                    if count < len(opp_list) - 2:
                        fight_prompt += str(opp_list[count]) + ", "

                    elif count == len(opp_list) - 2:
                        fight_prompt += str(opp_list[count]) + " and "

                    else:
                        fight_prompt += str(opp_list[count])

                    count += 1

        else:
            if boss == "the Thief":
                fight_prompt = "Looks like you'll be fighting the Thief"

            elif "and" in boss:
                boss_list = boss.split(" and ")
                boss1 = boss_list[0]
                opp_list.append(boss1)
                boss2 = boss_list[1]
                opp_list.append(boss2)

                fight_prompt = "Looks like you'll be fighting 2 humans, named " + boss
                opp_list.append(boss)

            else:
                fight_prompt = "Looks like you'll be fighting 1 human, named " + boss
                opp_list.append(boss)

    elif battle == "boss":
        fight_prompt = "You're going to be fighting the " + boss

    elif battle == "military zombies":
        if num > 1:
            fight_prompt = "You're going to be fighting " + str(num) + " military zombies"

        else:
            fight_prompt = "You're going to be fighting a military zombie"

        for i in range(num):
            fight_list.append("military zombie")

    print(fight_prompt)

    print("\nYou reach in your bag for a weapon:")
    if len(character[4]) == 1:
        print("But there's nothing there, you'll have to use your fists")

    select_weapon = choose_weapon()
    weapon_val = select_weapon[1] - 1
    weapon_choice = select_weapon[0]

    if battle == "zombies":
        descriptor = zom_description_list[random.randint(0,len(zom_description_list)-1)]
        loot = item_list[random.randint(0,len(item_list) - 1)]
        count = 1
        while num > 0:
            print("Zombie #",count)
            zombie = fight_list[0]
            if zombie == "a weak zombie":
                zombie = z.Zombie(75,zombie[2:],descriptor,loot)

            elif zombie == "a strong zombie":
                zombie = z.Zombie(125,zombie[2:],descriptor,loot)

            elif zombie == "a zombie":
                zombie = z.Zombie(100,zombie[2:],descriptor,loot)
            chance = random.randint(1, 10)

            if boss is None:
                if chance == 1:
                    print("\nAs you prepare to fight, you notice this zombie", zombie.appearance,"\n")

                else:
                    print()

            else:
                if boss not in killer_list and boss != "the Thief":
                    print("Before you attack, you apologise to", boss, "wishing you had saved him...")

            result= fight_zombie(zombie, weapon_choice, bonus_dam, weapon_val)
            fight_list.remove(fight_list[0])
            if result:
                num -= 1
                count += 1

            else:
                return False

    elif battle == "military zombies":
        loot = item_list[random.randint(0, len(item_list) - 1)]
        count = 1
        while num > 0:
            print("Zombie #", count)
            zombie = "military zombie"
            descriptor = military_description_list[random.randint(0, len(military_description_list) - 1)]

            zombie = z.Zombie(150, zombie, descriptor, loot)

            chance = random.randint(1, 5)
            if boss is None:
                print("\nAs you prepare to fight, you notice this military zombie", zombie.appearance)

            else:
                print("Before you attack, you stop and thank", boss, "for what he did for you...")

            result= fight_zombie(zombie, weapon_choice, bonus_dam, weapon_val)
            fight_list.remove(fight_list[0])
            if result:
                num -= 1
                count += 1

            else:
                return False

    elif battle == "humans":
        loot_list = []
        loot_counter = 0
        count = 1
        while num > 0:
            human_name = opp_list[0]
            print("Human Enemy #", count, "-", human_name)
            enemy_weapon = item_list[random.randint(0, len(item_list) - 1)]
            while enemy_weapon[1:7] != "weapon":
                enemy_weapon = item_list[random.randint(0, len(item_list) - 1)]

            weapon_chance = random.randint(1,5)
            if weapon_chance == 1:
                enemy_weapon = "hands"

            if enemy_weapon != "hands":
                loot_list.append(enemy_weapon)

            armour_chance = random.randint(1,2)

            if armour_chance == 1:
                enemy_armour = special_item_list[random.randint(0, len(special_item_list) - 1)]
                while enemy_armour[1:9] != "clothing":
                    enemy_armour = special_item_list[random.randint(0, len(special_item_list) - 1)]

                loot_list.append(enemy_armour)

            else:
                enemy_armour = None

            human_enemy = h.Human(human_name, enemy_weapon, enemy_armour)
            human_enemy.display_armour()

            print("He has", human_enemy.armour_val, "armour")

            result = fight_human(human_enemy, weapon_choice, bonus_dam, total_armour, weapon_val)
            opp_list.remove(opp_list[0])
            if result[0] == True:
                num -= 1
                count += 1
                loot_counter += 1

                if result[1] != False:
                    weapon_choice = result[1]

            else:
                return False
        for i in range(5 * loot_counter):
            loot_list.append(item_list[random.randint(0, len(item_list) -1)])

        if loot_counter > 1:
            print("It looks like they had some loot:")
        
        else:
            print("It looks like he had some loot:")
        for i in range(loot_counter * 3):
            loot = loot_list[random.randint(0, len(loot_list) -1)]
            print(loot)
            add_item(loot)
            loot_list.remove(loot)
        print()

    elif battle == "boss":
        loot_list = []
        print("Boss Battle -",boss)

        if boss == "Infected Commander":
            boss_weapon = boss_item_list[0]
            boss_armour = boss_item_list[1]

        elif boss == "Diseased Doctor":
            boss_weapon = boss_item_list[2]
            boss_armour = boss_item_list[3]

        elif boss == "Fuel Beast":
            boss_weapon = boss_item_list[4]
            boss_armour = boss_item_list[5]

        loot_list.append(boss_weapon)
        loot_list.append(boss_armour)

        boss_battle = b.Boss(boss)
        result = fight_boss(boss_battle, weapon_choice, bonus_dam, total_armour, weapon_val)

        if not result:
            return False

        for i in range(28):
            chance = random.randint(1, 10)

            if chance != 1:
                chance = random.randint(1, 2)

                if chance == 1:
                    loot_list.append(special_item_list[random.randint(0, len(special_item_list) -1)])

                else:
                    loot_list.append(item_list[random.randint(0, len(item_list) - 1)])

            else:
                loot_list.append(ultra_special_item_list[random.randint(0, len(ultra_special_item_list) -1)])

        print("It looks like the boss dropped some loot:")
        for i in range(5):
            loot = loot_list[random.randint(0, len(loot_list) - 1)]
            print(loot)
            add_item(loot)
            loot_list.remove(loot)
        print()

    if (weapon_choice == "**assault rifle**" and rifle_supp == False) or (weapon_choice == "*pistol*" and pistol_supp == False):
        chance = random.randint(1, 3)

        if chance == 1:
            print("But it looks like the shooting attracted some zombies")
            zom_num = random.randint(2, 3)

            fight_result = fight(zom_num, "zombies")

            if fight_result:
                print("The zombies lie dead, and you really need to find a suppressor")

            else:
                return False

    return True


def describe_human(human_type,human_count):
    if human_type == "raider":
        if human_count == 1:
            return "It looks like he is wearing " + raider_descriptions_list[random.randint(0, len(raider_descriptions_list)-1)]

        else:
            sentence = ""
            count = 0
            for i in range(human_count):
                count += 1
                if count == 1:
                    sentence += "It looks like one is wearing " + raider_descriptions_list[random.randint(0, len(raider_descriptions_list)-1)]

                else:
                    sentence += " and another is wearing " + raider_descriptions_list[random.randint(0, len(raider_descriptions_list)-1)]

            return sentence

    elif human_type == "survivor":
        if human_count == 1:
            return "It looks like he is wearing " + survivor_descriptions_list[random.randint(0, len(survivor_descriptions_list)-1)]

        else:
            sentence = ""
            count = 0
            for i in range(human_count):
                count += 1
                if count == 1:
                    sentence += "It looks like one is wearing " + survivor_descriptions_list[random.randint(0, len(survivor_descriptions_list)-1)]

                else:
                    sentence += " and another is wearing " + survivor_descriptions_list[random.randint(0, len(survivor_descriptions_list)-1)]

            return sentence


def select_random_item():
    chance = random.randint(1,10)
    armour_check = False
    your_item = None
    invalid_list = ["journal", "material satchel", "crafting recipes"]

    count = 30

    while (your_item == None or your_item in invalid_list) and count > 0:
        count -= 1

        for i in current_clothing:
            if len(i) > 0:
                armour_check == True

        if chance == 1 and armour_check == True:
            category = current_clothing[random.randint(0,4)]
            while len(category) == 0:
                category = current_clothing[random.randint(0, 4)]

        elif chance == 2 and len(character[8]) > 0:
            category = character[8]

        else:
            category = character[random.randint(3, 5)]
            while len(category) == 0:
                category = character[random.randint(3, 5)]

        if len(category) > 1:
            your_item = category[random.randint(0, len(category) - 1)]

        else:
            your_item = category[0]

        while your_item == "hands":
            category = character[random.randint(3, 5)]
            while len(category) == 0:
                category = character[random.randint(3, 5)]

            your_item = category[random.randint(0, len(category) - 1)]

        if category == character[3]:
            your_item = "(food) " + your_item

        elif len(character[4]) > 1 and category[0] == character[4][0]:
            if your_item == "*pistol*" or your_item == "**assault rifle**":
                your_item = "(gun) " + your_item

            else:
                your_item = "(weapon) " + your_item

        elif len(character[5]) > 0 and category[0] == character[5][0]:
            your_item = "(meds) " + your_item

        elif category[0] == character[9][0]:
            your_item = your_item

        elif category in current_clothing:
            your_item = "(clothing) " + your_item

    if count == 0:
        return None

    else:
        return your_item


def get_card(card):
    read_card = "The card is the "
    if card[0] == "A":
        read_card += "Ace of "
        value = 11

    elif card[0] == "K":
        read_card += "King of "
        value = 10

    elif card[0] == "Q":
        read_card += "Queen of "
        value = 10

    elif card[0] == "J":
        read_card += "Jack of "
        value = 10

    else:
        if card[0] == "1":
            read_card += "10 of "
            value = 10

        else:
            read_card += card[0] + " of "
            value = int(card[0])


    if card[-1] == "H":
        read_card += "Hearts"

    elif card[-1] == "C":
        read_card += "Clubs"

    elif card[-1] == "D":
        read_card += "Diamonds"

    elif card[-1] == "S":
        read_card += ("Spades")

    read_card += "\n"

    print(read_card)
    return(value)


def play_blackjack(name):
    print("You've chosen to play Blackjack with", name)
    line_break

    your_hand = 0
    opp_hand = 0

    print()
    print(name, "deals you a card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    your_hand += value

    print(name, "deals you another card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    if value == 11:
        if (your_hand + value) > 21:
            value = 1
    your_hand += value

    print("Your hand is now worth", your_hand)
    input("\nPress 1 to continue: ")
    print(line_break)

    print(name, "deals himself a card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    opp_hand += value

    print(name, "deals himself another card")
    card = card_list[random.randint(0, len(card_list) - 1)]
    card_list.remove(card)
    value = get_card(card)
    if value == 11:
        if (opp_hand + value) > 21:
            value = 1
    opp_hand += value

    print("His hand is now worth", opp_hand)
    input("\nPress 1 to continue: ")
    print(line_break)

    your_hit = True
    opp_hit = True
    win = None
    print_score = True

    while your_hit == True or opp_hit == True:
        if your_hit == True:
            print("Your hand is worth", your_hand)
            if opp_hit == False and print_score == True:
                print("His hand is worth", opp_hand)
            print("\nWill you:\n1. Hit\n2. Hold")
            choice = make_choice()

            if choice == 1:
                print("You choose to hit\n")
                print(name, "deals you another card")
                card = card_list[random.randint(0, len(card_list) - 1)]
                card_list.remove(card)
                value = get_card(card)
                if value == 11:
                    if (your_hand + value) > 21:
                        value = 1

                your_hand += value

                print("Your hand is now worth", your_hand)
                input("\nPress 1 to Continue: ")
                print(line_break)
                if your_hand > opp_hand:
                    opp_hit = True

                if your_hand >= 21:
                    if your_hand > 21:
                        print("You've gone bust")

                        win = False
                        return win

            elif choice == 2:
                print("You choose to hold")
                your_hit = False

        if your_hand > opp_hand:
            opp_hit == True

        if opp_hit == True and win is None:
            if win != False:
                if your_hand > opp_hand:
                    hit_chance = 1

                elif opp_hand > 18:
                    hit_chance = 0

                elif opp_hand == 18:
                    hit_chance = random.randint(1, 20)

                elif 15 <= opp_hand < 18:
                    hit_chance = random.randint(1, 3)

                elif 12 <= opp_hand < 15:
                    hit_chance = random.randint(1, 2)
                    if hit_chance != 1:
                        hit_chance = random.randint(1, 3)

                else:
                    hit_chance = 1

                if hit_chance == 1:
                    print(name, "deals himself another card")
                    card = card_list[random.randint(0, len(card_list) - 1)]
                    card_list.remove(card)
                    value = get_card(card)
                    if value == 11:
                        if (opp_hand + value) > 21:
                            value = 1
                    opp_hand += value

                    print("His hand is now worth", opp_hand)
                    print_score = False

                    if opp_hand >= 21:
                        if opp_hand > 21:
                            print("He's gone bust")
                            your_hit = False

                        opp_hit = False

                    elif opp_hand > your_hand and your_hit == False:
                        opp_hit = False
                        your_hit = False

                else:
                    if your_hand < 22:
                        print(name, "chooses to hold\n")
                        opp_hit = False
                        print_score = True

        elif win is None:
            if your_hand < 22:
                print(name, "chooses to hold")
                opp_hit = False
                print_score = True

    input("\nPress 1 to Continue: ")
    print(line_break)

    if your_hand == opp_hand:
        win = "Draw"

    elif your_hand > 21 or opp_hand > 21:
        if your_hand > 21:
            win = False

        else:
            win = True

    elif your_hand > opp_hand:
        win = True

    else:
        win = False

    return win


def armour_val(armour):
    if armour == head_armour[0]:
        return 20

    elif armour == head_armour[1]:
        return 30

    elif armour == torso_armour[0]:
        return 150

    elif armour == torso_armour[1]:
        return 60

    elif armour == torso_armour[2]:
        return 75

    elif armour == torso_armour[3] or armour == torso_armour[6]:
        return 20

    elif armour == torso_armour[4]:
        return 40

    elif armour == torso_armour[5]:
        return 125

    elif armour == leg_armour[0]:
        return 10

    elif armour == foot_armour[0]:
        return 15
    
    elif armour == foot_armour[1]:
        return 10

    elif armour == hand_armour[0]:
        return 50

    elif armour == hand_armour[1]:
        return 5


def equip_armour(armour,total_armour):
    if armour in head_armour:
        if len(current_clothing[0]) > 0:
            character[8][0].append("(clothing) " + current_clothing[0][0])
            total_armour -= armour_val(current_clothing[0][0])
            print("Your", current_clothing[0][0], "has been placed in your inventory")
            current_clothing[0].remove(current_clothing[0][0])

        current_clothing[0].append(armour)

    elif armour in torso_armour:
        if len(current_clothing[1]) > 0:
            character[8].append("(clothing) " + current_clothing[1][0])
            total_armour -= armour_val(current_clothing[1][0])
            print("Your", current_clothing[1][0], "has been placed in your inventory")
            current_clothing[1].remove(current_clothing[1][0])

        current_clothing[1].append(armour)

    elif armour in leg_armour:
        if len(current_clothing[2]) > 0:
            character[8][0].append("(clothing) " + current_clothing[2][0])
            total_armour -= armour_val(current_clothing[2][0])
            print("Your", current_clothing[2][0], "has been placed in your inventory")
            current_clothing[2].remove(current_clothing[2][0])

        current_clothing[2].append(armour)

    elif armour in foot_armour:
        if len(current_clothing[3]) > 0:
            character[8][0].append("(clothing) " + current_clothing[3][0])
            total_armour -= armour_val(current_clothing[3][0])
            print("Your", current_clothing[3][0], "has been placed in your inventory")
            current_clothing[3].remove(current_clothing[3][0])

        current_clothing[3].append(armour)

    elif armour in hand_armour:
        if len(current_clothing[4]) > 0:
            character[8][0].append("(clothing) " + current_clothing[4][0])
            total_armour -= armour_val(current_clothing[4][0])
            print("Your", current_clothing[4][0], "has been placed in your inventory")
            current_clothing[4].remove(current_clothing[4][0])

        current_clothing[4].append(armour)

    armour_added = armour_val(armour)
    total_armour += armour_added

    print("You are now wearing the", armour, "for", armour_added, "armour")
    print("Your total armour is now", total_armour)
    character[8].remove("(clothing) " + armour)

    return total_armour


def remove_item(item):
    if item[0:2] == "(m":
        character[5].remove(item[7:])

    elif item[0:2] == "(f":
        character[3].remove(item[7:])

    elif item[0:2] == "(w":
        weapon_durability.remove(weapon_durability[character[4].index(item[9:]) - 1])
        max_weapon_durability.remove(max_weapon_durability[character[4].index(item[9:]) - 1])
        character[4].remove(item[9:])

    elif item[0:2] == "(g":
        character[4].remove(item[6:])

    elif item[0:2] == "(c":
        if item in character[8]:
            character[8].remove(item)

        else:
            for i in current_clothing:
                for j in i:
                    if j == item[12:]:
                        i.remove(item[12:])

def cook_food():
    cook_check =  False
    ingredients = character[3]
    cook_list = []

    if "chicken" in ingredients and "pasta" in ingredients and "tomato sauce" in ingredients:
        cook_check = True
        cook_list.append("chicken and pasta")

    if "sausages" in ingredients and "pasta" in ingredients and "tomato sauce" in ingredients:
        cook_check = True
        cook_list.append("sausage and pasta")

    if "strawberries" in ingredients and ("banana" in ingredients or "apple" in ingredients) and "can of whipped cream" in ingredients:
        cook_check = True
        cook_list.append("fruit and cream")

    if "can of tuna" in ingredients and "bread" in ingredients:
        cook_check = True
        cook_list.append("tuna sandwiches")

    if "chicken" in ingredients and "beef jerky" in ingredients and "bread" in ingredients:
        cook_check = True
        cook_list.append("chicken and beef sandwiches")

    if "chicken" in ingredients and "MRE" in ingredients:
        cook_check = True
        cook_list.append("deluxe MRE")

    if "can of peaches" in ingredients and "can of whipped cream" in ingredients:
        cook_check = True
        cook_list.append("peaches and cream")

    if "cereal" in ingredients and "bag of marshmallows" in ingredients and "butter" in ingredients:
        cook_check = True
        cook_list.append("cereal treats")

    if "bag of rice" in ingredients and "chicken" in ingredients and "carrots" in ingredients and "spring onions" in ingredients:
        cook_check = True
        cook_list.append("chicken stir-fry")

    if "bag of rice" in ingredients and ("chicken" in ingredients or "venison" in ingredients) and "condensed milk" in ingredients and "spring onions" in ingredients and "mushrooms" in ingredients:
        cook_check = True
        if "chicken" in ingredients:
            cook_list.append("chicken casserole")

        if "venison" in ingredients:
            cook_list.append("venison casserole")

    if "venison" in ingredients and "mushrooms" in ingredients and "carrots" in ingredients and "can of soup" in ingredients and "spring onions" in ingredients:
        cook_check = True
        cook_list.append("venison stew")

    if "oats" in ingredients and "condensed milk" in ingredients and "strawberries" in ingredients and "honey" in ingredients:
        cook_check = True
        cook_list.append("overnight oats")

    if "bag of rice" in ingredients and "condensed milk" in ingredients:
        cook_check = True
        cook_list.append("rice pudding")

    if "pre-made meal" in ingredients and "MRE" in ingredients:
        cook_check = True
        cook_list.append("mega MRE")

    if "bag of marshmallows" in ingredients and "biscuits" in ingredients and "box of chocolates" in ingredients:
        cook_check = True
        cook_list.append("smores")

    if "egg" in ingredients and "butter" in ingredients:
        egg_count = 0
        for i in ingredients:
            if i == "egg":
                egg_count += 1

        if egg_count >= 3:
            cook_list.append("omelette")

    if cook_check == True:
        print("It looks like you have enough ingredients to do some cooking:\n1. Cook\n2. Don't cook")
        choice = make_choice()

        if choice == 1:
            count = 1
            print("What would you like to cook?")
            for i in cook_list:
                print(str(count) + ". " + i)
                count += 1
            print(str(count) + ". nothing")

            choice = make_choice()

            if choice != (count):
                recipe = cook_list[choice - 1]

                if recipe == "chicken and pasta":
                    remove_list = ["chicken", "pasta", "tomato sauce"]
                    portion = 2

                elif recipe == "omelette":
                    remove_list = ["egg", "egg", "egg", "butter"]
                    portion = 1

                elif recipe == "sausage and pasta":
                    remove_list = ["sausages", "pasta", "tomato sauce"]
                    portion = 2

                elif recipe == "fruit and cream":
                    remove_list = ["strawberries", "can of whipped cream"]

                    if "apple" in ingredients:
                        remove_list.append("apple")

                    else:
                        remove_list.append("banana")

                    portion = 2

                elif recipe == "tuna sandwiches":
                    remove_list = ["can of tuna", "bread"]
                    portion = 2

                elif recipe == "chicken and beef sandwiches":
                    remove_list = ["chicken", "beef jerky", "bread"]
                    portion = 4

                elif recipe == "deluxe MRE":
                    remove_list = ["chicken", "MRE"]
                    portion = 1

                elif recipe == "peaches and cream":
                    remove_list = ["can of peaches", "can of whipped cream"]
                    portion = 2

                elif recipe == "cereal treats":
                    remove_list = ["cereal", "bag of marshmallows", "butter"]
                    portion = 2

                elif recipe == "chicken stir-fry":
                    remove_list = ["bag of rice", "chicken", "spring onions", "carrots"]
                    portion = 2

                elif recipe == "chicken casserole":
                    remove_list = ["condensed milk", "chicken", "spring onions", "mushrooms"]
                    portion = 2

                elif recipe == "venison casserole":
                    remove_list = ["condensed milk", "venison", "spring onions", "mushrooms"]
                    portion = 2

                elif recipe == "venison stew":
                    remove_list = ["venison", "mushrooms", "carrots", "can of soup"]
                    portion = 2

                elif recipe == "overnight oats":
                    remove_list = ["oats", "honey", "condensed milk", "strawberries"]
                    portion = 4

                elif recipe == "mega MRE":
                    remove_list = ["MRE", "pre-made meal"]
                    portion = 1

                elif recipe == "rice pudding":
                    remove_list = ["bag of rice", "condensed milk"]
                    portion = 4

                elif recipe == "smores":
                    remove_list = ["biscuits", "bag of marshmallows", "box of chocolates"]
                    portion = 4

                for i in remove_list:
                    character[3].remove(i)

                for i in range(portion):
                    character[3].append(recipe)

                if portion == 1:
                    print("Nice, you cooked up '" + recipe + "'")

                else:
                    print("Nice, you cooked " + str(portion) + " portions of '" + recipe + "'")

                if character[7][0] == "restaurant":
                    print("Since you're cooking at the restaurant, your food is a little better than expected\n")

                else:
                    print()


def take_rest(medical_prompt):
    print("You'll be taking some rest today")

    if medical_prompt != "":
        if len(afflictions) > 0:
            print("You lie down and try get some sleep")
            print("Hopefully your", medical_prompt, "will heal and you'll be able to go out tomorrow\n")

            if character[7][0] == "house":
                print("Since you're resting in your comfy bed, you should have a better chance of healing")

            for i in afflictions:
                if character[7][0] == "house":
                    chance = random.randint(1, 2)

                else:
                    chance = random.randint(1, 3)
                if chance == 1:
                    print("Your", i, "has healed")
                    afflictions.remove(i)

                else:
                    print("Your", i, "hasn't healed")

        if character[0][0] < 100:
            chance = random.randint(1, 2)
            if chance == 1:
                HP_healed = random.randint(1, 25)
                print("You gained", HP_healed, "HP")
                character[0][0] += HP_healed

                if character[0][0] > 100:
                    character[0][0] = 100

                print("You now have", character[0][0], "/ 100 HP")

    else:
        print("You don't quite know why you chose to rest today, but everyone deserves a day off...")


def journal_entry(day, info):
    journal_entry = "Day " + str(day) + " - " + info
    journal.append(journal_entry)


def eat_food():
    calories_used = random.randint(1400,2000)
    character[2][0] = character[2][0] - calories_used
    if character[2][0] < 0:
        character[2][0] = 0
    print("Today you used", calories_used, "calories")
    print("You have", character[2][0], "calories left\n")

    cook_food()

    print("Would you like to eat something?\n1. Yes\n2. No, it's time to sleep")
    choice = make_choice()

    if choice == 1:
        eat = True

        while character[2][0] < 5000 and eat is True and len(character[3])> 0:
            temp_food_list = character[3]
            food_checked = []
            multiple_foods = []
            food_list = []
            numbers = ["1","2","3","4","5","6","7","8","9","0"]

            for i in temp_food_list:
                food = i
                count = 0

                if food not in food_checked:
                    for j in temp_food_list:
                        if j == food:
                            count += 1

                food_checked.append(food)

                if count > 1:
                    multiple_foods.append(food)
                    food = str(count) + "x " + food
                    food_list.append(food)
                
                elif food not in multiple_foods:
                    food_list.append(food)

            print("You have:")
            count = 1
            for i in food_list:
                if i[0] not in numbers and i[1] not in numbers:
                    print(str(count) + ". " + i + " - " + str(get_cals(i)) + " calories")

                elif i[0] in numbers and i[1] not in numbers:
                    print(str(count) + ". " + i + " - " + str(get_cals(i[3:])) + " calories each")

                else:
                    print(str(count) + ". " + i + " - " + str(get_cals(i[4:])) + " calories each")

                count += 1

            if len(character[3]) > 1:
                print(str(count) + ". " + "Consume all")

            choice = make_choice()
            if choice == count:
                total_cals = 0

                for i in character[3]:
                    total_cals += get_cals(i)

                character[3] = []

                print("You consumed everything for", total_cals, "calories")
                character[2][0] += total_cals
                print("You now have:", character[2][0], "calories")
                eat = False

            else:
                if food_list[choice - 1][0] in numbers and food_list[choice - 1][1] not in numbers:
                    food_eaten = food_list[choice - 1][3:]

                elif food_list[choice - 1][0] and food_list[choice - 1][1] in numbers:
                    food_eaten = food_list[choice - 1][4:]

                else:
                    food_eaten = food_list[choice - 1]
 
                character[2][0] += get_cals(food_eaten)
                print("You consumed:", food_eaten, "for", get_cals(food_eaten),"calories")
                character[3].remove(food_eaten)

                print("You now have:", character[2][0], "calories\n")
                print("Do you want to eat more?\n1. Yes\n2. No, it's time to sleep")
                choice = make_choice()
                if choice == 2:
                    eat = False

        if len(character[3]) == 0 and eat == True:
            print("You have no food")


def loot_car(car):
    fuel_chance = random.randint(1, 3)

    chance = random.randint(1, 2)
    if chance == 1:
        if car != "Police Cruiser":
            print("You spend a few minutes looting the", car, "and find:")
            random_item(2, 4, "normal", "no fuel")

        else:
            print("You spend a few minutes looking around the interior and don't find much")
            print("Before you leave, you pop the boot and find:")

            chance = random.randint(1, 3)

            if chance == 1:
                print("(gun) *pistol*")
                print("(ammo) *10 pistol bullets*")
                add_item("(gun) *pistol*")
                add_item("(ammo) *10 pistol bullets*")

            elif chance == 2:
                print("(clothing) *police vest*")
                print("(food) MRE")
                add_item("(clothing) *police vest*")
                add_item("(food) MRE")

            else:
                random_item(1, 4, "normal", "no fuel")
                random_item(1, 2, "normal", "meds")

        print("\nYou take these items and check if there's anything left in the tank")
        if fuel_chance == 1:
                print("Looks like you got very lucky today, there's still some fuel left:")

                chance = random.randint(1, 2)
                if chance == 1:
                    fuel = "(fuel) 1 litre of fuel"

                else:
                    fuel = "(fuel) 2 litres of fuel"

                print(fuel)
                add_item(fuel)

        else:
            print("Looks like this car was siphoned already, or just ran out of fuel")

    else:
        print("You check everywhere in the", car, "but there's nothing to be found")
        print("You're disappointed, but you'll still check if there's anything left in the tank\n")

        if fuel_chance == 1:
                print("It's not all bad, there's still some fuel left:")

                chance = random.randint(1, 2)
                if chance == 1:
                    fuel = "(fuel) 1 litre of fuel"

                else:
                    fuel = "(fuel) 2 litres of fuel"

                print(fuel)
                add_item(fuel)

        else:
            print("Unlucky, looks like this car was siphoned already, or just ran out of fuel")

    input("\nPress 1 to continue: ")
    print(line_break)


def filler_loot():
    print("\nDespite your difficulties, you still manage to scrape up something:")
    random_item(1, 2, "normal", "no rot")


def fight_killer(enemy, ally, killer, total_armour):
    print("You join " + ally + "'s" + " side and prepare to fight")
    print(enemy, "looks at you in disbelief, insisting you're making a mistake")
    print("But", ally, "tells you not to listen to him\n")

    chance = random.randint(1, 2)

    if chance == 1:
        print("Suddenly", enemy, "charges at", ally, "and delivers a blow that knocks him to the ground")
        print("It looks like this fight is between you and", enemy)

        result = fight(1, "humans", enemy, total_armour)

        if result:
            print(enemy, "falls to the ground dead")
            if enemy == killer:
                print("You search his pockets, and sure enough there's a bloody knife\n")

            else:
                print("You search his pockets, but there's no knife")
                print("He wasn't the killer!\n")

            chance = random.randint(1, 2)

            if chance == 1:
                if ally == killer:
                    print("You spin around, but the real killer", ally, "is dead, killed by the blow from", enemy)
                    print("It seems that before you killed him,", enemy, "saved your life...")

                else:
                    print("Glad that the killer is finally dead, you turn to help up", ally, "but he's dead too")
                
                print("It looks like you're the only one left alive")     

            else:
                if ally == killer:
                    print("You spin around and see", ally, "struggling to get up, with an evil glare on his face")
                    print("But he's almost dead, and you take the opportunity to make sure of it")
                    print("It looks like you're the only one left alive")

                else:
                    print("You're glad the killer has been taken care of, but when you turn around", ally, "is struggling to get up")
                    print("He's been hurt bad and needs medicine\n")
                    if len(character[5]) > 0:
                        print("You have some medicine in your bag, and can save him")
                        print("Click the corresponding button to select an item")
                        print("You have:")
                        count = 1
                        for i in character[5]:
                            print(str(count) + ". " + i)
                            count += 1
                        choice = make_choice()
                        print("You give him", character[5][choice - 1])
                        character[5].remove(character[5][choice - 1])

                        print("He thanks you for saving his life, and trusting him")
                        print("He promises to try help you in the future")
                        survivor_group = [ally]
                        character[6].append(survivor_group)
                        print(ally, "is now your Friend")
                        print("\nHe's had enough and leaves the old building, but you decide to stay back")

                    else:
                        print("You tell him you don't have any medicine and he nods and closes his eyes")
                        print("In his final moments he thanks you for your trust, and for fighting by his side")
                        print("Putting him down gently, it looks like you were the only one who survived...")

                return True

        else:
            return False

    else:
        print("You take his advice and a fight ensues")
        print("\nWith superior numbers on your side it doesn't take long, and", enemy, "lies dead before you")

        if ally == killer:
            chance = random.randint(1, 2)
            
            if chance == 1:
                print("But when you turn to look at " + ally + "," + " he's staring back with an evil grin")
                print("You killed the wrong person!")
                print("He dashes at you and it looks like another fight!\n")

                result = fight(1, "humans", ally, total_armour)
                
                if result:
                    print("Sure enough, you find a bloody knife on his corpse")
                    print("It looks like you stopped the killer, but you let him trick you into killing", enemy)

                else:
                    return False

            else:
                print("You check " + enemy + "'s" + " body, but you don't find anything\n")
                print("You're about to turn around and ask", ally, "when he grabs you and slices your throat...\nYOU DIED")
                return False
        
        else:
            print("Sure enough, you find a bloody knife on his corpse and", ally, "nods at you")
            print("It looks like you stopped the killer\n")
            print(ally, "thanks you for your trust and for fighting alongside him")
            print("He promises to try help you in the future")
            survivor_group = [ally]
            character[6].append(survivor_group)
            print(ally, "is now your Friend")
            print("\nHe's had enough and decides to leave the old building behind, but you decide to stay")

            return True


def food_search(group_num, day, group=None, victim=None):
    canteen_loot = ["(food) can of soup", "(food) condensed milk", "(food) can of peaches", "(food) can of beans", "(food) can of tuna", "(food) instant noodles"]
    if group_num == 1:
        print("Opening the door, you find yourself in what looks to be supply for the canteen")
        loot_amount = random.randint(5, 7)
        print("The place isn't in great shape, but you still manage to find:")
        for i in range(loot_amount):
            food = canteen_loot[random.randint(0, len(canteen_loot) - 1)]
            print(food)
            add_item(food)

        print("\nWith the food in your bag, you leave this place and head back to the", character[7][0])
        journal_entry(day, "Stopped a killer and found some food in an old government building")

    else:
        print("The", group_num, "of you decide to take a look around the old building")
        survivor = group[random.randint(0, len(group) - 1)]
        print("You're searching the area", victim, "was supposed to search when you spot a door chained shut")
        print("Checking some of the neighbouring offices,", survivor, "finds a key\n")
        print("Opening the door, you find yourselves in what looks to be supply for the canteen")
        print("You split the food evenly, and end up with:")
        loot_amount = random.randint(4, 6)

        for i in range(loot_amount):
            food = canteen_loot[random.randint(0, len(canteen_loot) - 1)]
            print(food)
            add_item(food)

        print("\nAfter packing the food in your bag, you say goodbye and head home")
        journal_entry(day, "Looted an old government building with a group and found some food")

def weapon_search(killer, day):
    input("\nPress 1 to continue: ")
    print(line_break)
    print("It's just you left in the building, and you decide to take a look around")
    print("You're checking the area", killer, "was supposed to search, when you spot a door chained shut")
    print("It seems", killer, "didn't care enough to report back about it, he had other plans\n")
    print("Searching around, you find a key in one of the offices\n")

    chance = random.randint(1, 3)

    if chance == 1:
        food_search(1, day)

    elif chance == 2:
        print("Opening the door, you find yourself in what looks to be storage for medical supplies")
        pharmacy_loot = ["(meds) bandages", "(meds) painkillers", "(meds) first aid kit"]
        loot_amount = random.randint(3, 5)

        for i in range(loot_amount):
            meds = pharmacy_loot[random.randint(0, len(pharmacy_loot) - 1)]
            print(meds)
            add_item(meds)

        print("\nWith the medical supplies in your bag, you leave this place and head back to the", character[7][0])
        journal_entry(day, "Stopped a killer and found some supplies in a medical storage room")

    else:
        print("You open the door, and it looks the security office they were talking about")
        print("You take a look through the lockers and find:")
        chance = random.randint(1, 2)

        if chance == 1:
            security_loot = ["(ammo) *3 pistol bullets*", "(ammo) *5 pistol bullets*", "(ammo) *10 pistol bullets*", "(clothing) *police vest*"]
            loot_amount = random.randint(2, 3)

            for i in range(loot_amount):
                item = security_loot[random.randint(0, len(security_loot) - 1)]
                print(item)
                add_item(item)

        else:
            print("(gun) *pistol*")
            add_item("(gun) *pistol*")

            chance = random.randint(1, 3)

            if chance == 1:
                print("(ammo) *20 pistol bullets*")
                add_item("(ammo) *20 pistol bullets*")

            else:
                print("(ammo) *10 pistol bullets*")
                add_item("(ammo) *10 pistol bullets*")

        print("\nTaking the supplies from the security office, you head back to the", character[7][0])
        journal_entry(day, "Stopped a killer and found some supplies in a security office")


def killer_return(killer):
    chance = random.randint(1, 2)

    if chance == 1:
        enemy_group = [killer]
        enemy_list.append(enemy_group)
        killer_list.append(killer)


def fire_escape_exit(survivor, survivor2, killer, bag_items, total_armour):
    zombies_killed_in_func = 0

    print("Deciding against the main door, you look for an alternative and spot signs pointing towards a fire exit")
    print("Hopeful of a way out, you hurry along until you reach a room with a large window on the wall")
    print("It's slightly ajar, and light shines through the dusty air\n")
    input("Press 1 to continue: ")
    print(line_break)
    print("You push the window open and peer out, it's a fire escape!")
    print("Stepping out and looking down into the alleyway, you see it's full of zombies!")
    print("Taking care not to make any noise, you make your way down the narrow stairway\n")

    chance = random.randint(1, 2)

    if chance == 1:
        print("But someone jumps out the window above you and races down the stairs!")
        
        chance = random.randint(1, 2)

        if chance == 1:
            last_survivor = survivor

        else:
            last_survivor = survivor2

        print("It's " + last_survivor + "!")

        print("He sees you and goes to shout something but slips and tumbles off the side")
        print("Just about managing to hold on, he swings high above the ground")
        print(last_survivor, "shouts in fear as he sees the zombies gathered below him and begs for your help")
        print("Will you:\n1. Save him\n2. Leave him for the zombies")

        choice = make_choice()

        if choice == 1:
            print("You can't just let him die like this, grabbing his arm and pulling him up")

            if last_survivor != killer:
                print("He thanks you profusely, but you still need to get yourselves out of this mess")
                print(last_survivor, "grabs you and points toward a gap near the end of the alleyway\n")
                print("It looks like his fall brought most of the zombies underneath you")
                print("Thinking quick, the pair of you slide down the fire escape ladder and make a run for it\n")
                input("Press 1 to continue: ")
                print(line_break)

                chance = random.randint(1, 2)

                if chance == 1:
                    print("Somehow the two of you make it through and get away from the dozens of undead unharmed")
                    print("You've saved", survivor, "and he owes you his life\n")
                    print("He opens up his bag and gives you:")
                    random_item(3, 6, "normal", "no rot")
                    survivor_group = [last_survivor]
                    character[6].append(survivor_group)
                    print()
                    print(last_survivor, "is now your Friend")
                    print("\nAfter this you say goodbye and head home, glad to have escaped this place in one piece")

                    log = "Had to escape a killer through a horde of zombies, but made a new friend named " + last_survivor
                    killer_return(killer)
                    journal_entry(day, log)

                else:
                    print("But you're not fast enough, and the zombies begin to close around you!")
                    chance = random.randint(1, 2)

                    if chance == 1:
                        print("An undead hand grabs you and pulls you back, but", last_survivor, "hacks it off and helps you up")
                        print("The two of you are surrounded now and as you prepare for a last stand,", last_survivor, "nods at you and wishes you good luck\n")
                        print("Before you can say anything he charges into the group of zombies and they pool around him")
                        print("A gap opens up in the wall of zombies and you punch through, thanking him for his sacrifice\n")
                        print("You get away unscathed, and on your way back home your mourn today's victims...")

                        journal_entry(day, "A survivor sacrificed himself so I could escape a horde of zombies")

                    else:
                        print("Looks like you'll have to fight your way through!")
                        zom_num = random.randint(3, 6)

                        result = fight(zom_num, "zombies")

                        if result:
                            zombies_killed_in_func += zom_num

                            print("You've made it out the other side, and as you turn back you see", last_survivor, "has too")
                            print("The pair of you exit the alleyway and lose the zombies, before stopping to catch your breath\n")
                            print("You've saved", survivor, "and he owes you his life")
                            print("He opens up his bag and gives you:")
                            random_item(3, 6, "normal", "no rot")
                            survivor_group = [last_survivor]
                            character[6].append(survivor_group)
                            print()
                            print(last_survivor, "is now your Friend")
                            print("\nAfter this you say goodbye and head home, glad to have escaped this place in one piece")

                            log = "Had to fight through a horde of zombies to escape a killer, but made a new friend named " + last_survivor
                            killer_return(killer)
                            journal_entry(day, log)

                        else:
                            return False

            else:
                print("But he doesn't thank you, and instead flashes an evil grin")
                print(last_survivor, "was the killer all along!\n")
                result = fight(1, "humans", last_survivor, total_armour)

                if result:
                    print("The killer lies dead and the zombies swarm below you")
                    print("Picking up his body, you heave it over the rails and drop it into their outstretched hands")
                    print("Using it as a distraction you manage to escape, you can't risk heading back into the building now the zombies know you're here...")

                    print("Heading back to the", character[7][0], "you think about what happened today...")

                    journal_entry(day, "Took care of a killer and used his body to distract a horde of zombies")

                else:
                    return False
        
        else:
            print("You never trusted him, and you watch as his grip weakens and he falls to his death")
            print("As soon as his body hits the ground he's swarmed by zombies and you turn to make your escape")
            print("You slide down the ladder and run for the street\n")

            chance = random.randint(1, 2)

            if chance == 1:
                zom_num = random.randint(2, 3)
                print("But there are", zom_num, "zombies in your way!")

                result = fight(zom_num, "zombies")

                if result:
                    zombies_killed_in_func += zom_num
                    print("You fight your way through, taking one last look back at the old building before heading home...")

                else:
                    return False
            
            else:
                print("It looks like all the zombies are distracted with " + last_survivor + "'s body")
                print("Your path is clear and you head home unscathed, wondering if you made the right choice...")

            journal_entry(day, "I didn't help a survivor and he fell to his death, but he could have been a killer")

    else:
        print("They haven't noticed you yet, and you manage to climb down and hide behind some bins without making any noise")
        print("The zombies are mostly gathered around the far end of the alleyway, looks like you might be able to sneak through\n")
        print("You stick to the shadows and begin to sneak up the alleyway")
        
        if len(zombie_survivors) > 0:
            missing_friend = False
            print("Hearing movement to your right, you stare directly into the eyes of a familiar zombie")
            if len(zombie_survivors) > 1:
                named_zombie_group = zombie_survivors[random.randint(0, len(zombie_survivors) - 1)]
                named_zombie = named_zombie_group[0]

            else:
                named_zombie_group = zombie_survivors[0]
                named_zombie = named_zombie_group[0]

            if len(named_zombie_group) > 1:
                missing_friend = True
                named_zombie2 = named_zombie_group[1]

            print("\nIt's " + named_zombie + "!\n")
            if missing_friend:
                enemy_group = [named_zombie2, named_zombie]
                enemy_list.append(enemy_group)

                print("But his friend", named_zombie2, "is nowhere to be seen...")

            print("He snarls and shambles towards you, alerting the rest")
            zom_num = random.randint(2, 4)
            print("Turning to run, you find yourself facing", str(zom_num + 1), "zombies\n")
            print("Looks like you'll be fighting your way through anyway...\n")

            result = fight(zom_num, "zombies")

            if result:
                zombies_killed_in_func += zom_num
                print("With nearly all the zombies in your path dead, only", named_zombie, "remains")
                zom_num = 1

                result = fight(zom_num, "zombies", named_zombie)

                if result:
                    zombies_killed_in_func += zom_num
                    if named_zombie == "the Thief":
                        print("You grab your bag off its back and run off")
                        print("When you're sure you're not being followed you check it, and everything's there")
                        for i in bag_items:
                            add_item(i)
                            bag_items.remove(i)

                    else:
                        print("You look back down at", named_zombie, "then break into a sprint, leaving the zombies in the dust")

                    log = "While escaping a killer I came face to face with the undead corpse of " + named_zombie
                    killer_return(killer)
                    journal_entry(day, log)

                    print("Heading home, you count yourself lucky for escaping unharmed")

                else:
                    return False
            
            else:
                return False

        else:
            print("You creep around a burnt out car, only to find a zombie slouched behind it!")
            print("It growls, but you haven't alerted the rest just yet\n")

            zom_num = 1

            result = fight(zom_num, "zombies")

            if result:
                zombies_killed_in_func += zom_num

                print("The zombie is dead, and thankfully none of the others noticed")
                print("Somehow you manage to slip by the rest, and head home to the", character[7][0])
                print("But the killer is still out there somewhere...")

                journal_entry(day, "Had to stealthily kill a zombies to escape a killer")

                killer_return(killer)

            else:
                return False
    
    return zombies_killed_in_func


def window_exit(survivor, survivor2, killer, total_armour):
    run_for_it = False

    print("You ask him why and he explains that someone locked the main door, he believes it was", survivor)
    print("He would have to smash a window to escape, and was afraid someone would hear")
    print("That seems to check out and the pair of you make your way towards a window in a nearby room")

    chance = random.randint(1, 3)

    if chance == 1 or survivor2 == killer:
        print("\nBut as you walk behind him you notice his shoes are flecked with blood")
        print("Will you:\n1. Ask him about the blood\n2. Make a run for it")
        choice = make_choice()

        if choice == 2:
            killer = survivor2
            run_for_it = True

        else:
            print("You ask him about the blood and he stops and grins")
            print("He shows you a cut on his palm and explains he tried to crack the glass earlier and cut himself")
            print("Will you:\n1. Follow him to the window\n2. Make a run for it")
            choice = make_choice()

            if choice == 2:
                run_for_it = True
                killer = survivor2

    else:
        print("You don't see any sign of", survivor, "on your way and you get there with no hassle")

    if run_for_it:
        print("Thinking quick you dash the opposite way down the hall")
        print("Turning the corner you nearly trip on the body of", survivor)
        print("His throat has been slit and he's dead in a pool of blood!")
        print("You spin around and", killer, "rounds the corner, leaping over the body\n")

        result = fight(1, "humans", killer, total_armour)

        if result:
            print(killer, "lies dead, on his body you find the key for the front door and in his bag you find:")
            random_item(2, 5, "normal", "no rot")
            random_item(0, 1, "special")

            print("\nThe old building is quiet now, and you'll take another look around before you go")
            weapon_search(killer)

        else:
            return False

    else:
        print("Entering the room, you see it's well lit by the large window in the centre")
        print("There's a slight crack in it, and you should be able to smash it open")
        print("It looks like", survivor2, "was telling the truth\n")
        input("Press 1 to continue: ")
        print(line_break)

        if survivor2 == killer:
            print("But as you climb up on a desk and look through the window, you notice it's barred")
            print(survivor2, "never meant to escape and before you can react, he pulls you down and stabs you in the neck...\nYOU DIED")
            
            return False

        else:
            print("You climb up on a desk and look through the window, looks like you can jump down from here")
            print("Smashing the glass with a paperweight, you climb through")
            chance = random.randint(1, 2)

            if chance == 1:
                print("Next up is", survivor2, "and he pushes himself through headfirst before toppling into the bushes outside")
                print("He gets up and smiles at you, thanking you for trusting him")
                print("Before he leaves he opens his bag and gives you:")
                random_item(3, 6, "normal", "no rot")

                print("You thank him and head home, but", survivor, "is still out there somewhere...")
                journal_entry(day, "Escaped a killer with the help of another survivor")

            else:
                print("Next up is", survivor2, "and he pushes himself through headfirst before stopping halfway")
                print("You ask him what's wrong, right as he's dragged back inside")
                print("Hearing his screams cut short, you have no choice but to run")
                print("You take a detour home, but", survivor, "is still out there somewhere...")
                journal_entry(day, "Escaped a killer with the help of another survivor, but he didn't make it")

            killer_return(killer)

    return True


def tunnel_exit(survivor, survivor2, killer, not_zombie_liar, total_armour):
    print("You tell him you're looking for a way out now, and he agrees")
    print("He already tried the front door, but someone locked it")
    print("\nBut he knows a different way out")
    print("You tell him to lead the way, and you head down to the ground floor, keeping an eye out for", survivor)
    print("The two of you walk into the conference room, and he pushes aside a couch to reveal a hidden escape route")
    print("It was a tunnel used by the politicians during the outbreak, but", survivor2, "was afraid", survivor, "knew about it")
    print("He says he last saw him upstairs, and now the way should be clear\n")

    chance = random.randint(1, 3)
    run_for_it = False

    if chance == 1 or survivor2 != killer:
        input("Press 1 to continue: ")
        print(line_break)

    else:
        print("But as you walk over to escape tunnel you notice a bloody handprint on the wall behind the couch")
        print("Will you:\n1. Mention it to " + survivor2 + "\n2. Make a run for it")
        choice = make_choice()

        if choice == 1:
            print(survivor2, "asks you what you're waiting for and you point towards the handprint")
            print("His face drops as he notices it, and he turns to you to explain")

            if survivor2 == not_zombie_liar:
                print("He tells you this is where he saw the zombies earlier, and he saw one of them by this couch")
                print("That must have been what left the handprint")

            else:
                print("He tells you to be careful, as the killer may have been looking around here for the escape tunnel")
                print(survivor2, "thinks that", survivor, "must have left the handprint here")

            print("Will you:\n1. Trust " + survivor2 + "\n2. Make a run for it")
            choice = make_choice()

            if choice == 1:
                print("Deciding to trust him, you both head over to the escape tunnel")

            else:
                run_for_it = True

        else:
            run_for_it = True
    
    if survivor2 == killer and not run_for_it:
        print("You lean over to take a look inside and see the body of " + survivor + "," + " before", survivor2, "slices his knife across your throat and pushes you in...\nYOU DIED")

        return False
    
    elif not run_for_it:
        chance = random.randint(1, 2)
        print("You both hop down and begin walking along the dark tunnel, as", survivor2, "takes out his flashlight")

        if chance == 1:
            print("He holds it up and lights up the path, before letting out a low gasp and dropping it to the ground")
            print("You turn around to see a blade jutting from his neck, and", survivor, "standing behind him")
            print("\nYou shout in fear and sprint up the tunnel in the dark, somehow pushing aside the manhole on the other side and escaping")
            print("Horrified at what happened, you run all the way home to the", character[7][0])

            journal_entry(day, "Escaped a killer through a secret tunnel, but I was the only one who made it")

        else:
            print("The murky tunnel is covered in dust and cobwebs, but it's safer than the old building")
            print("Once you reach the end, you push up a manhole and emerge onto the street")
            print("It seems deserted, and he shakes your hand before the two of you go your separate ways")
            print("\nBut before you leave, he thanks you trusting him and promises to repay you in the future\n")
            survivor_group = [survivor2]
            character[6].append(survivor_group)
            print(survivor2, "is now your Friend")
            print("\nYou turn to towards the old government building knowing", survivor, "is somewhere inside, before you head home")

            journal_entry(day, "Escaped a killer with the help of a new friend")

        killer_return(killer)
    
    else:
        print("You pretend to agree with him, before sprinting towards the door")
        print("Turning sharply to the left and you look over your shoulder, and crash right into", survivor)

        if survivor != killer:
            print("\nHe grabs you and pushes you ahead, with the keys for the front door in his other hand")
            print("Checking behind your shoulder again, you see", killer, "run out of the room and give chase")
            print(killer, "was the killer all along!\n")

            print("The pair of you make for the main door, but", killer, "is hot on your heels")

            chance = random.randint(1, 2)

            if chance == 1:
                print("He's almost caught up to you when he trips and tumbles forwards, hitting his head on the tiles")
                print(survivor, "wastes no time, and has the door open before", killer, "can get back up")
                print("The pair of you jump out into the street as he slams the door and locks it\n")

                print("You're not going to stick around, and you thank", survivor, "before hurrying home...")

                journal_entry(day, "Managed to escape a killer with the help of another survivor")

                killer_return(killer)
            
            else:
                print(survivor, "goes to unlock the door, but he's not going to be quick enough")
                print("You're going to have to fight " + killer + "!\n")

                result = fight(1, "humans", killer, total_armour)

                if result:
                    print(survivor, "turns around and gasps when he sees the body")
                    print("\nHe thanks you for fighting off the killer and the pair of you step out into the street")
                    print("Before", survivor, "leaves, he promises to repay you\n")
                    survivor_group = [survivor]
                    character[6].append(survivor_group)
                    print(survivor2, "is now your Friend\n")
                    
                    print("\nBut the old building is quiet now, and you'll take another look around before you go")
                    weapon_search(killer)

                else:
                    return False
        
        else:
            print("He pushes you away, but his eyes widen when he sees", survivor2, "behind you")
            print(survivor2, "shouts at you to get away from him, but", survivor, "insists he's on your side!")
            print("Will you:\n1. Side with " + survivor + "\n2. Side with " + survivor2)
            choice = make_choice()

            if choice == 1:
                ally = survivor
                enemy = survivor2

            elif choice == 2:
                ally = survivor2
                enemy = survivor

            result = fight_killer(enemy, ally)

            if result:
                weapon_search(killer)

            else:
                return False
    
    return True


def repair_weapon(weapon_parts):
    repair_list = []
    count = 0
    weapons_repaired = 0
    repair_list = list(character[4][1:])

    remove_list = []

    for i in repair_list:
        if i == "*pistol*" or i == "**assault rifle**":
            repair_list.remove(i)

    repair_loop = True
    all_repaired = False
    temp_repair_list = []

    while repair_loop:
        save_counts = []
        if weapons_repaired != len(repair_list):
            print("Choose a weapon to repair:")
            count = 1
            weapon_count = 1
            for i in repair_list:
                if weapon_durability[count - 1] < max_weapon_durability[count - 1]:
                    print(str(weapon_count) + ". " + i + " - condition: " + str(weapon_durability[count - 1]) + "/" + str(max_weapon_durability[count - 1]))
                    save_counts.append(count -1)
                    weapon_count += 1
                    temp_repair_list.append(i)
                count += 1
            print(str(weapon_count) + ". " + "Exit")
            weapon_choice = make_choice()

        else:
            all_repaired = True

        if weapon_choice != weapon_count and not all_repaired:
            weapon_chosen = temp_repair_list[weapon_choice - 1]
            print("You have chosen to repair your", weapon_chosen)
            weapon_condition = weapon_durability[save_counts[weapon_choice - 1]]
            max_condition = max_weapon_durability[save_counts[weapon_choice - 1]]

            if weapon_condition == 0:
                cost = 3

            elif weapon_condition < max_condition // 2:
                cost = 2

            else:
                cost = 1

            if cost > 1:
                print("\nIt will cost", cost, "weapon parts to repair")

            else:
                print("\nIt will cost 1 weapon part to repair")
            
            if weapon_parts > 1:
                print("You have", weapon_parts, "parts in your inventory\n")

            else:
                print("You have 1 weapon part in your inventory\n")

            if weapon_parts < cost:
                print("You can't repair this weapon")
                print(line_break)

            else:
                print("Will you:\n1. Repair your", weapon_chosen, "\n2. Choose a different weapon")
                choice = make_choice()

                if choice == 1:
                    weapon_parts -= cost
                    condition_diff = max_condition - weapon_condition
                    
                    weapon_durability[save_counts[weapon_choice - 1]] += condition_diff
                    print("Your", weapon_chosen, "has been repaired")
                    temp_repair_list.remove(temp_repair_list[weapon_choice - 1])
                    weapons_repaired += 1

                else:
                    print("You decide to choose a different weapon")
                
                print(line_break)

        else:
            repair_loop = False

    return weapon_parts


def scrap_weapon():
    print("Choose a weapon to scrap:")
    count = 1
    weapon_count = 1
    for i in character[4]:
        if i != "hands":
            if i != "*pistol*" and i != "**assault rifle**":
                print(str(weapon_count) + ". " + i + " - condition: " + str(weapon_durability[count - 1]) + "/" + str(max_weapon_durability[count - 1]))
                weapon_count += 1
            count += 1
    print(str(weapon_count) + ". " + "Exit")
    choice = make_choice()

    if choice != weapon_count:
        weapon_chosen = character[4][choice]
        print("You have chosen to scrap your", weapon_chosen)

        weapon_condition = weapon_durability[character[4].index(weapon_chosen) - 1]
        max_condition = max_weapon_durability[character[4].index(weapon_chosen) - 1]

        scrap_success = False

        if weapon_condition > (max_condition * 0.8):
            scrap_success = True
        
        elif weapon_condition > (max_condition * 0.5):
            chance = random.randint(1, 3)

            if chance != 1:
                scrap_success = True

        elif weapon_condition > (max_condition * 0.3):
            chance = random.randint(1, 2)

            if chance == 1:
                scrap_success = True
        
        else:
            chance = random.randint(1, 3)

            if chance == 1:
                scrap_success = True

        if scrap_success:
            parts_found = random.randint(1, 3)

            if parts_found > 1:
                print("\nYou've scrapped it and recovered", parts_found, "weapon parts")

            else:
                print("\nYou've scrapped it and recovered 1 weapon part")

        else:
            print("But you weren't able to recover any weapon parts...")
            parts_found = 0

        print(line_break)
        remove_item("(weapon) " + weapon_chosen)
        return [True, parts_found]

    else:
        parts_found = 0
        return [False, parts_found]
    

def crafting_recipes():
    print("You open the book and begin reading:\n")

    print("basic spear:")
    print("Requires a knife, 1 wooden pole, and 1 piece of rope\n")

    print("heavy spear:")
    print("Requires a machete, 1 wooden pole, and 1 piece of rope\n")

    print("quality machete:")
    print("Requires a machete, 2 pieces of leather, 1 weapon part, and 1 piece of rope\n")

    print("heavy hammer:")
    print("Requires a hammer, 4 nails and 3 weapon parts\n")

    print("*tri-blade spear*:")
    print("Requires a machete, 2 knives, a wooden pole, and 2 pieces of rope\n")

    print("*spiked baseball bat*:")
    print("Requires a baseball bat, 10 nails, and the use of a hammer\n")

    print("handmade armour:")
    print("Requires 8 pieces of leather and 2 pieces of rope\n")

    print("handmade boots:")
    print("Requires 2 pieces of leather and 1 piece of rope")

def craft_list(weapon_parts, workshop_satchel):
    craft_list = []
    nails = workshop_satchel[0]
    rope = workshop_satchel[1]
    leather = workshop_satchel[2]
    wood = workshop_satchel[3]

    if "knife" in character[4] and wood >= 1 and rope >= 1:
        craft_list.append("basic spear")

    if "machete" in character[4] and wood >= 1 and rope >= 1:
        craft_list.append("heavy spear")
    
    if "knife" in character[4] and "machete" in character[4] and wood >= 1 and rope >= 2:
        knife_count = 0
        for i in character[4]:
            if i == "knife":
                knife_count += 1
        
        if knife_count >= 2:
            craft_list.append("*tri-blade spear*")

    if "baseball bat" in character[4] and "hammer" in character[4] and nails >= 10:
        craft_list.append("*spiked baseball bat*")

    if "hammer" in character[4] and nails >= 4 and weapon_parts >= 3:
        craft_list.append("heavy hammer")

    if "machete" in character[4] and leather >= 2 and rope >= 1 and weapon_parts >= 1:
        craft_list.append("quality machete")

    if leather >= 8 and rope >= 2:
        craft_list.append("handmade armour")

    if leather >= 2 and rope >= 1:
        craft_list.append("handmade boots")

    return craft_list

def craft_item(weapon_parts, workshop_satchel):
    craftable = craft_list(weapon_parts, workshop_satchel)
    craft_loop = True

    if len(craftable) > 0:
        while len(craftable) > 0 and craft_loop == True:
            craftable = craft_list(weapon_parts, workshop_satchel)
            if len(craftable) > 0:
                print("Select an item to craft:")
                count = 1
                for i in craftable:
                    print(str(count) + ". " + i)
                    count += 1
                print(str(count) + ". " + "Exit")
                choice = make_choice()

                if choice <= len(craftable):
                    item_chosen = craftable[choice - 1]

                    if item_chosen == "basic spear":
                        add_item("(weapon) basic spear")
                        remove_item("(weapon) knife")
                        workshop_satchel[1] = workshop_satchel[1] - 1
                        workshop_satchel[3] = workshop_satchel[3] - 1

                    elif item_chosen == "heavy spear":
                        add_item("(weapon) heavy spear")
                        remove_item("(weapon) machete")
                        workshop_satchel[1] = workshop_satchel[1] - 1
                        workshop_satchel[3] = workshop_satchel[3] - 1

                    elif item_chosen == "*tri-blade spear*":
                        add_item("(weapon) *tri-blade spear*")
                        remove_item("(weapon) machete")
                        remove_item("(weapon) knife")
                        remove_item("(weapon) knife")
                        workshop_satchel[1] = workshop_satchel[1] - 2
                        workshop_satchel[3] = workshop_satchel[3] - 1

                    elif item_chosen == "*spiked baseball bat*":
                        add_item("(weapon) *spiked baseball bat*")
                        remove_item("(weapon) baseball bat")
                        workshop_satchel[0] = workshop_satchel[0] - 10

                    elif item_chosen == "heavy hammer":
                        add_item("(weapon) heavy hammer")
                        remove_item("(weapon) hammer")
                        workshop_satchel[0] = workshop_satchel[0] - 4
                        weapon_parts -= 3

                    elif item_chosen == "quality machete":
                        add_item("(weapon) quality machete")
                        remove_item("(weapon) machete")
                        workshop_satchel[2] = workshop_satchel[2] - 2
                        workshop_satchel[1] = workshop_satchel[1] - 1
                        weapon_parts -= 1

                    elif item_chosen == "handmade armour":
                        add_item("(clothing) *handmade armour*")
                        workshop_satchel[2] = workshop_satchel[2] - 8
                        workshop_satchel[1] = workshop_satchel[1] - 2

                    elif item_chosen == "handmade boots":
                        add_item("(clothing) *handmade boots*")
                        workshop_satchel[2] = workshop_satchel[2] - 2
                        workshop_satchel[1] = workshop_satchel[1] - 1

                    print("You have crafted '" + item_chosen + "'")
                    print(line_break)

                else:
                    craft_loop = False

            else:
                print("There is nothing else you can craft")
                craft_loop = False

    else:
        print("There is nothing you can craft")

    return workshop_satchel

def combat_heal():
    if character[0][0] <= 75 and len(character[5]) > 0:
        print("\nBut it seems you've been injured in the fight")
        print("Will you:\n1. Use some meds\n2. Keep moving")
        choice = make_choice()

        if choice == 1:
            print("What item will you use?")
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

        else:
            print("Deciding you can handle it, you keep moving")

    print()