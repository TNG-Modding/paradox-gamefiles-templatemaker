from . import fileReader, fileWriter, templateRenderer

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
    intemplatorOrders = fileReader.readJson("intemplator.json")
    
    for order in intemplatorOrders:
        if order["disabled"]:
            continue
        print("processing order for %s" % (order["name"]))
        processOrder(order["templateDirectoryPath"], order["specFilePath"], order["outputDirectoryPath"], order["dumpContents"], order["isBom"])