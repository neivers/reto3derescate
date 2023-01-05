while True:
    try:
        entrada_1 = input().split(" ")
        if int(entrada_1[0]) >= 1:
            break
        else:
            print("")
    except:
        print("")

existencia = []        
for i in range(int(entrada_1[0])):
    while True:
        entrada_2 = []
        entrada_2.append(i+1)
        try:
            entrada_2.append(int(input()))
            if entrada_2[1] >= 1:
                break
            else:
                print()
        except:
            print()
    existencia.append(entrada_2)

paciente = []
dic_sucursales = dict()

for i in existencia:
    dic_sucursales[i[0]] = [i[1],i[1]]

for i in range(int(entrada_1[1])):
    dato = [] 
    dato = input().split(" ")
    dato = list(map(int, dato))  
    paciente.append(dato)
    if dato[0] in dic_sucursales:
        if dato[1] < 83 and dato[2] < 48:
            dic_sucursales[dato[0]][1] = dic_sucursales[dato[0]][1] - 15
        elif (dato[1] >= 83 and dato[1] <= 124) and (dato[2] >= 48 and dato[2] <= 66 ):
            continue
        elif (dato[1] >= 124 and dato[1] <= 141) and (dato[2] >= 66 and dato[2] <= 83 ):
            continue
        elif (dato[1] >= 141 and dato[1] <= 158) and (dato[2] >= 83 and dato[2] <= 97 ):
            dic_sucursales[dato[0]][1] = dic_sucursales[dato[0]][1] - 3
        elif (dato[1] >= 158 and dato[1] <= 186) and (dato[2] >= 97 and dato[2] <= 112 ):
            dic_sucursales[dato[0]][1] = dic_sucursales[dato[0]][1] - 6
        elif (dato[1] >= 186 and dato[1] <= 197) and (dato[2] >= 112 and dato[2] <= 128 ):
            dic_sucursales[dato[0]][1] = dic_sucursales[dato[0]][1] - 18   
        elif dato[1] >= 197 and dato[2] >= 128:
            dic_sucursales[dato[0]][1] = dic_sucursales[dato[0]][1] - 30    
        elif dato[1] >= 159 and dato[2] <= 94:
            dic_sucursales[dato[0]][1] = dic_sucursales[dato[0]][1] - 24

dic_sucursales_menor = sorted(dic_sucursales.items(), key=lambda x: x[1][1])
dic_sucursales_mayor = sorted(dic_sucursales.items(), key=lambda x: x[1][1],reverse=True)

print("{0} {1}".format(dic_sucursales_menor[0][0],dic_sucursales_menor[0][1][1]))

print("{0} {1}".format(dic_sucursales_mayor[0][0],dic_sucursales_mayor[0][1][1]))

dic_sucursales_menor = sorted(dic_sucursales.items(), key=lambda x: x[0])
for i in range(len(dic_sucursales_menor)):
    print("{0} {1:.2f}%".format(dic_sucursales_menor[i][0],(float(100) - dic_sucursales_menor[i][1][1] * 100 / dic_sucursales_menor[i][1][0])))

    