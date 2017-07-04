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
    Test:
        print check_db_exists()
    Fix:
        - none.
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
    Test:
		create_db()
    Fix:
        - update player table to include player's last name[], first name[],
            and nickname[].
        - update player table to include: country of league[],
            league team is in [], player's team[], player's name[],
            and player's number[].
    """
    # check if database exists
    if check_db_exists():
        # if db exists. log action and returns False
        print "log: create_db(): db exists, will not create."
        return False
    # if database does not exists.
    else:
        # create database and log
        db_file_name = 'playerdb'
        database = sqlite3.connect(db_file_name)
        print "log: create_db(): db created."
        # create table and commit to cursor object and log
        cursor = database.cursor()
        cursor.execute('''
            CREATE TABLE players(id INTEGER PRIMARY KEY, playerid TEXT,
                                playernumber TEXT, playername TEXT, playerteam TEXT,
                                playerposition TEXT)    
        ''')
        print "log: create_db(): table created."
        # commit changes and log
        database.commit()
        print "log: create_db(): changes commited."
        # close database and log
        database.close()
        print "log: create_db(): db closed."
        # return True
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
    Test:
        add_player(pid='x0', pnum='8', pname='cazorla', pteam='arsenal', ppos='mf')
    Fix:
        - update player details to include player's last name[], first name[],
            and nickname[].
        - update player details to include: country of league[],
            league team is in [], player's team[], player's name[],
            and player's number[].
    """
    # check if db exists
    if check_db_exists():
        # check if player exists
        if find_player(pname):
            # if player exists. log action and return False.
            print "log: add_player(): player exists, will not add."
            return False
        # if player does not exist
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
            # add player details
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
            # log action and return True
            print "log: add_player(): changes committed."
            return True
    # if databse does not exists
    else:
        # log action and return False
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
        True (bool): the successful execution of finding player
        found_pid (str): the player's internal id as string to process
        found_pnum (str): the player's number as string to process
        found_pname (str): the player's name as string to process
        found_pteam (str): the player's team as string to process
        found_ppos (str): the player's position as string to process
        False (bool): false for failed execution of finding player
    Test:
        find_player('carzola')
    Fix:
		- update cursor-set to include player's last name[], first name[],
            and nickname[].
        - update cursor-set to include: country of league[],
            league team is in [], player's team[], player's name[],
            and player's number[].
    """
    # pass search term
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
            # store player details and log action
            found_pid, found_pnum, found_pname, found_pteam, found_ppos = cursor.fetchone()
            print "log: find_player(): player found!"
            # return True and player data
            return True, found_pid, found_pnum, found_pname, found_pteam, found_ppos
        # if player is not found
        else:
            # log action and return False
            print "log: find_player(): player not found"
            return False
    # if database cannot be found
    else:
        #log action and return False
        print "log: find_player(): database does not exist, player cannot be found."
        return False

def player_id_generator(leaguectry, tleague, pteam, nameplayer, numplayer):
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
    Test:
        leaguectry = 'en'
        tleague = 'pr'
        pteam = 'ar'
        nameplayer = 'sc'
        numplayer = '08'
        player_id_generator(leaguectry, tleague, pteam, nameplayer, numplayer)
    Fix:
        - update player details to include player's last name[], first name[],
            and nickname[].
    """
    # pass player details
    league_country = leaguectry
    team_league = tleague
    player_team = pteam
    name_player = nameplayer
    number_player = numplayer
    # if player details are stored, and true
    if league_country and team_league and player_team and name_player and number_player:
        # combine to form unique player id number
        player_id = league_country + "." + team_league + "." + player_team + "." + name_player + "." + number_player
        # log and return True
        print "log: player_id_generator(): player id is:", player_id
        return True, player_id
    # if player details are not stored, or any value returns False
    else:
        # log failure and return False
        print "log: player_id_generator(): player id cannot be set."
        return False

def list_player(pname):
    """
    This function lists all of a players details and statistics.
    calling find_player() and determine if player was found and
    if returned object is a tuple. player details are returned as
    tuple.
    return True, player id, player number, player name,
    player team, player position. If found, will log and return
    player id number name team and position as arguments. If not
    found, logs and return False.
    Args:
        pname (str): the player's name as string to process
    Returns:
        True (bool): the successful execution of listing player
        list_pid (str): the player's internal id as string to process
        list_pnum (str): the player's number as string to process
        list_pname (str): the player's name as string to process
        list_pteam (str): the player's team as string to process
        list_ppos (str): the player's position as string to process
        False (bool): false for failed execution of listing player
    Test:
        list_player('carzola')
    Fix:
        - update list to include player's last name[], first name[],
            and nickname[].
        - update list to include: country of league[],
            league team is in [], player's team[], player's name[],
            and player's number[].
    """
    # pass search term
    find_playername = pname
    # is player found, True or False?
    playerfound = find_player(find_playername)[0]
    # is returned object a tuple?
    istuple = isinstance(find_player(find_playername), tuple)
    if istuple is True and playerfound is True:
        # store player details
        rval, list_pid, list_pnum, list_pname, list_pteam, list_ppos = find_player(find_playername)
        # log action and list players
        print "log: list_player(): listing player!"
        print "log: list_player(): ", rval, list_pid, list_pnum, list_pname, list_pteam, list_ppos
        # return True and player details, if successful
        return True, list_pid, list_pnum, list_pname, list_pteam, list_ppos
    #if not tuple or player is not found
    else:
        #log action and return False
        print "log: list_player(): player cannot be listed."
        return False

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


#check_db_exists()
#create_db()
#add_player(pid='x0', pnum='8', pname='carzola', pteam='arsenal', ppos='mf')
#pdetails = find_player('carzola')
#print pdetails[0], pdetails[1], pdetails[2], pdetails[3], pdetails[4], pdetails[5]
#list_player('carzola')
leaguectry = 'en'
tleague = 'pr'
pteam = 'ar'
nameplayer = 'sc'
numplayer = '08'
player_id_generator(leaguectry, tleague, pteam, nameplayer, numplayer)

#if check_db_exists() != True:
#    create_db()
#add_player('carzola', 'arsenal', 'mf')
#find_player('carzola')
#list_player('carzola') #
#check_player_exists('carzola') #
#update_player('carzola', ppos_stat=True, pteam_stat=True, pnum_stat=True)
#create_db()