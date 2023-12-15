import os
import importlib

def listToKey(method):
    return method[:-3].replace("_",".")

def onlyVariants(filename):
    if filename[:2]=="__" or filename[-3:]!=".py":
        return False
    else:
        return True

def onlyGroups(filename):
    if filename[:2]=="__" or filename[-3:]==".py":
        return False
    else:
        return True

def listMethods(initModPath):
    methods=os.listdir(os.path.dirname(initModPath))
    methods=list(filter(onlyVariants, methods))
    return methods

def listGroups(initModPath):
    methods=os.listdir(os.path.dirname(initModPath))
    methods=list(filter(onlyGroups, methods))
    return methods

def dynamicImporter(initModPath, namespace, library):
    exported={}
    modulenames=listMethods(initModPath)
    for method in modulenames:
        methodkey=listToKey(method)
        exported[methodkey]=importlib.import_module(namespace+"."+library+"."+method[:-3])
    return exported
