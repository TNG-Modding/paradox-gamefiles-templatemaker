import os

from . import fileReader as fileReader
from . import fileWriter as fileWriter
from . import templateRenderer as templateRenderer

def ProcessTemplateForSpec(templateFilePath, spec, outputPath, dumpContents, isBom = False):
    print("Writing %s using %s to %s" % (spec["varname"], templateFilePath, outputPath))

    tempOutputDirectoryPath = "./%s" % (spec["varname"])

    fileWriter.CreateOrReplaceDirectoryWithFolder(templateFilePath, tempOutputDirectoryPath)
    templateRenderer.RenderTemplate(tempOutputDirectoryPath, spec, isBom)
    
    if dumpContents:
        fileWriter.DumpFolderContentsIntoDirectory(tempOutputDirectoryPath, outputPath)
        fileWriter.RemoveDirectory(tempOutputDirectoryPath)
    else:
        fileWriter.MoveDirectory(tempOutputDirectoryPath, outputPath)

def ProcessOrder (templateFilePath, specFilePath, outputPath, dumpContents, isBom = False):

    specs = fileReader.ReadJson(specFilePath)
    
    if "specs" in specs:
        # Series of specs in the file
        for spec in specs["specs"]:
            ProcessTemplateForSpec(templateFilePath, spec, outputPath, dumpContents, isBom)
    else:
        # Only one spec in the file
        ProcessTemplateForSpec(templateFilePath, specs, outputPath, dumpContents, isBom)

def ProcessOrders ():
    intemplator = fileReader.ReadJson("intemplator.json")
    
    for order in intemplator["orders"]:
        print("Processing order for %s" % (order["name"]))
        ProcessOrder(order["templateDirectoryPath"], order["specFilePath"], order["outputDirectoryPath"], order["dumpContents"], order["isBom"])