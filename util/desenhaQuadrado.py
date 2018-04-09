def desenhaQuadrado(altura, largura, simbolo = '#', preenchimento = ' '):
    print(simbolo * largura)
    for _ in range(altura-2):
        print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
    print(simbolo * largura)

print('Um quadrado:')
desenhaQuadrado(10, 50)

print('\nOutro quadrado:')
desenhaQuadrado(4, 8, '$', 'A')