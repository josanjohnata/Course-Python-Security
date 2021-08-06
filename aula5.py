lista = [1, 2, 23, -4, 5, 645, 9, 10, 888];
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'minha-sogra', 'Milk', 'cobra'];
# print(lista, lista_animais[1])
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))

# if 'lobo' in lista_animais:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista, Será incluido.')
#     # a função .append() adiciona um item na lista
#     lista_animais.append('lobo')
#     print(lista_animais)
# a função .pop() exclui o ultimo item da lista ou qualquer item, basta colocar a posição do item como parametro
# lista_animais.pop()
# print(lista_animais)

# a função .sort() servi para ordenar uma lista
# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# a função .reverse() servi para ordenar de forma reversa uma lista
# lista.reverse()
# lista_animais.reverse()
# print(lista)
# print(lista_animais)

# a tupla serve para criar objetos imutaveis
tupla = (1, 2, 5, 69, 8, 9)
# print(tupla)
# o len() serve para verificar o indici da lista
# print(len(tupla))

# o tuple() serve para converter um array em um objeto
# tupla_animal = tuple(lista_animais)
# print(type(tupla_animal))
# print(tupla_animal)

# o list() serve paa converter um objeto em um array
tupla_animal = list(lista_animais)
print(type(tupla_animal))
print(tupla_animal)
