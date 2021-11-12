# Author CCG 11/12/2021

subjects = ['math' , 'history' , 'science']
print(subjects)

subjects.append('english')
print(subjects)

print(subjects.index('math'))

subjects.sort()
print(subjects)

subjects2 = subjects.copy()

subjects2.reverse()
print(subjects2)