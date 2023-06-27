# mostra somente os números ímpares de 0 a 21...
for numero in range(100):
    if numero % 2 == 0:
        continue
    if numero == 21:
        break
    print(numero)
