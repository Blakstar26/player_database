#!/usr/bin/env python
import os

def check_db_exists():
""" 
This functions checks that database exists. 
If it exists, returns True, else returns False. 
Takes no arguments. 
Args:
    no arguments
"""
"""
Test
    print check_db_exists()
"""
""" 
fix 
"""

    my_file = 'playerdb.txt'
    if os.path.isfile(my_file):
        print "log... db exists."
        return True
    else:
        print "log... db does not exist. creating db."
        return False

def create_db():
""" 
This function creates a database if none exists. 
First checking if databse exists, creating 
a database, and then returns True. If database exists 
or cannot be created for some reason, print to log 
and return False. Takes no arguments. 
Args: 
    no arguments
"""
"""
Test
    print create_db()
"""
""" 
fix 
"""
    ### CHANE THE ORDER OF ASSIGNMENT ###
    #header = "player_number, player_name, player_team, player_pos\n"
    my_file = 'playerdb.txt'
    if check_db_exists():
        with open(my_file, 'w') as f:
            #f.write(header)
            f.write("start db")
            print "log... db created."
            return True
    else:
        print "log... cannot create db. already exists?"
        return False

def check_player_exists(pname):
""" 
This function checks if player exists. 
Opens file and searches for player name, line by line.
If found, logs and returns True or logs and returns 
False if otherwise.
Args: 
    pname (str): the player's name as string to process 
Returns: 
    True (bool): True for the successful execution of checking player exists
    False (bool): False for the failed execution of checking player exists
"""
""" 
Test 
    pname = 'carzola'
    print check_player_exists(pname)
"""
""" 
fix 
"""
    player_name = pname
    my_file = 'playerdb.txt'
    with open(my_file, 'r') as f:
        for line in f:
            if player_name in line:
                print "log... player exists."
                return True
            else:
                print "log... player does not exist."
                return False

def add_player(pname, pteam, ppos):
""" 
This function adds a player to database. 
First checking if player already exists.
If player does not exists, the file is opened
and player is added, logs and returns True.
Otherwise doing nothing, logs and returns False.
Args: 
    pname (str): the player's name as string to process
    pteam (str): the player's team as string to process
    ppos (str): the player's position as string to process
Returns: 
    True (bool): True for the successful execution of adding player
    False (bool): False for the failed execution of adding player
"""
""" 
Test 
    pname = 'carzola'
    pteam = 'arsenal'
    ppos = 'mf'
    print add_player(pname, pteam, ppos)
"""
""" 
fix 
"""
    if check_player_exists is True:
        player_name = pname
        player_team = pteam
        player_position = ppos
        player_number = "8"
        ### CHANE THE ORDER OF ASSIGNMENT ###
        player = player_number + " " + player_name + " " + player_team + " " + player_position
        my_file = 'playerdb.txt'
        with open(my_file, 'w') as f:
            f.write(player)
            print "log... player added."
            return True
    else:
        print "log... player exists. cannot add player."
        return False

def find_player(pname):
""" 
This function finds a player in database. 
Opening file and searching for player line by line
and if found, will load data to buffer, log and
return player number name team and position as 
arguments. If not found logs return False. 
Args: 
    pname (str): the player's name as string to process
Returns: 
    pnumber (str): the player's number as string to process
    pname (str): the player's name as string to process
    pteam (str): the player's team as string to process
    ppos (str): the player's position as string to process
    True (bool): the successful execution of finding player
    False (bool): false for failed execution of finding player
"""
""" 
Test 
    pname = 'carzola'
    print find_player(pname)
"""
""" 
fix 
"""
    player_name = pname
    my_file = 'playerdb.txt'
    with open(my_file, 'r') as f:
        for line in f:
            if player_name in line:
                player_stats = line.split(" ")
                player_number, player_name, player_team, player_position = player_stats
                '''print "log... ", player_number
                print "log... ", player_name
                print "log... ", player_team
                print "log... ", player_position'''
                #print player_stats
                print "log... ", player_name, "found."
                return player_number, player_name, player_team, player_position, True
            else:
                print "log... player not found."
                return False

def list_player(pname):
    """doc string"""
    print "1"
    player_number, player_name, player_team, player_position = find_player(pname)
    print "2"
    #player_stats = find_player(pname)
    print "player number: ", player_number
    print "player name: ", player_name
    print "player team: ", player_team
    print "player position: ", player_position
    print "method_7"

def update_player(pname, ppos_stat, pteam_stat, pnum_stat):
    """doc string"""
    if ppos_stat is False and pteam_stat is False and pnum_stat is False:
        return False
    else:
        if check_player_exists(pname):
            ### CHANE THE ORDER OF ASSIGNMENT ###
            player_number, player_name, player_team, player_position = find_player(pname)
            player_stats = find_player(pname)

            if ppos_stat:
                new_player_position = get_new_player_position()
                player_position = new_player_position
            if pteam_stat:
                new_player_team = get_new_player_team()
                player_team = new_player_team
            if pnum_stat:
                new_player_number = get_new_player_number()
                player_number = new_player_number

            #check_db_exists()
            f = open("playerdb.txt", "r")
            lines = f.readlines()
            f.close()
            f = open("playerdb.txt", "w")
            outdated_player_stats = player_stats
            for line in lines:
                if line != outdated_player_stats + "\n":
                    f.write(line)
                else:
                    ### CHANE THE ORDER OF ASSIGNMENT ###
                    player_stats = player_number + " " + player_name + \
                        " " + player_team + " " + player_position
                    f.write(player_stats)
                    print "log... player is updated."
            f.close()
        else:
            return False
    print "method_3"
    
def delete_player():
    """doc string"""
    print "method_4"
    
def list_all_players():
    """doc string"""
    print "method_5"
    
def get_player():
    """doc string"""    
    print "method_6"

def get_new_player_number():
    return "1"

def get_new_player_position():
    return "DF"

def get_new_player_team():
    return "hull"
    
#write db column titles
#playerdb = "playerdb.txt"
#f = open(playerdb,'w')
#f.write("player_name, player_team, player_pos")
#f.close()

if check_db_exists() != True:
    create_db() 
add_player('carzola', 'arsenal', 'mf')
find_player('carzola')
list_player('carzola')
check_player_exists('carzola')
update_player('carzola', ppos_stat=True, pteam_stat=True, pnum_stat=True)
#create_db()