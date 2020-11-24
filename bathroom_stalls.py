import math
from collections import defaultdict

cases = int(input())

for i in range(cases):
    case_args = input().split(" ")
    stalls, people = int(case_args[0]), int(case_args[1])
    
    stall_set = {stalls}
    count = defaultdict(lambda: 0)
    count[stalls] = 1
    x0, x1 = 0, 0

    person = 0
    while True:
        x = max(stall_set)

        n = x >> 1

        x0 = n
        x1 = n
        
        if x % 2 == 0:
            x1 -= 1

        person += count[x]
        if person >= people:
            break

        stall_set.remove(x)
        stall_set.add(x0)
        stall_set.add(x1)

        count[x0] += count[x]
        count[x1] += count[x]

    print("Case #{}: {} {}".format(i + 1, x0, x1))
