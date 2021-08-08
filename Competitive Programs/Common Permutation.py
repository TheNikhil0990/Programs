n1 = input("Enter string value 1: ")
n2 = input("Enter string value 2: ")
common = list(set(n1) & set(n2))
print(common)
