#!/usr/bin/env python
import os

def check_db_exists():
    """doc string"""
    my_file = 'playerdb.txt'
    if os.path.isfile(my_file):
        print "log... db exists."
        return True
    else:
        print "log... db does not exist. creating db"
        create_db()
        return False

def create_db():
    """doc string"""
    header = "player_number, player_name, player_team, player_pos\n"
    my_file = 'playerdb.txt'
    with open(my_file, 'w') as f:
        f.write(header)
        print "log... db created."

def check_player_exists():
    """doc string"""
    print "method_100"

def add_player(pname, pteam, ppos):
    """doc string"""
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

def find_player(pname):
    """doc string"""
    player_name = pname
    my_file = 'playerdb.txt'
    with open(my_file, 'r') as f:
        for line in f:
            if player_name in line:
                player_stats = line.split(" ")
                player_number, player_name, player_team, player_position = player_stats
                print "log... ", player_number
                print "log... ", player_name
                print "log... ", player_team
                print "log... ", player_position
                #print player_stats
                print "log... ", player_name, "found."
                return player_number, player_name, player_team, player_position
            else:
                print "log... player not found."

def list_player(pname):
    """doc string"""
    player_number, player_name, player_team, player_position = player_stats = find_player(pname)
    print "player number: ", player_number
    print "player name: ", player_name
    print "player team: ", player_team
    print "player position: ", player_position
    print "method_7"

def update_player():
    """doc string"""
    player_number, player_name, player_team, player_position = player_stats = find_player()
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
#create_db()