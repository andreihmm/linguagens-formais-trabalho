# Conversão de AFND para AFD

Este projeto foi desenvolvido como parte da disciplina **Linguagens Formais e Autômatos**. O objetivo principal foi praticar **Python** enquanto aprimorava a compreensão do **algoritmo de conversão de um Autômato Finito Não Determinístico (AFND) para um Autômato Finito Determinístico (AFD)**.

## 📌 Objetivos
- Implementar o algoritmo de conversão de **AFND para AFD** em Python.
- Reforçar os conceitos teóricos sobre autômatos.
- Aplicar prática de programação para manipulação de conjuntos e transições de estados.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- Estruturas de dados como **dicionários** e **conjuntos** para representar estados e transições.

## 📖 Como funciona a conversão?
O algoritmo segue os seguintes passos:
1. Criar o **fecho-ε** para cada estado do AFND.
2. Gerar o conjunto de estados do AFD a partir do fecho-ε dos estados do AFND.
3. Construir as novas transições determinísticas para o AFD.
4. Definir os novos estados finais com base nos estados finais do AFND.

## 📝 Exemplo de Entrada e Saída
**Entrada (AFND):**
```
A B C D E F G H 
A
E
A h C
A 1 B
A h G
B 1 B
B 0 F
C 0 D
D 1 D
D 0 E
D 0 H
F h G
G 1 H
H 0 H
H 1 E
```
**Saída (AFD convertido):**
```
ACG BH BE B FG H E FGH EH D 
ACG
BE E EH 
ACG 1 BH
BH 1 BE
BE 1 B
B 1 B
B 0 FG
FG 1 H
H 1 E
H 0 H
BE 0 FG
BH 0 FGH
FGH 1 EH
EH 1 E
EH 0 H
FGH 0 H
ACG 0 D
D 1 D
D 0 EH
```
**Fornecer palavras para serem testadas no AFD:**
```
00
11
010
101
110
01
1001
0011
1110
1101
1010
010101
00011
11100
```
**Saída:**
```
00 aceita
11 aceita
010 aceita
101 aceita
110 nao aceita
01 nao aceita
1001 aceita
0011 nao aceita
1110 nao aceita
1101 nao aceita
1010 nao aceita
010101 nao aceita
00011 nao aceita
11100 nao aceita

```


## 📌 Conclusão
Este projeto permitiu reforçar o entendimento sobre a conversão de AFND para AFD, além de exercitar habilidades em **Python** e **estruturação de algoritmos**. A implementação pode ser expandida para suportar **autômatos mais complexos** e ser integrada a um simulador visual.

---
🔗 Sinta-se à vontade para contribuir ou sugerir melhorias! 😊

