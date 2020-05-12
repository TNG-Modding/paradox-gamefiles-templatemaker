local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local Class = require(GetReplicatedStorage("Lib/middleclass"))
local ServiceTemplate = require(GetReplicatedStorage("Lib/RbxDependency/Service"))

local {{ serviceName }}Requestor = Class("{{ serviceName }}Requestor")

function {{ serviceName }}Requestor:initialize()
	local dependencies = { }
	ServiceTemplate.initialize(self, "{{ serviceName }}Requestor", dependencies)

	local {{ serviceName }}Events = GetReplicatedStorage("Events/{{ serviceName }}")
    if {{ serviceName }}Events == nil then
        ServiceTemplate.Warn(self, "Could not find {{serviceName}} events folder.")
        return
	end
	{% for event in events %}
	self.Request{{ event.name }} = GetReplicatedStorage("Request{{ event.name }}", {{ serviceName }}Events){% endfor %}
end
{% for event in events %}
function {{ serviceName }}Requestor:Request{{ event.name }} ({{ event.params }})
	print("{{ serviceName }}Requestor -- Requesting {{ event.name }}!")
	self.Request{{ event.name }}:FireServer({{ event.params }})
end
{% endfor %}
return {{ serviceName }}Requestor
