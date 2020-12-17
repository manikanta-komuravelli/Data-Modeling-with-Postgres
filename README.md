Project submission for Data Modeling with Postgres
This is the first project submission for the Nanodegree.

Introduction:
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

My role was to create a database schema and ETL pipeline for the analysis.

There are two Datasets:

Song datasets:These are json files present under /data/song_data. Below is the sample file:
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

Log datasets: These are json files present under /data/log_data. Below is the sample file:
{"artist":"None","auth":"Logged In","firstName":"Celeste","gender":"F","itemInSession":0,"lastName":"Williams","length":NaN,"level":"free","location":"Klamath Falls, OR","method":"GET","page":"HOME","registration":1541078578796.0,"sessionId":438,"song":"None","status":200,"ts":1541990217796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.1;WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"53"}

Database Schema Usage:
I used Star Schema for this modeling, There is one fact table with all the fields associated to each event, and there are 4 dimentional tables, with their primary key referenced to the fact table

Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
Below are the names of the fields:
songplay_id 
start_time
user_id 
level 
song_id 
artist_id
session_id 
location 
user_agent

Dimension Tables
users - users in the app
Below are the names of the fields:
user_id 
first_name
last_name 
gender 
level 

songs - songs in music database
Below are the names of the fields:
song_id
title 
artist_id 
year
duration 

artists - artists in music database
Below are the names of the fields:
artist_id 
name 
location 
lattitude 
longitude 

time 
Below are the names of the fields:
start_time 
hour 
day 
week 
month 
year 
weekday 

Note: The first field under each dimension table is the Primary Key for the respective table and is referenced in the fact table.

Project Template followed:
test.ipynb displays the first few rows of each table to let you check your database.
create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
sql_queries.py contains all your sql queries, and is imported into the last three files above.
README.md provides discussion on the project.


Below are the Implementation steps followed:
1. Completed the sql_queries.py file by writing the create, drop and insert statements respectively for all the above mentioned tables.

2. Executed the following command in the Terminal Window
python create_tables.py

3. Utilised the test.ipynb to check if all the tables are created by create_tables.py

4. Completed the etl.ipynb by following the steps mentioned, utilised the pandas concepts to process the data and created the basic schematic of the pipeline to insert the json data into the database.

5. With the experience of completing etl.ipynb. I have completed the etl.py to read all the json files for song data and log data and inserted them into the database by executing the below command in the terminal window.
python etl.py


All the points above are exclusively written in the mentioned files.