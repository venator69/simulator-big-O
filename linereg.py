a = [(2,5),(3,5),(6,7),(2,8),(2,9),(9,7)]
b = [(2,4),(2,5),(8,7),(1,8),(11,9),(2,7)]
c = [(2,5),(1,5),(8,7),(4,8),(11,9),(14,7)]
def linsum(a):
    sumx = 0
    sumy = 0
    sumxy = 0
    sumx2= 0
    for i in range(len(a)):
        sumx += a[i][0]
    for i in range(len(a)):
        sumy += a[i][1]
    for i in range(len(a)):
        sumxy += a[i][0] * a[i][1]
    for i in range(len(a)):
        sumx2 += a[i][0]**2
    return([sumx,sumy,sumxy,sumx2])
def linreg(n):
    b0 = (len(n) * linsum(n)[2] - linsum(n)[0]*linsum(n)[1])/(len(n)*linsum(n)[3]-linsum(n)[3]**2)
    b1 = (linsum(n)[1] - b0 *linsum(n)[0])/len(n)
    return([round(b0,6),round(b1,6)])

