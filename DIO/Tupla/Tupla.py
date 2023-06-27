# A diferença da tupla para a lista é que a tupla não é mutavel, seu valores não são mutáveis
frutas = ("laranja", "pera", "uva",)  # Para declarar uma tupla podemos apenas utilizar os parêntes e uma virgula no final da lista
print(frutas)
letras = tuple("python")  # Podemos também declarar usando o 'tuple'
print(letras)
numeros = tuple([1, 2, 3, 4])  # Podemos considerar uma lista em uma tupla, tornando ela imutavel
print(numeros)
pais = ("Brasil",)  # Podemos também declarar uma tupla de somente 1 elemente
