valores = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
valores5 = { 'V': 5,  'L': 50,  'D': 500 } 
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

rangos = {
    0: {1: 'I', 5 : 'V', 'next': 'X'},
    1: {1: 'X', 5 : 'L', 'next': 'C'},
    2: {1: 'C', 5 : 'D', 'next': 'M'},
    3: {1: 'M', 'next': ''}
}

def numParentesis(cadena):
    return len(cadena)-len(cadena.lstrip('('))

    num = 0
    for c in cadena:
        if c == '(':
            num += 1
        else:
            break
    return num


def contarParentesis(numRomano):
    res = []
    grupoParentesis = numRomano.split(')')

    ix = 0
    while ix < len(grupoParentesis):
        grupo = grupoParentesis[ix]
        numP = numParentesis(grupo)
        for j in range(ix+1, ix+numP):
            if grupoParentesis[j] != '':
                return 0
        res.append((numP, grupo[numP:]))
        ix += max(numP,1)

    return res
        






def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano: 
        #incrementamos el valor del número arábigo con el valor numérico del símbolo romano
        if letra in valores:
            numArabigo += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1
                if letra in valores5:
                    return 0

                if numRepes > 3:
                    return 0


            elif valores[ultimoCaracter] < valores[letra]:
                if numRepes > 1: # No permite repeticiones en las restas
                    return 0

                if ultimoCaracter in valores5: #No permite restas de valores de 5 (5, 50, 500)
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter) #No permite que se resten unidades de más de un orden
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter]*2
                numRepes = 1
        elif ultimoCaracter == ')':
            numArabigo = numArabigo * 1000
        else:  #si el simbolo romano no es permitido devolvemos error (0)
            return 0

        ultimoCaracter = letra

    return numArabigo

def invertir(cad):
    res = ''
    for i in range(len(cad)-1, -1, -1):
        res+= cad[i]
    return res

def arabigo_a_romano(valor):
    #cad = invertir(str(valor))
    cad = str(valor)[::-1]
    res = ''

    for i in range(len(cad)-1, -1, -1):
        digit = int(cad[i])
        if digit <= 3:
            res += digit*rangos[i][1]
        elif digit == 4:
            res += (rangos[i][1]+rangos[i][5])
        elif digit == 5:
            res += rangos[i][5]
        elif digit < 9:
            res += (rangos[i][5]+rangos[i][1]*(digit-5))
        else:
            res += rangos[i][1]+rangos[i]['next']

    return res

