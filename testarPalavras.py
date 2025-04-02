with open("AFD.txt", "r") as f:
    lines = f.readlines()

estadosFinais = lines[2].split(" ")
estadosFinais.remove("\n")

def verificarPalavraAceita(palavra):
    palavraAceita = True
    estadoAtual = lines[1].replace("\n", "")
    temTransicao = False
    for letra in palavra:
        for transicao in range(3, len(lines)):
            temTransicao = False
            qOut = lines[transicao].split(" ")[0]
            qIn = lines[transicao].split(" ")[2].replace("\n","")
            letraDaTransicao = lines[transicao].split(" ")[1]
            if estadoAtual == qOut and letra == letraDaTransicao:
                estadoAtual = qIn
                temTransicao = True
                break
        if temTransicao == False:
            return False
    if estadosFinais.count(estadoAtual) < 1:
        return False
    return palavraAceita


with open("palavras.txt", "r") as p:
    palavras = p.readlines() 
        
with open("saidap2.txt", "w") as s:
    for palavra in palavras:
        palavraFormatada = palavra.replace("\n","")
        if verificarPalavraAceita(palavraFormatada):
            s.write(f"{palavraFormatada} aceita\n")
        else:
            s.write(f"{palavraFormatada} nao aceita\n")