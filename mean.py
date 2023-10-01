def meansum(a):
    tempsum = [0,0]
    mean = [0,0]
    for i in range(len(a)):
        tempsum[0] += a[i][0]
        tempsum[1] += a[i][1]
    mean[0] = tempsum[0] / len(a)
    mean[1] = tempsum[1] / len(a)
    return(mean)
