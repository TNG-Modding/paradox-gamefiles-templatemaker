local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local ServiceTemplate = require(GetReplicatedStorage("Lib/RbxDependency/Service"))

local Class = require(GetReplicatedStorage("Lib/middleclass"))
local {{ serviceName }}Responder = Class("{{ serviceName }}Responder", ServiceTemplate)

function {{ serviceName }}Responder:initialize()
	local dependencies = { }
	ServiceTemplate.initialize(self, "{{ serviceName }}Responder", dependencies)

	local {{ serviceName }}Events = GetReplicatedStorage("Events/{{ serviceName }}")
    if {{ serviceName }}Events == nil then
        ServiceTemplate.Warn(self, "Could not find {{serviceName}} events folder.")
        return
	end
	{% for event in events %}
	self.Receive{{ event.name }} = GetReplicatedStorage("Request{{ event.name }}", {{ serviceName }}Events){% endfor %}
end
{% for event in events %}
function {{ serviceName }}Responder:Respond{{ event.name }}({{ event.params }})
	print("{{ serviceName }}Responder -- Responding about {{ event.name }}!")
	self.Receive{{ event.name }}:FireAllClients({{ event.params }})
end
{% endfor %}
return {{ serviceName }}Responder
