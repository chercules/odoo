"""
Notas = {"Carlos": 10,"Adriana":7,"Lucy":10,"Mario":6.5,"Jesus":8}

reprobados= [nombres for nombres,nota in Notas.items() if nota <= 7]
print(reprobados)


inventario = {"Puntas":30,
              "Tornillos": 140,
              "Tuercas":250,
              "Arandelas":70}

pedidos = [ producto for producto,unidades in inventario.items() if unidades<100 ]
print(pedidos)

asteriscos = [n*'*' for n in range(1,6)]
print(asteriscos)

palabras = ["casa","mesa","silla","ventana"]

iniciales =[inicial[0] for inicial in palabras]
print(iniciales)

datos  =[14 , 18, 21, 29,36,41,58,63,74]

pares = [par for par in datos if par % 2 == 0 if par >30 ]
print(pares)

utensilios = ["Mesa","Interruptor", "Silla", "Microscopio","Cubo"]
mayoresa7 = [mayor for mayor in utensilios if len(mayor)>7]
print(mayoresa7)

multiplos = [mul for mul in range(1,31) if mul%11 == 0 or mul%7 == 0]
print(multiplos)

pares = [npar if npar % 2 ==0 else 0 for npar in range(1,16)]
print(pares)

dt = [7,"H",2.5,"m",8.2,24,"p"]

dtp = ["Texto" if type(tipo)== str else
       "Numero" if type(tipo)==int else
       "Flotante" for tipo in dt ]
print(dtp)


personas = [["Jorge",36],["Silvia",24],["Tomas",47],
            ["Irene",19],["Ignacio",21],["Julia",43],
            ["Sara",38],["Miguel",25]]
Mayores30 = [person for person in personas if person[1]>30]
print(Mayores30)

NombreMayores = [pm[0] for pm in Mayores30 if pm[1]>30]
print(NombreMayores)
"""

personas = [["Jorge",36],["Silvia",24],["Tomas",47],
            ["Irene",19],["Ignacio",21],["Julia",43],
            ["Sara",38],["Miguel",25]]
Mayores230 = [[per[0],"Mayor"] if per[1]>30 else
             [per[0],"Menor"] for per in personas ]
print(Mayores230)
Mayores330 = [[per[0],"Mayor" if per[1]>30 else "Menor"]
             for per in personas ]
print(Mayores330)

