N = int(input("кол-во:"))
results = list()
a = list()
for i in range(N):
    x = int(input())
    a.append(x)


for i in range(len(a) - 1):
    if a[i] < a[i+1]:
        results.append(0)
    elif a[i] > a[i+1]:
        results.append(1)
    
if sum(results) == 0:
    print("возрастающий")
elif sum(results)+1 == len(a):
    print("убывающий")
else:
    print("возрастающий убывающий")
print (results)




