#!/usr/bin/env python
import os

def check_db_exists():
    """doc string"""
    my_file = 'playerdb.txt'
    if os.path.isfile(my_file):
        print "exists"
    else:
        print "db does not exist. creating db"
        create_db()

def create_db():
    """doc string"""
    header = "player_number, player_name, player_team, player_pos\n"
    my_file = 'playerdb.txt'
    with open(my_file, 'w') as f:
        f.write(header)
        print "db created"

def add_player(pname='carzola', pteam='arsenal', ppos='mf'):
    """doc string"""
    ### CHANE THE ORDER OF ASSIGNMENT ###
    player_name = pname
    player_team = pteam
    player_position = ppos
    player_number = "8"
    player = player_number + " " + player_name + " " + player_team + " " + player_position
    my_file = 'playerdb.txt'
    with open(my_file, 'w') as f:
        f.write(player)
        print "player added."

def find_player(pname='carzola'):
    """doc string"""
    player_name = pname
    my_file = 'playerdb.txt'
    with open(my_file, 'r') as f:
        for line in f:
            if player_name in line:
                player_stats = line.split(" ")
                player_number, player_name, player_team, player_position = player_stats
                print player_number
                print player_name
                print player_team
                print player_position
                #print player_stats
                print player_name, "found."
                return player_number, player_name, player_team, player_position
            else:
                print "player not found."

def list_player(pname):
    """doc string"""
    player_number, player_name, player_team, player_position = player_stats = find_player()
    print("method_7")

def update_player():
    """doc string"""
    player_number, player_name, player_team, player_position = player_stats = find_player()
    print("method_3")
    
def delete_player():
    """doc string"""
    print("method_4")
    
def list_all_players():
    """doc string"""
    print("method_5")
    
def get_player():
    """doc string"""    
    print("method_6")
    
#write db column titles
#playerdb = "playerdb.txt"
#f = open(playerdb,'w')
#f.write("player_name, player_team, player_pos")
#f.close()

check_db_exists()
add_player()
find_player()
#create_db()