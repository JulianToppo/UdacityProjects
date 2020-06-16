#drop tables
music_library_drop="DROP TABLE IF EXISTS music_library"
user_library_drop="DROP TABLE IF EXISTS user_library"
song_library_drop="DROP TABLE IF EXISTS song_library"

#create tables
## music_library table with two partition keys (sessionId ,itemInSession)
create_music_library_table="""CREATE TABLE IF NOT EXISTS music_library(
                         sessionId int,
                         itemInSession int,
                         artist text,
                         song text,
                         length float,
                        PRIMARY KEY (sessionId, itemInSession))"""

## user_library table with two partition keys (sessionId ,itemInSession) and one clustering key (itemInSession) for ordering the result
create_user_library_table="""CREATE TABLE IF NOT EXISTS user_library (
                            artist text,
                            song text,
                            itemInSession int,
                            firstName text,
                            lastName text,
                            userId int,
                            sessionId int,  
                            PRIMARY KEY ((userId, sessionId), itemInSession))"""

# song_library table with a partition key(song) and one clustering key(userId)
create_song_library_table="""CREATE TABLE IF NOT EXISTS song_library (
                            firstName text,
                            lastName text,
                            userId int,
                            song text, 
                            PRIMARY KEY ((song), userId))"""



#insert tables
music_library_insert="""INSERT INTO music_library (sessionId, itemInSession, artist, song, length)
                        VALUES (%s, %s, %s, %s, %s)"""

user_table_insert="""INSERT INTO user_library (artist, song, itemInSession, firstName, lastName,userId,sessionId)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""

song_table_insert= """INSERT INTO song_library (firstName, lastName, userId, song)
                    VALUES (%s, %s, %s, %s)"""


#select from tables
select_from_music_library= """SELECT artist, song, length FROM music_library WHERE sessionId=%s AND itemInSession=%s"""

select_from_user_library="""SELECT artist, song, itemInSession, firstName, lastName FROM user_library 
                   WHERE userid=%s AND sessionid=%s"""

select_from_song_table= """SELECT firstName, lastName, userId, song FROM song_library WHERE song=%s"""
