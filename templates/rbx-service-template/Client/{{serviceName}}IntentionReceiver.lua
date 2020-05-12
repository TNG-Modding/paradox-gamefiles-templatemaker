local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local ServiceTemplate = require(GetReplicatedStorage("Lib/RbxDependency/Service"))

local Class = require(GetReplicatedStorage("Lib/middleclass"))
local {{ serviceName }}IntentionReceiver = Class("{{ serviceName }}IntentionReceiver", ServiceTemplate)

function {{ serviceName }}IntentionReceiver:initialize()
	local dependencies = { "{{ serviceName }}Requestor", "{{serviceName}}Replicator" }
	ServiceTemplate.initialize(self, "{{ serviceName }}IntentionReceiver", dependencies)
end
{% for event in events %}
function {{ serviceName }}IntentionReceiver:Intend{{ event.name }} ({{ event.params }}) 
	print("{{ serviceName }}IntentionReceiver -- Intending {{ event.name }}!")
	self.{{ serviceName }}Replicator:Fake{{ event.name }} ({{ event.params }})
	self.{{ serviceName }}Requestor:Request{{ event.name }} ({{ event.params }})
end
{% endfor %}
return {{ serviceName }}IntentionReceiver