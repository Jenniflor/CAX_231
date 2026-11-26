#This program calculates the sum of even numbers from 1 to 50 using a for loop and a while loop.
#First, we will use a for loop to calculate the sum of even numbers from 1 to 50..
sum_even = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i
    # print(i, end=" ")
else:
    print("\nDone counting!")

print("The sum of even numbers from 1 to 50 is:", sum_even)
#Setting the while loop to calculate the sum of even numbers from 1 to 50 with 2 variables, counter and sum_even_while
counter = 0
sum_even_while = 0

while counter <= 50:
    if counter % 2 == 0:
        sum_even_while += counter
    counter += 1

print("The sum of even numbers from 1 to 50 (using while loop) is:", sum_even_while)