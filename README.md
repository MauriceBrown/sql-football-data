# European Football Data Analysis using SQL and pandas

## Purpose

This project was created as a demonstration of working with SQL. I'm using python's built in sqlite3 library to connect to a sqlite database and I'm executing the SQL queries through pandas so that the results are returned as a pandas DataFrame. I'm also using matplotlib and seaborn for charting.

**NOTE:** I'm not trying to answer any specific questions or show-off any particularly deep analysis, **the project is a just an excuse to run some SQL queries**.

The [jupyter notebook file](https://github.com/MauriceBrown/sql-football-data/blob/main/European%20Football%20Data%20Analysis.ipynb) in this repo walks through an exploration and analysis of this data.

**NOTE:** In most instances I would actually do a lot of the data manipulation in pandas since it typically requires less code, however I've tried to make the examples more "SQL-heavy" here. Occasionally I'll show SQL and pandas versions of the same data manipulations to illustrate this point.

## Database schema overview

This dataset is single relational database with eight tables, containing data and metadata for European football matches from 2008 to 2016. The data comes from a [Kaggle post](https://www.kaggle.com/datasets/hugomathien/soccer).

The database has a "snowflake" schema depicted in the schema diagram below. The arrows point in the direction of the *primary* key (i.e. the arrow head *faces* the primary key side of the relationship). **NOTE:** Replationships to the "player" and "team" tables don't use the *actual* primary key of those tables, but the column used in the realtionship *is* unique in each table (i.e. we could make that the primary key of the table if we were to rebuild the database).

![DB Schema Diagram](https://github.com/MauriceBrown/sql-football-data/blob/main/DB%20Schema%20Diagram.png)

## Getting the data

The sqlite file is too large to be uploaded to github so I've saved the tables to separate csv files (found in the "csv_data" folder) and created two utility scripts for working with the csv files and the database.

1. db_to_csv.py
    * This script save data from each table into a separate csv file
    * The **match** table is too large to be uploaded as a single file, so the scrip splits it into a number of separate files
2. create_db_from_csv.py
    * This script recreates the database and loads the csv data into it so you can work with the database using SQL
    * The **db_schema.csv** file contains the sqlite master table which can be used to create each table by copying the contents of the "sql" column

Once you setup your python environment, open a command window and run the command `python create_db_from_csv.py` to create the database file.

If you want to split the database into separate csv files you can run the command `python db_to_csv.py`.

## Other project ideas

There are many other projects we could undertake with this data including those under the following headings:

1. Create a prediction model for match results
      * Create a classification model for match results (i.e. predict who will win)
      * Create a model for predicting stats (number of goals, goal difference, number of cards etc)
2. Player evaluation
      * Analyse how players fit in different teams' playing systems or different leagues
      * Analyse how well fifa predicts players' "potential" and career outcomes
         * This would require more years of data
      * Model player transfer value / wage expectations based on individual and team results
