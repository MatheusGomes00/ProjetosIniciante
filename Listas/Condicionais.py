lista_ingredientes = []
# for ingrediente in range(3):
#     lista_ingredientes.append(input("Entre com o ingrediente: "))
# print(lista_ingredientes)
# if lista_ingredientes:
#     for ingrediente in lista_ingredientes:
#         print("Adding " + ingrediente + '.')
#     print("Finished making you pizza!")
# else:
#     print("Are you sure you want a plain pizza?")
# ingredients_list = [input(order) for order in range(1, 7)]
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
ingredients_list = []
print("Lista de pedidos: \n")
while True:
    for ingredient in range(0, 6):
        order = input()
        if order == "":
            break
        else:
            ingredients_list.append(order)
    break
# print(ingredients_list)
if ingredients_list:
    for ingredient in ingredients_list:
        if ingredient in available_toppings:
            print("Adding " + ingredient + ".")
        else:
            print("Sorry, we don't have " + ingredient + ".")
else:
    print("Are you sure you want a plain pizza?")
print("\nFinished making your pizza!")

for i in range(10):
    if i == 1:
        print(i, "st")
    elif i == 2:
        print(i, "nd")
    elif i == 3:
        print(i, "rd")
    elif i != 0:
        print(i, "th")
