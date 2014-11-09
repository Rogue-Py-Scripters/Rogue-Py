from __future__ import division
import random
import re

import sys
import time

import colorama
from colorama import Fore, Back, Style

colorama.init()

print('Welcome to RoguePy')

# Constants
max_number_of_armor_pieces = 4

Character = {
    'Name': raw_input('Enter your characters name: '),
    'XP': 0,
    'Level': 0,
    'Health': 100,
    'Max_Health': 100,
    'Inventory': [['fists', 1]],
    'Armor': [],
    'Alive': True,
    'Tier': 1,
    'Gold': 0,
    'Arrows': 0,
    'Rail Gun Ammunition': 0
}


# Utility
def match(pattern, string):
    return re.match(pattern, string) is not None


def color(s, c):
    return c + str(s) + Fore.RESET + Back.RESET + Style.RESET_ALL


if Character['Name'] == '':
    Character['Name'] = 'DefaultPy'
elif match('micha?e?l ?bay', Character['Name'].lower()):
    pretty_print('You hear faint explosions in the background')


def effective_armor_defense():
    total = 0
    for i in Character['Armor']:
        total += i[1]
    length = len(Character['Armor'])
    # total /= (length + 1) / length
    if len(Character['Armor']) == max_number_of_armor_pieces:
        total *= 1.5
    return total


def print_inv():
    for item in Character['Inventory']:
        pretty_print("Name: %s Damage:  %.2f" % (item[0], item[1]))


def pretty_print(s, c=Fore.GREEN):
    print(c + Style.BRIGHT)
    for i in str(s):
        time.sleep(1 / len(s))
        sys.stdout.write(i)
        sys.stdout.flush()
    print(Fore.RESET + Style.RESET_ALL)


pretty_print('Hello %s' % (Character['Name']))

raw_input('Press ENTER to start ')

# Item Lists
current_tier = {}

tier1 = {'pen': 7, 'butterfly': 0.1, 'bottle of Aspirin': 5, 'fern': 5, 'baby': 15, 'teddy bear': 6,
         'keyboard': 7, 'mouse': 6, 'salt shaker': 5, 'lamp': 7, 'shoebox': 5, 'plunger': 7, 'bow': 10}
# 20-40
tier2 = {'fountain pen': 20, 'sharpened twig': 20, 'branch': 30, 'sapling': 25, 'rock': 35, 'dead raccoon': 37,
         'brick': 27,
         'plastic bag': 15, 'sharpened soda can': 20, 'woven grass sword': 24, 'deer antler': 27, 'antelope antler': 2,
         'dead squirrel': 20, ' toilet seat': 27, 'boot': 20, 'wooden club': 37, 'broken stone sword': 40,
         'magic stick': 30, 'sharpened stick': 20, 'long bow': 30}
# 50-70
tier3 = {'stone axe': 57, 'wooden battle axe': 50, 'stone pickaxe': 50, 'dull stone sword': 53, 'bone sword': 60,
         'bent iron dagger': 57, 'sharpened wooden dagger': 50, 'stone dagger': 53, 'stone scythe': 56,
         'police baton': 0, 'dull iron spear': 57, 'nunchucks': 55, 'metal folding chair': 70, 'laptop': 68,
         'unicorn horn': 69, 'unicycle': 63, 'half a bicycle': 63, 'third of a tricycle': 63, 'composite bow': 70}
#80-120
tier4 = {'iron sword': 86, 'iron dagger': 80, 'iron battle axe': 2, 'iron long sword': 97, 'iron flail': 93,
         'iron spear': 80, 'dull steel cleaver': 80, 'solid iron club': 101, 'iron chain': 90, 'iron shovel': 84,
         'solid gold toilet seat': 110, 'crossbow': 120, 'steel sword': 109, 'iron battle hammer': 113,
         'steel long sword': 119}
#120-200
tier5 = {'diamond encrusted rapid fire crossbow': 200, 'gold trimmed diamond sword': 153, 'iridium battle hammer': 167,
         'carbon steel battle axe': 172, 'hand gun': 130, 'carbon steel tipped spear': 124,
         'solid gold folding chair': 350, 'shoulder mounted rail gun': 299}

weapon_tiers = [tier1, tier2, tier3, tier4, tier5]
weapon_index = dict(
    tier1.items() + tier2.items() + tier3.items() + tier4.items() + tier5.items() + {'fists': 1}.items())
#weapon_index['hands'] = 1

loot = []

