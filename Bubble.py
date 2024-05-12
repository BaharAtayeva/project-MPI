import time
start = time.time()
with open('bubble.txt', 'r') as file:
    data = file.read()
must_bubble = data
must_bubble = must_bubble.split()
for g in must_bubble:
  must_bubble[must_bubble.index(g)] = int(g)
statement = True
while statement == True:
  statement = False
  for i in range(len(must_bubble)-1):
    if must_bubble[i] > must_bubble[i+1]:
      temp = must_bubble[i]
      statement = True
      must_bubble[i] = must_bubble[i+1]
      must_bubble[i+1] = temp

    
print(must_bubble)

#code
end = time.time()
print(end-start)