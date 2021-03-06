# списки

sp1 = ['яблоко', 'груша', 'йогурт', 'орехи', 'киви'] # список обрамляется в []
print(sp1)

print(sp1[2]) # счет начинается с индекса 0, следов., 0, 1, 2 - это йогурт

sp1[3] = 'грецкие орехи' # замена одного элемента на другой
print(sp1)

sp1.append ('сыр')# метод "добавляет" через "."
print(sp1)

del sp1 [1] # метод "удаляет" выбранные данные из списка. ставим вначале
print (sp1)

sp2 = [000, 111, 222, 333, 444, 555, 666]
sp3 = [777, 888, 'девять', 101, 'одинадцать']
sp4 = [sp2, sp3, sp1] # списки в списке (объединение)
print(sp4)

print (sp4 [1][1]) # можем обратиться к элементу списка в списке

# списки можно складывать (из двух списков сделать один)

sp5 = [1, 2, 3]
sp6 = [4, 5, 6]
sp7 = sp5 + sp6
print(sp7)

# также списки можно умножать

sp8 = [5,7]
sp9 = sp8*10
print(sp9)

print (sp1[2:])
print (sp1 [1:3])

# .remove (удаление) - поиск по значению
# .pop (исчезает, лопает) - поиск по индексу
# .insert (добавляет в указанное место) - 
#  len(list_with_two) - возвращает значение длины массива
# .clear - очистить
# .sort - сортировка
# .count - счетчик
# .reverse - выстраивает элементы списка в обратном порядке
# .copy - копирует
# .link - связь, связывает, соединяет?
