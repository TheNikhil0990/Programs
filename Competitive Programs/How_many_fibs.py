fibbo = []
f1 = 1
f2 = 1
fibbo.append(f1)
fibbo.append(f2)
print('Enter the Input:')


for i in range(0, 100):
    temp = f1 + f2
    fibbo.append(temp)
    f1 = f2
    f2 = temp

value = input().split(" ")
f1 = int(value[0])
f2 = int(value[1])

count = 0
if (f1 <= 1):
    count = 2

for i in fibbo:
    if(i >= f1 and i <= f2):
        count+=1

print("OUTPUT:",count)
