#Посчитать количество 9 в списке.

l = [1,2,3,9,5,6,9,8,9,10]
i = 0

while i < len(l)-1:
	i += 1
	if l[i] == 9:
		print(l[i])


#Вывести количество четный и нечетных елементов в рандомной последовательности.

import random

l = []
for i in range(6):
	l.append(random.randint(1, 100))
print(l)
count_even = 0
count_odd = 0
for element in l:
	if element %2 == 0:
		count_even += 1
else: 
	count_odd += 1
print("Odd:", count_odd) 
print("Even:", count_even)
		
#Пользователь должен ввести последовательность чисел через пробел.Для каждого числа выведите слово YES (в отдельной строке),
#если это число ранее встречалось в последовательности или NO, если не встречалось.

numbers = (input(('Введите последовательность'.split(',')))) 
s = set()
for elem in numbers:
	if element in numbers:
		print("YES")
else:
	print("NO")
	s.add(element)
print(s)






