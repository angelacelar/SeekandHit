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


### Provide test data

We need to *INSERT INTO* both tables some test data. But in order to prove solution is right, as derived from the situation description, there should be a larger number of crew members in *crew_members* table than in *aircrafts* and some crew members (*member_id* values) should appear multiple times in *aircrafts* table:

```bash
'Inserting test data into table that contains information about crew members.'
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Honorato','Blackburn','2018-12-01'),('Ian','Morse','2018-08-11'),('Kristen','Clark','2018-04-18'),('Kitra','Rice','2018-01-18'),('Valentine','Pacheco','2017-12-04'),('Hayley','Peters','2019-02-07'),('Aristotle','Sims','2018-01-01'),('Nolan','Lowe','2018-11-10'),('Victor','Key','2017-10-27'),('Tate','Bray','2017-11-17');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Leila','Reilly','2018-03-04'),('Amity','Garrett','2018-12-03'),('Gisela','Workman','2018-10-04'),('Rhoda','Aguirre','2018-06-23'),('Karyn','Olsen','2018-10-10'),('Hayes','Garner','2019-05-12'),('Leila','Kline','2018-07-04'),('Brett','Levy','2018-03-05'),('Hyatt','Branch','2018-07-25'),('Deacon','Haney','2018-01-13');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Montana','Herman','2018-08-16'),('Lucas','Pitts','2018-08-19'),('Pandora','Waller','2018-08-07'),('Mia','Clemons','2019-01-17'),('Eleanor','Robinson','2018-10-04'),('Mona','Maxwell','2017-06-01'),('Nolan','Norton','2018-08-17'),('Steven','Mack','2017-07-08'),('Brielle','Ayala','2018-08-11'),('Mohammad','Graves','2017-07-12');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Jerome','Mccarthy','2018-05-14'),('Abdul','Allison','2018-09-02'),('Jamalia','Mcguire','2018-03-27'),('Orson','Morales','2017-06-28'),('Fuller','Walton','2019-04-28'),('Melinda','Mcgee','2018-10-18'),('Axel','Boyle','2018-12-08'),('Eugenia','Davmember_id','2017-09-13'),('Emmanuel','Ball','2018-10-07'),('Demetrius','Rutledge','2019-03-26');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Lee','Maddox','2018-09-24'),('Lani','Patrick','2018-04-01'),('April','Mendez','2017-06-01'),('Amos','Dale','2017-07-11'),('Harding','Russell','2019-04-14'),('Charde','Donaldson','2018-01-12'),('Merritt','Bishop','2018-11-27'),('Maia','Kinney','2018-03-10'),('Aubrey','Santana','2017-10-03'),('Veronica','Sampson','2018-01-13');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Marshall','Hughes','2017-07-22'),('Beverly','Berry','2017-07-19'),('Burke','Dyer','2018-06-15'),('Violet','Zamora','2017-11-23'),('Imani','Griffin','2018-10-05'),('Marsden','Cross','2018-03-12'),('Cameron','Griffin','2017-11-24'),('Levi','Hamilton','2018-05-21'),('Tatyana','Dickson','2017-06-19'),('Dacey','Tate','2018-07-14');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Jacob','Roberson','2018-05-31'),('Brianna','Battle','2018-09-08'),('Vernon','Gallagher','2018-03-12'),('Sandra','Goff','2018-11-01'),('Martina','Potter','2017-10-11'),('Gavin','Herman','2018-01-02'),('Ashton','Parsons','2018-02-01'),('Lucius','Rice','2019-01-16'),('Kristen','Whitaker','2017-08-20'),('Paula','Bowers','2018-05-15');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Ashely','Erickson','2019-05-02'),('Cassandra','Boyle','2019-04-03'),('Elvis','Cantu','2017-09-01'),('Josiah','Tyler','2018-11-15'),('Gail','Bennett','2018-04-22'),('Emi','Patrick','2017-09-15'),('Gavin','Cleveland','2017-08-19'),('Allegra','Giles','2018-05-03'),('Richard','Mckay','2019-03-26'),('Nasim','Mason','2017-10-24');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Kevin','Reynolds','2019-05-09'),('Charissa','Kane','2017-11-16'),('Orlando','Welch','2018-02-06'),('Buckminster','Blackburn','2017-08-22'),('Courtney','Gallegos','2018-01-04'),('Hayley','Farley','2017-11-07'),('Jamal','Huffman','2018-01-24'),('Claire','Rivas','2018-03-31'),('Amber','Giles','2019-02-06'),('Dahlia','Walton','2017-11-17');
INSERT INTO "crew_members" (first_name,last_name,birth_date) VALUES ('Germane','Hunt','2018-09-05'),('Chadwick','Abbott','2018-02-23'),('Georgia','Frederick','2018-01-12'),('Summer','Gilliam','2018-10-22'),('Lillian','Hansen','2017-11-27'),('Abdul','Tillman','2017-08-06'),('Edan','Rosario','2017-08-10'),('Mufutau','Cook','2019-05-17'),('Jena','Kirby','2018-11-03'),('Gavin','Hayden','2019-02-07');

'Inserting test data into table that contains information about aircrafts.'
'Intentionally generated a fewer number of aircrafts. Having the same number of'
'crew members and aircrafts leads to bad test data - it is unable to have ZERO experience.'
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (15,1),(3,2),(1,3),(19,4),(10,5),(5,6),(10,7),(6,8),(11,9),(12,10);
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (17,11),(6,12),(5,13),(13,14),(20,15),(14,16),(2,17),(8,18),(3,19);
```

