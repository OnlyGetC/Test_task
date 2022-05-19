
import sys

a = sys.argv[1]
file4 = open(a, "r")

#Reading file
l = []
while True:
    line = file4.readline()
    if not line:
        break
    l.extend(line.strip().split())
nums = [int(i) for i in l]

#Counting the number of moves
'''
Алгоритм основан на сравнении каждого числа списка с остальными,
путём определения по модулю разницы между ними. Разности конкретного числа со всеми остальными суммируются.
После полного перебора определяется минимальная суммарная разница, которая и является наименьшим количеством ходов.

The algorithm is based on comparing each number in the list with the rest,
by determining the modulo difference between them. The differences of a particular number with all the others are summed up.
After a complete enumeration, the minimum total difference is determined, which is the least number of moves.
'''
turns = 9**99
sum = 0

for i in nums:
    for j in nums:
        sum += abs(i -j)
    if sum < turns:
        turns = sum
    sum = 0

print(turns)