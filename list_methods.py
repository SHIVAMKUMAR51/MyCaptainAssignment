#add element to list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#clear all the elements from list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

#returns how many times that specified element occurs
fruits = ['apple', 'banana', 'cherry','cherry','cherry']
x = fruits.count("cherry")
print(x)


#add element(s) to the end of the list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)


#returns the index of the first element with the specified value
ruits = ['apple', 'banana', 'cherry']
x = fruits.index("apple")
print(x)

#adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry','banana']
fruits.remove("banana")
print(fruits)

#reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#reverse sort(sort elements in the descending order)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)