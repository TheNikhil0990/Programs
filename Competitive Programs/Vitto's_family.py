  
def cal(val, arr):
		arr.sort()
		d = 0
		if val%2:
			mid = arr[val//2]
		else:
			mid = 0.5*(arr[val//2 - 1] + arr[val//2])
			
		for a in arr:
			d += abs(a - mid)
			
		return int(d)

def main():
	Test_case = int(input())
	for _ in range(Test_case):
		arr = list(map(int, input().split()))
		print("Output:",cal(arr[0], arr[1:]))

main()        
