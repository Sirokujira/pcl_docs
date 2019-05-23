#  written by Jongkyu Kim (j.kim@fu-berlin.de)

import os
import sys

CAT_NAME = 'Classes'
# CAT_NAMES = ['Indexes', 'Functions', 'Struct', 'Enums', 'Defines', 'Classes']
CAT_NAMES = ['Classes']
INDEX_TEMP = "api_index.rst.txt"

def generateIndex(inDir, outDir, outFile):
    listModules = []
    listFiles = []
    # print(os.listdir(inDir))
    for fileName in os.listdir(inDir):
        if os.path.isdir(inDir + "/" + fileName) == True:
            listModules.append(fileName)
        else :
            fileExt = fileName.split(".")[-1]
            if fileExt == "hpp" or fileExt == "cpp" :
                listFiles.append(fileName)

    listModules = sorted(listModules)
    listFiles = sorted(listFiles)
    # print(listModules)

    for CATEGORY_NAME in CAT_NAMES:
        moduleName = outDir.split("/")[-1]
        generateDoxyIndex(outDir, moduleName, CATEGORY_NAME, listModules, listFiles, outFile)

        for listModule in listModules:
            curInDir = inDir + "/" + listModule
            curOutDir = outDir + "/" + listModule
            generateIndex(curInDir, curOutDir, outFile)


def generateDoxyIndex(outDir, moduleName, CATEGORY_NAME, listModules, listFiles, outFile):
    if len(listModules) > 0 and os.path.isdir(outDir) == False:
        os.mkdir(outDir)

    if len(listFiles) == 0:
        return

    # title
    # outFile = open(outDir + ".rst", "w")
    # outFile.write(moduleName[0].upper() + moduleName[1:] + "\n")
    # outFile.write("=" * len(moduleName) + "\n\n")
    # print(CATEGORY_NAME)
    # outFile.write("\n.. toctree::\n")
    # outFile.write("   :maxdepth: 2\n")
    # outFile.write("   :caption: %s:\n\n" % (CATEGORY_NAME))

    # doxygenfile
    for fileName in listFiles :
        outFile.write(".. doxygenfile:: %s/%s\n" % (outDir[2:], fileName))
        outFile.write("   :project: myproject\n\n")

    # toctree
    outFile.write(".. toctree::\n")
    outFile.write("   :caption: %s:\n" % CATEGORY_NAME)
    outFile.write("   :titlesonly:\n")
    outFile.write("   :maxdepth: 1\n")
    outFile.write("   :hidden:\n\n")
    for childModuleName in listModules :
       outFile.write("   %s/%s\n" % (moduleName, childModuleName) )


def generateRST(outDir, moduleName, listModules, listFiles) :
    if len(listModules) > 0 and os.path.isdir(outDir) == False:
        os.mkdir(outDir)

    if len(listFiles) == 0:
        return

    # title
    outFile = open(outDir + ".rst", "w")
    outFile.write(moduleName[0].upper() + moduleName[1:] + "\n")
    outFile.write("=" * len(moduleName) + "\n\n")

    # doxygenfile
    for fileName in listFiles :
        outFile.write(".. doxygenfile:: %s/%s\n" % (outDir[2:], fileName))
        outFile.write("   :project: myproject\n\n")

    # toctree
    outFile.write(".. toctree::\n")
    outFile.write("   :caption: %s:\n" % CAT_NAME)
    outFile.write("   :titlesonly:\n")
    outFile.write("   :maxdepth: 1\n")
    outFile.write("   :hidden:\n\n")
    for childModuleName in listModules :
       outFile.write("   %s/%s\n" % (moduleName, childModuleName) )
    outFile.close()


def generateRSTs(inDir, outDir):
    listModules = []
    listFiles = []
    for fileName in os.listdir(inDir) :
        if os.path.isdir(inDir + "/" + fileName) == True:
            listModules.append(fileName)  
        else :
            fileExt = fileName.split(".")[-1]
            if fileExt == "hpp" or fileExt == "cpp" :
                listFiles.append(fileName)
    
    listModules = sorted(listModules)
    listFiles = sorted(listFiles)

    print(inDir, outDir, listModules, listFiles)

    moduleName = outDir.split("/")[-1]
    generateRST(outDir, moduleName, listModules, listFiles)

    for moduleName in listModules :
        curInDir = inDir + "/" + moduleName
        curOutDir = outDir + "/" + moduleName
        generateRSTs(curInDir, curOutDir)

'''
Alphabet
========

.. doxygenfile:: 
   :project: myproject

.. doxygenfile:: 
   :project: myproject

.. doxygenfile:: 
   :project: myproject

.. toctree::
   :caption: Modules:
   :titlesonly:
   :maxdepth: 1
   :hidden:

   alphabet/aminoacid
   alphabet/gaps
   alphabet/nucleotide
'''


###################
inDir = sys.argv[1]
outDir = sys.argv[2]

# generate index.rst
inFile = open(INDEX_TEMP, "r")
outFile = open(outDir + "/index.rst", "w")
for line in inFile:
    outFile.write(line)
inFile.close()
generateIndex(inDir, outDir, outFile)
outFile.close()
generateRSTs(inDir, outDir)
