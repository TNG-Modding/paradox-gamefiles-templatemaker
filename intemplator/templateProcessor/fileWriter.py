import errno
import shutil
import os
import codecs

def dumpFolderContentsIntoDirectory(sourceDirectory, outputDirectory):    
    files = os.listdir(sourceDirectory)
    for f in files:
        oldFileLocation = os.path.join(sourceDirectory, f)
        newFileLocation = os.path.join(outputDirectory, f)
        shutil.move(oldFileLocation, newFileLocation)

def createOrReplaceDirectoryWithFolder(sourceDirectory, outputDirectory):
    try:
        if os.path.isdir(outputDirectory):
            shutil.rmtree(outputDirectory)
        shutil.copytree(sourceDirectory, outputDirectory)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(sourceDirectory, outputDirectory)
        else:
            print('Directory not copied. Error: %s' % e)

def moveDirectory(sourceDirectory, outputDirectory):
    outputFilePath = os.path.join(outputDirectory, os.path.basename(sourceDirectory))
    if os.path.exists(outputFilePath):
        shutil.rmtree(outputFilePath)
    shutil.move(sourceDirectory, outputDirectory)

def removeDirectory(directoryPath):
    try:
        shutil.rmtree(directoryPath)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

def writeFileContents(filepath, contents, isBom):
    encoding = isBom and 'utf-8-sig' or 'utf-8'
    file = codecs.open(filepath, 'w', encoding)
    file.write(contents)
    file.close()

