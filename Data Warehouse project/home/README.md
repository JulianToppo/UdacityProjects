# Project Datawarehouse

## 1.Project description

Sparkify is a music streaming startup with a growing user base and song database.

Their user activity and songs metadata data resides in json files in S3. The goal of the current project is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. 

## Project structure

This project includes five script files:

- create_cluster.ipynb is where the AWS components for this project are created programmatically
- create_table.py is where fact and dimension tables for the star schema in Redshift are created.
- etl.py is where data gets loaded from S3 into staging tables on Redshift and then processed into the analytics tables on Redshift.
- sql_queries.py where SQL statements are defined, which are then used by etl.py, create_table.py.
- README.md is current file.

#### Staging Tables
- staging_events
- staging_songs

####  Fact Table
- songplays - records in event data associated with song plays i.e. records with page NextSong - 
*songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

#### Dimension Tables
- users - users in the app - 
*user_id, first_name, last_name, gender, level*
- songs - songs in music database - 
*song_id, title, artist_id, year, duration*
- artists - artists in music database - 
*artist_id, name, location, lattitude, longitude*
- time - timestamps of records in songplays broken down into specific units - 
*start_time, hour, day, week, month, year, weekday*

## Steps to run the project :
1. Fill in the following information in *dwh.cfg* .
    ```
    1.[CLUSTER]
    HOST=''
    DB_NAME=''
    DB_USER=''
    DB_PASSWORD=''
    DB_PORT=5439

    [IAM_ROLE]
    ARN=

    [S3]
    LOG_DATA='s3://udacity-dend/log_data'
    LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
    SONG_DATA='s3://udacity-dend/song_data'

    [AWS]
    KEY=
    SECRET=

    [DWH]
    DWH_CLUSTER_TYPE       = multi-node
    DWH_NUM_NODES          = 4
    DWH_NODE_TYPE          = dc2.large
    DWH_CLUSTER_IDENTIFIER = 
    DWH_DB                 = 
    DWH_DB_USER            = 
    DWH_DB_PASSWORD        = 
    DWH_PORT               = 5439
    DWH_IAM_ROLE_NAME      = 
    ```
2. Run the `IaC.ipynp` jupyter notebook to launch a redshift cluster and create an IAM role that has read access to S3.
3. Add redshift database and IAM role info to `dwh.cfg`. 
4. In a terminal, run the command `python create_tables.py` to create the table schemas in your redshift database.
5. Again, run `python etl.py` in a terminal and run the analytic queries on your Redshift database to compare your results with the expected results.