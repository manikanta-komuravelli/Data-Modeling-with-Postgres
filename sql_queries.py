# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays(
songplay_id serial primary key,
start_time date references time(start_time),
user_id int not null references users(user_id),
level varchar,
song_id varchar references songs(song_id),
artist_id varchar references artists(artist_id),
session_id int,
location varchar,
user_agent varchar
)
""")

user_table_create = ("""
create table if not exists users(
user_id int primary key,
first_name varchar not null,
last_name varchar not null,
gender varchar,
level varchar
)
""")

song_table_create = ("""
create table if not exists songs(
song_id varchar primary key,
title varchar not null,
artist_id varchar not null references artists(artist_id),
year int,
duration numeric not null
)
""")

artist_table_create = ("""
create table if not exists artists(
artist_id varchar primary key,
name varchar not null,
location varchar,
latitude numeric,
longitude numeric
)
""")

time_table_create = ("""
create table if not exists time(
start_time date primary key,
hour int,
day int,
week int,
month int,
year int,
weekday varchar
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values (%s, %s, %s, %s, %s, %s, %s, %s)
on conflict (songplay_id) do nothing;
""")

user_table_insert = ("""
insert into users (user_id, first_name, last_name, gender, level)
values (%s, %s, %s, %s, %s)
on conflict (user_id) do 
update 
set level= excluded.level
""")

song_table_insert = ("""
insert into songs (song_id, title, artist_id, year, duration)
values (%s, %s, %s, %s, %s)
on conflict (song_id) do nothing;
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location, latitude, longitude)
values (%s, %s, %s, %s, %s)
on conflict (artist_id) do nothing;
""")


time_table_insert = ("""
insert into time (start_time, hour, day, week, month, year, weekday)
values (%s, %s, %s, %s, %s, %s, %s)
on conflict (start_time) do nothing;
""")

# FIND SONGS

song_select = ("""
select song_id, artists.artist_id from songs
join artists
on songs.artist_id=artists.artist_id
where songs.title= %s
and artists.name= %s
and songs.duration= %s
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, artist_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]