CREATE TABLE "aircrafts" (
	aircraft_id int NOT NULL PRIMARY KEY,
	member_id int,
	was_pilot char(1) default 'F',
	FOREIGN KEY(member_id) REFERENCES crew_members(member_id)
);

INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (15,1),(3,2),(1,3),(19,4),(10,5),(5,6),(10,7),(6,8),(11,9),(12,10);
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (17,11,'T'),(6,12,'T'),(5,13,'T'),(13,14,'F'),(20,15,'F'),(14,16,'T'),(2,17,'T'),(8,18,'T'),(3,19,'T'),(19,20,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (6,21,'F'),(5,22,'F'),(2,23,'T'),(9,24,'T'),(8,25,'T'),(10,26,'F'),(7,27,'T'),(1,28,'F'),(17,29,'F'),(16,30,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (6,31,'F'),(8,32,'F'),(14,33,'F'),(20,34,'F'),(1,35,'T'),(16,36,'F'),(3,37,'T'),(11,38,'F'),(11,39,'T'),(18,40,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (8,41,'T'),(1,42,'T'),(8,43,'T'),(6,44,'T'),(1,45,'T'),(3,46,'F'),(17,47,'F'),(15,48,'T'),(10,49,'F'),(6,50,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (4,51,'F'),(18,52,'F'),(10,53,'F'),(19,54,'T'),(17,55,'T'),(18,56,'F'),(2,57,'F'),(9,58,'T'),(19,59,'F'),(19,60,'T');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (20,61,'F'),(20,62,'T'),(19,63,'F'),(8,64,'F'),(20,65,'F'),(10,66,'T'),(7,67,'F'),(4,68,'T'),(16,69,'F'),(20,70,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (1,71,'T'),(17,72,'F'),(2,73,'T'),(14,74,'T'),(3,75,'T'),(14,76,'T'),(9,77,'F'),(6,78,'F'),(8,79,'F'),(4,80,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (17,81,'F'),(3,82,'T'),(17,83,'T'),(9,84,'T'),(20,85,'F'),(16,86,'F'),(13,87,'T'),(2,88,'T'),(16,89,'F'),(18,90,'F');
INSERT INTO "aircrafts" (member_id,aircraft_id) VALUES (19,91,'F'),(4,92,'F'),(8,93,'F'),(1,94,'F'),(6,95,'T'),(5,96,'F'),(5,97,'F'),(14,98,'T'),(9,99,'T'),(14,100,'F');




'OVAKO VALJA'