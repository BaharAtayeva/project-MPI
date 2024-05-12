import time
start = time.time()
with open('insertion.txt', 'r') as file:
    data = file.read()
insertion = data
insertion = insertion.split()
for g in insertion:
  insertion[insertion.index(g)] = int(g)
for i in range(1, len(insertion)):
  temp = insertion[i]
  n = i-1
  while n >=0 and temp < insertion[n] :
    insertion[n+1] = insertion[n]
    n -= 1
    insertion[n+1] = temp
print(insertion)
#code
end = time.time()
print(end-start)