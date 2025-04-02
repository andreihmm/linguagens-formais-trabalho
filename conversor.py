entradaEstados = []
entradaInicial = None
entradaFinais = []
entradaTransicoes = []

saidaEstados = []
saidaInicial = ""
saidaFinais = []
saidaTransicoes = []

def normalizarEstados(valor):
    return "".join(sorted(valor))

def gerarFechoh(entradaInicial, saidaInicial):
    i=0
    if saidaInicial.count(entradaInicial) < 1:
        saidaInicial += entradaInicial
        saidaInicial = normalizarEstados(saidaInicial)
    # while entradaTransicoes[i][0] == entradaInicial:
    for i in range(0, len(entradaTransicoes)):
        if entradaInicial == entradaTransicoes[i][0] and entradaTransicoes[i][2] == "h" and saidaInicial.count(entradaTransicoes[i][4]) == 0:
            saidaInicial += entradaTransicoes[i][4]
            saidaInicial = gerarFechoh(entradaTransicoes[i][4], saidaInicial)
        i += 1
    return normalizarEstados(saidaInicial)

def gerarTransicoes(saidaInicial, saidaTransicoes, saidaEstados):
    transicaoNovaUm = ""
    transicaoNovaZero = ""
    estadoNovoUm = ""
    estadoNovoZero = ""
    for estado in saidaInicial:
        for i in range(0, len(entradaTransicoes)):
            if estado == entradaTransicoes[i][0]:
                if entradaTransicoes[i][2] == "1":
                    estadoNovoUm = gerarFechoh(entradaTransicoes[i][4], estadoNovoUm)
                elif entradaTransicoes[i][2] == "0":
                    estadoNovoZero = gerarFechoh(entradaTransicoes[i][4], estadoNovoZero)
            i += 1

    estadoNovoUm = normalizarEstados(estadoNovoUm)
    estadoNovoZero = normalizarEstados(estadoNovoZero)

    if estadoNovoUm != "":
        if saidaEstados.count(estadoNovoUm) < 1:
            saidaEstados.append(estadoNovoUm)
        transicaoNovaUm = saidaInicial + " 1 " + estadoNovoUm
        if saidaTransicoes.count(transicaoNovaUm) < 1:
            saidaTransicoes.append(transicaoNovaUm)
            saidaTransicoes = gerarTransicoes(estadoNovoUm, saidaTransicoes, saidaEstados)


    if estadoNovoZero != "":
        if saidaEstados.count(estadoNovoZero) < 1:
            saidaEstados.append(estadoNovoZero)
        transicaoNovaZero = saidaInicial + " 0 " + estadoNovoZero
        if saidaTransicoes.count(transicaoNovaZero) < 1:
            saidaTransicoes.append(transicaoNovaZero)
            saidaTransicoes = gerarTransicoes(estadoNovoZero, saidaTransicoes, saidaEstados)
    return saidaTransicoes

def gerarFinais(entradaFinais, saidaFinais, saidaEstados):
    for elementoD in saidaEstados:
        for estadoFinalND in entradaFinais:
            if elementoD.count(estadoFinalND) != 0:
                saidaFinais.append(elementoD)
    return saidaFinais

with open("entrada.txt") as arquivo:
    content = arquivo.readlines()
    entradaEstados = content[0].split(" ")
    entradaEstados.remove("\n")
    entradaInicial= content[1].replace("\n", "")
    entradaFinais = content[2].replace("\n", "").split(" ")
    for linha in range(3, len(content)):
        entradaTransicoes.append(content[linha].replace("\n", ""))

    # print(entradaEstados)
    # print(entradaInicial)
    # print(entradaFinais)
    # print(entradaTransicoes)

    saidaInicial = gerarFechoh(entradaInicial, saidaInicial)
    saidaEstados.append(saidaInicial)

    saidaTransicoes = gerarTransicoes(saidaInicial, saidaTransicoes, saidaEstados)
    saidaFinais = gerarFinais(entradaFinais, saidaFinais, saidaEstados)

    # print(saidaFinais)
    # print(saidaEstados)
    # print(saidaInicial)

with open("AFD.txt", "w") as f:
    for elemento in saidaEstados:
        f.write(f"{elemento} ")
    f.write("\n")
    f.write(saidaInicial)
    f.write("\n")
    for elemento in saidaFinais:
        f.write(f"{elemento} ")
    f.write("\n")
    for line in saidaTransicoes:
        f.write(f"{line}\n")
