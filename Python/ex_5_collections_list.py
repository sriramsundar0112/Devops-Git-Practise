# Python - List

# List - [] 
# Ordered, changeable, allows duplicates
# List is iterable. Can be accessed using For-loop
# Can be accessed using index
# Most used methods:
# append - add element to the last of the list
# insert - add the element to the specified index--> (index, element)
# pop - removes the element from the given index.
# extend - To combine two lists. a.extend(b) - Will add the list B at end of A

a=[1,2.2,"Sriram"]
print(a)

a.append(400)# Appending the item to the end of the list.
print(a)

a.insert(0,"First Value") # Adding element at the specified index
print(a)


print(a[1]) # Accessing using specified index

a.pop(2) # Removing element at the given index
print(a)

cars=["Suzuki","Tata","Hyundai"]
bikes=["Yamaha","Hero","TVS"]
cars.extend(bikes)
print(cars)

# To find the number of items in the list
print(len(cars))