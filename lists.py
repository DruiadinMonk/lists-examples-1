# Creating Lists
list_1 = []

list_2 = [1, 2, 3]

list_3 = ["word", "yes", "no"]

a = 123
b = "BIG WORDS!"
c = 7.298

list_4 = [a, b, c]




# Adds an element at the end of the list
d = str(a)

list_4.append(d)

# Removes all the elements from the list
list_4.clear()

# # Returns the number of elements with the specified value
x = list_4.count(123)

list_4 = [1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1]

x = list_4.count(1)

# # Add the elements of a list (or any iterable), to the end of the current list
list_1.extend(list_2)

list_1.extend(list_2)

# Operators
list_1 = []

list_1 = list_2 + list_2

# # Returns the index of the first element with the specified value	
a = list_1.index(1)

# Position:  0  1  2  3  4  5
# Value: 	[1, 2, 3, 1, 2, 3]



# # Adds an element at the specified position
list_1.insert(3, 4)


list_2 = ["Apple", "Baaaananaaa", "Charlie"]

list_2.insert(1, "WORD SALAAD!")

print(list_2)


# # Removes the element at the specified position
list_2.pop(0)


# Removes the first item with the specified value
# list_2.remove("WORD SALSA!")

list_2.remove("WORD SALAAD!")


print(list_2)


# # Reverses the order of the list
list_2.reverse()

print(list_2)

# # Sorts the list
list_2.sort()	

print(list_2)

list_2 += 1, 4, 2, 6, 3, 7, 5

print(list_2)

# list_2.sort()

print(list_2)

list_2.pop(0)
list_2.pop(0)

print(list_2)

list_2.sort()

print(list_2)



# OTHER LIST OPTIONS

# For loops
list_1 = []
for i in range(10):
	list_1.append(i)

print(list_1)




lol = [[1, 2, 3], ['a', 'b', 'c'], [1.1, 2.2, 3.3]]

print(lol)

lol.append(0)

print(lol)
