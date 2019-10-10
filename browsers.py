browsers = ['Chrome', 'Safari', 'Firefox', 'Edge']
print("My favourite browser is " + browsers[0])
print(browsers[0:3])

#browsers.append('Opera')
#print(browsers)

#browsers.extend(['Opera', 'Explorer', 'Chromium'])
#print(browsers)

#browsers.insert(0, 'Opera')
#print(browsers)

#popped_item = browsers.pop(1)
#print(browsers)
#print(popped_item)

#del browsers[1]
#print(browsers)

browsers.remove('Edge')
print(browsers)

browsers.sort()
print(browsers)

browsers.reverse()
print(browsers)

#Part 2
pos =(100, 200)
print(type(pos[0]))	
another_pos = (100,)
print(type(another_pos))

#Part 3
countries = {'Sweden', 'Norway', 'Denmark'}
print(countries)