#Написать функцию, которая будет считать и возвращать сумму двух чисел. Если сумма больше 10 - вывести на экран “This sum is greater than 10. It’s {sum}”, если меньше - “This sum is less than 10. It’s {sum}”
a = 10
s = int(input("Введите сумму")) 

def func(suma):
	if suma > 10:
		sum1 = a + s
		print(f"This sum is greater than 10.It`s {sum1}")
	elif suma < 10:
		t = a - s
		print(f"This sum is less than 10.It`s {t}")


func(s)

#Написать функцию, которая будет принимать пароль. Если его длина не менее 10 символов вывести: “Your password is strong.” в противном случае “Your password is not strong enough.”

a = 10
b = str(input("Enter your password"))

def func(password):
	if len(password) > 10:
		print(f"Your password is strong")
	elif len(password) < 10:
		print(f"Your password isn`t strong enough")


func(b)

