Project Explanation:

Introduction
The following project consists of createing a database which can be used to analyze the user activity on their new music streaming app.The set of user activities which were before stored in set of folders now can queried from a set of tables easily.
The following project consists of six files:
-create_tables.py
-etl.ipynb
-etl.py
-README.md
-sql_queries.py
-test.ipynb

-sql_queries.py
The structure of every tables being used in the project is taken care in this file.The insertion,creationg and drop queries are declared in this file which can be used by other files for making changes.

-create_tables.py
This files takes care of initialisation of the database and making connection to it.The five tables songs,artists,user,time,songplay are initialised within thin file.
Note:Every time when trying to make new entry to a tables make sure the tables are resetted using create_table.py.

-etl.py
This files is responsible for copying the data from the files in log_data and song_data(directories) and making entries into the tables.

-test.ipynb
This file can be used to check whether the tables have been created and the entries are made accordingly.

-etl.ipynb
Notebook to develop ETL processes for each table



Approach:
I've considered defining one fact table named 'songplays' and four dimension tables named songs,users,artists,time.
The files in log_data are used to make entries in user and time tables.Whereas,the files in song_data are used for making entries in artists and song table.


Working of the code:
For the efficient working of the following files have been implemented:
1.Start with running create_tables.py.This will initialise the database and create the required five tables.
2.Follow with running etl.py.This will load the data from the log_data,song_data and start making entries in the tables.
