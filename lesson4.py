#Сгенерировать случайное число с помощью randint и вывести его на экран
import random
random.randint(0,100)
print(random.randint(0,100))

#Дан список чисел [1,2,3,4,5,6]. Перемешать список с помощью функции random.shuffle и вывести случайное число с помощью random.choice
import random
List = [1,2,3,4,5,6]
random.shuffle(List)
print(List)
random.choice(List)
print(random.choice([1,2,3,4,5,6]))

#Сгенерировать случайное число с плавающей точкой с помощью random.random() и вывести его на экран
import random
random.random()
print(random.random())

#Сгенерировать случайное число с плавающей точкой в диапазоне от 0 до 25 с помощью random.uniform и вывести его на экран
import random
random.uniform(0,25)
print(random.uniform(0,25))

#Есть список со словам “rock”, “scissors”, “paper”. Создайте прототип игры камень-ножницы-бумага с компьютером, в основе которой будет находится функции random.choice и input()

import random

"""
1 - Rock / Камень
2 - Scissors / Ножницы
3 - Paper / Бумага
"""
print("Let`s play rock, paper, scissors")
print("Choose rock, scissors or paper by 1 - (Rock), 2 -(scissors), 3 - (paper)")
x = random.randint(1, 3)
y = input()

#lose
if x == 1 and y == "2":
    print("Rock vs Scissors! You lose!")
elif x == 2 and y == "3":
    print("Scissors vs Paper! You lose!")
elif x == 3 and y == "1":
    print("Paper vs rock! You lose!")
    
#won
elif x == 2 and y == "1":
    print("Rock vs Scissors! You won!")
elif x == 3 and y == "2":
    print("Scissors vs Paper! You won!")
elif x == 1 and y == "3":
    print("Paper vs Rock! You won!")

#draw
elif x == 1 and y == "1":
    print("Rock vs Rock! Draw!")
elif x == 2 and y == "2":
    print("Scissors vs Scissors! Draw!")
elif x == 3 and y == "3":
    print("Paper vs Paper! Draw!")

else:
    print("What?") # if unknown command 