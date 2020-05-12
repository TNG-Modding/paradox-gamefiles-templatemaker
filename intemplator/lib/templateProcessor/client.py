def CopyTemplate(sourceDirectory, outputDirectory):
    try:
        if os.path.isdir(outputDirectory):
            shutil.rmtree(outputDirectory)
        shutil.copytree(sourceDirectory, outputDirectory)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(sourceDirectory, outputDirectory)
        else:
            print('Directory not copied. Error: %s' % e)

def ProcessCopiedTemplate(outputPath):
    for path, dirs, files in os.walk(PATH):
        for filename in files:
            fullpath = os.path.join(path, filename)
            
            templateFile = open(fullpath, 'r')
            contents = templateFile.read()
            
            templateFile.close()

            with open(fullpath, 'w') as f:
                f.write(data)

def GetInputFile (path):
    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)
        return data

def RenderTemplate(newFilePath, inputFile):
    # print(newFilePath)
    jinjaEnvironment = jinja2.Environment(loader = jinja2.FileSystemLoader(newFilePath))
    for root, dirs, files in os.walk(newFilePath):
        for file in files:
            filepath = os.path.join(root, file)
            relativeTemplatePath = os.path.relpath(filepath, newFilePath)
            template = jinjaEnvironment.get_template(relativeTemplatePath)
            templatedContents = template.render(inputFile)

            path = os.path.join(root, file)
            templatedFile = open(filepath, 'w')
            templatedFile.write(templatedContents)
            templatedFile.close()
            
            fileNameTemplate = jinja2.Environment(loader=jinja2.BaseLoader).from_string(file)
            newFileName = fileNameTemplate.render(inputFile)
            os.rename(path, os.path.join(root, newFileName))            

def GetTemplateFilePath(templateName):
    return os.path.join(os.path.dirname(__file__),'templates/' + templateName)
