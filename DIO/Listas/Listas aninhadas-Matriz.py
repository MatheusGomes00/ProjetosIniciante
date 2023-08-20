# matriz = [
#     [1, "a", 2],
#     ["b", 3, 4],
#     [6, 5, "c"]
# ]
# # primeiro linha depois coluna
# print(matriz[0])
# print(matriz[0][0])
# print(matriz[0][-1])
# print(matriz[-1][-1])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(len(arr))

for line in arr:
    for element in line:
        print(element, end=" ")
    print()

leftDigSum = 0
for linha in range(len(arr)):
    leftDigSum += arr[linha][linha]
print(leftDigSum, "\n")

rightDigSum = 0
for line, element in enumerate(arr):
    rightDigSum += element[len(arr) - line - 1]
print(rightDigSum, "\n")
