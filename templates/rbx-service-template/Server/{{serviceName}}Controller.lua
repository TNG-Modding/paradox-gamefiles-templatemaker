local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local Class = require(GetReplicatedStorage("Lib/middleclass"))
local Controller = require(GetReplicatedStorage("Lib/RbxDependency/Controller"))

local {{ serviceName }}Controller = Class("{{ serviceName }}Controller", Controller)

local Players = game:GetService("Players")

function {{ serviceName }}Controller:initialize()
	local dependencies = { "{{ serviceName }}Manager" }
	Controller.initialize(self, "{{ serviceName }}Controller", dependencies)
end

function {{ serviceName }}Controller:ConnectEndpoints()
    Controller.ConnectEndpoints(self)

	local {{ serviceName }}Events = GetReplicatedStorage("Events/{{ serviceName }}")
    if {{ serviceName }}Events == nil then
        Controller.Warn(self, "Could not find {{serviceName}} events folder.")
        return
    end

    {% for event in events %}
	local request{{ event.name }} = GetReplicatedStorage("Request{{ event.name }}", {{ serviceName }}Events)
    if request{{ event.name }} == nil then
        Controller.Warn(self, "Could not find request event for {{ event.name }}.")
    else
        request{{ event.name }}.OnServerEvent:Connect(function({{ event.params }}) 
            self:{{ event.name }}({{ event.params }})
        end)
    end
	{% endfor %}
end

function {{ serviceName }}Controller:OnPlayerAdded(player)
    self.{{ serviceName }}Manager:AddPlayer(player)
end

function {{ serviceName }}Controller:OnPlayerRemoved(player)
    self.{{ serviceName }}Manager:RemovePlayer(player)
end
{% for event in events %}
function {{ serviceName }}Controller:{{ event.name }}({{ event.params }})	
	self.{{ serviceName }}Manager:{{ event.name }}({{ event.params }})
end
{% endfor %}
return {{ serviceName }}Controller
