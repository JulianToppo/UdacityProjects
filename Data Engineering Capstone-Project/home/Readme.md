## Project Explanation

## Introduction

The following project consists of management of a relational database for U.S immigration data using four datasets.
The main dataset will include data on immigration to the United States, and supplementary datasets will include data on airport codes, U.S. city demographics, and temperature data

### Data Description
 U.S. City Demographic Data (demog): comes from OpenSoft and includes data by city, state, age, population, veteran status and race.

I94 Immigration Data (sas_data): comes from the US National Tourism and Trade Office and includes details on incoming immigrants and their ports of entry.

Airport Code Table (airport): comes from datahub.io and includes airport codes and corresponding cities.

Countries (countries): comes from I94_SAS_Labels_Descriptions.SAS

Visas (visa): comes from I94_SAS_Labels_Descriptions.SAS

Immigrant Entry Mode (mode): comes from I94_SAS_Labels_Descriptions.SAS

Airlines: comes from https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat

## Approach
The following set of data needs to be accesed from their respective data locations and then various ETL steps are performed for maintaining the datasets.
The three major steps used here in order are:
##### - Gathering the Data
##### - Explore and Assess the Data
##### - Defination the Data Model
##### - Run Pipelines to Model the Data

<br/>

**Gathering the data** generally involves reading the data from different data sources
Loading involves reading of the data 

**Explore and Assess the Data** involving steps 
* Clean demographics dataset, filling null values withn 0 and grouping by city and state and pivot Race in diferent columns
* Clean airports dataset filtering only US airports and discarting anything else that is not an airport. Extract iso regions and cast as float elevation feet.
* Clean the immigrantion dataset. Rename columns with understandable names. Put correct formats in dates and select only important columns
* Clean airlines dataset and filter only airlines with IATA code.

**Defination the Data Model** involves description of the data model and **Mapping Out Data Pipelines**
List the steps necessary to pipeline the data into the chosen data model

* Tranform data:
    - Transform demographics dataset grouping by state an calculate all the totals and ratios for every race in every state.
    - Transform immigration dataset on order to get arrival date in different columns (year, month, day) for partitioning the dataset.
* Generate Model (Star Schema):
    - Create all dimensions in parquet.
    - Create fact table in parquet particioned by year, month, day of th arrival date.
    - Insert in fact table only items with dimension keys right. For integrity and consistency.
    <br>

**Build the data pipelines** to create the data model.

**Data Quality Checks**
- Integrity constraints on the relational database (e.g., unique key, data type, etc.)
- Unit tests for the scripts to ensure they are doing the right thing
- Source/Count checks to ensure completeness

## Working
The following steps need to be followed for the proper function of the required queries.

Run the **Capstone Project Template.ipynb** step by step for reading data and then using those data sets to be create data models which are then written in the filesystem in parquet format.

## Data Model 
The following data model is designed in the following way

#### Star Schema
* Dimension Tables:
  * dim_demographics:<br>
    State, state_code, Total_Population, Male_Population, Female_Population, American_Indian_and_Alaska_Native, Asian, Black_or_African-American, Hispanic_or_Latino, White, Male_Population_Ratio, Female_Population_Ratio, American_Indian_and_Alaska_Native_Ratio, Asian_Ratio, Black_or_African-American_Ratio, Hispanic_or_Latino_Ratio, White_Ratio.
  * dim_airports:<br>
    ident, type, name, elevation_ft, continent, iso_country, iso_region, municipality, gps_code, iata_code, local_code, coordinates.
  * dim_airlines:<br>
    Airline_ID, Name, IATA, ICAO, Callsign, Country, Active.
  * dim_countries:<br>
    cod_country, country_name
  * dim_get_visa:<br>
    cod_visa, visa.
  * dim_get_mode:<br>
    cod_mode, mode_name.

- Fact Table:
  * immigration_fact_table<br>
    cic_id, cod_port, cod_state, visapost, matflag, dtaddto, gender, airline, admnum, fltno, visatype, cod_visa, cod_mode, cod_country_origin, cod_country_cit, year, month, bird_year, age, counter, arrival_date, departure_date, arrival_year, arrival_month, arrival_day.
