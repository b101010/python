n = 5
#a = [0,2,4,6]
a=[]

for i in range(0,n,2):
    a.append(i)

b = len(a)
print(a)

for j in a:
    for i in range(n-1):
        print(' ', end='')
    print('/', end='')
    for i in range(j):
        print(' ', end='')
    print('\\')
    n=n-1

for j in reversed(a):
    for i in range(n):
        print(' ', end='')
    print('\\', end='')
    for i in range(j):
        print(' ', end='')
    print('/')
    n=n+1
  
        
