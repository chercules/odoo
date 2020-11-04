#Listas se declaran con Corchetes y el Indice comienza con cero
#            0   1   2   3
secuencia = [1 , 3 , 5 , 7]
print(secuencia[2])

#Agregar un elemento a una Lista
secuencia.append(22)

#Imprimir el ultimo elemento se hace con indice -1
print(secuencia[-1])

#Eliminar el ultimo elemento de una lista
valor_eliminado=secuencia.pop(-1)
print(secuencia," Valor Eliminado", valor_eliminado)

#Recorrer una Lista
for i in secuencia:
    print(i)

#TUPLAS NO SE PUEDEN MODIFICAR SUS ELEMENTOS
claves = ("123","es")
print(claves[1])
