# temos escopo global e local, o local sempre fica em um bloco de uma função
# apesar de não ser considerada uma boa prática, podemos utilizar a palavra-chave reservada 'global'
# quando trabalhamos com listas, precisamos fazer uma cópia 'copy()' para que a variável local não se altere
salario = 2000  # variável definida no escopo global, fora de qualquer bloco de função


def salario_bonus(bonus, lista):
    global salario  # assim dizemos para o interpretador que a variável 'salario' é global
    # lista.append(2) -> desta forma alteramos a lista original
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f'Lista auxiliar {lista_aux}')
    salario += bonus
    return salario


lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)
