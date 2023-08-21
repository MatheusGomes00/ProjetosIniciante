"""
Python possui em sua biblioteca padrão um módulo para 
manipular da a e hora. Podemos acessar a documentação
do módulo com o link
https://docs.python.org/3.6/library/datetime.html
"""
import locale, os
from datetime import datetime, timedelta
from time import strftime, strptime, localtime, gmtime, mktime
import time

# Podemos formatar a impressão da data/hora passando uma string
# com a máscara. Podemos acessar a documentação com a definição dos
# acrônimos pelo seguinte link https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
now = datetime.now()
print("Data sem formatação: {}".format(now))
print("Data formatada: {}".format(now.strftime('%A %d de %b de %Y')))
print("Data formatada: {}".format(now.strftime('%d/%m/%y')))
print("Data formatada: {}".format(now.strftime('%d/%m/%Y')))

days_of_week = {
    1: u'Segunda-Feira',
    2: u'Terça-Feira',
    3: u'Quarta-Feira',
    4: u'Quinta-Feira',
    5: u'Sexta-Feira',
    6: u'Sábado',
    7: u'Domingo'
}

number_of_day = datetime.now().isoweekday()
print('{}'.format(days_of_week[number_of_day]))

# Você pode alterar o locale para exibir a formatação de acordo 
# com o país desejado. Nota: locale deve estar disponível na máquina.
# import locale                               
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
 #print('Data formatada: {}'.format(now.strftime('%A %d de %b de %Y')))

# Outra necessidade muito comum é calcular a diferença enre duas datas. 
# Quando ocorre uma operação matemática com objetos dos tipos 'date', 
# 'time' ou 'datetime', o Python irá devolver um objeto 'timedelta',
# no qual a diferença entre as unidades é expressada em microsegundos.

now = datetime.now().date()
birth = datetime(now.year + 1, 9, 17, 12, 0, 0, 0).date() # Cria um novo objeto datetime que representa o próximo aniversário. Ele é criado somando 1 ao ano atual (now.year + 1), definindo o mês como março (3), o dia como 21, a hora como 12, e os minutos e segundos como 0. Em seguida, o método .date() é chamado para extrair apenas a parte da data. A variável birth guarda a data do próximo aniversário.
diff_days = (birth - now).days

print('Hoje: {}'.format(now.strftime('%d-%m-%Y')))
print('Próxi. aniversário: {}'.format(birth.strftime('%d-%m-%Y')))
print('Faltam {} dias.'.format(diff_days))

# diff em horas
diff_hours = (birth - now).total_seconds() / 60 / 60
diff_minutes = (birth - now).total_seconds() / 60
diff_seconds = (birth - now).total_seconds()

print('Faltam {:.0f} horas.'.format(diff_hours))
print('Faltam {:.0f} minutos.'.format(diff_minutes))
print('Faltam {:.0f} segundos.'.format(diff_seconds))

# Algumas vezes vamos precisar transformar textos em datas,
# por exemplo, podemos ler um arquivo txt com informações de 
# usuários inativos no sistema. Ao parsear o arquivo durante o 
# processo de leitura, vamos obter a data com o tipo string.
'... lê o arquivo e obtem a linha com a data'
inactive_user_date = '10/10/15'
conv_date = datetime.strptime(inactive_user_date, '%d/%m/%y').date()
print(conv_date)


locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

now = localtime()
time_formatado = strftime('%a, %d %b %Y %H:%M:%S + 0000', now)  # +0000: Fuso horário (neste caso, UTC).
print('{}'.format(time_formatado))

# 'time()' retorna o tempo do sistea em segundos
now_sec = time.time()
# 'gmtime()' converte segundos para struct_time
struct_time = time.gmtime(now_sec)
print(struct_time, now_sec)

# somando uma hora
now = time.time()
new = now + (60 * 60)
now = time.localtime(now)
new = time.localtime(new)
print(strftime('%H:%M:%S', now))
print(strftime('%H:%M:%S', new))

# Calculando a diferença
t1 = mktime(strptime('21 Ago 23', '%d %b %y'))
t2 = mktime(strptime('17 Set 23', '%d %b %y'))

diff = timedelta(seconds=(t2 - t1))
print(diff)
