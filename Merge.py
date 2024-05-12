import time
start = time.time()
with open('merge.txt', 'r') as file:
    data = file.read()
insertion = data
insertion = insertion.split()
for g in insertion:
  insertion[insertion.index(g)] = int(g)
must_bubble = insertion

def merge(must_bubble):
    if (len(must_bubble) > 1):
        left_part = must_bubble[:(len(must_bubble) // 2)]
        right_part = must_bubble[(len(must_bubble) // 2):]
        merge(left_part)
        merge(right_part)
        a = b = 0
        zero = 0
        while a < len(left_part) and b < len(right_part):
            if left_part[a] <= right_part[b]:
                must_bubble[zero] = left_part[a]
                a += 1
            else:
                must_bubble[zero] = right_part[b]
                b += 1
            zero += 1

        while a < len(left_part):
            must_bubble[zero] = left_part[a]
            a += 1
            zero += 1

        while b < len(right_part):
            must_bubble[zero]=right_part[b]
            b += 1
            zero += 1

merge(must_bubble)
print(must_bubble)

end = time.time()
print(end-start)