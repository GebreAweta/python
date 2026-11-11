# name = input("please enter your name:")
# age = int(input("please enter your age:"))
# print('Your name is:', name, 'and you are ',  age, 'years old.')
# lists in python
# countries = ['USA', 'Ethiopia', 'Kenya', 'England', 'Dubai']
# print(countries[0])
# print(countries[1])
# print(countries[2])
# print(countries[3])
# print(countries[4])
# print(countries[1:3])
# print(countries[-2])
# print(type(countries))
#   List methods
list1 = [1,2,3,4,5]
list2 = ['coffee', 'banana', 'apple', 'avocado', 'mango']
# list1.extend(list2)
# print(list1)
list2.insert(2, 'orange')
print(list2)
print(list2.count('avocado'))
list1.reverse()
print(list1)
list3 = list2.copy()
print(list3)
list2.remove('banana')
print(list2)