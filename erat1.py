# sajat szerzemeny, nagy szamokra belassul
def erat(n):

    a = []
    c = []

    a.extend(range(2,n+1))

    while len(a) >= 1:
        e = a[0]
        c.append(a[0])
        for i in a:    
            if i % e == 0:
                a.remove(i)
      
    return c

print(erat(1000))    

