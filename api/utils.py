# -------------------- UTILS -------------------

# Pasa del cursor devuelto por Mongo a un array de diccionarios
def cursorToArray(cursor):
    elements = []
    for item in cursor:
        print(item)
        elements.append(cursorItemToDictionary(item))
    print(elements)
    return elements

# Pasa del diccionario que devuelve Mongo a otro sin el object ID
def cursorItemToDictionary(item):
    dic = {}
    for key in item.keys():
        if (key != '_id'):
            dic[key] = item[key]
    return dic
