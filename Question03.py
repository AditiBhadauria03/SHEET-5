# 3.Max and Min of an Array
# T ake input an array A of size N and write a program to print maximum and minimum
# elements of the input array .Here N represents the length of the array .

A = [1, 2, 3, 4, 5]
max = A[0]
min = A[0]
for num in A:
    if num > max:
        max = num
    if num < min:
        min = num
print(max, min)

