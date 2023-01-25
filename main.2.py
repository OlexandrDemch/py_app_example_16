a = '1'
b = a.title()
a = '2'
b = a.lower()
a = '3'
b = str.capitalize(a)
list = []
for i in range(3):

   print('Введіть', i+1, 'слово:')

   list.append(input())

sep = input('Введіть роздільник:')  

print(sep.join(list))    

list = []

b = input('Введіть кількість слів')

for i in range(3):

   print('Введіть', i+1, 'слово:')

   list.append(input())

sep = input('Введіть роздільник:')  

print(sep.join(list))    