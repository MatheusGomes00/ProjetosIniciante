def calcular_total(numeros):
    return sum(numeros)


def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucesso = numero + 1
    return antecessor, sucesso


def func_3():  # se não for passado o 'return' o programa irá executar as tarefas e depois retornar 'none'
    print("Hello word")


print(calcular_total([20, 30, 50]))
print(retornar_antecessor_e_sucessor(10))  # (9, 11) retorna uma tupla devido ser um valor imutável
print(func_3())
