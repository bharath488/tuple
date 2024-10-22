'''
Write a program to get the tuple elements and print it.
Sample Input:
3
20
10
30
Sample Output:
(20, 10, 30)
'''
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(tuple(lst))
'''
 Write a program to get the elements of tuple in a single line separated by space and print the tuple values.
Sample Input:
20 10 30
Sample Output:
20, 10, 30
'''
a=map(int,input().split())
b=tuple(a)
print(b)
'''
Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
input_string = input("Enter numbers separated by space: ")


numbers_tuple = tuple(map(int, input_string.split()))


print(len(numbers_tuple))
'''
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''
n = int(input("Enter the number of elements: "))

elements = []

for _ in range(n):
    value = int(input())
    elements.append(value)

numbers_tuple = tuple(elements)

total_sum = sum(numbers_tuple)

print(total_sum)
'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
n = int(input("Enter the number of elements: "))


elements = []


for _ in range(n):
    value = int(input())
    elements.append(value)


numbers_tuple = tuple(elements)

max_value = max(numbers_tuple)

print(max_value)
'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
n = int(input("Enter the number of elements: "))

elements = []
for _ in range(n):
    value = int(input())
    elements.append(value)

numbers_tuple = tuple(elements)

min_value = min(numbers_tuple)

print(min_value)
'''
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
tuple_input = input("Enter tuple values separated by space: ")
tuple_values = tuple(map(int, tuple_input.split()))

x = int(input("Enter the value to count: "))

count_x = tuple_values.count(x)

print(count_x)
'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
tuple_input = input("Enter tuple elements separated by space: ")
tuple_values = tuple(map(int, tuple_input.split()))

total_sum = 0

for num in tuple_values:
    total_sum += num

print(total_sum)
'''
 Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
'''
input_values = input("Enter numbers separated by space: ")
numbers = list(map(int, input_values.split()))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
if even_count > odd_count:
    result = "Even"
elif odd_count > even_count:
    result = "Odd"
else:
    result = "Equal"

print(result)
'''
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
tuple_input = input("Enter tuple elements separated by space: ")
tuple_values = tuple(map(int, tuple_input.split()))

x = int(input("Enter the number to count: "))
count_x = tuple_values.count(x)
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
factorial_count = calculate_factorial(count_x)
print(factorial_count)
'''
