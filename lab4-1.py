# Author CCG 11/12/2021

colors = ['red', 'yellow' , 'green' , 'blue']
colors.extend(['purple' , 'orange' , 'pink'])
print(colors.count('yellow'))

colors.insert(3, 'teal')
print(colors)
colors.clear()

print(colors.count('red'))