#Monster Lists
#{Name: [Attack damage, Health]

monster_tier1 = {'Cricket': [5, 1], 'Bat': [10, 5], 'Mouse': [10, 20], 'Monkey': [15, 20], 'Giraffe': [5, 50],
                 'Baby Chimpanzee': [20, 25], 'Chimpanzee': [25, 30]}
monster_tier2 = {'Gorilla': [30, 50], 'Baboon': [30, 65], 'Locust Swarm': [35, 95], 'Venomous Snake': [40, 45],
                 'Pit Viper': [45, 90], 'Anaconda': [50, 100]}
monster_tier3 = {'Pterodactyl': [80, 100], 'Peregrine Falcon': [70, 80], 'Griffin': [70, 130], 'ICBShark': [90, 150],
                 'Weeping Angels': [80, 150], 'Koopa Cloud': [90, 100]}
monster_tier4 = {'Dalek': [120, 190], 'Total Bisquid': [150, 200], 'IT Client': [155, 210], 'Huuptic Elder': [170, 250],
                 'Tuxxy Penguin': [180, 260], 'Octodad': [140, 240]}
monster_tier5 = {'Loch Ness Monster': [200, 300], 'Yeti': [230, 310], 'Vampire': [220, 320], 'Dragon': [250, 330],
                 'Goblin': [240, 325], 'Zombie': [210, 300]}

monster_tiers = [monster_tier1, monster_tier2, monster_tier3, monster_tier4, monster_tier5]

# number is amount of healing
healing = {'Tier One Potion Of Healing': 10, 'Tier Two Potion Of Healing': 20, 'Tier Three Potion Of Healing': 30,
           'Tier Four Potion Of Healing': 40, 'Tier Five Potion Of Healing': 50}

#number is % of extra damage
strength = {'Tier One Potion of Strength': 5, 'Tier Two Potion of Strength': 10, 'Tier Three Potion of Strength': 15,
            'Tier Four Potion of Strength': 20, 'Tier Five Potion of Strength': 25}

#number is amount of damage resistance (could handle similar to armor)
resistance = {'Tier One Potion of Resistance': 5, 'Tier Two Potion of Resistance': 10,
              'Tier Three Potion of Resistance': 15, 'Tier Four Potion of Resistance': 20,
              'Tier Five Potion of Resistance': 25}

#Possible Return States
STAGE_DEFEATED = 0
PLAYER_DEFEATED = 1


def boss_wrapper():
    bossas = []
    STAGE_1 = 1
    STAGE_2 = 2
    STAGE_3 = 3


    def boss_func(name):
        def get_handler(f):
            bossas.append([name, f])

        return get_handler

    #stage ranges between 1, 2, 3
    @boss_func('Lion King')
    def lion_king(stage):
        if stage == STAGE_1:
            pretty_print('The lion king sends forth the pack of cubs')
            create_attack('pack of cubs', 25, 10, 0, True)

        elif stage == STAGE_2:
            pretty_print('The lion king enters the battle')
            create_attack('lion king', 50, 25, 0, True)
        elif stage == STAGE_3:
            pretty_print('The lion king has been defeated. He runs away in fear of your skill')

    return bossas


bosses = boss_wrapper()


def init_boss_battle(tier):
    boss = bosses[tier - 1]
    pretty_print('The %s has appeared!' % boss[0])
    for j in [1, 2, 3]:
        res = boss[1](j)
        if res is None:
            if not Character['Alive']:
                break
        else:
            if res == PLAYER_DEFEATED:
                break


monster_adjs = ["large", "small", "fiercesome", "terrifying", "devastating", "terrifyingly devastating", "mangey"]


def indefinite_article(word):
    return 'an' if (word[0] in ['a', 'e', 'i', 'o', 'u']) else 'a'


#Random Event Function
def tree_falls_on_road():
    pretty_print('A tree has fallen on the road...')
    keep_looping = True
    while keep_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'move branch' or s == 'movebranch' or s == 'kick branch' or s == 'move tree' or s == 'movetree':
            pretty_print('You are not strong enough')
            keep_looping = True
        elif s == 'jump branch' or s == 'jump over branch' or s == 'jump tree' or s == 'jump over tree':
            pretty_print('You have jumped over the tree and continue your journey')
            keep_looping = False
        else:
            pretty_print('I dont understand what you want to do to this tree')
            keep_looping = True


