unordered_list = [75, 20, 29, 110, 51, 63]
print("This is the unordered list:", unordered_list)
n = len(unordered_list) # Number of elements in the list
for b in range(n):
    for g in range(0, n-b-1):
        if unordered_list[g] > unordered_list[g+1]:
            unordered_list[g], unordered_list[g+1] = unordered_list[g+1], unordered_list[g]

print("List has been sorted:", unordered_list)