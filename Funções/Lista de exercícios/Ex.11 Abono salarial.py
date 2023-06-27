def verifica(hora, valor):
    s = 0
    if hora <= 40:
        salario = (hora * valor)
        s = f'Não passou de 40 horas semanais\nValor salário: {salario * 4}'
    elif hora > 40:
        extra = hora - 40 
        salario = ((40 * valor) + (extra * (valor * 1.5))) * 4
        s = f'{extra:.1f} hora(s) extra.\nValor salário: {salario:.2f}'
    return s

horas = float(input('Número de horas trabalhadas por semana: '))
valorHoras = float(input('Valor por hora trabalhada: '))
print(verifica(horas, valorHoras))



'''A jornada de trabalho semanal de um
funcionário é de 40 horas. O funcionário
que trabalhar mais de 40 horas receberá
hora extra, cujo cálculo é o valor da
hora regular com um acréscimo de 50%.
Escreva uma função que receba o
número de horas trabalhadas em uma
semana e o salário por hora, e retorne o
salário do funcionário.'''