#Monster Attack  (defense_modifier is percent damage reduction)
def create_attack(name, monster_hp, attk_strength, defense_modifier=random.randrange(11), is_planned=False):
    def f():
        monster_health = monster_hp
        adj = random.choice(monster_adjs)
        if is_planned:
            pass
        else:
            pretty_print('%s %s has appeared and starts attacking you' % (adj, name))
        monster_attacks = False
        player_attack_weapon = None
        end_battle = False
        while True:
            # pretty_print('Item: %s' % player_attack_weapon)
            print_healths = False
            if player_attack_weapon and not end_battle:
                dmg = ([x[1] for x in Character['Inventory'] if x[0] == player_attack_weapon][0]) * (
                1 - defense_modifier / 100)
                monster_health -= dmg
                pretty_print(
                    'You attack with your %s and the %s %s loses %.2f health' % (player_attack_weapon, adj, name, dmg))
                print_healths = True
                player_attack_weapon = None
            #Add random chance of enemy dying
            if monster_health <= 0:
                pretty_print('You have defeated the %s %s' % (adj, name))
                give_loot()
                end_battle = True
            if monster_attacks and not end_battle:
                dmg = attk_strength * (1 - effective_armor_defense() / 100)
                Character['Health'] -= dmg
                pretty_print('The %s %s attacks and you lose %.2f health' % (adj, name, dmg))
                print_healths = True
                monster_attacks = False
            if Character['Health'] <= 0:
                pretty_print('The %s %s has defeated you' % (adj, name))
                Character['Alive'] = False
                end_battle = True
            if print_healths and not end_battle:
                pretty_print('You now have %.2f health and the %s %s now has %.2f' % \
                             (Character['Health'], adj, name, monster_health))
            if end_battle:
                break
            s = raw_input('What do you want to do? ').lower()
            if default_commands(s):
                pass
            elif s.lower().replace(' ', '').startswith('inv'):
                print_inv()
            elif match("attack(?: with )?(.*)", s):
                item = re.match("attack(?: with )?(.*)", s).group(1)
                if item == '':
                    item = 'fists'
                if item in [x[0].lower() for x in Character['Inventory']]:
                    if len([x for x in Character['Inventory'] if x[0].lower() == item][0]) == 2:
                        player_attack_weapon = item
                    else:
                        pretty_print('You fail to inflict any damage with your %s' % item)
                else:
                    pretty_print('You attack with your imaginary %s' % item)
                monster_attacks = True
            elif s in ["flee", "run", "hide"]:
                if random.randint(0, 4) == 0:
                    pretty_print('You successfully %s from the %s %s' % (s, adj, name))
                    end_battle = True
                else:
                    verb = 'finds' if s == "hide" else 'catches'
                    pretty_print('The %s %s %s you' % (adj, name, verb))
                    monster_attacks = True
            else:
                pretty_print('You stumble around in confusion whilst the %s %s attacks you' % (adj, name))
                monster_attacks = True

    return f


#Random Event Function One
def lose_way_right():
    pretty_print('You got lost, choose a direction to go in')
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'go right' or s == 'right' or s == 'move right':
            pretty_print('You find the path again and continue on your journey')
            continue_looping = False
        elif s == 'go left' or s == 'left' or s == 'move left':
            pretty_print('You have been walking for hours when you realize you have been walking in a circle.')
            continue_looping = True
        elif s == 'go up' or s == 'up' or s == 'move up' or s == 'fly up':
            pretty_print('404 wings not found')
            continue_looping = True
        elif s == 'go forward' or s == 'forward' or s == 'move forward' or s == 'go saight' or s == 'saight' or s == 'move saight':
            pretty_print('Your face has been confronted with a tree')
            continue_looping = True
        else:
            pretty_print('That is not how to get unlost dufus')
            continue_looping = True


#Random Event Function Two
def lose_way_left():
    pretty_print('You got lost, choose a direction to go in')
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'go right' or s == 'right' or s == 'move right':
            pretty_print('You have been walking for hours when you realize you have been walking in a circle.')
            continue_looping = True
        elif s == 'go left' or s == 'left' or s == 'move left':
            pretty_print('You find the path again and continue on your journey')
            continue_looping = False
        elif s == 'go up' or s == 'up' or s == 'move up' or s == 'fly up':
            pretty_print('404 wings not found')
            continue_looping = True
        elif s == 'go forward' or s == 'forward' or s == 'move forward' or s == 'go straight' or s == 'straight' or s == 'move straight':
            pretty_print('Your face has been confronted with a tree')
            continue_looping = True
        else:
            pretty_print('That is not how to get unlost dufus')
            continue_looping = True


