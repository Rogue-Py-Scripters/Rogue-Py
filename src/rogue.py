from __future__ import division
import random
import re
import sys
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

print 'Welcome to RoguePy'

# Constants
max_number_of_armor_pieces = 4

Character = {
    'Name': raw_input('Enter your characters name: '),
    'XP': 0,
    'Level': 0,
    'Health': 100,
    'Inventory': [['fists', 1]],
    'Armor': [],
    'Alive': True,
    'Tier': 1
}


# Utility
def match(pattern, string):
    return re.match(pattern, string) is not None


def color(s, c):
    return c + str(s) + Fore.RESET + Back.RESET + Style.RESET_ALL


if Character['Name'] == '':
    Character['Name'] = 'DefaultPy'
elif match('micha?e?l ?bay', Character['Name'].lower()):
    print 'You hear faint explosions in the background'


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
        print "Name: %s Damage:  %.2f" % (item[0], item[1])


print 'Hello %s' % (Character['Name'])

raw_input('Press ENTER to start ')

# Item Lists
current_tier = {}

tier1 = {'pen': 7, 'butterfly': 0.1, 'bottle of Asprin': 5, 'fern': 5, 'baby': 15, 'teddy bear': 6,
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
            print 'The lion king sends forth the pack of cubs'
            create_attack('pack of cubs', 25, 10, 0, True)

        elif stage == STAGE_2:
            print 'The lion king enters the battle'
            create_attack('lion king', 50, 25, 0, True)
        elif stage == STAGE_3:
            print 'The lion king has been defeated. He runs away in fear of your skill'

    return bossas


bosses = boss_wrapper()


def init_boss_battle(tier):
    boss = bosses[tier - 1]
    print 'The %s has appeared!' % boss[0]
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
    print 'A tree has fallen on the road...'
    keep_looping = True
    while keep_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'move branch' or s == 'movebranch' or s == 'kick branch' or s == 'move tree' or s == 'movetree':
            print 'You are not strong enough'
            keep_looping = True
        elif s == 'jump branch' or s == 'jump over branch' or s == 'jump tree' or s == 'jump over tree':
            print 'You have jumped over the tree and continue your journey'
            keep_looping = False
        else:
            print 'I dont understand what you want to do to this tree'
            keep_looping = True


#Monster Attack  (defense_modifier is percent damage reduction)
def create_attack(name, monster_hp, attk_strength, defense_modifier=0, is_planned=False):
    def f():
        monster_health = monster_hp
        adj = random.choice(monster_adjs)
        if is_planned:
            pass
        else:
            print '%s %s has appeared and starts attacking you' % (adj, name)
        monster_attacks = False
        player_attack_weapon = None
        end_battle = False
        while True:
            #print 'Item: %s' % player_attack_weapon
            print_healths = False
            if player_attack_weapon and not end_battle:
                dmg = ([x[1] for x in Character['Inventory'] if x[0] == player_attack_weapon][0]) * (
                    1 - defense_modifier / 100)
                monster_health -= dmg
                print 'You attack with your %s and the %s %s loses %.2f health' % (player_attack_weapon, adj, name, dmg)
                print_healths = True
                player_attack_weapon = None
            #Add random chance of enemy dying
            if monster_health <= 0:
                print 'You have defeated the %s %s' % (adj, name)
                end_battle = True
            if monster_attacks and not end_battle:
                dmg = attk_strength * (1 - effective_armor_defense() / 100)
                Character['Health'] -= dmg
                print 'The %s %s attacks and you lose %.2f health' % (adj, name, dmg)
                print_healths = True
                monster_attacks = False
            if Character['Health'] <= 0:
                print 'The %s %s has defeated you' % (adj, name)
                Character['Alive'] = False
                end_battle = True
            if print_healths and not end_battle:
                print 'You now have %.2f health and the %s %s now has %.2f' % \
                      (Character['Health'], adj, name, monster_health)
            if end_battle:
                break
            s = raw_input('What do you want to do? ').lower()
            if s.lower().replace(' ', '').startswith('inv'):
                print_inv()
            elif match("attack(?: with )?(.*)", s):
                item = re.match("attack(?: with )?(.*)", s).group(1)
                if item == '':
                    item = 'fists'
                if item in [x[0] for x in Character['Inventory']]:
                    player_attack_weapon = item
                else:
                    print 'You attack with your imaginary %s' % item
                monster_attacks = True
            elif s in ["flee", "run", "hide"]:
                if random.randint(0, 4) == 0:
                    print 'You successfully %s from the %s %s' % (s, adj, name)
                    end_battle = True
                else:
                    verb = 'finds' if s == "hide" else 'catches'
                    print 'The %s %s %s you' % (adj, name, verb)
                    monster_attacks = True
            else:
                print 'You stumble around in confusion whilst the %s %s attacks you' % (adj, name)
                monster_attacks = True

    return f


#Random Event Function One
def lose_way_right():
    print 'You got lost, choose a direction to go in'
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'go right' or s == 'right' or s == 'move right':
            print 'You find the path again and continue on your journey'
            continue_looping = False
        elif s == 'go left' or s == 'left' or s == 'move left':
            print 'You have been walking for hours when you realize you have been walking in a circle.'
            continue_looping = True
        elif s == 'go up' or s == 'up' or s == 'move up' or s == 'fly up':
            print '404 wings not found'
            continue_looping = True
        elif s == 'go forward' or s == 'forward' or s == 'move forward' or s == 'go saight' or s == 'saight' or s == 'move saight':
            print 'Your face has been confronted with a tree'
            continue_looping = True
        else:
            print 'That is not how to get unlost dufus'
            continue_looping = True


#Random Event Function Two
def lose_way_left():
    print 'You got lost, choose a direction to go in'
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'go right' or s == 'right' or s == 'move right':
            print 'You have been walking for hours when you realize you have been walking in a circle.'
            continue_looping = True
        elif s == 'go left' or s == 'left' or s == 'move left':
            print 'You find the path again and continue on your journey'
            continue_looping = False
        elif s == 'go up' or s == 'up' or s == 'move up' or s == 'fly up':
            print '404 wings not found'
            continue_looping = True
        elif s == 'go forward' or s == 'forward' or s == 'move forward' or s == 'go straight' or s == 'straight' or s == 'move straight':
            print 'Your face has been confronted with a tree'
            continue_looping = True
        else:
            print 'That is not how to get unlost dufus'
            continue_looping = True


#Random Event Function Three
def lose_way_straight():
    print 'You got lost, choose a direction to go in'
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'go right' or s == 'right' or s == 'move right':
            print 'You have been walking for hours when you realize you have been walking in a circle.'
            continue_looping = True
        elif s == 'go left' or s == 'left' or s == 'move left':
            print 'Your face has been confronted with a tree'
            continue_looping = True
        elif s == 'go up' or s == 'up' or s == 'move up' or s == 'fly up':
            print '404 wings not found'
            continue_looping = True
        elif s == 'go forward' or s == 'forward' or s == 'move forward' or s == 'go straight' or s == 'straight' or s == 'move straight':
            print 'You find the path again and continue on your journey'
            continue_looping = False
        else:
            print 'That is not how to get unlost dufus'
            continue_looping = True


#Random Event Function Four
def abandoned_cottage():
    print 'You find a abandoned cottage, the front door has collapsed'
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        pre = s.partition(' ')
        if pre in 'enter go in open':
            event = random.randint(0, 1)
            if event == 0:
                Character['Health'] -= 0.5 * Character['Health']
                print 'The cottage collapses but you manage to make it out in time, -50 Health'
            elif event == 1:
                print 'You find a %s'
                continue_looping = False
        elif pre in 'ignore abandon leave skip avoid':
            print 'You avoid the cottage and continue your journey'
            continue_looping = True
        else:
            print 'I don\'t understand what you want to do to this cottage'
            continue_looping = True


#Random Event Function Five
def find_leaf():
    print 'You pass an interesting leaf while walking'
    continue_looping = True
    while continue_looping:
        s = raw_input('What do you want to do? ')
        s = s.lower()
        if s == 'pick up leaf' or s == 'take leaf' or s == 'put leaf in inventory':
            continue_looping = False
        elif s == 'eat leaf':
            print 'You get ebolaids and die'
            Character['Alive'] = False
            continue_looping = False
        else:
            print 'You want to "what" to this leaf?'
            continue_looping = True


function_list_common = [tree_falls_on_road, lose_way_left, lose_way_right, lose_way_straight, abandoned_cottage,
                        find_leaf]

#def get_random_event


print 'You wake up in the middle of the night...'
print 'Your house has been broken into!'
starter_item = random.sample(tier1, 1)[0]
print 'You grab your trusty %s and head out into the night, determined to catch the robber' % starter_item
Character['Inventory'].append([starter_item, weapon_index[starter_item]])


def words(s):
    s = s.lower()
    if s == 'inventory':
        print_inv()
        return False
    elif s == 'help':
        print 'Type what you want to do ex. Go forward, to use an item, type use: and item, to equip items, use equip:'
        print 'Commands: inventory, help, equip:, use:, attack'
        return False
    #elif str == 'forward' or str == 'goforward' or str == 'go forward':

    else:
        print 'I don\'t now what you want to do'
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


def random_monster(tier):
    monster = random.choice(monster_tiers[tier - 1].keys())
    stats = monster_tiers[tier - 1][monster]
    return create_attack(monster, stats[1], stats[0], 0)


while Character['Alive']:
    print Fore.CYAN + Style.BRIGHT
    continuation = ('-' * 25) + '\nYOU CONTINUE YOUR JOURNEY\n' + ('-' * 25)
    for i in continuation:
        time.sleep(2 / len(continuation))
        sys.stdout.write(i)
        sys.stdout.flush()
    print Fore.RESET + Style.RESET_ALL

    #words() #Waits for input such as inventory or help and to equp armor here, have this loop continuosly until the command go is typed
    act_type = random_act()  #Returns if monster or event(eventually finding items too)
    if act_type == 'event':
        random_event(Character['Tier'])()  # Returns rendom event of specified tier
        #Run event function
    elif act_type == 'monster':
        random_monster(Character['Tier'])()  #Returns random monster of specified tier
        #Run monster function
    else:
        print 'I no know what u mean'
        pass
        #error handling


        #keep_playing = True
        #while keep_playing:
        #while(Character['Alive']):
        #action = raw_input('What do you want to do')
        #words(action)
        #Character['Inventory'].append(['op', 50])
        #create_attack('4chan', 500, 1, 5)()