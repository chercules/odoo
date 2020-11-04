#Diccionarios se declaran con llaves {}
diccionario = {"SV":"EL SALVADOR",
               "GT":"GUATEMALA",
               "NI":"NICARAGUA",
               "HO":"HONDURAS"}

print(diccionario.get("GT"))

for i,valor in diccionario.items():
    print(i,":",valor)

print(diccionario.keys())
print(diccionario.values())

if "GT" in diccionario.keys():
    print(diccionario.get("GT"))