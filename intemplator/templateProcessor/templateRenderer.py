import jinja2
import os

from . import fileWriter

def processCopiedTemplate(outputPath):
    for path, dirs, files in os.walk(outputPath):
        for filename in files:
            fullpath = os.path.join(path, filename)
            
            templateFile = open(fullpath, 'r')
            contents = templateFile.read()
            
            templateFile.close()

            with open(fullpath, 'w') as f:
                f.write(contents)

def renderTemplate(newFilePath, inputFile, isBom):    
    jinjaEnvironment = jinja2.Environment(loader = jinja2.FileSystemLoader(newFilePath))
    
    for root, _, files in os.walk(newFilePath):
        for file in files:
            
            filepath = os.path.join(root, file)

            relativeTemplatePath = os.path.relpath(filepath, newFilePath)
            fileNameTemplate = jinja2.Environment(loader=jinja2.BaseLoader).from_string(file)
            newFileName = fileNameTemplate.render(inputFile)
            newFilepath = os.path.join(root, newFileName)
            if os.path.splitext(relativeTemplatePath)[1] == ".dds":
                os.rename(filepath, newFilepath)            
                continue
            template = jinjaEnvironment.get_template(relativeTemplatePath)
            templatedContents = template.render(inputFile)

            fileWriter.writeFileContents(filepath, templatedContents, isBom)
            
            
            os.rename(filepath, newFilepath)            


