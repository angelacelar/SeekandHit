--Selecting the Redis logical database. 
--New connections always use the database 0.

redis.pcall("select",0)

local planeID = ARGV[1]

if redis.pcall("exists", "parking") == 1 then
  redis.pcall("del", "parking");
end

for i=1,99 do
  redis.pcall("sadd", "parking", i)
end

redis.replicate_commands()

function place_assignment(table,planeID)
	
	if is_place_assigned(parking,planeID) then
		--print("Plane's parking place is ")
		redis.pcall('get',planeID)
	end
		
	local free_places={}
	
	for i=1, length(parking), 1 do
		if redis.pcall('exists', planeID) ~= nil then
			table.insert(free_places, i)
		end
	end
	
	local x=math.randomseed( os.time() )
	
	if length(free_places) ~=0 then
	    local randomnum=math.random(length(free_places))
	else
	    randomnum = math.random(99)
	end
	
	redis.pcall('set', parking[randomnum], planeID)

end

function is_place_assigned(table,planeID)
	for _, value in pairs(table) do
		if value == planeID then
			return true
		end
	end
	return false
end

function length(table)
	local count=0
	for _, value in pairs(table) do
		count=count+1
	end
	
	return count
end

local find_it=place_assignment(parking, planeID)

find_it()
