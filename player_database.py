#!/usr/bin/env python
import os
import sqlite3

def check_db_exists():
    """
    This function checks that database exists.
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
    my_file = 'playerdb'
    if os.path.isfile(my_file):
        print "log: check_db_exists(): db exists."
        return True
    else:
        print "log:  check_db_exists(): db does not exist."
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
		create_db()
    """
    """
    fix
    """
    # check if db exists
    if check_db_exists():
        print "log: create_db(): db exists, will not create."
        return False
    else:
        # create database
        db_file_name = 'playerdb'
        database = sqlite3.connect(db_file_name)
        print "log: create_db(): db created."
        # create table and commit to cursor object
        cursor = database.cursor()
        cursor.execute('''
            CREATE TABLE players(id INTEGER PRIMARY KEY, playerid TEXT,
                                playernumber TEXT, playername TEXT, playerteam TEXT,
                                playerposition TEXT)    
        ''')
        print "log: create_db(): table created."
        # commit changes
        database.commit()
        print "log: create_db(): changes commited."
        # close database
        database.close()
        print "log: create_db(): db closed."
        return True

def add_player(pid, pnum, pname, pteam, ppos):
    """
    This function adds a player to database. First checking
	if database exists, then checking if player exists.
	If database does not exists, logged and nothing happens,
	returns False. If player exists, logged and returns False.
    If database exists, and player does not exist, the database
	is opened and player is added, logged and returns True.
    Args:
		pid (str): the player's internal id number as string to process
		pnum (str): the player's number as string to process
        pname (str): the player's name as string to process
        pteam (str): the player's team as string to process
        ppos (str): the player's position as string to process
    Returns:
        True (bool): True for the successful execution of adding player
        False (bool): False for the failed execution of adding player
    """
    """
    Test:
        add_player(pid='x0', pnum='8', pname='cazorla', pteam='arsenal', ppos='mf')
    """
    """
    Fix:
        - add player last and first names
		- add player nickname
    """
    # check if db exists
    if check_db_exists():
        # check if player exists
        if find_player(pname):
            print "log: add_player(): player exists, will not add."
            return False
        else:
            print "log: add_player(): player does not exist, adding now."
            # open database
            db_file_name = 'playerdb'
            database = sqlite3.connect(db_file_name)
            # define player attributes
            cursor = database.cursor()
            added_playerid = pid
            added_playernumber = pnum
            added_playername = pname
            added_playerteam = pteam
            added_playerposition = ppos
            # insert player
            cursor.execute('''
				INSERT INTO players(playerid, playernumber, playername, playerteam,
                    playerposition) VALUES(?,?,?,?,?)''',
                           (added_playerid, added_playernumber, added_playername,
                            added_playerteam, added_playerposition))
            print "log: add_player(): player added."
            # committing changes
            database.commit()
            # close database
            database.close()
            print "log: add_player(): changes committed."
            return True
    else:
        print "log:  add_player(): db does not exist, cannot add player."
        return False

def find_player(pname):
    """
    This function finds a player in the database.
    Opening file and searching for player by first name,
	last name, or both. If found, will load data to buffer,
    log and return player number name team and position as
    arguments. If not found logs and return False.
    Args:
        pname (str): the player's name as string to process
    Returns:
        True, found_pid, found_pnum, found_pname, found_pteam, found_ppos
        True (bool): the successful execution of finding player
        found_pid (str): the player's internal id as string to process
        found_pnum (str): the player's number as string to process
        found_pname (str): the player's name as string to process
        found_pteam (str): the player's team as string to process
        found_ppos (str): the player's position as string to process
        False (bool): false for failed execution of finding player
    """
    """
    Test:
        find_player('carzola')
    """
    """
    Fix:
		- no fixes
    """
    find_playername = pname
	# check if db exists
    if check_db_exists():
        # open database
        db_file_name = 'playerdb'
        database = sqlite3.connect(db_file_name)
        # set cursor and find player
        cursor = database.cursor()
        cursor.execute('''SELECT playerid, playernumber, playername, playerteam,
                            playerposition FROM players WHERE playername = ?''', (find_playername,))
        data = cursor.fetchone()
        # check if player found
        if data is not None:
            # store player data
            found_pid, found_pnum, found_pname, found_pteam, found_ppos = cursor.fetchone()
            print "log: find_player(): player found!"
            print "log: find_player(): player id: ", found_pid
            print "log: find_player(): player number: ", found_pnum
            print "log: find_player(): player name: ", found_pname
            print "log: find_player(): player team: ", found_pteam
            print "log: find_player(): player position: ", found_ppos
            # return player data
            return True, found_pid, found_pnum, found_pname, found_pteam, found_ppos
        # if player is not found
        else:
            print "log: find_player(): player not found"
            return False
    else:
        print "log: find_player(): database does not exist, player cannot be found."
        return False

def player_id_generator():
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
    Test:
        player_id_generator()
    """
    """
    Fix:
        - no fix.
    """
    print "log: player_id_generator(): nothing to do."
    return False

def list_player(pname):
    """doc string"""
    playerID = pname
    player_number, player_name, player_team, player_position = find_player(playerID)
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
                    print "log: player is updated."
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

#check_db_exists()
#create_db()
#add_player(pid='x0', pnum='8', pname='carzola', pteam='arsenal', ppos='mf')
pdetails = find_player('carzola')
print pdetails[0], pdetails[1], pdetails[2], pdetails[3], pdetails[4], pdetails[5]

#if check_db_exists() != True:
#    create_db()
#add_player('carzola', 'arsenal', 'mf')
#find_player('carzola')
#list_player('carzola') #
#check_player_exists('carzola') #
#update_player('carzola', ppos_stat=True, pteam_stat=True, pnum_stat=True)
#create_db()