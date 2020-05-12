return {
    {{ serviceName }}Controller = require(script.Parent.Server.{{ serviceName }}Controller),
    {{ serviceName }}Manager = require(script.Parent.Server.{{ serviceName }}Manager),
    {{ serviceName }}Processor = require(script.Parent.Server.{{ serviceName }}Processor),
    {{ serviceName }}Responder = require(script.Parent.Server.{{ serviceName }}Responder)
}