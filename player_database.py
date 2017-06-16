#!/usr/bin/env python
import os

def check_db_exists():
    """doc string"""
    my_file = 'playerdb.txt'
    if os.path.isfile(my_file):
        print "log... db exists."
        return True
    else:
        print "log... db does not exist. creating db."
        return False

def create_db():
    """doc string"""
    ### CHANE THE ORDER OF ASSIGNMENT ###
    header = "player_number, player_name, player_team, player_pos\n"
    my_file = 'playerdb.txt'
    with open(my_file, 'w') as f:
        f.write(header)
        print "log... db created."

def check_player_exists(pname):
    """doc string"""
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
    print "method_100"

def add_player(pname, pteam, ppos):
    """doc string"""
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
    else:
        print "log... player exists. cannot add player."

def find_player(pname):
    """doc string"""
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
                #print "log... ", player_name, "found."
                return player_number, player_name, player_team, player_position
            else:
                print "log... player not found."

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