# Redis/Lua

This folder contains Redis script in Lua parking.lua. 

To start the script you need to imput the following command which sets gives the script one key(planeID) with argument (3):

```bash
redis-cli --eval parking.lua 1 planeID 3
```

## Problem 

Since we wrote our first task, Picky Airlines has gotten really popular. We expanded our fleet
and now we have 80 autonomous planes! They are pretty awesome, but we haven't
programmed them to find their parking spot yet and the airports are really mad at us since they
just stay on the runway after landing, and the passengers have to walk to the terminal as well.
We own one hundred parking spots, and we are planning to use Redis to assign each plane
(with IDs 1 to 80) to its own parking spot (IDs 1 to 99) which will stay assigned to it forever.

Your task is to write a Redis script in Lua that takes an airplane ID as an argument and assigns
a random available parking spot to the plane if it doesn't have one yet. It should always return
the parking spot ID (even if it was assigned earlier). And don't worry about multiple airports, we will have a separate Redis instance running with this script at each airport.

## Description of solution

Deriving from problem:
  1. create table of parking spots
  2. assign a parking spot for the airplane given by its ID

Before anything happens, we need to select the Redis logical database. 
New connections always use the database 0:

```bash
redis.pcall("select",0)
```
Arguments of keys are always stored in global variable ARGV, and we can store the plane's ID in a local variable:

```bash
local planeID = ARGV[1]
```

To check if the table *parking* already exists (and delete it):

```bash
if redis.pcall("exists", "parking") == 1 then
  redis.pcall("del", "parking");
end
```
To create a new table *parking* with 99 unique spot ID's:

```bash
for i=1,99 do
  redis.pcall("sadd", "parking", i)
end
```
In order to enable script effects replication, you need to issue the following Lua command before any write operated by the script:

```bash
redis.replicate_commands()
```

To assign a place to the plane, function *place_assignment* takes two arguments: a table, plane's ID.

Firstly, *place_assignment* calls another function *is_place_assigned* which takes two arguments: a table, plane's ID; to check if the plane already has it's assigned parking place. For every value in table checks if the planeID value is equal to it:
		a. if equal -> return True
        	b. if no value from table is equal to planeID -> return False
		
```bash
function is_place_assigned(table,planeID)
	for _, value in pairs(table) do
		if value == planeID then
			return true
		end
	end
	return false
end
```
If *is_place_assigned* returns True, *redis.pcall('get',planeID)* command is issued to get the planeID.

```bash
if is_place_assigned(parking,planeID) then
		--print("Plane's parking place is ")
		redis.pcall('get',planeID)
	end
```

Secondly, using *for* loop all values of table *parking* are checked with *redis.pcall('exists', planeID) ~= nil* and empty parking spots are inserted in local variable *free_places*.

```bash
local free_places={}
	
	for i=1, length(parking), 1 do
		if redis.pcall('exists', planeID) ~= nil then
			table.insert(free_places, i)
		end
	end
```

Thirdly, to assign a random parking place to the plane, in local variable *x* random seed function is called. If there are any free spots, in local variable *randomnum* is stored a random number in range [1,length of free_places].
Finally, with *redis.pcall('set', parking[randomnum], planeID)* command, a parking place is assigned to the plane.

```bash
function place_assignment(table,planeID)
	
	local x=math.randomseed( os.time() )
	
	if length(free_places) ~=0 then
	    local randomnum=math.random(length(free_places))
	else
	    randomnum = math.random(99)
	end
	
	redis.pcall('set', parking[randomnum], planeID)

end
```

In third step, length of a local variable was necessary. It was given by function *length* which takes one argument (a table), and in a local variable counts how many keys does table have a.k.a. it's "length".

```bash
function length(table)
	local count=0
	for _, value in pairs(table) do
		count=count+1
	end
	
	return count
end
```

To execute the script, local variable that calls the *place_assignment* function is called:

```bash
local find_it=place_assignment(parking, planeID)

find_it()
```
