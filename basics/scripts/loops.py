
for i in range(10):
    print(i, " Hola")

for i in range(5, 10):
    print(i, " Hola")

for i in ("1", "2", "3"):
    print(i)

for i,v in enumerate(("1", "2", "3")):
    print(i, " ", v)

t = [1, 2, 3, 4, 5, 6]
i = 0
while (t[i] < 5):
    print(t[i])
    i += 1