local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local Class = require(GetReplicatedStorage("Lib/middleclass"))

local Roact = require(GetReplicatedStorage("Roact/init"))
local RoactUIController = require(GetReplicatedStorage("Lib/RbxDependency/RoactUIController"))

local {{ serviceName }}UIReplicator = Class("{{ serviceName }}UIReplicator", RoactUIController)

function {{ serviceName }}UIReplicator:initialize()
	
end
{% for event in events %}
function {{ serviceName }}UIReplicator:UpdateOnFaked{{ event.name }}({{ event.params }})
	print("{{ serviceName }}UIReplicator -- Updating ui about faked client version of {{ event.name }} action!")
end

function {{ serviceName }}UIReplicator:UpdateOn{{ event.name }}({{ event.params }})
	print("{{ serviceName }}UIReplicator -- Updating ui about {{ event.name }} action!")
end
{% endfor %}
return {{ serviceName }}UIReplicator
