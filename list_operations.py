#list that already exists
list_operations = [ 1,2]
print(list_operations, "values in the list")
# user input with as string then converted to integers to add values separated by space to the list
try:
    user_input = input("Enter 3 values to add to the list separated by space: ")
    new_values = [int(x) for x in user_input.split()[:3]]
    list_operations.extend(new_values)
    print("Updated list:", list_operations)

    print("Sorted list(using sorted() method):", sorted(list_operations))
except ValueError:
    print("Invalid input. Please enter integers only.")

# .sort() method to sort the list in place
list_operations.sort()
print("Sorted list(using .sort() method):", list_operations)
#deleting the last element of the list using del statement
del list_operations[-1]
print("List after deleting the last element:", list_operations)
#using reverse() method to reverse the list
list_operations.reverse()
print("List after reversing:", list_operations)
