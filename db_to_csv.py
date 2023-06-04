import os
import sqlite3

import pandas as pd


if __name__ == '__main__':
    folder_path_base = os.path.dirname(__file__)
    folder_path_csv = os.path.join(folder_path_base, 'csv_data')

    # create csv folder if it doesn't already exist
    if not os.path.exists(folder_path_csv):
        os.mkdir(folder_path_csv)

    tables = [
        'country',
        'league',
        'match',
        'player',
        'player_attributes',
        'team',
        'team_attributes'    
    ]

    print('Connecting to database.')

    # database connection
    db_file_name = 'database.sqlite'
    db_file_path = os.path.join(folder_path_base, db_file_name)
    con = sqlite3.connect(db_file_path)

    for table in tables:
        df = pd.read_sql(f'SELECT * FROM {table};', con)
        file_path = os.path.join(folder_path_csv, f'{table}.csv')
        df.to_csv(file_path, index=False)

    print('DB file decompiled into csv files.')
    print('Splitting "match.csv" file into smaller files.')

    # split match file into a number of smaller files to allow upload to github
    file_name_input = 'match.csv'
    file_path_input = os.path.join(folder_path_csv, file_name_input)

    df2 = pd.read_csv(file_path_input)

    row_count = df2.shape[0]
    chunks = 15
    chunk_size = row_count // chunks

    for i in range(chunks):
        if i != (chunks - 1):
            df_chunk = df2.iloc[i * chunk_size : (i + 1) * chunk_size]
        else:
            df_chunk = df2.iloc[i * chunk_size :]
            
        file_name_output = f'match_{i + 1}.csv'
        file_path_output = os.path.join(folder_path_csv, file_name_output)
        df_chunk.to_csv(file_path_output, index=False)

    # remove large "match.csv" files, leaving only the smaller files we just created
    os.remove(os.path.join(folder_path_csv, 'match.csv'))

    print('Complete.')