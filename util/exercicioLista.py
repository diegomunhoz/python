# *********************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                     ******
# ******   Programa: Exemplos de manipulação de lista                                    ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                 ******
# ******   Data....: 24/03/2018                                                          ******
# *********************************************************************************************

l = [4,5,6]

print("Lista definida: 'l'")
for x in l:
    print(x, end=',')
print("")

print("Tamanho da lista: ",len(l))

l.append(10)
print("Comando: apeend(10)")
for x in l:
    print(x, end=',')
print("")

l.extend("ABC")
print("l.extend('ABC')")
for x in l:
    print(x,end=',')
print("")

l.insert(4,30)
print("Comando l.insert(4,30)")
for x in l:
    print(x, end=',')
print("")

l.remove(6)
print("Comando l.remove(6)")
for x in l:
    print(x, end=',')
print("")

l.pop()
print("Comando l.pop()")
for x in l:
    print(x, end=',')
print("")

l.pop(1)
print("Comando l.pop(1)")
for x in l:
    print(x, end=',')
print("")