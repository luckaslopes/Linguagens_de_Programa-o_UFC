def por_valor(x):
    x += 10

def por_referencia(lista):
    lista[0] += 10

a = 5
b = [5]

por_valor(a)
por_referencia(b)

print("Valor após por_valor:", a)     # 5
print("Valor após por_referencia:", b[0])  # 15
