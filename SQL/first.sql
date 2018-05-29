CREATE DATABASE crewdb;
\c crewdb
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




'C:/Users/Korisnik/Desktop/dataMay-24-2018-aircrafts.sql'

'PRVA TOČKA'
SELECT crew_members.first_name FROM crew_members ORDER BY birth_date LIMIT 1;

'Find name of the n-th crew member (second oldest, fifth oldest and so on)'
SELECT crew_members.first_name FROM crew_members ORDER BY birth_date LIMIT 1 OFFSET 1;

'Find name of the most experienced crew member - that one who knows most aircrafts'
SELECT crew_members.first_name FROM crew_members 
INNER JOIN (
	SELECT COUNT(aircrafts.member_id) AS most, aircrafts.member_id AS member_id 
	FROM aircrafts 
	GROUP BY member_id 
	) crewtb 
ON crew_members.member_id = crewtb.member_id 
ORDER BY COALESCE(crewtb.most) DESC
LIMIT 1;

'Find name of the least experienced crew member - that one who knows least aircrafts (counting from zero)'
SELECT crew_members.first_name FROM crew_members
LEFT JOIN (
	SELECT COUNT(aircrafts.member_id) AS most, aircrafts.member_id AS member_id
	FROM aircrafts 
	GROUP BY member_id 
	) b
ON crew_members.member_id = b.member_id
ORDER BY COALESCE(b.most,0),crew_members.member_id ASC
LIMIT 1;
