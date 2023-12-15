import easy_namespacing as EN

__all__ = EN.listMethods(__file__)

methods=EN.dynamicImporter(__file__, "entity_generator", "messages")

def listM():
    return list(map(EN.listToKey, EN.listMethods(__file__)))

def useM(label):
    global methods
    return methods[label].generateMessage()