Having the same number of crew members and aircrafts leads to bad test data - it is unable to have ZERO experience.

### Prove solution is right

SQL queries should be able to execute correctly on created database and provided test data.

#### 1. Find name of the oldest crew member
	
```bash
SELECT crew_members.first_name FROM crew_members ORDER BY birth_date LIMIT 1;
```
Selecting the *first_name* column from table *crew_members* we can find their names. In order for it to be one name, *LIMIT 1* limits the data to one row from table. To get the oldest one's name *ORDER BY* clause is used to order table rows ascending by the column *birth_date* which contains the data on their dates of birth.

#### 2. Find name of the n-th crew member (second oldest, fifth oldest and so on)

```bash
SELECT crew_members.first_name FROM crew_members ORDER BY birth_date LIMIT 1 OFFSET 1;
```
*OFFSET n* keyword is used with *ORDER BY* clause to skip n rows of table, so we can get n-th oldest crew member.

#### 3. Find name of the most experienced crew member - that one who knows most aircrafts.

```bash
SELECT crew_members.first_name FROM crew_members 
INNER JOIN (
	SELECT COUNT(aircrafts.member_id) AS most, aircrafts.member_id AS member_id 
	FROM aircrafts 
	GROUP BY member_id 
	) crewtb 
ON crew_members.member_id = crewtb.member_id 
ORDER BY COALESCE(crewtb.most,0) DESC
LIMIT 1;
```

*INNER JOIN* joins two tables and returns all rows where the values in columns *ON* what the tables are joining match.
As we need the name of the most experienced crew member, table that joins on first *SELECT*ed data is actually data *SELECTED* from table *aircrafts*. Using *COUNT(aircrafts.member_id)* first column of second table are values that correspond to how many times did any *member_id* appear in *aircrafts.member_id* column. To be able to *JOIN* table on mutual *member_id* colum, *aircrafts.member_id* column is also selected.
Second table values should be grouped by *member_id* values with *GROUP BY* clause. *LIMIT 1* gives us only one name, and the joined table is ordered by *COUNT(aircrafts.member_id)* column in *DESC* (descending order) so it's the most experienced crew member.
*COALESCE()* function ensures that there is no *NULL* values: changes *NULL* value with wanted value (0).

/*INNER JOIN* was used in order to use up less memory when. It was assumed that at least one crew member has experience with at least one aircraft in order to even finding the name of the most experienced one./

####  4. Find name of the least experienced crew member - that one who knows least aircrafts (counting from zero)

```bash
SELECT crew_members.first_name FROM crew_members
LEFT JOIN (
	SELECT COUNT(aircrafts.member_id) AS most, aircrafts.member_id AS member_id
	FROM aircrafts 
	GROUP BY member_id 
	) b
ON crew_members.member_id = b.member_id
ORDER BY COALESCE(b.most,0),crew_members.member_id ASC
LIMIT 1;
```
*LEFT JOIN* was used in this query in order to include all crew members from *crew_members*, even the ones without any experience.
To ensure their experience was marked as not *NULL* value in joined table, *COALESCE* function was used on second table's column *b.most* with *ORDER BY* clause in *ASC* (ascending) order.

