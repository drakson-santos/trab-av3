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


def testar_casos_expressao(variaveis_utilizadas,tabela_verdade,expressao):
    lista_teste = []
    expressao_calculo = substituir_operadores(expressao)
    for caso in range(tabela_verdade['casos']):
        expressao_caso = expressao_calculo
        for variavel in variaveis_utilizadas:
            expressao_caso = expressao_caso.replace(variavel,str(tabela_verdade[variavel][caso]))
        resultado_teste = eval(expressao_caso)
        lista_teste.append(resultado_teste)
    tabela_verdade[expressao] = lista_teste
    tabela_verdade.pop('casos', None)
    return tabela_verdade


def app_calc(expressao):
    variaveis_utilizadas = checar_variaveis_utilizadas(expressao)
    tabela_verdade = gerar_tabela_verdade(variaveis_utilizadas)
    resultado = testar_casos_expressao(variaveis_utilizadas,tabela_verdade,expressao)
    return resultado

resultado = app_calc('~(A v ~(B)) ^ C')
