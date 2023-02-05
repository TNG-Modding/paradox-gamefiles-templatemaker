import json
import os

def getTemplateFilePath(templateName):
    return os.path.join(os.path.dirname(__file__),'templates/' + templateName)

def readJson (path):
    with open(path, "r", encoding="utf-8") as jsonFile:
        data = json.load(jsonFile)
        return data