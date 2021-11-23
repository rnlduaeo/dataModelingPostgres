# DROP TABLES

songplay_table_drop = "DROP table if exists songplay cascade;"
user_table_drop = "DROP table if exists users cascade;"
song_table_drop = "DROP table if exists song cascade;"
artist_table_drop = "DROP table if exists artist cascade;"
time_table_drop = "DROP table if exists time cascade;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
        (songplay_id  SERIAL PRIMARY KEY, 
         song_id text REFERENCES songs(song_id), 
         length numeric, 
         userId text REFERENCES users(user_id), 
         ts numeric, 
         level text, 
         artist_id text REFERENCES artists(artist_id), 
         session_id text, 
         location text, 
         user_agent text);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id text PRIMARY KEY, 
        firstname text, 
        lastname text, 
        gender text, 
        level text);
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
        song_id text PRIMARY KEY, 
        title text, 
        duration numeric, 
        year integer, 
        artist_id text REFERENCES artists(artist_id));
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
        artist_id text PRIMARY KEY, 
        artist_latitude numeric, 
        artist_longitude numeric, 
        artist_location text, 
        artist_name text);
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
        start_time timestamp PRIMARY KEY,  
        hour integer, 
        day integer, 
        weekofyear integer, 
        month integer, 
        year integer, 
        weekday integer);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (song_id, userId, ts, level, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users (user_id, firstname, lastname, gender, level) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) 
    DO UPDATE 
    SET level = EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, weekofyear, month, year, weekday) 
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, songs.artist_id 
      FROM songs 
      JOIN artists 
        ON songs.artist_id = artists.artist_id 
     WHERE songs.title=%s 
       AND artists.artist_name=%s 
       AND songs.duration=%s
""")

# QUERY LISTS
insert_table_queries = [artist_table_insert]
create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]