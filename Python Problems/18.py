n,k=7,11
a,l=3,4
for i in range(1,5):
    for j in range(n,k):
        print(j,end=" ")
    print("")
    n=n-a
    k=k-l
    a-=1
    l-=1
