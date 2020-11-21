# Works on first two test sets and gives a wrong answer on third
# I have no idea why that happens

import math

cases = int(input())

for i in range(cases):
    case_args = input().split(" ")
    stalls, people = int(case_args[0]), int(case_args[1])
    
    stall_set = {stalls}
    count = {stalls: 1}
    x0, x1 = 0, 0

    person = 0
    while True:
        x = max(stall_set)
        x0 = math.ceil((x - 1) / 2)
        x1 = math.floor((x - 1) / 2)

        person += count[x]
        if person >= people:
            break

        stall_set.remove(x)
        stall_set.add(x0)
        stall_set.add(x1)

        if x0 not in count.keys(): count[x0] = 0
        if x1 not in count.keys(): count[x1] = 0
        count[x0] += count[x]
        count[x1] += count[x]

    print("Case #{}: {} {}".format(i + 1, x0, x1))
