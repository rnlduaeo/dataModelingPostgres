## Summary of the project
This project includes data and ETL scripts for Sparkify analytic team to query what songs users are listening to based on given data. 

Each data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. Python scripts create fact and dimension tables for a star schema for a particular anlaytic focus, and do an ETL pipeline that transfers data from files in two local directories into these tables in Postgres.

## Database schema design
1. Fact Table  
songplays - records in log data associated with song plays i.e. records with page NextSong  
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

2. Dimension Tables
users - users in the app  
user_id, first_name, last_name, gender, level  

songs - songs in music database  
song_id, title, artist_id, year, duration  

artists - artists in music database  
artist_id, name, location, latitude, longitude  

time - timestamps of records in songplays broken down into specific units  
start_time, hour, day, week, month, year, weekday  

## ETL pipeline
create_tables.py includes sql statements that create tables and insert data into those tables. etl.py reads and processes files from song_data and log_data and loads them into your tables. create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
Through test.ipynb, you can test you data to check and evaluate whether data is loaded in a right manner


## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

## State and justify your database schema design and ETL pipeline.

## [Optional] Provide example queries and results for song play analysis. 