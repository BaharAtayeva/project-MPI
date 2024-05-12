import time
start = time.time()
with open('quick.txt', 'r') as file:
    data = file.read()
must_bubble = data
must_bubble = must_bubble.split()
for g in must_bubble:
  must_bubble[must_bubble.index(g)] = int(g)

quick = must_bubble[::1]
final = []
l = []
r = []
n = len(quick)//2 + 1
pv = quick[0]
final.append(pv)
quick = quick[1:]
for i in quick:
    for x in range(n+1):
        if i >= final[x]:
            if i >= final[len(final)-1]:
                final.append(i)
                break
            elif i < final[x]:
                final.insert(x,i)
                continue
        elif i < final[x]:
            final.insert(x,i)
            break

print(final)
#code
end = time.time()
print(end-start)