from . import fileReader, fileWriter, templateRenderer, contentCreator
import json, os

def processTemplateForSpec(templateFilePath, spec, outputPath, dumpContents, isBom = False):
    print("Writing %s using %s to %s" % (spec["varname"], templateFilePath, outputPath))

    tempOutputDirectoryPath = "./%s" % (spec["varname"])

    fileWriter.createOrReplaceDirectoryWithFolder(templateFilePath, tempOutputDirectoryPath)
    templateRenderer.renderTemplate(tempOutputDirectoryPath, spec, isBom)

    if dumpContents:
        fileWriter.dumpFolderContentsIntoDirectory(tempOutputDirectoryPath, outputPath)
        fileWriter.removeDirectory(tempOutputDirectoryPath)
    else:
        fileWriter.moveDirectory(tempOutputDirectoryPath, outputPath)

def processOrder(templateFilePath, specFilePath, outputPath, dumpContents, isBom = False):
    specs = fileReader.readJson(specFilePath)
    
    for spec in specs:
        processTemplateForSpec(templateFilePath, spec, outputPath, dumpContents, isBom)

def processOrders():
    intemplatorOrders = fileReader.readJson("orders.json")
    
    for order in intemplatorOrders:
        if order["disabled"]:
            continue
        print("processing order for %s" % (order["name"]))
        processOrder(order["templateDirectoryPath"], order["specFilePath"], order["outputDirectoryPath"], order["dumpContents"], order["isBom"])

def createNewOrder(name, type):    
    ordersFile = open("./orders.json", "r", encoding="utf-8")
    orders = json.load(ordersFile)
    ordersFile.close()

    createdOrders = contentCreator.createContent(type, "./", "../", name)
    for createdOrder in createdOrders:
        for existingOrder in orders:
            if existingOrder["name"] != createdOrder["name"]:
                continue
            orders.remove(existingOrder)
            break
        orders.append(createdOrder)
    
    with open("./orders.json", "w", encoding="utf-8") as ordersFile:
        json.dump(orders, ordersFile, indent=4)

def setup():
    if os.path.exists("./intemplator") or os.path.exists("./orders.json"):
        print("Already initialized.")
        return
    os.mkdir("./intemplator")
    os.mkdir("./intemplator/templates")
    os.mkdir("./intemplator/specs")
    with open("./intemplator/orders.json", "w", encoding="utf-8") as ordersFile:
        json.dump([], ordersFile, indent=4)
