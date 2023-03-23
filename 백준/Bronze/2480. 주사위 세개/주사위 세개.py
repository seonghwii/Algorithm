a, b, c = map(int, input().split())

abc = [a, b, c]
Abc = set(abc)

if len(Abc)  == 1:
    print(10000 + a * 1000)
elif len(Abc) == 3:
    print(max(abc)*100)
else:
    for x in Abc:
        abc.remove(x)
    print(1000 + abc[0]*100)