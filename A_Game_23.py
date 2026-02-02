n, m = list(map(int, input().split(" ")))

# m = n * 2^a * 3^b
# 2^a * 3^b = m/n
# lets try to get the number of 2 and 3 i.e a and b by factorizing either 2 or 3 
# the idea is to get the other number (q) with m which its gcf is n,
#  and get the number of 2 and 3 it (q) will be factored

 
if m%n!=0:
    print(-1)
else:
    counter = 0
    q = m / n
    while True:
        if q % 2 == 0:
            q /= 2
        elif q % 3 == 0:
            q /= 3
        else:
            break
        counter += 1
    
    if q != 1:
        print(-1)
    else:
        print(counter)
