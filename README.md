# European Football Data Analysis using SQL and pandas

This data comes from a [Kaggle post](https://www.kaggle.com/code/dimarudov/data-analysis-using-sql/input).

The data is stored in a sqlite database file with the schema defined below. The arrows point in the direction of the *primary* key (i.e. the arrow head *faces* the primary key side of the relationship). A bi-dreictional arrow indicates that the related columns are not the *primary* key in **either** table.

![DB Schema Diagram](https://github.com/MauriceBrown/sql-football-data/blob/main/DB%20Schema%20Diagram.png)

The sqlite file is too large to be uploaded to github so I've saved the tables to separate csv file and created two utility scripts for working with the csv files and the database.

1. db_to_csv.py
    * This script save data from each table into a separate csv file
    * The **match** table is too large to be uploaded as a single file, so the scrip splits it into a number of separate files
2. create_db_from_csv.py
    * This script recreates the database and loads the csv data into it so you can work with the database using SQL
    * The **db_schema.csv** file contains the sqlite master table which can be used to create each table by copying the contents of the "sql" column
