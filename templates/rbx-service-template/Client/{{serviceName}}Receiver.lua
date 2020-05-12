local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local ServiceTemplate = require(GetReplicatedStorage("Lib/RbxDependency/Service"))

local Class = require(GetReplicatedStorage("Lib/middleclass"))
local {{ serviceName }}Receiver = Class("{{ serviceName }}Receiver", ServiceTemplate)	

function {{ serviceName }}Receiver:initialize()
	local dependencies = { "{{ serviceName }}Replicator" }
	ServiceTemplate.initialize(self, "{{ serviceName }}Receiver", dependencies)
end

function {{ serviceName }}Receiver:ConnectEndpoints()
    ServiceTemplate.ConnectEndpoints(self)

	local {{ serviceName }}Events = GetReplicatedStorage("Events/{{ serviceName }}")
    if {{ serviceName }}Events == nil then
        ServiceTemplate.Warn(self, "Could not find {{serviceName}} events folder.")
        return
    end
    {% for event in events %}
	local receive{{ event.name }} = GetReplicatedStorage("request{{ event.name }}", {{ serviceName }}Events)
    if receive{{ event.name }} == nil then
        ServiceTemplate.Warn(self, "Could not find receive event for {{ event.name }}.")
    else
        receive{{ event.name }}.OnClientEvent:Connect(function({{ event.params }}) 
            self:{{ event.name }}({{ event.params }})
        end)
    end
	{% endfor %}
end
{% for event in events %}
function {{ serviceName }}Receiver:Receive{{ event.name }}({{ event.params }})
	print("{{ serviceName }}Receiver -- Recieving info about {{ event.name }} action!")
	if player ~= ServiceTemplate.Player then
		return
	end
	
	self.{{ serviceName }}Replicator:{{ event.name }}({{ event.params }})
end
{% endfor %}
return {{ serviceName }}Receiver