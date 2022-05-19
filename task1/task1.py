n = int(input("Enter number n "))
m = int(input("Enter a number of walk length m ")) - 1
if n < m:
    print("n cannot be less than m")
    while n < m:
        m = int(input("Enter a number of length m "))
a = ''
for i in range(1, n + 1):
    a += str(i)
# print('Start array', a)
end = -1

open = a[0]
start = 0
space = ''
end_1 = m

t = 0

while open != end:
    space += a[start]
    end = a[end_1]
    a += a
    start += m
    end_1 = start + m
# print(f"Received path = {space}")
print(space)