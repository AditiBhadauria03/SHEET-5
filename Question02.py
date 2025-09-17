# 2.Copy the Array
# You are given a constant array A and an integer B.
# You are required to return another array where Arr[i] = A[i] + B.

A=[1,2,3,2,1]
B=3
Arr=[]
for i in range(len(A)):
    Arr.append(A[i]+B)
print(Arr)

