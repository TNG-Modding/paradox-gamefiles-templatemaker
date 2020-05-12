return {
    {{ serviceName }}IntentionReceiver = require(script.Parent.Client.{{ serviceName }}IntentionReceiver),
    {{ serviceName }}Receiver = require(script.Parent.Client.{{ serviceName }}Receiver),
    {{ serviceName }}Replicator = require(script.Parent.Client.{{ serviceName }}Replicator),
    {{ serviceName }}Requestor = require(script.Parent.Client.{{ serviceName }}Requestor),
    {{ serviceName }}UIReplicator = require(script.Parent.Client.{{ serviceName }}UIReplicator),
}