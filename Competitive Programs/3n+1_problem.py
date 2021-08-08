# Initialise maxstep as -1
MAXSTEP = -1

# Function to calculate cycle length
def calculate_cycle_length(n):
  #Initial step as 1
  steps = 1
  while n != 1:
    steps += 1
    if n % 2 == 0:
      n //= 2
    else:
      n = 3 * n + 1 
  return steps

# Input values  
start, end = map(int, input().split())  
 
for num in range(start, end+1):
  steps = calculate_cycle_length(num)
  if steps > MAXSTEP:
    MAXSTEP = steps
    
    
#Print Result
print(start, end, MAXSTEP)
