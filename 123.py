#6) Вывести первые 10 символов в строке
#7) Вывести последние 25 символов в строке
#8) Вывести строку “HELLO WORLD” в нижнем регистре
#9) Вставить слова: ”I like {fruit} and {vegetables}” 
#10) "length - {}, width - {}, height - {}"
#11) Заменить слова Yes на No в строке: “Do you like summer? - Yes”
#12) "This is a {subj}. It's {prop}."


#s1 = "Integer egestas tristique scelerisque." #6) Вывести первые 10 символов в строке
#s1[:10]		

#s2 = "Nunc nec sodales ante, eu efficitur velit." #7) Вывести последние 25 символов в строке
#s2[25:]

#a = "HELLO WORLD" #8) Вывести строку “HELLO WORLD” в нижнем регистре
#a.lower()




#a = "fruit"
#b = "vegetables"

#def func(food):						#9) Вставить слова: ”I like {fruit} and {vegetables}”
#	food = a + b
#	return food

#print('I like, {} and {}'.format(a, b)) 


#10) "length - {}, width - {}, height - {}"

#a = "lenght"
#b = "width"
#c = "height"
											
#def func(properties):
#	prop = a + b + c
#	return properties

#print('{}\n{}\n{}'.format(a, b, c))


#11) Заменить слова Yes на No в строке: “Do you like summer? - Yes”

#a = "No"
#b = "Yes" #Для красоты	
#print("Do you like summer - {}".format(a))

#12) print("This is a {subj}. It's {prop})