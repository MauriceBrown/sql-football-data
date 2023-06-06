import os
import sqlite3

import pandas as pd

if __name__ == '__main__':
    folder_path_base = os.path.dirname(__file__)
    folder_path_csv = os.path.join(folder_path_base, 'csv_data')
    
    db_file_name = 'database.sqlite'
    db_file_path = os.path.join(folder_path_base, db_file_name)        

    # Create db file
    con = sqlite3.connect(db_file_path)

    # Create tables
    con.execute('''
        CREATE TABLE "Country" (
            "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
            "name"	TEXT UNIQUE
            );
        ''')    
    
    con.execute('''
            CREATE TABLE "League" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "country_id"	INTEGER,
                "name"	TEXT UNIQUE,
                FOREIGN KEY("country_id") REFERENCES "country"("id")
            );
        ''')
    
    con.execute('''
            CREATE TABLE "Match" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "country_id"	INTEGER,
                "league_id"	INTEGER,
                "season"	TEXT,
                "stage"	INTEGER,
                "date"	TEXT,
                "match_api_id"	INTEGER UNIQUE,
                "home_team_api_id"	INTEGER,
                "away_team_api_id"	INTEGER,
                "home_team_goal"	INTEGER,
                "away_team_goal"	INTEGER,
                "home_player_X1"	INTEGER,
                "home_player_X2"	INTEGER,
                "home_player_X3"	INTEGER,
                "home_player_X4"	INTEGER,
                "home_player_X5"	INTEGER,
                "home_player_X6"	INTEGER,
                "home_player_X7"	INTEGER,
                "home_player_X8"	INTEGER,
                "home_player_X9"	INTEGER,
                "home_player_X10"	INTEGER,
                "home_player_X11"	INTEGER,
                "away_player_X1"	INTEGER,
                "away_player_X2"	INTEGER,
                "away_player_X3"	INTEGER,
                "away_player_X4"	INTEGER,
                "away_player_X5"	INTEGER,
                "away_player_X6"	INTEGER,
                "away_player_X7"	INTEGER,
                "away_player_X8"	INTEGER,
                "away_player_X9"	INTEGER,
                "away_player_X10"	INTEGER,
                "away_player_X11"	INTEGER,
                "home_player_Y1"	INTEGER,
                "home_player_Y2"	INTEGER,
                "home_player_Y3"	INTEGER,
                "home_player_Y4"	INTEGER,
                "home_player_Y5"	INTEGER,
                "home_player_Y6"	INTEGER,
                "home_player_Y7"	INTEGER,
                "home_player_Y8"	INTEGER,
                "home_player_Y9"	INTEGER,
                "home_player_Y10"	INTEGER,
                "home_player_Y11"	INTEGER,
                "away_player_Y1"	INTEGER,
                "away_player_Y2"	INTEGER,
                "away_player_Y3"	INTEGER,
                "away_player_Y4"	INTEGER,
                "away_player_Y5"	INTEGER,
                "away_player_Y6"	INTEGER,
                "away_player_Y7"	INTEGER,
                "away_player_Y8"	INTEGER,
                "away_player_Y9"	INTEGER,
                "away_player_Y10"	INTEGER,
                "away_player_Y11"	INTEGER,
                "home_player_1"	INTEGER,
                "home_player_2"	INTEGER,
                "home_player_3"	INTEGER,
                "home_player_4"	INTEGER,
                "home_player_5"	INTEGER,
                "home_player_6"	INTEGER,
                "home_player_7"	INTEGER,
                "home_player_8"	INTEGER,
                "home_player_9"	INTEGER,
                "home_player_10"	INTEGER,
                "home_player_11"	INTEGER,
                "away_player_1"	INTEGER,
                "away_player_2"	INTEGER,
                "away_player_3"	INTEGER,
                "away_player_4"	INTEGER,
                "away_player_5"	INTEGER,
                "away_player_6"	INTEGER,
                "away_player_7"	INTEGER,
                "away_player_8"	INTEGER,
                "away_player_9"	INTEGER,
                "away_player_10"	INTEGER,
                "away_player_11"	INTEGER,
                "goal"	TEXT,
                "shoton"	TEXT,
                "shotoff"	TEXT,
                "foulcommit"	TEXT,
                "card"	TEXT,
                "cross"	TEXT,
                "corner"	TEXT,
                "possession"	TEXT,
                "B365H"	NUMERIC,
                "B365D"	NUMERIC,
                "B365A"	NUMERIC,
                "BWH"	NUMERIC,
                "BWD"	NUMERIC,
                "BWA"	NUMERIC,
                "IWH"	NUMERIC,
                "IWD"	NUMERIC,
                "IWA"	NUMERIC,
                "LBH"	NUMERIC,
                "LBD"	NUMERIC,
                "LBA"	NUMERIC,
                "PSH"	NUMERIC,
                "PSD"	NUMERIC,
                "PSA"	NUMERIC,
                "WHH"	NUMERIC,
                "WHD"	NUMERIC,
                "WHA"	NUMERIC,
                "SJH"	NUMERIC,
                "SJD"	NUMERIC,
                "SJA"	NUMERIC,
                "VCH"	NUMERIC,
                "VCD"	NUMERIC,
                "VCA"	NUMERIC,
                "GBH"	NUMERIC,
                "GBD"	NUMERIC,
                "GBA"	NUMERIC,
                "BSH"	NUMERIC,
                "BSD"	NUMERIC,
                "BSA"	NUMERIC,
                FOREIGN KEY("country_id") REFERENCES "country"("id"),
                FOREIGN KEY("league_id") REFERENCES "League"("id"),
                FOREIGN KEY("home_team_api_id") REFERENCES "Team"("team_api_id"),
                FOREIGN KEY("away_team_api_id") REFERENCES "Team"("team_api_id"),
                FOREIGN KEY("home_player_1") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_2") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_3") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_4") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_5") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_6") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_7") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_8") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_9") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_10") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("home_player_11") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_1") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_2") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_3") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_4") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_5") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_6") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_7") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_8") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_9") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_10") REFERENCES "Player"("player_api_id"),
                FOREIGN KEY("away_player_11") REFERENCES "Player"("player_api_id")
            );
        ''')
    
    con.execute('''
            CREATE TABLE "Player" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "player_api_id"	INTEGER UNIQUE,
                "player_name"	TEXT,
                "player_fifa_api_id"	INTEGER UNIQUE,
                "birthday"	TEXT,
                "height"	INTEGER,
                "weight"	INTEGER
            );
        ''')
    
    con.execute('''
            CREATE TABLE "Player_Attributes" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "player_fifa_api_id"	INTEGER,
                "player_api_id"	INTEGER,
                "date"	TEXT,
                "overall_rating"	INTEGER,
                "potential"	INTEGER,
                "preferred_foot"	TEXT,
                "attacking_work_rate"	TEXT,
                "defensive_work_rate"	TEXT,
                "crossing"	INTEGER,
                "finishing"	INTEGER,
                "heading_accuracy"	INTEGER,
                "short_passing"	INTEGER,
                "volleys"	INTEGER,
                "dribbling"	INTEGER,
                "curve"	INTEGER,
                "free_kick_accuracy"	INTEGER,
                "long_passing"	INTEGER,
                "ball_control"	INTEGER,
                "acceleration"	INTEGER,
                "sprint_speed"	INTEGER,
                "agility"	INTEGER,
                "reactions"	INTEGER,
                "balance"	INTEGER,
                "shot_power"	INTEGER,
                "jumping"	INTEGER,
                "stamina"	INTEGER,
                "strength"	INTEGER,
                "long_shots"	INTEGER,
                "aggression"	INTEGER,
                "interceptions"	INTEGER,
                "positioning"	INTEGER,
                "vision"	INTEGER,
                "penalties"	INTEGER,
                "marking"	INTEGER,
                "standing_tackle"	INTEGER,
                "sliding_tackle"	INTEGER,
                "gk_diving"	INTEGER,
                "gk_handling"	INTEGER,
                "gk_kicking"	INTEGER,
                "gk_positioning"	INTEGER,
                "gk_reflexes"	INTEGER,
                FOREIGN KEY("player_fifa_api_id") REFERENCES "Player"("player_fifa_api_id"),
                FOREIGN KEY("player_api_id") REFERENCES "Player"("player_api_id")
            );
        ''')
    
    con.execute('''
            CREATE TABLE "Team" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "team_api_id"	INTEGER UNIQUE,
                "team_fifa_api_id"	INTEGER,
                "team_long_name"	TEXT,
                "team_short_name"	TEXT
            );
        ''')
    
    con.execute('''
            CREATE TABLE "Team_Attributes" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "team_fifa_api_id"	INTEGER,
                "team_api_id"	INTEGER,
                "date"	TEXT,
                "buildUpPlaySpeed"	INTEGER,
                "buildUpPlaySpeedClass"	TEXT,
                "buildUpPlayDribbling"	INTEGER,
                "buildUpPlayDribblingClass"	TEXT,
                "buildUpPlayPassing"	INTEGER,
                "buildUpPlayPassingClass"	TEXT,
                "buildUpPlayPositioningClass"	TEXT,
                "chanceCreationPassing"	INTEGER,
                "chanceCreationPassingClass"	TEXT,
                "chanceCreationCrossing"	INTEGER,
                "chanceCreationCrossingClass"	TEXT,
                "chanceCreationShooting"	INTEGER,
                "chanceCreationShootingClass"	TEXT,
                "chanceCreationPositioningClass"	TEXT,
                "defencePressure"	INTEGER,
                "defencePressureClass"	TEXT,
                "defenceAggression"	INTEGER,
                "defenceAggressionClass"	TEXT,
                "defenceTeamWidth"	INTEGER,
                "defenceTeamWidthClass"	TEXT,
                "defenceDefenderLineClass"	TEXT,
                FOREIGN KEY("team_fifa_api_id") REFERENCES "Team"("team_fifa_api_id"),
                FOREIGN KEY("team_api_id") REFERENCES "Team"("team_api_id")
            );
        ''')
    

    # Read data from csv files and write to db
    tables = [
        'country',
        'league',
        'match',
        'player',
        'player_attributes',
        'team',
        'team_attributes'        
    ]
    
    '''
    for file_name in os.listdir(folder_path_csv):
        for table in tables:
            if table in file_name:
                print(f'{table} found in {file_name}.')
    '''

    for table in tables:
        if table != 'match':
            file_path = os.path.join(folder_path_csv, f'{table}.csv')
            data_df = pd.read_csv(file_path)
        else:
            file_names = os.listdir(folder_path_csv)
            data_dfs = []
            for file_name in file_names:
                if 'match' in file_name:
                    file_path = os.path.join(folder_path_csv, file_name)
                    temp_df = pd.read_csv(file_path)
                    data_dfs.append(temp_df)
            
            data_df = pd.concat(data_dfs, axis=0)

        sql = f'INSERT INTO {table} VALUES ({",".join(["?"]*len(data_df.columns))})'
        cursor = con.cursor()
        cursor.executemany(sql, data_df.values)
        con.commit()

    # close database connection
    con.close()


