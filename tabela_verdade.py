def gerar_tabela_verdade(variaveis):
    tabela_verdade = {}
    comb = 2**len(variaveis)
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


var = ("A B C D E F").split(" ")

tabela  = gerar_tabela_verdade(var)

for x in var:
    print(f"{x} : {tabela[x]}")


