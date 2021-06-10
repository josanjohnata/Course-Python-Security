lista = [1, 2, 23, -4, 5];
lista_animais = ['cachorro', 'gato', 'elefante'];
# print(lista, lista_animais[1])
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))

if 'lobo' in lista_animais:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista, Será incluido.')
    # a função .append() adiciona um item na lista
    lista_animais.append('lobo')
    print(lista_animais)
# a função .pop() exclui o ultimo item da lista
lista_animais.pop()
print(lista_animais)