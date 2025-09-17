# Add to list elements

A1=[1,2,3,4]
A2=[4,5,6,7]
A3=[]
for i in range(len(A1)):
    A3.append(A1[i]+A2[i])
print(A3)