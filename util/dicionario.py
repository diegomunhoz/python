


a = {}
b = dict()
c  = dict([('arma', 'espada'), ('defesa', 'escudo'), ('vidas', 5)])

inventario = {'arma': 'espada', 'defesa': 'escudo', 'vidas': 5}

# print(c['vidas'])
# c['vidas'] += 50
# print(c['vidas'])

print('len:' ,len(inventario))
print('list:', list(inventario))

del inventario['arma']
print('list:', list(inventario))