#Random Event Function Three
def lose_way_straight():
    pretty_print('You got lost, choose a direction to go in')
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'go right' or s == 'right' or s == 'move right':
            pretty_print('You have been walking for hours when you realize you have been walking in a circle.')
            continue_looping = True
        elif s == 'go left' or s == 'left' or s == 'move left':
            pretty_print('Your face has been confronted with a tree')
            continue_looping = True
        elif s == 'go up' or s == 'up' or s == 'move up' or s == 'fly up':
            pretty_print('404 wings not found')
            continue_looping = True
        elif s == 'go forward' or s == 'forward' or s == 'move forward' or s == 'go straight' or s == 'straight' or s == 'move straight':
            pretty_print('You find the path again and continue on your journey')
            continue_looping = False
        else:
            pretty_print('That is not how to get unlost dufus')
            continue_looping = True


#Random Event Function Four
def abandoned_cottage():
    pretty_print('You find a abandoned cottage, the front door has collapsed')
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        pre, b, c = s.partition(' ')
        if pre in 'enter go in open yes':
            event = random.randint(0, 1)
            if event == 0:
                Character['Health'] -= 0.5 * Character['Health']
                pretty_print('The cottage collapses but you manage to make it out in time, -50 Health')
            elif event == 1:
                pretty_print('You find a %s')
                continue_looping = False
        elif pre in 'ignore abandon leave skip avoid':
            pretty_print('You avoid the cottage and continue your journey')
            continue_looping = False
        else:
            pretty_print('I don\'t understand what you want to do to this cottage')
            continue_looping = True


#Random Event Function Five
def find_leaf():
    pretty_print('You pass an interesting leaf while walking')
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if match('pick ?up.*', s) or s.startswith('take') or s == 'put leaf in inventory' or s.startswih('examine'):
            continue_looping = False
        elif s == 'eat leaf':
            pretty_print('You get ebolaids and die')
            Character['Alive'] = False
            continue_looping = False
        else:
            pretty_print('You want to "what" to this leaf?')
            continue_looping = True


#Random Event Function Six
def chest():
    pretty_print('You see a chest')
    continue_looping = True
    while continue_looping:
        s = raw_input('Do you want to open the chest?')
        s = s.lower()
        if s == 'open chest' or s == 'yes':
            pretty_print('You open the chest')
            event = random.randrange(4)
            if event == 0:
                Character['Health'] -= 0.5 * Character['Health']
                pretty_print('A trap was sprung and you lost 50% of your health')
            elif event == 1:
                pretty_print('You find a %s')
                # weapon
            elif event == 2:
                pretty_print('You find a %s')
                # potion
            elif event == 3:
                pretty_print('You find a %s')
                # misc.
            else:
                pretty_print('The chest starts to move and become a %s mimmic')
                tier = Character['Tier']
                create_attack("Mimmic", 50 * tier, 50 * tier)
                # %s adj.
                # monster attack
                continue_looping = False
        elif s == 'no':
            pretty_print('You disregaurd the chets and continue on your journey.')
            continue_looping == False
        else:
            pretty_print('I don\'t under stand what you want to do to that chest')
            continue_looping = False


function_list_common = [tree_falls_on_road, lose_way_left, lose_way_right, lose_way_straight, abandoned_cottage,
                        find_leaf, chest]

#def get_random_event


pretty_print('You wake up in the middle of the night...')
pretty_print('Your house has been broken into!')
starter_item = random.sample(tier1, 1)[0]
pretty_print('You grab your trusty %s and head out into the night, determined to catch the robber' % starter_item)
Character['Inventory'].append([starter_item, weapon_index[starter_item]])


def words(s):
    s = s.lower()
    s = s.letters()
    if s == 'inventory':
        print_inv()
        return False
    elif s == 'help':
        pretty_print(
            'Type what you want to do ex. Go forward, to use an item, type use: and item, to equip items, use equip:')
        pretty_print('Commands: inventory, help, equip:, use:, attack')
        return False
    elif s == 'Left Right Up Down ABAB':
	pretty_print ('debug code 307')
    else:
        pretty_print('I don\'t now what you want to do')
        return True


def random_item_from(lst):
    return random.sample(lst, 1)[0]


def random_act(events=None):
    if not events:
        events = {'event': 3, 'monster': 7}
    total = sum(events.values())
    num = random.randrange(total)

    for k, v in events.items():
        if num < v:
            return k
        else:
            num -= v

    return None


