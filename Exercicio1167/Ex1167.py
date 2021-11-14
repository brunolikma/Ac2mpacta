anoInicio = int(input())
anoFim = int(input())
contador = 0
for i in range (anoInicio, anoFim +1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)
        contador = contador + 1

print(f'bissextos: {contador}')