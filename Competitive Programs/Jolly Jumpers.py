def isJolly(a, n): 
    diffSet = [False] * n
    for i in range(0, n-1):
        d = abs(a[i]-a[i + 1])
        if (d == 0 or d > n-1 or diffSet[d] == True):
            return False
        diffSet[d] = True
    return True

a = []
b=int(input("\nEnter the number of input elements: "))
print("Enter", b , "elements:\t")
for i in range(0,b):
    c= int(input())
    a.append(c)
print(a)    
n = len(a)

if isJolly(a, n):
	print("Yes,it is Jolly")
else:
	print("No,it is not Jolly")
"""
OUTPUT 1:
Enter the number of input elements: 4

Enter 4 elements: 
1
4
2
3
[1, 4, 2, 3]
Yes,it is Jolly

OUTPUT 2:
Enter the number of input elements: 6

Enter 6 elements:
5
1
4
2
-1
6
[5, 1, 4, 2, -1, 6]
No,it is not Jolly
"""
