# кортеж
immutable_var = (1, [3, 5], 'строка', True)
print(immutable_var)
immutable_var [1][1] = 7
print(immutable_var)
# в случае замены элемента кортежа возникает ошибка выполнения кода,
# исключением является элементы которые сами по себе являются изменяемыми

# список
mutable_list = [1, 2, 3, 7, 4, 'строка', True]
print(mutable_list)
mutable_list.append(False)
mutable_list.remove(7)
print(mutable_list)
