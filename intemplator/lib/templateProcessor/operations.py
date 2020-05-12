# Template Processor
import os
import jinja2
import json
import errno
import shutil

from . import client

def ProcessTemplate(templateName, inputFilePath, outputPath):
    templateFilePath = GetTemplateFilePath(templateName)
    inputData = GetInputFile(inputFilePath)
    serviceName = inputData["serviceName"]
    newFilePath = os.path.join(outputPath, serviceName)
    CopyTemplate(templateFilePath, newFilePath)
    RenderTemplate(newFilePath, inputData)