def random_event(tier):
    return random.choice(function_list_common)


def give_loot():
    gold = 10 * Character['Tier'] + random.randrange(16)
    Character['Gold'] += gold
    pretty_print('You gained %d gold!' % gold)
    xp = 30 + random.randrange(21)
    Character['XP'] += xp
    pretty_print('You gained %d XP!' % xp)

    if random.randrange(2) == 0:
        arrows = random.randrange(4) + 1
        Character['Arrows'] += arrows
        pretty_print('Additionally, you find %d arrows' % arrows)
    if random.randrange(4) == 0 and Character['Tier'] > 3:
        rail_gun = random.randrange(7) + 1
        Character['Rail Gun Ammunition'] += rail_gun
        pretty_print('You find %d rail gun ammo' % rail_gun)

    if Character['XP'] >= 100:
        pretty_print(color('Level Up!', Fore.YELLOW + Style.BRIGHT))
        Character['Level'] += 1
        Character['Max_Health'] += 50 + random.randrange(51)
        Character['Health'] = Character['Max_Health']

    lst = healing.keys() + strength.keys() + resistance.keys()
    Character['Inventory'].append([random.choice(lst)])


def random_monster(tier):
    monster = random.choice(monster_tiers[tier - 1].keys())
    stats = monster_tiers[tier - 1][monster]
    return create_attack(monster, stats[1], stats[0], 0)


def boss_battles(count):
    did_battle = False
    if count == 20:
        init_boss_battle(1)
<<<<<<< HEAD
	Character['Tier'] += 1
    if count == 40:
        init_boss_battle(2)
	Character['Tier'] += 1
    if count == 60:
        init_boss_battle(3)
	Character['Tier'] += 1
    if count == 80:
        init_boss_battle(4)
	Character['Tier'] += 1
    if count == 100:
        init_boss_battle(5)
	Character['Tier'] += 1
=======
        did_battle = True
    if count == 40:
        init_boss_battle(2)
        did_battle = True
    if count == 60:
        init_boss_battle(3)
        did_battle = True
    if count == 80:
        init_boss_battle(4)
        did_battle = True
    if count == 100:
        init_boss_battle(5)
        did_battle = True

    if Character['Alive'] and did_battle:
        Character['Tier'] += 1
        pretty_print(color('You are now Tier %d' % Character['Tier'], Fore.YELLOW + Style.BRIGHT))


def default_commands(s):
    if s.lower().strip().startswith("stat"):
        pretty_print('-' * 25)
        pretty_print('Your health is %.2f of %.2f' % (Character['Health'], Character['Max_Health']))
        pretty_print('You have %d arrows' % Character['Arrows'])
        if Character['Rail Gun Ammunition'] > 0:
            pretty_print('You have %d rail gun ammo' % Character['Rail Gun Ammunition'])
        pretty_print('You are level %d' % Character['Level'])
        pretty_print('You are tier %d' % Character['Tier'])
        pretty_print('You have %d gold' % Character['Gold'])
        pretty_print('You have %d XP' % Character['XP'])
        pretty_print('-' * 25)
        return True

    return False
>>>>>>> 454435debfa2caf42dddce5dd5f69d222bc214d3


counter = 0
while Character['Alive']:
    counter += 1

    print(Fore.CYAN + Style.BRIGHT)
    continuation = ('-' * 25) + '\nYOU CONTINUE YOUR JOURNEY\n' + ('-' * 25)
    for i in continuation:
        time.sleep(2 / len(continuation))
        sys.stdout.write(i)
        sys.stdout.flush()
    print(Fore.RESET + Style.RESET_ALL)

    #words() #Waits for input such as inventory or help and to equp armor here, have this loop continuosly until the command go is typed
    act_type = random_act()  #Returns if monster or event(eventually finding items too)
    if act_type == 'event':
        random_event(Character['Tier'])()  # Returns rendom event of specified tier
        #Run event function
    elif act_type == 'monster':
        random_monster(Character['Tier'])()  #Returns random monster of specified tier
        #Run monster function
    else:
        pretty_print('I no know what u mean')
        pass
        #error handling
    boss_battles(counter)


        #keep_playing = True
        #while keep_playing:
        #while(Character['Alive']):
        #action = raw_input('What do you want to do')
        #words(action)
        #Character['Inventory'].append(['op', 50])
        #create_attack('4chan', 500, 1, 5)()
