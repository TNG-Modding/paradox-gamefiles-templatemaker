local GetReplicatedStorage = require(game.ReplicatedStorage:WaitForChild("GetReplicatedStorage"))
local Class = require(GetReplicatedStorage("Lib/middleclass"))
local PlayerCharacterManager = require(GetReplicatedStorage("Lib/RbxDependency/PlayerCharacterManager"))

local {{ serviceName }}Manager = Class("{{ serviceName }}Manager", PlayerCharacterManager)

local Players = game:GetService("Players")

function {{ serviceName }}Manager:initialize()
	local dependencies = { "{{ serviceName }}Processor", "{{ serviceName }}Responder" }
	PlayerCharacterManager.initialize(self, "{{ serviceName }}Manager", dependencies)
end

function {{ serviceName }}Manager:OnPlayerAdded(player)
    PlayerCharacterManager.OnPlayerAdded(self, player)
end

function {{ serviceName }}Manager:OnPlayerRemoved(player)
    PlayerCharacterManager.OnPlayerRemoved(self, player)
end
{% for event in events %}
function {{ serviceName }}Manager:{{ event.name }}({{ event.params }})
	print("{{ serviceName }}Manager -- Managing {{ event.name }} action!")
	self.{{ serviceName }}Processor:Process{{ event.name }}({{ event.params }})
	self.{{ serviceName }}Responder:Respond{{ event.name }}({{ event.params }})
end
{% endfor %}
function {{ serviceName }}Manager:Update(step)
	PlayerCharacterManager.Update(self, step)
end

return {{ serviceName }}Manager
