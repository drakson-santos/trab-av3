def gerar_tabela_verdade(variaveis):
    tabela_verdade = {}
    comb = 2**len(variaveis)
    tabela_verdade['casos'] = comb
    varia = comb / 2
    for var in variaveis:
        lista = []
        valor = True
        aux = 0
        for i in range(0,comb):
            if aux == varia:
                valor = not(valor)
                lista.append(valor)
                aux = 1
            else:
                aux += 1
                lista.append(valor)

        tabela_verdade[var] = lista
        varia = varia / 2
    return tabela_verdade


def checar_variaveis_utilizadas(expressao):
    variaveis = ('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split(' ')
    variaveis_utilizadas = []
    for letra in variaveis:
        if letra in expressao:
            variaveis_utilizadas.append(letra)
    return variaveis_utilizadas

def substituir_operadores(expressao):
    operadores_inicial = ('~ ^ v').split(' ')
    operadores_final = ('not and or').split(' ')
    for i in range(len(operadores_inicial)):
        expressao = expressao.replace(operadores_inicial[i],operadores_final[i])
    return expressao

# → 8594
def se_entao(a,b):
    if a == True and b == True:
        return True
    if a == True and b == False:
        return False
    if a == False and b == True:
        return True
    if a == False and b == False:
        return True

# ↔ 8596
def se_somente_se(a,b):
    if a == True and b == True:
        return True
    if a == True and b == False:
        return False
    if a == False and b == True:
        return False
    if a == False and b == False:
        return True

#  (A → B) ^ (B → A)
def resolver_por_partes(expressao):

    if '(' in expressao:
        expressao = expressao.replace("(","|(")
        expressao = expressao.replace(")",")|")
        expressao_dividida = expressao.split("|")
        for termo in range(len(expressao_dividida)):
            if "(" in expressao_dividida[termo] and ")" in expressao_dividida[termo]:
                expressao_dividida[termo] = expressao_dividida[termo].replace("(","")
                expressao_dividida[termo] = expressao_dividida[termo].replace(")","")
                expressao_dividida[termo] = str(simplificar_expressao(expressao_dividida[termo]))
        expressao_nova = ''
        for termo in expressao_dividida:
            expressao_nova = expressao_nova + str(termo)
        expressao = expressao_nova
    else:
        s_e = chr(8594)
        s_s_s = chr(8596)
        if (s_e in expressao):
            expressao_dividida = expressao.split(s_e,1)
            expressao = str(se_entao(simplificar_expressao(expressao_dividida[0]),simplificar_expressao(expressao_dividida[1])))
        elif (s_s_s in expressao):
            expressao_dividida = expressao.split(s_s_s,1)
            expressao = str(se_somente_se(simplificar_expressao(expressao_dividida[0]),simplificar_expressao(expressao_dividida[1])))

    return simplificar_expressao(expressao)

def simplificar_expressao(expressao):
    s_e = chr(8594)
    s_s_s = chr(8596)
    if (s_e in expressao) or (s_s_s in expressao):
        return resolver_por_partes(expressao)
    else:
        return eval(expressao)

def testar_casos_expressao(variaveis_utilizadas,tabela_verdade,expressao):
    lista_teste = []
    expressao_calculo = substituir_operadores(expressao)
    for caso in range(tabela_verdade['casos']):
        expressao_caso = expressao_calculo
        for variavel in variaveis_utilizadas:
            expressao_caso = expressao_caso.replace(variavel,str(tabela_verdade[variavel][caso])) # Trocando por true ou false

        resultado_teste = simplificar_expressao(expressao_caso)
        lista_teste.append(resultado_teste)

    tabela_verdade[expressao] = lista_teste
    tabela_verdade.pop('casos', None)
    return tabela_verdade


def app_calc(expressao):
    variaveis_utilizadas = checar_variaveis_utilizadas(expressao)
    tabela_verdade = gerar_tabela_verdade(variaveis_utilizadas)
    resultado = testar_casos_expressao(variaveis_utilizadas,tabela_verdade,expressao)
    return resultado

resultado = app_calc('(A → B) ^ (B → A)')
print(resultado)

resultado = app_calc('A ↔ B')
print(resultado)




