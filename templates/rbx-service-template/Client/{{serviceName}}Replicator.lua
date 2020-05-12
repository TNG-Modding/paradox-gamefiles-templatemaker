local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local Class = require(GetReplicatedStorage("Lib/middleclass"))
local ServiceTemplate = require(GetReplicatedStorage("Lib/RbxDependency/Service"))

local {{ serviceName }}Replicator = Class("{{ serviceName }}Replicator", ServiceTemplate)

function {{ serviceName }}Replicator:initialize()
	local dependencies = { "{{ serviceName }}UIReplicator" }
	ServiceTemplate.initialize(self, "{{ serviceName }}Replicator", dependencies)
end
{% for event in events %}
function {{ serviceName }}Replicator:Fake{{ event.name }}({{ event.params }}) 
	print("{{ serviceName }}Replicator -- Managing faked client version of {{ event.name }} action!")
	self.{{ serviceName }}UIReplicator:UpdateOnFaked{{ event.name }}({{ event.params }})
end

function {{ serviceName }}Replicator:{{ event.name }}({{ event.params }}) 
	print("{{ serviceName }}Replicator -- Managing {{ event.name }} action!")
	self.{{ serviceName }}UIReplicator:UpdateOn{{ event.name }}({{ event.params }})
end
{% endfor %}
function {{serviceName}}Replicator:Update(dt)
end

return {{ serviceName }}Replicator