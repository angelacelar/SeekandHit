# SQL - Crew database
This folder contains files with the SQL queries that are solution to the problem called "Crew database", and test data used for testing the solution.

## Problem

You are an architect of a database system for a ari company. Your task is to create database architecture and then to prove your solution is right by few sql queries as given later.

When there are some concerns about how to implement some features, please put a comment in SQL, and we would discuss it later on. 

Your solution at the end should be 1 SQL file of PostgreSQL compatible code which contains both database structure, testing data and sample queries.

### Situation

In our database we want to be able to store data about Crew members and Aircrafts, each entity should have proper details which are derived from later description and needs. We also need to be able to assign crew members to aircraft, because we need to be able to determine which crew member has the experience with which aircraft to be later able to plan shifts and trainings. This means that every crew member could have experience with more than one aircraft and so on.

### Queries

- Find name of the oldest crew member
- Find name of the n-th crew member (second oldest, fifth oldest and so on)
- Find name of the most experienced crew member - that one who knows most aircrafts
- Find name of the least experienced crew member - that one who knows least aircrafts (counting from zero)

## Description of solution

Deriving from the tasks:
  1. create database architecture
  2. provide test data
  3. prove solution is right by given SQL queries; 

first step should be creating the actual tables where we will store data, second step should be filling tables with data so we can do the third step, which is prove the solution is right by SQL queries as given ladder in text.

Before we can add any tables, database should be created first:

```bash
  CREATE DATABASE crewdb;
```
After creating the database, connection to it must be made:

```bash
  \c crewdb
 ```

### Create database architecture

There are two entities in our problem, and each of them should have their own table as they should have proper details.
From later description and needs, we can derive details of entities and create tables two tables "crew_members" and "aircrafts" with SQL queries:

```bash
 CREATE TABLE crew_members (
	member_id int NOT NULL PRIMARY KEY,
	first_name varchar(30),
	last_name varchar(30),
	birth_date date
);
CREATE TABLE aircrafts (
	aircraft_id SERIAL PRIMARY KEY,
	member_id int NOT NULL,
	FOREIGN KEY(member_id) REFERENCES crew_members(member_id)
);
```

Table *crew_members* needs to have: unique ID (*member_id*), name of the crew member (*first_name*), *last_name* (not explicitly needed), date of birth (*birth_date*). Each table should have a *PRIMARY KEY* field, and in *crew_members PRIMARY KEY* is *member_id*: unique value given to each of the crew members as their ID.

Table *aircrafts* needs to have: unique ID (*aircraft_id*), crew member ID(*member_id*). *PRIMARY KEY* is *aircraft_id*, and since we need to be able to determine which crew member has experience with which aircraft, *member_id* is *FOREIGN KEY* field in this table. Now data from tables can *JOIN* on this mutual *member_id* field.





