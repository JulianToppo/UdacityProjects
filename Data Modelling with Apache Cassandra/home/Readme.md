## Project Explanation

## Introduction

The following project consists of creating a database which can be used to analyze the user activity on their new music streaming app.The set of user activities which were before stored in set of folders now can queried from a set of tables easily.
The following project consists of following files and folders:
* queries.py
* Project_1B_ Project_ETL.ipynb
* event_datafile_new.csv
* event_data
* images

- queries.py consists of the set of queries for dropping,creating and selecting within the database.
- 'Project_1B_ Project_ETL.ipynb" consists of set of functions and code that needs to be followed for the proper generating of a combined csv file and implementation of the queries.
- "event_datafile_new.csv" is the final csv consisting of the combined data from all the csv files.
- "event_data" consists of set of csv files to be used to generate the data for the tables.


## Approach
The following set of tables have been structured taking in consideration the requirementnt of the three queries.The following tables named music_library,user_library and song_library with their partition and clustering are being generated.
The data present in csv files in event_data are being used to put enteries into the tables using the process of Extract,Transform and Load and thus creating a pipeline for the datatransfer.

## Working
The following steps need to be followed for the proper function of the required queries.
- Run the Project_1B_ Project_Template.ipynb step by step for creating list of the files from the folder(event_data) and then using those set of list to be used to crete a new csv file named event_datafile_new.csv.
- Run the create,insert and select queries for the three tables (music_library,user_library and song_library) respectively.