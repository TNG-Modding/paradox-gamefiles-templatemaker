import jinja2
import json, os
from .contentSubTypes import subTypes
from .contentTypeSubtypes import contentTypeSubTypes
import shutil

def defineOrder(displayName, modRootDirectoryPath, specFilepath, templatesDirectoryPath, contentSubType):
    
    outputPath = str.lower(contentSubType["name"].replace(" ","_"))
    return {
        "name": "%s %s" % (displayName, contentSubType["name"]),
        "specFilePath": specFilepath,
        "templateDirectoryPath": os.path.join(templatesDirectoryPath, outputPath),
        "outputDirectoryPath": os.path.join(modRootDirectoryPath, contentSubType["outputPath"]),
        "disabled": not contentSubType["isTemplate"], # Graphics should start disabled so they are only run when the user wants to.
        "dumpContents": contentSubType["isDumpsContents"],
        "isBom": contentSubType["isBom"]
    }

def copyStockFileToOrderTemplatesFolder(displayName, contentSubtypeInstructions, stockFilepath, orderContentTemplatesDirectoryPath):
    contentSubtypeVarname = str.lower(contentSubtypeInstructions["name"].replace(" ","_"))
    orderTemplatesDirectoryPath = os.path.abspath(os.path.join(orderContentTemplatesDirectoryPath, contentSubtypeVarname))
    if not os.path.exists(orderTemplatesDirectoryPath):
        os.makedirs(orderTemplatesDirectoryPath)
    
    fileNameJinjaTemplate = jinja2.Environment(loader=jinja2.BaseLoader).from_string(os.path.basename(stockFilepath))
    

    orderSpecFile = {
        "varname": "%s_{{varname}}" % str.lower(displayName.replace(" ", "_")),
        "displayName": "{{displayName}} %s" % displayName,
        "desc": "{{desc}}",
    }

    newFileName = fileNameJinjaTemplate.render(orderSpecFile)
    outputFilepath = os.path.join(orderTemplatesDirectoryPath, newFileName)
    if os.path.splitext(stockFilepath)[1] == ".dds":
        shutil.copy(stockFilepath, outputFilepath)
        return
    
    stockFile = open(stockFilepath, "r")
    fileContentsJinjaTemplate = jinja2.Environment(loader=jinja2.BaseLoader).from_string(stockFile.read())
    stockFile.close()
    contents = fileContentsJinjaTemplate.render(orderSpecFile)
    
    with open(outputFilepath, "w") as outputFile:
        outputFile.write(contents)

def defineOrders(displayName, modRootDirectoryPath, specFilepath, templatesOutputDirectoryPath, contentSubTypes):    
    orders = []
    stockFilesDirectoryPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "contentTemplates")
    for contentSubType in contentSubTypes:
        if not contentSubType in subTypes:
            print("Missing %s content type." % contentSubType)
            continue
        subType = subTypes[contentSubType]
        order = defineOrder(displayName, modRootDirectoryPath, specFilepath, templatesOutputDirectoryPath, subType)

        for relativeStockFilePath in subType["files"]:
            stockFilePath = os.path.join(stockFilesDirectoryPath, relativeStockFilePath)
            copyStockFileToOrderTemplatesFolder(displayName, subType, stockFilePath, templatesOutputDirectoryPath)
                
                
        orders.append(order)
    return orders

def createContent(type, intemplatorDirectoryPath, modRootDirectoryPath, displayName):
    varName = str.lower(displayName.replace(" ", "_"))

    specContents = [
        {
            "varname": varName,
            "displayName": displayName,
            "desc": displayName
        }
    ]
    specsFilepath = os.path.join(intemplatorDirectoryPath, "specs")

    specFilepath = os.path.join(specsFilepath, "%s.json" % varName)
    with open(specFilepath, "w", encoding="utf-8") as specFile:
        json.dump(specContents, specFile, indent=4)

    templatesFilepath = os.path.join(intemplatorDirectoryPath, "templates")
    contentTemplatesDirectoryPath = os.path.join(templatesFilepath, varName)
    if os.path.exists(contentTemplatesDirectoryPath):
        shutil.rmtree(contentTemplatesDirectoryPath, ignore_errors=False, onerror=None)
    os.mkdir(contentTemplatesDirectoryPath)
    
    if not type in contentTypeSubTypes:
        print("Missing %s type." % type)
        return
    subTypes = contentTypeSubTypes[type]

    orders = defineOrders(displayName, modRootDirectoryPath, specFilepath, contentTemplatesDirectoryPath, subTypes)

    return orders 