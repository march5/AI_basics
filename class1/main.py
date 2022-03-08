#miarka o dlugosci n
n = int(input())

for i in range(n):
    print("|....", end="")
print("|")

print(" ", end="")
for i in range(n):
    print('%3s' % i, end="")
    print('%2s' % "", end="")

