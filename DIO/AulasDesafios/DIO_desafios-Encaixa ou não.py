N = int(input())
for i in range(N):
    A, B = input().split()
    print("encaixa" if A.endswith(B) else "nao encaixa")

# v = int(input())
# if v > 0:
#     for i in range(v):
#         n1 = (input())
#         n2 = (input())
#         h = len(n2)
#         k = len(n1)
#         print(h)
#         flag = True
#         if k > 0 and h > 0:
#             if k >= h:
#                 for j in range(h):
#                     teste = -1
#                     if n1[teste] == n2[teste]:
#                         flag = True
#                     else:
#                         flag = False
#                         continue
#                     teste -= 1
#                 if flag is True:
#                     print('encaixa')
#                 else:
#                     print('nao encaixa')
#             else:
#                 print('nao encaixa')
#         else:
#             continue

notas = str(''' n = int(input())
for i in range(n):
    n1, n2 = input(), input()
    teste = 0
    cont = 0
    if n2 > n1:
        print('nao encaixa')
    else:
        for j in range(100):
            teste -= 1
            if n1[teste] == n2[teste]:
                cont += 1
        if cont == 5:
            print('encaixa')
        else:
            print('nao encaixa')''')
