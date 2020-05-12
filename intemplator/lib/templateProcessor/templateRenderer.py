import jinja2
import os

from . import fileWriter as fileWriter

def ProcessCopiedTemplate(outputPath):
    for path, dirs, files in os.walk(PATH):
        for filename in files:
            fullpath = os.path.join(path, filename)
            
            templateFile = open(fullpath, 'r')
            contents = templateFile.read()
            
            templateFile.close()

            with open(fullpath, 'w') as f:
                f.write(data)

def RenderTemplate(newFilePath, inputFile):    
    jinjaEnvironment = jinja2.Environment(loader = jinja2.FileSystemLoader(newFilePath))
    
    for root, dirs, files in os.walk(newFilePath):
        for file in files:
            
            filepath = os.path.join(root, file)

            relativeTemplatePath = os.path.relpath(filepath, newFilePath)

            template = jinjaEnvironment.get_template(relativeTemplatePath)
            templatedContents = template.render(inputFile)

            fileWriter.WriteFileContents(filepath, templatedContents)
            
            fileNameTemplate = jinja2.Environment(loader=jinja2.BaseLoader).from_string(file)
            newFileName = fileNameTemplate.render(inputFile)
            os.rename(filepath, os.path.join(root, newFileName))            


